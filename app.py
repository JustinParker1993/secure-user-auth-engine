import psycopg2
import bcrypt


class UserManager:
    def __init__(self, db_config):
        """Initializes the PostgreSQL database connection."""
        self.conn = psycopg2.connect(**db_config)
        self.create_table()

    def create_table(self):
        """Creates a users table if one doesn't exist."""
        with self.conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL
                );
            """)
            self.conn.commit()

    def _hash_password(self, password: str) -> str:
        """Hashes passwords securely using bcrypt with an automated salt."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def register_user(self, username: str, password: str) -> bool:
        """Registers a new user into PostgreSQL using parameterized queries."""
        hashed = self._hash_password(password)
        try:
            with self.conn.cursor() as cursor:
                # Sanitized placeholder input to strictly eliminate SQL Injection
                cursor.execute(
                    "INSERT INTO users (username, password_hash) VALUES (%s, %s);",
                    (username, hashed)
                )
                self.conn.commit()
            return True
        except psycopg2.errors.UniqueViolation:
            self.conn.rollback()
            return False  # Username already exists

    def verify_user(self, username: str, password: str) -> bool:
        """Validates credentials against the salted bcrypt database string."""
        with self.conn.cursor() as cursor:
            cursor.execute(
                "SELECT password_hash FROM users WHERE username = %s;",
                (username,)
            )
            result = cursor.fetchone()
            if result:
                # result is a tuple, e.g., (stored_hash_string,)
                stored_hash = result[0]
                # Compare incoming plain text against stored cryptographic hash
                return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))
            return False
        
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env if exists
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)

# -------------------------------
# App Settings
# -------------------------------

APP_NAME: str = os.getenv("APP_NAME", "Mastra Voice EHR Demo")
DEBUG: bool = os.getenv("DEBUG", "True") == "True"

# Memory settings
MEMORY_RETENTION: int = int(os.getenv("MEMORY_RETENTION", 5))

# Audit logging
AUDIT_LOGGING: bool = os.getenv("AUDIT_LOGGING", "True") == "True"

# Server settings
HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", 8000))

# Logging
LOG_FORMAT: str = "[%(levelname)s] %(asctime)s - %(name)s - %(message)s"

# -------------------------------
# Helper functions
# -------------------------------

def print_config():
    """
    Print current configuration for debugging purposes.
    """
    print(f"APP_NAME: {APP_NAME}")
    print(f"DEBUG: {DEBUG}")
    print(f"MEMORY_RETENTION: {MEMORY_RETENTION}")
    print(f"AUDIT_LOGGING: {AUDIT_LOGGING}")
    print(f"HOST: {HOST}")
    print(f"PORT: {PORT}")
    print(f"BASE_DIR: {BASE_DIR}")

# -------------------------------
# Example usage
# -------------------------------

if __name__ == "__main__":
    print_config()
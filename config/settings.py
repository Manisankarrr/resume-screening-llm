import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# -----------------------------
# GROQ API CONFIGURATION
# -----------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "CRITICAL: GROQ_API_KEY is missing. Please check your .env file."
    )

# Default Groq model (fast + stable)
DEFAULT_LLM_MODEL = "llama-3.1-8b-instant"
"""
Project configuration for the Personal Chef Agent.
"""

import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# API KEYS

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# LANGSMITH TRACING


os.environ["LANGCHAIN_TRACING_V2"] = "true"

if LANGSMITH_API_KEY:
    os.environ["LANGCHAIN_API_KEY"] = LANGSMITH_API_KEY

# =========================================================
# MODELS
# =========================================================

DEFAULT_TEXT_MODEL = os.getenv(
    "MODEL_NAME",
    "llama-3.1-8b-instant",
)

DEFAULT_MULTIMODAL_MODEL = os.getenv(
    "VISION_MODEL",
    "meta-llama/llama-4-scout-17b-16e-instruct"
)

DEFAULT_WHISPER_MODEL = os.getenv(
    "WHISPER_MODEL",
    "whisper-large-v3"
)

# =========================================================
# MAIN LLM
# =========================================================

llm = ChatGroq(
    model=DEFAULT_TEXT_MODEL,
    groq_api_key=GROQ_API_KEY
)

vision_llm = ChatGroq(
    model=DEFAULT_MULTIMODAL_MODEL,
    groq_api_key=GROQ_API_KEY
)

# =========================================================
# PROJECT DIRECTORIES
# =========================================================

RECORDINGS_DIR = "recordings"
IMAGES_DIR = "images"
OUTPUTS_DIR = "outputs"
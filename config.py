"""Project configuration for the Personal Chef Agent.

Keep this file small and easy to edit while experimenting in notebooks.
"""

import os

from dotenv import load_dotenv


load_dotenv()

# Add your real API key in the local .env file.
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Update these model names as you experiment with Groq and Llama models.
DEFAULT_TEXT_MODEL = "llama-3.1-8b-instant"
DEFAULT_MULTIMODAL_MODEL = "llama-3.2-11b-vision-preview"
DEFAULT_WHISPER_MODEL = "whisper-large-v3"

# Common project folders.
RECORDINGS_DIR = "recordings"
IMAGES_DIR = "images"
OUTPUTS_DIR = "outputs"

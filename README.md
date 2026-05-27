# Personal Chef Agent

A lightweight Python project for experimenting with an AI-based Personal Chef Agent in Jupyter notebooks.

The goal is to keep the project simple while supporting:

- Groq API calls
- Llama multimodal models
- image understanding
- audio transcription with Whisper-compatible workflows
- notebook-based experimentation

## Project Structure

```text
personal-chef-agent/
├── .venv/
├── .env
├── requirements.txt
├── README.md
├── notebooks/
│   ├── chef_agent.ipynb
│   ├── image_testing.ipynb
│   └── audio_testing.ipynb
├── utils.py
├── config.py
├── recordings/
├── images/
└── outputs/
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your Groq API key to `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

4. Start Jupyter:

```bash
jupyter notebook
```

Open the notebooks in the `notebooks/` folder and experiment from there.

## Files

- `config.py`: loads environment variables and keeps shared model settings.
- `utils.py`: contains helper functions for images, audio files, and saving outputs.
- `notebooks/chef_agent.ipynb`: main notebook for building the chef agent.
- `notebooks/image_testing.ipynb`: notebook for testing image understanding.
- `notebooks/audio_testing.ipynb`: notebook for testing audio transcription.

## Notes

Keep API keys in `.env` and do not commit real secrets to git.

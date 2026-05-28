# Agentic PersonalChef

> An experimental multimodal AI system that analyzes fridge inventory, understands voice queries, and generates personalized recipes — powered by LangGraph agentic workflows, Groq LLMs, and real-time web search.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Agentic-green?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-Workflows-orange?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LPU%20Inference-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active%20Prototype-yellow?style=flat-square)

---

## Overview

**Agentic PersonalChef** is a research-grade AI prototype exploring the intersection of multimodal perception, agentic reasoning, and real-world culinary assistance. The system processes inputs across three modalities — text, image, and audio — and orchestrates an LLM-powered agent to generate personalized, search-augmented recipe recommendations based on whatever ingredients a user actually has available.

This project serves as a practical testbed for applied agentic AI design patterns: tool use, memory, multimodal context handling, and stateful multi-turn conversation — all implemented on a modern, extensible Python stack.

**Real-world use cases this architecture targets:**

- Reducing food waste by surfacing recipes for available ingredients
- Voice-driven cooking assistance for hands-free kitchen interaction
- Fridge scanning for automatic inventory detection via computer vision
- Personalized nutrition-aware meal planning at scale

---

## Core Capabilities

| Capability | Description |
|---|---|
| Conversational Recipe Agent | Stateful multi-turn chef agent with persistent memory via LangGraph checkpointing |
| Fridge Vision Analysis | Uploads a fridge image; the multimodal LLM identifies all visible ingredients automatically |
| Voice Query Input | Records user speech, transcribes via Whisper, and routes the query into the agent pipeline |
| Web-Augmented Reasoning | Tavily search integration allows the agent to retrieve current recipes and nutritional data |
| Personalized Recommendations | Combines detected inventory with user preferences and dietary goals |
| Macro Estimation | Optionally generates protein/carb/fat breakdowns per suggested recipe |
| Modular Notebook Architecture | Each capability is isolated in a dedicated experimental notebook for clean iteration |

---

## Multimodal AI Pipeline

The system handles three input modalities in a unified agentic loop:

```
[Text Input]  ──────────────────────────────────┐
                                                 ▼
[Image Input] ──► Vision LLM (Llama 4 Scout) ──► Ingredient Inventory
                                                 ▼
[Audio Input] ──► Whisper Transcription ────────► User Query
                                                 ▼
                                         LangGraph Chef Agent
                                                 ▼
                                    Tavily Web Search (tool use)
                                                 ▼
                                    Personalized Recipe Response
```

**Text:** Direct conversational queries processed by the primary LLM via LangGraph's `create_agent` with `InMemorySaver` checkpointing for multi-turn coherence.

**Image:** A base64-encoded fridge photo is passed to the Llama 4 Scout vision model, which returns a structured ingredient inventory. This inventory feeds directly into the recipe generation prompt.

**Audio:** `sounddevice` captures microphone input; `scipy` writes a WAV file; the Groq Whisper API transcribes the audio. The resulting text becomes the user query in the agent pipeline.

---

## Architecture

This project is structured as a **rapid AI experimentation environment** — a deliberate architectural choice that enables fast iteration across model configurations, prompt strategies, and multimodal input combinations without the overhead of premature deployment abstractions.

```
┌─────────────────────────────────────────────────┐
│              Notebook Experimentation Layer      │
│  chef_agent.ipynb  │  image_testing.ipynb       │
│  audio_testing.ipynb                             │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│               Shared Utility Layer               │
│  config.py — model config, API init, env vars   │
│  utils.py  — image load, audio I/O, output save │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              AI Processing Pipeline              │
│  LangGraph Agent  ◄──── Tavily Web Search       │
│  LangChain Groq   ◄──── Llama 3.1 / Llama 4    │
│  Whisper API      ◄──── Groq ASR Endpoint       │
└─────────────────────────────────────────────────┘
```

**Design principles:**

- **Separation of concerns** — configuration, utilities, and experiment notebooks are fully decoupled
- **Modular model routing** — text and vision workflows use distinct LLM instances, swappable via environment variables
- **Stateful agent memory** — `InMemorySaver` checkpointing enables coherent multi-turn sessions without external storage dependencies
- **Tracing enabled** — LangSmith integration is wired in from day one for observability during experimentation

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13+ |
| Experimentation Environment | Jupyter Notebook |
| LLM Orchestration | LangChain, LangGraph |
| LLM Inference | Groq (LPU-accelerated) |
| Text Model | Llama 3.1 8B Instant |
| Vision Model | Meta Llama 4 Scout 17B |
| Speech Transcription | Whisper Large v3 (via Groq API) |
| Web Search | Tavily Search API |
| Audio Capture | sounddevice, scipy |
| Image Processing | Pillow (PIL) |
| Notebook Widgets | ipywidgets (file upload UI) |
| Observability | LangSmith tracing |
| Dependency Management | python-dotenv, venv |

---

## Project Structure

```
Agentic_PersonalChef/
├── notebooks/
│   ├── chef_agent.ipynb          # Core agentic chef workflow
│   ├── image_testing.ipynb       # Multimodal fridge vision experiments
│   └── audio_testing.ipynb       # Whisper transcription pipeline
├── config.py                     # Model config, API keys, LLM instances
├── utils.py                      # Image loading, audio I/O, output helpers
├── requirements.txt              # Pinned dependencies
├── .env.example                  # Environment variable template
├── .gitignore                    # Excludes API keys, checkpoints, outputs
├── recordings/                   # Audio input files (git-ignored)
├── images/                       # Image inputs (git-ignored)
└── outputs/                      # Agent response outputs (git-ignored)
```

---

## Engineering Highlights

**Agentic tool use in practice.** The chef agent is built on LangGraph's `create_agent` primitive with a `web_search` tool wired via the Tavily client. This demonstrates real tool-calling behavior — the agent decides when to search and synthesizes results into structured recipe output.

**Multimodal context chaining.** The vision and text pipelines are explicitly chained: the fridge image produces an ingredient inventory string, which becomes grounding context for the downstream recipe agent. This mirrors production RAG and perception-action loops.

**Voice-to-recipe end-to-end.** The audio pipeline captures microphone input, transcribes via Whisper, and merges the transcription with visual inventory data into a unified agent prompt — demonstrating a complete multimodal input fusion pattern.

**Configurable model routing.** `config.py` exposes all model identifiers as environment variables (`MODEL_NAME`, `VISION_MODEL`, `WHISPER_MODEL`), making model swaps zero-code changes.

**LangSmith-ready observability.** Tracing is enabled from project initialization, enabling full agent trace inspection during development — a practice that transfers directly to production monitoring.

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Agentic_PersonalChef.git
cd Agentic_PersonalChef

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Add your API keys to .env:
#   GROQ_API_KEY=...
#   TAVILY_API_KEY=...
#   LANGSMITH_API_KEY=...  (optional, for tracing)

# 5. Launch Jupyter
jupyter notebook
```

---

## Usage

**Text-based recipe generation:**

Open `notebooks/chef_agent.ipynb`, run the setup cells, then invoke the agent:

```python
response = agent.invoke(
    {"messages": [HumanMessage(content="I have leftover rice, eggs, and soy sauce. What can I make?")]},
    config={"configurable": {"thread_id": "session-1"}}
)
print(response["messages"][-1].content)
```

**Image-based fridge scanning:**

Open `chef_agent.ipynb` and run the `FileUpload` widget cell. Upload a photo of your fridge — the vision model will return a structured ingredient inventory, which the agent uses to suggest recipes automatically.

**Voice query:**

Run the audio recording cell to capture 5 seconds of microphone input. The system transcribes it via Whisper and merges it with the fridge inventory for a fully multimodal prompt.

---

## Status

This project is in **active prototype development**. The core agentic pipeline is functional and has been tested end-to-end across all three input modalities. Current focus areas include:

- Refining the multimodal prompt fusion strategy for higher-quality recipe outputs
- Expanding the image understanding pipeline to handle varied lighting and fridge layouts
- Iterating on the agent's system prompt to improve dietary preference handling
- Building out the `audio_testing.ipynb` notebook with a full Whisper evaluation suite

The notebook-based architecture is the deliberate foundation for this phase — it enables rapid hypothesis testing across model configurations, prompt strategies, and input preprocessing approaches before committing to a deployment structure.

---

## Why This Project Stands Out

Most LLM projects stop at a chat interface. This one integrates three input modalities, a real tool-calling agent loop, and a working end-to-end pipeline from fridge photo to structured recipe — built and iterated entirely in a local experimentation environment.

The architecture reflects how production AI systems are actually designed: modular components with clear interfaces, configurable model routing, observability wired in from the start, and a separation between the experimentation layer and the shared utility layer. The notebook environment isn't a limitation — it's the right tool for this phase of development, enabling fast iteration across model choices and prompt strategies that would be slow and risky to test in a deployed system.

For a recruiter or technical reviewer, this project demonstrates: applied LangGraph knowledge, multimodal system integration, real API orchestration (Groq, Tavily, Whisper), and the product thinking to scope a system that solves an actual problem — not just a demo.

---

## Contributing

Contributions, experiments, and feedback are welcome. If you're exploring similar AI systems — multimodal agents, recipe generation, or agentic workflow design — feel free to open an issue or PR.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-idea`)
3. Commit your changes with clear messages
4. Open a pull request with a description of what you explored

For significant changes, open an issue first to discuss the approach.

---
---

## Author

**Prayas**


Building at the intersection of agentic systems, multimodal AI, and practical product engineering.

---

*Built with Python · LangGraph · Groq · Tavily · Whisper*

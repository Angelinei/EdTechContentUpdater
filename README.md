<<<<<<< HEAD
<<<<<<< HEAD
# AgentPro

AgentPro is a flexible framework for building AI agents with multiple specialized tools. This repository allows you to create powerful agents that can search the internet, generate code, analyze YouTube videos, create presentations, and more.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue" alt="License: Apache 2.0">
</p>

## Features

- 🧠 **Flexible Agent Architecture**: Built on the ReAct framework to combine reasoning and action
- 🔧 **Modular Tool System**: Easily extend with custom tools
- 🌐 **Internet Search**: Real-time web search using the Ares API
- 💻 **Code Generation & Execution**: Generate and run Python code on-the-fly
- 🎬 **YouTube Analysis**: Search, extract transcripts, and summarize YouTube videos
- 📊 **Presentation Generation**: Create PowerPoint presentations automatically

## Quick Start

### Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/traversaal-ai/AgentPro.git
cd AgentPro
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory with your API keys:

```
OPENAI_API_KEY=your_openai_api_key
TRAVERSAAL_ARES_API_KEY=your_traversaal_ares_api_key
```
Ares internet tool: Searches the internet for real-time information using the Traversaal Ares API. To get `TRAVERSAAL_ARES_API_KEY`. Follow these steps:

1. Go to the [Traversaal API platform](https://api.traversaal.ai/)
2. Log in or create an account
3. Click **"Create new secret key"**
4. Copy the generated key and paste in `.env` file :

### Running the Agent

From the command line:

```bash
python main.py
```

This starts an interactive session with the agent where you can enter queries.

### Basic Usage

```python
from agentpro import AgentPro, ares_tool, code_tool, youtube_tool
agent = AgentPro(tools=[ares_tool, code_tool, youtube_tool])

# Run a query
response = agent("Generate a summary on the latest AI advancements")
print(response)
```
You can also use the [Quick Start](https://github.com/traversaal-ai/AgentPro/blob/main/agentpro/examples/Quick_Start.ipynb) Jupyter Notebook to run AgentPro directly in Colab.

## 🌍 Traversaal x Optimized AI Hackathon 2025

We’re teaming up with the **Optimized AI Conference 2025** to host a **global hackathon on AI Agents** — open to all developers, builders, researchers, and dreamers working on intelligent systems.

### The Challenge

**Build a real, functional AI Agent** that solves a real-world problem.

This isn’t about flashy demos. We want to see domain-specific, usable, vertical agents — like:
- 🧑‍💼 Customer Support Agents
- 🔬 Research Assistants
- 📊 Data Analyst Agents
- 💡 Or something totally original

You can use any framework, but we recommend trying **[AgentPro](https://github.com/Traversaal/AgentPro)** — our open-source toolkit designed for rapid prototyping and robust architecture.

### Key Dates

- **Hackathon Starts:** April 9, 2025  
- **Submission Deadline:** April 15, 2025  
- **Winners Announced:** April 15, 2025 (Live @ Optimized AI Conference)

### Prizes + Recognition

| Prize Tier         | Reward     |
|--------------------|------------|
| 🥇 Grand Prize      | $1,000     |
| 🥈 Runner-Up        | $500     |
| 🥉 Honorable Mention x2 | $250       |

Plus:
- 1:1 **Mentorship opportunities**
- Invitation to **Traversaal’s AI Fellowship Program**

### Want to be a Judge?
We’re looking for global experts in AI, product, UX, and enterprise applications to help evaluate the submissions. 👉 [Apply to be a Judge](https://forms.gle/zpC4GbEjAkD1osY68)

For more details, follow this [link](https://hackathon.traversaal.ai/)

📩 Questions? Reach us at [hackathon-oai@traversaal.ai](hackathon-oai@traversaal.ai)


## Data Science Agent
https://github.com/user-attachments/assets/aeeb91e4-134e-4a14-bbc4-2523ba236c56


## Tools Overview
The AgentPro toolkit comes with a variety of default tasks, such as:

- **Internet Research**: "What are the latest developments in quantum computing?"
- **Code Generation**: "Create a Python script to analyze stock prices and generate a chart"
- **YouTube Analysis**: "Find and summarize recent videos about machine learning"
- **Presentation Creation**: "Make a presentation about renewable energy sources"

### AresInternetTool

Searches the internet for real-time information using the Traversaal Ares API.

```python
ares_tool = AresInternetTool()
result = ares_tool.run("recent advances in AI")
```

### CodeEngine

Generates and executes Python code based on natural language descriptions.

```python
code_tool = CodeEngine()
result = code_tool.run("create a bar chart comparing FAANG stocks")
```

### YouTubeSearchTool

Searches for YouTube videos, extracts transcripts, and summarizes content.

```python
youtube_tool = YouTubeSearchTool()
result = youtube_tool.run("machine learning tutorials")
```

### SlideGenerationTool

Creates PowerPoint presentations from structured content.

```python
slide_tool = SlideGenerationTool()
slides = [
    {"slide_title": "Introduction", "content": "Overview of the topic"},
    {"slide_title": "Key Points", "content": "The main arguments and findings"}
]
result = slide_tool.run(slides)
```

### DataAnalysisTool

Analyzes data files and provides statistical insights, visualizations, and exploratory data analysis.

```python
data_tool = DataAnalysisTool()

# Basic usage with a file path
result = data_tool.run("path/to/data.csv")

# With specific analysis parameters
analysis_params = {
    "file_path": "path/to/data.csv",
    "analysis_type": "visualization",
    "viz_type": "correlation",
    "columns": ["age", "income", "education"]
}
result = data_tool.run(analysis_params)
```

## Creating Custom Tools

You can create your own tools by extending the `Tool` base class:

```python
from agentpro.tools.base import Tool

class MyCustomTool(Tool):
    name: str = "My Custom Tool"
    description: str = "Description of what your tool does"
    arg: str = "Information about the required input format"

    def run(self, prompt: str) -> str:
        # Your tool implementation here
        return "Result of the tool operation"
```

Then initialize your agent with the custom tool:

```python
custom_tool = MyCustomTool()
agent = AgentPro(tools=[custom_tool, ares_tool, code_tool])
```

## Project Structure

```
agentpro/
├── agentpro/
│   ├── __init__.py
│   ├── agent.py              # Main agent implementation
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── base.py           # Base tool classes
│   │   ├── ares_tool.py      # Internet search
│   │   ├── code_tool.py      # Code generation
│   │   ├── youtube_tool.py   # YouTube analysis
│   │   └── slide_tool.py     # Presentation generation (**Work in progress**)
│   └── examples/
│       ├── __init__.py
│       └── example_usage.py  # Usage examples
├── main.py                   # CLI entry point
├── requirements.txt          # Dependencies
└── .env                      # API keys (create this file)
```

## Requirements

- Python 3.8+
- OpenAI API key
- Traversaal Ares API key (for internet search)

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for more details.
=======
# content-audit-agent
MVP for an autonomous content auditing AI agent
>>>>>>> f3c36162ce27b169800f21b0d4e10f3b98bdbd84
=======
**Traversaal-x-Optimized-AI-Hackathon**

**An autonomous AI agent that audits educational content for outdated, redundant, or missing materials — built with FastAPI for the Traversaal x Optimized AI Hackathon. Designed to integrate effortlessly with Notion, Google Drive, and LMS platforms. Smart. Modular. Ready for scale.**

**Our Approach**

**Problem:** Education teams struggle with manual updates of content and version control.

**Solution:** Automate this with a smart agent that scans documents and gives update suggestions.

**Strategy:** Design a pluggable agent that works with multiple data sources and can be extended to NLP tasks such as summarization, gap detection, or question generation.

Setup Instructions

**1. Clone the repository**

git clone https://github.com/Angelinei/Traversaal-x-Optimized-AI-Hackathon.git
cd Traversaal-x-Optimized-AI-Hackathon

**2. Create a virtual environment**

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

**3. Install dependencies**

pip install -r requirements.txt

**4. Run the app**

uvicorn app.main:app --reload

The API will be available at : http://localhost:8000


**Project Overview**

The **Content Analysis Agent** is built for EdTech teams looking to:

- **Automate audits** of their course materials
- **Detect outdated, redundant, or missing content**
- **Integrate seamlessly** with Google Drive, Notion, LMS, etc. (OAuth-ready)
- Work with **adaptive workflows** using a flexible agentic backend

**Built with :**

- **FastAPI** for high-performance backend
- **Python** for core logic
- Integrations with **LangChain**, **OAuth**, and frontends like **Lovable** or **Zapier**

**Bonus: Built with AgentPro by Traversaal**

This project integrates [AgentPro](https://github.com/traversaal-ai/AgentPro), Traversaal's open-source, production-grade framework for AI agents.

We used AgentPro to structure our content audit agent in modular, testable steps :

- **Step-based execution**
- **Context-aware chaining**
- **FastAPI-compatible and scalable**

**File Structure Explained**

app/main.py: FastAPI entry point

routes/: API endpoints

services/: Core logic for document analysis

models/: Data models and schemas

utils/: File parsing or helper functions

tests/: Unit tests

**Agentic Architecture**

![Agentic Architecture](agentic_diagram)

**✨ Built with love by Angeline Poitout
AI builder • Edtech Specialist since 2021 behind ThreadFlow**
>>>>>>> c8d6895e141bae5f95b3081c1cc5d0a69cd93557
#   E d T e c h C o n t e n t U p d a t e r  
 
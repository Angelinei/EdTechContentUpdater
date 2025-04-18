**Traversaal-x-Optimized-AI-Hackathon**


**An autonomous AI agent that audits educational content for outdated, redundant, or missing materials — built with FastAPI for the Traversaal x Optimized AI Hackathon. Designed to integrate effortlessly with Notion, Google Drive, and LMS platforms. Smart. Modular. Ready for scale.**


**Our Approach**

**Problem:** Education teams struggle with manual updates of content and version control.

**Solution:** Automate this with a smart agent that scans documents and gives update suggestions.

**Strategy:** Design a pluggable agent that works with multiple data sources and can be extended to NLP tasks such as summarization, gap detection, or question generation.


**Project Overview**

The **Content Analysis Agent** is built for EdTech teams looking to:

- **Automate audits** of their course materials
- **Detect outdated, redundant, or missing content**
- **Integrate seamlessly** with Google Drive, Notion, LMS, etc. (OAuth-ready)
- Work with **adaptive workflows** using a flexible agentic backend

Built with :

- **FastAPI** for high-performance backend
- **Python** for core logic
- Integrations with **LangChain**, **OAuth**, and frontends like **Lovable** or **Zapier**

Setup

1. Clone the repo:
   
   git clone https://github.com/Angelinei/EdTechContentUpdater.git
   cd EdTechContentUpdater

Install dependencies:

pip install -r requirements.txt

Set up environment:

Copy .env.example to .env.

Add your OPENPERPLEX_API_KEY in .env.

Run the app:

uvicorn main:app --reload

Usage

Health Check: GET /health

Evaluate Accuracy: POST /api/evaluate-accuracy with JSON like {"topic":"AI education","content_snippet":"AI tutors improve retention"}

Scan PDF: POST /api/scan-pdf with a PDF file


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

 
 

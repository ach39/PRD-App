# 🎯 PM-Sight: Multi-Transcript AI PRD Architect

**PM-Sight** is a high-performance tool designed for Technical Product Managers to solve "Meeting Fatigue." It leverages **Gemini 2.5 Flash** to synthesize multiple meeting transcripts into a single, cohesive Product Requirements Document (PRD).

Unlike standard summarizers, PM-Sight tracks the **evolution of decisions** across multiple syncs—ensuring that technical constraints discussed in a later meetings correctly override initial design assumptions.

## 👨‍💼 CONTEXT

This project was built to demonstrate the intersection of AI Engineering and Product Operations. It showcases the ability to manage long-context LLM windows, handle multi-turn requirements, and build production-ready Streamlit interfaces.

---

## 🚀 KEY FEATURES

1. **Multi-File Context:** Upload multiple `.txt` transcripts (e.g., Kickoff + Tech Sync).
2. **Conflict Resolution:** Identifies when requirements change between meetings.
3. **TPM-Standard Output:** Generates structured PRDs including:
      - Vision & Root Problem
      - Gherkin-style User Stories (Given/When/Then)
      - Technical Constraints & Blockers
      - Named Action Items
4. **Markdown Export:** Download the final PRD for immediate use in Jira, Confluence, or Notion.

---

## 📝 HOW IT WORKS (The TPM Workflow)
1. **Upload Transcripts:** Drag and drop all transcripts related to a specific feature.
2. **AI Processing:** The system uses a "Chain of Density" prompt to extract the most relevant technical and product details.
3. **Review & Export:** Edit the output in the UI and click "Download PRD" to save as a .md file with embedded page breaks for easy PDF printing.

---

## 🛠️ Technical Architecture

- **LLM:** Google Gemini 2.5 Flash (1M Token Context Window)
- **Frontend:** Streamlit 1.54.0
- **Language:** Python 3.14
- **Security:** Environment-based secrets management (python-dotenv)

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/pm-sight-project.git](https://github.com/YOUR_USERNAME/pm-sight-project.git)
   cd pm-sight-project
   pip install -r requirements.txt
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Configure Environment:**  
  Create a .env file and add your Google AI Key.  
    `GOOGLE_API_KEY=your_key_here`
4. **Run the App**
   ```bash
   python -m streamlit run app.py

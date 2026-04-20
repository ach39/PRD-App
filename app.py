import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2
import docx

load_dotenv()

st.set_page_config(page_title="PRD Generator", page_icon=":robot_face:", layout="wide")
st.title("PRD Generator")

# Get API key from sidebar or environment variable
with st.sidebar:
    st.header("API Key")
    # Keep it optional if app in running inside TRAE.
    google_api_key_input = st.text_input("Enter your Google API Key:", type="password", help="You can get your API key from https://aistudio.google.com/app/apikey")
    google_api_key = google_api_key_input or os.getenv("GOOGLE_API_KEY")
    st.markdown("---")
    st.subheader("LLM")
    st.markdown("gemini-2.5-flash")

def generate_prd(api_key, transcript_content):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""**Persona:** You are a Senior Technical Product Manager at a Tier-1 tech firm.

    **Task:** Ingest one or more long meeting transcripts and synthesize them into a single, cohesive PRD (Product Requirements Document). Pay special attention to the 'Evolution of Decisions': If a requirement was discussed in one meeting but changed in a later one, ensure the final PRD reflects the LATEST agreement.

    **Instructions:**
    Based on the following transcript(s), generate a PRD with the following sections:

    *   **[VISION]:** A 1-2 line statement stating the vision behind this feature.
    *   **[PROBLEM STATEMENT]:** Capture the pain-point, the 'Why' behind it, instead of just summarizing the meeting notes.
    *   **[SOLUTION]:** An executive summary of the solution. Add architecture diagram if applicable. Add high-level flow chart if applicable.Add any assumptions made.
    *   **[TRADEOFFS]:** Discuss the different tradeoffs mentioned in the transcript, including the pros and cons of each. Do not make up tradeoffs.
    *   **[CONSTRAINTS]:** Capture any technical or non-technical constraints discussed.
    *   **[DOGS NOT BARKING]:** Mention any issues/constraints that were not brought up in the meeting but are worth considering to minimize risks.
    *   **[USER STORIES]:** Add user stories in INVEST format.
    *   **[APPENDIX]:** Add appendix on next page, where meeting-notes and action items are included. Meeting notes are succint and captures key takeaways in bullet format.Meeting notes must be easy to read and must be formatted with appropriarte number format. Each action item must have an owner and completion date and must be presented in a tabular format. Action-items table should have following columns - 'Action Item', 'Owner', 'completion date', 'Status'. 
     

    **Transcript(s):**
    {transcript_content}

    **PRD:**
    """
    response = model.generate_content(prompt)
    return response.text

def get_text_from_file(uploaded_file):
    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    return ""

st.header("Upload Transcripts")
uploaded_files = st.file_uploader("Upload one or more transcript files (.txt, .pdf, .doc, .docx)", type=["txt", "pdf", "doc", "docx"], accept_multiple_files=True)

if st.button("Generate PRD"):
    if uploaded_files:
        with st.spinner(f"Reading {len(uploaded_files)} files..."):
            transcript_content = ""
            file_names = []
            for uploaded_file in uploaded_files:
                file_names.append(uploaded_file.name)
                transcript_content += get_text_from_file(uploaded_file) + "\n\n"
        
        st.success(f"Successfully uploaded and processed {len(uploaded_files)} files: {', '.join(file_names)}")
        
        if google_api_key:
            with st.spinner("Generating PRD..."):
                try:
                    prd = generate_prd(google_api_key, transcript_content)
                    st.session_state.prd = prd
                except Exception as e:
                    st.error(f"An error occurred during PRD generation: {e}")
        else:
            st.error("Please enter your Google API Key in the sidebar or set the GOOGLE_API_KEY environment variable.")
    else:
        st.error("Please upload at least one transcript file.")

if "prd" in st.session_state:
    st.header("Generated PRD")
    st.markdown(st.session_state.prd)
    st.download_button(
        label="Download PRD as Markdown",
        data=st.session_state.prd,
        file_name="prd.md",
        mime="text/markdown",
    )

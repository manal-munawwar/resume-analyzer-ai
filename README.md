# Resume Analyzer AI 📈

An AI-powered Streamlit app that compares an uploaded PDF resume against a pasted job description and generates a full hiring-readiness report: ATS score, shortlisting probability, good-fit highlights, areas of improvement, skill-match breakdown, and a SWOT analysis — all via Google's Gemini model.

## How It Works

1. **Upload** — You drop a PDF resume in the sidebar and paste a job description (up to 20,000 characters) in the main text area.
2. **Extraction** — `pdf.py` uses `pypdf` to read every page of the resume and concatenate the extracted text.
3. **Analysis** — `analysis.py` sends **6 separate prompts** to Gemini (`gemini-2.5-flash-lite`), each asking the model to compare the resume text against the job description and return at least 5 bullet points covering:
   - **ATS Score** (0–100) — keyword matches, skills alignment, experience relevance, education fit, formatting/ATS-readability
   - **Shortlisting Probability** (0–100) — core skill match, experience vs. requirement, domain relevance, certifications, role alignment
   - **Good Fit** — matching skills, achievements, soft skills, domain knowledge, role alignment
   - **Areas of Improvement** — missing skills, experience gaps, missing certifications, formatting issues, tailoring opportunities
   - **Skill Match** — technical/soft skills alignment and gaps
   - **SWOT Analysis** — Strengths, Weaknesses, Opportunities, Threats
4. **Display** — Each section's response is rendered directly in the Streamlit app.

## Tech Stack

| Component | Library |
|---|---|
| UI | Streamlit |
| AI model | `google-generativeai` (Gemini 2.5 Flash Lite) |
| PDF parsing | `pypdf` |
| Config | python-dotenv |

## Project Structure

```
resume-analyzer-ai/
├── interface.py        # Streamlit UI: file uploader, JD text area, triggers analysis
├── analysis.py          # Builds the 6 Gemini prompts and renders results
├── pdf.py                # Extracts raw text from the uploaded PDF resume
├── requirements.txt      # streamlit, google-generativeai, python-dotenv, pypdf
├── LICENSE                # MIT
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9+
- A [Google AI Studio](https://aistudio.google.com/) API key

### Installation

```bash
git clone https://github.com/manal-munawwar/resume-analyzer-ai.git
cd resume-analyzer-ai
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Run

```bash
streamlit run interface.py
```

### Usage

1. In the sidebar, upload your resume as a **PDF**.
2. Paste the target **job description** into the main text area.
3. Click **Get Results**.
4. Review the six generated sections: ATS score, shortlisting probability, good-fit points, improvement areas, skill match, and SWOT analysis.

## Notes & Limitations

- Each click triggers **6 separate Gemini API calls** — this is more thorough but slower and uses more quota than a single combined prompt.
- No error handling if the API key is missing/invalid beyond what the SDK raises by default.
- `pdf.py`'s exception handler currently swallows the actual error message (`except Exception as e:` returns a generic string instead of including `e`) — worth fixing for easier debugging.
- Resume parsing relies on extractable text; scanned/image-only PDFs won't work without OCR.
- Results are free-form text from the LLM, not structured/validated JSON — scores are descriptive, not guaranteed-numeric fields you can reliably parse downstream.

## Possible Improvements

- Combine the 6 prompts into a single structured (JSON) response to reduce API calls and latency
- Add OCR fallback for scanned resumes
- Persist/export the report (PDF or Markdown download)
- Add a progress indicator per section instead of one global spinner

## License

MIT — see [LICENSE](LICENSE).

## Author

**Manal Munawwar**
- GitHub: [@manal-munawwar](https://github.com/manal-munawwar)
- LinkedIn: [manal-munawwar](https://www.linkedin.com/in/manal-munawwar/)

import os
from pyexpat import model 
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

from pdf import extract_text    # method in pdf.py to extract text from the pdf document

key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

model = genai.GenerativeModel('gemini-2.5-flash-lite')

def analyze_resume(pdf_doc, job_des):
    
    if pdf_doc is not None:
        pdf_text = extract_text(pdf_doc) # to extract text from the pdf document using the method in pdf.py
        st.write(f"Resume Text Extracted Successfully: ")
        
    else:
        st.write('Error !! Drop the file again and make sure it is a valid pdf document')
        
    ats_score = model.generate_content(f'''Compare the given resume {pdf_text} with the job description {job_des}.
Provide an ATS score on a scale of 0 to 100.
Explain the score in at least 5 bullet points, focusing on:
- Keyword matches
- Relevant skills alignment
- Experience relevance
- Education fit
- Formatting or ATS-readability issues''')
    
    probability = model.generate_content(f'''Compare the given resume {pdf_text} with the job description {job_des}.
Estimate the probability of being shortlisted on a scale of 0 to 100.
Explain the probability in at least 5 bullet points, covering:
- Core skill match
- Years of experience vs. requirement
- Industry/domain relevance
- Certifications or qualifications
- Overall role alignment''') 
    
    good_fit = model.generate_content(f'''Compare the given resume {pdf_text} with the job description {job_des}.
Provide at least 5 bullet points explaining why the candidate is a good fit.
Focus on:
- Matching technical skills
- Relevant achievements
- Transferable soft skills
- Industry/domain knowledge
- Alignment with role responsibilities''')
    
    areas_of_improvement = model.generate_content(f'''Compare the given resume {pdf_text} with the job description {job_des}.
Provide at least 5 bullet points highlighting areas of improvement.
Cover:
- Missing or weak skills
- Gaps in experience
- Certifications not listed
- Resume formatting issues
- Opportunities to tailor content to the job description''')
    
    skill_match = model.generate_content(f'''Compare the given resume {pdf_text} with the job description {job_des}.
Identify and evaluate the skill match between the candidate and the role.
Generate at least 5 bullet points that highlight:
- Core technical skills that align
- Soft skills relevant to the role
- Industry/domain-specific expertise
- Transferable skills that strengthen the profile
- Any missing or partially matched skills
''')
    
    SWOT_analysis = model.generate_content(f'''Compare the given resume {pdf_text} with the job description {job_des}.
Provide a SWOT analysis in at least 5 bullet points:
- Strengths: skills/experiences that match
- Weaknesses: gaps or missing elements
- Opportunities: transferable skills or potential growth areas
- Threats: competition, ATS filtering risks, or overqualification''')
    
    return (st.write(ats_score.text), 
            st.write(probability.text), 
            st.write(good_fit.text), 
            st.write(areas_of_improvement.text), 
            st.write(skill_match.text),
            st.write(SWOT_analysis.text))
    
    
    
    
    
        
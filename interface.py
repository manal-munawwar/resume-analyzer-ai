import streamlit as st

from analysis import analyze_resume # method in analysis.py to analyze the resume and job description and provide results
st.set_page_config("Resume Analyzer", page_icon="📈")

st.title(":red[Resume Analyzer using AI 📈💰📊]")

st.title(':blue[AI powered Resume Analyzer with given Job Description using AI 📋]')

st.subheader('''This page helps you to compare the resume and the given job description and provide an ATS score, probability of being shortlisted, good fit points and areas of improvement points, and SWOT analysis. 💯🚀🎯''')

st.sidebar.subheader("Drop you resume here 👇")

pdf_doc = st.sidebar.file_uploader('CLICK HERE', type=['pdf'])

st.sidebar.markdown('Designed and Developed by : Manal Munawwar 👀')
st.sidebar.markdown('https://github.com/manal-munawwar/resume-analyzer-ai')
st.sidebar.markdown('Feel free to connect with me on LinkedIn: https://www.linkedin.com/in/manal-munawwar/')

job_des = st.text_area('Copy and paste the JD here 👇', max_chars=20000)

submit = st.button('Get Results 🎯')

if submit:
    with st.spinner('Loading... ⏳'):
        analyze_resume(pdf_doc, job_des)
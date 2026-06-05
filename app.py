import streamlit as st

from utils.pdf_parser import *
from utils.skill_matcher import *
from utils.groq_helper import *

st.title(
    "AI Placement Prep Assistant"
)

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

jd = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze"):

    if resume and jd:

        resume_text = extract_text_from_pdf(
            resume
        )

        resume_skills = extract_skills(
            resume_text
        )

        jd_skills = extract_skills(
            jd
        )

        score, matched, missing = \
            calculate_match_score(
                resume_skills,
                jd_skills
            )

        st.success(
            f"Match Score: {score:.2f}%"
        )

        st.subheader(
            "Matched Skills"
        )

        st.write(matched)

        st.subheader(
            "Missing Skills"
        )

        st.write(missing)

        analysis = analyze_resume(
            resume_text,
            jd
        )

        st.subheader(
            "AI Analysis"
        )

        st.write(analysis)

        questions = \
            generate_interview_questions(
                jd
            )

        st.subheader(
            "Interview Questions"
        )

        st.write(questions)
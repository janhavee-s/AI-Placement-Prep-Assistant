from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(resume_text, jd):

    prompt = f"""
    Analyze this resume against the job description.

    Resume:
    {resume_text}

    Job Description:
    {jd}

    Give:

    1. ATS Score out of 100
    2. Missing Skills
    3. Strengths
    4. Resume Improvements
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content


def generate_questions(jd):

    prompt = f"""
    Generate:

    5 Technical Questions

    5 HR Questions

    Based on this JD:

    {jd}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content


def generate_interview_questions(job_description):

    prompt = f"""
    Based on the following job description,
    generate:

    5 Technical Interview Questions

    5 HR Interview Questions

    Job Description:
    {job_description}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
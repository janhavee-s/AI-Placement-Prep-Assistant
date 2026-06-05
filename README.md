# AI Placement Prep Assistant

https://ai-placement-prep-assistant-y2gmflwd75uhbi5ikedqxy.streamlit.app/

https://youtu.be/YXIOS2ipTkk?si=SmJLu4uj16OKwV9k

## Overview

AI Placement Prep Assistant is an AI-powered tool designed to help college students and fresh graduates improve their placement and job application process. The application analyzes a resume against a target job description, identifies missing skills, provides ATS-friendly feedback, and generates personalized interview questions.

This project was built as part of the Amplify Builder Challenge with the goal of solving a real problem faced by students during internship and placement season.

---

## Problem

Many students apply to internships and jobs using the same resume for every role. This often results in:

* Poor alignment between resumes and job descriptions
* Missing keywords required by Applicant Tracking Systems (ATS)
* Difficulty identifying skill gaps
* Time-consuming manual resume reviews
* Lack of role-specific interview preparation

Current solutions are often spread across multiple platforms, requiring students to switch between resume checkers, interview preparation websites, and career guidance resources.

---

## What I Tried

I wanted to create a single platform that could help students understand how well their resume matches a specific job role and provide actionable feedback.

The application currently:

1. Extracts text from uploaded resume PDFs
2. Identifies technical skills from resumes and job descriptions
3. Calculates a skill match score
4. Highlights missing skills
5. Uses an LLM to generate ATS-style feedback
6. Generates role-specific interview questions

I initially attempted to use the Gemini API for AI-powered analysis. However, due to API access restrictions on my Google project, I switched to the Groq API with Llama 3.3, which provided reliable and fast responses.

---

## Features

### Resume Analysis

* Upload a resume PDF
* Extract resume content automatically

### Skill Matching

* Compare resume skills with job description requirements
* Display matching skills
* Display missing skills

### ATS Feedback

* Resume strengths
* Areas for improvement
* ATS-style recommendations

### Interview Preparation

* Technical interview questions
* Behavioral interview questions
* Role-specific preparation guidance

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Groq API
* Llama 3.3 70B

### Libraries

* Streamlit
* PDFPlumber
* Pandas
* Python Dotenv
* Groq

---

## Project Structure

```text
AI-Placement-Prep-Assistant/

├── app.py
├── requirements.txt
├── README.md

├── data/
│   └── skills.csv

├── utils/
│   ├── pdf_parser.py
│   ├── skill_matcher.py
│   └── groq_helper.py
```

---

## How to Run

### Clone Repository

```bash
git clone <repository-url>
cd AI-Placement-Prep-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## Current Limitations

This project is an MVP (Minimum Viable Product).

Current limitations include:

* Skill extraction is based on a predefined skills list
* ATS scoring is AI-generated rather than calculated using a dedicated ATS engine
* No resume PDF report export yet
* No mock interview simulation yet
* Limited support for non-technical job roles

---

## Future Improvements

* Resume bullet-point enhancement
* Personalized learning roadmap generation
* Mock interview simulator
* ATS score visualization dashboard
* Resume improvement tracking
* PDF report generation
* Support for multiple job roles and industries

---

## What I Learned

Through this project I learned:

* Building AI-powered applications with Streamlit
* Integrating LLM APIs into production workflows
* Resume parsing and skill extraction techniques
* Prompt engineering for career guidance tasks
* Deploying AI applications publicly
* Handling API integration and troubleshooting challenges

---

## Builder Challenge Reflection

This project demonstrated how AI can simplify placement preparation by combining resume analysis, skill-gap identification, ATS feedback, and interview preparation into a single workflow. While the current version is a work in progress, it successfully validates the idea and provides a foundation for future improvements.

---

## Author

**Janhavee Singh**

B.Tech Computer Science | Artificial Intelligence | Machine Learning | Data Science

AI Placement Prep Assistant demonstrates the integration of resume intelligence, skill-gap analysis, ATS optimization, and AI-driven career guidance to help students and fresh graduates navigate the placement process more effectively. By combining resume evaluation, job-description matching, and personalized interview preparation, the project aims to create a transparent, accessible, and student-focused career readiness platform powered by modern AI technologies.

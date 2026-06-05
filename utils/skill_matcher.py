import pandas as pd

skills = pd.read_csv("data/skills.csv")

skill_list = skills.iloc[:,0].tolist()


def extract_skills(text):

    found = []

    for skill in skill_list:

        if skill.lower() in text.lower():

            found.append(skill)

    return list(set(found))

def calculate_match_score(
        resume_skills,
        jd_skills
):

    matched = list(
        set(resume_skills)
        &
        set(jd_skills)
    )

    missing = list(
        set(jd_skills)
        -
        set(resume_skills)
    )

    score = (
        len(matched)
        /
        max(len(jd_skills),1)
    ) * 100

    return score, matched, missing
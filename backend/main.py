from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .database import SessionLocal
from .models import (
    Student,
    Internship,
    Application,
    Project,
    SavedProject
)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# REQUEST MODELS
# =========================================================

class StudentRegister(BaseModel):

    name: str
    email: str
    password: str
    branch: str


class StudentLogin(BaseModel):

    email: str
    password: str


class ProfileUpdate(BaseModel):

    college: str
    degree: str
    graduation_year: str
    technical_skills: str
    interests: str
    projects: str
    certifications: str


class SkillsUpdate(BaseModel):

    skills: str


class InterestsUpdate(BaseModel):

    interests: str


# =========================================================
# BASIC ROUTES
# =========================================================

@app.get("/")
def home():

    return {
        "message": "AI Internship Matcher Backend is Working!"
    }


@app.get("/test")
def test():

    return {
        "status": "success",
        "message": "Backend API is working correctly!"
    }


# =========================================================
# REGISTER
# =========================================================

@app.post("/register")
def register_student(
    student: StudentRegister
):

    db = SessionLocal()

    existing_student = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing_student:

        db.close()

        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    new_student = Student(
        name=student.name,
        email=student.email,
        password=student.password,
        branch=student.branch
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    db.close()

    return {
        "message": "Student registered successfully!",
        "student_id": new_student.id
    }


# =========================================================
# LOGIN
# =========================================================

@app.post("/login")
def login_student(
    student: StudentLogin
):

    db = SessionLocal()

    existing_student = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if not existing_student:

        db.close()

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    if existing_student.password != student.password:

        db.close()

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    student_id = existing_student.id

    student_name = existing_student.name

    db.close()

    return {
        "message": "Login successful!",
        "student_id": student_id,
        "name": student_name
    }


# =========================================================
# GET STUDENT
# =========================================================

@app.get("/student/{student_id}")
def get_student(
    student_id: int
):

    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    student_data = {

        "id": student.id,

        "name": student.name,

        "email": student.email,

        "branch": student.branch,

        "college": student.college,

        "degree": student.degree,

        "graduation_year": student.graduation_year,

        "technical_skills": student.technical_skills,

        "selected_skills": student.selected_skills,

        "interests": student.interests,

        "projects": student.projects,

        "certifications": student.certifications

    }

    db.close()

    return student_data


# =========================================================
# UPDATE PROFILE
# =========================================================

@app.put("/student/{student_id}/profile")
def update_profile(
    student_id: int,
    profile: ProfileUpdate
):

    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    student.college = profile.college

    student.degree = profile.degree

    student.graduation_year = profile.graduation_year

    student.technical_skills = profile.technical_skills

    student.interests = profile.interests

    student.projects = profile.projects

    student.certifications = profile.certifications

    db.commit()

    db.close()

    return {
        "message": "Profile updated successfully!"
    }


# =========================================================
# UPDATE SKILLS
# =========================================================

@app.put("/student/{student_id}/skills")
def update_skills(
    student_id: int,
    skills_data: SkillsUpdate
):

    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    student.selected_skills = skills_data.skills

    db.commit()

    db.close()

    return {
        "message": "Skills saved successfully!"
    }


# =========================================================
# UPDATE INTERESTS
# =========================================================

@app.put("/student/{student_id}/interests")
def update_interests(
    student_id: int,
    interests_data: InterestsUpdate
):

    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    student.interests = interests_data.interests

    db.commit()

    db.close()

    return {
        "message": "Interests saved successfully!"
    }


# =========================================================
# GET ALL INTERNSHIPS
# =========================================================

@app.get("/internships")
def get_internships():

    db = SessionLocal()

    internships = db.query(
        Internship
    ).all()

    result = []

    for internship in internships:

        result.append({

            "id": internship.id,

            "title": internship.title,

            "company": internship.company,

            "description": internship.description,

            "skills": internship.skills,

            "duration": internship.duration,

            "location": internship.location

        })

    db.close()

    return result


# =========================================================
# GET SINGLE INTERNSHIP
# =========================================================

@app.get("/internships/{internship_id}")
def get_internship(
    internship_id: int
):

    db = SessionLocal()

    internship = db.query(
        Internship
    ).filter(
        Internship.id == internship_id
    ).first()

    if not internship:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Internship not found"
        )

    result = {

        "id": internship.id,

        "title": internship.title,

        "company": internship.company,

        "description": internship.description,

        "skills": internship.skills,

        "duration": internship.duration,

        "location": internship.location

    }

    db.close()

    return result


# =========================================================
# APPLY FOR INTERNSHIP
# =========================================================

@app.post(
    "/student/{student_id}/apply/{internship_id}"
)
def apply_internship(
    student_id: int,
    internship_id: int
):

    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    internship = db.query(Internship).filter(
        Internship.id == internship_id
    ).first()

    if not internship:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Internship not found"
        )

    existing_application = db.query(
        Application
    ).filter(
        Application.student_id == student_id,
        Application.internship_id == internship_id
    ).first()

    if existing_application:

        db.close()

        raise HTTPException(
            status_code=400,
            detail="You have already applied for this internship."
        )

    application = Application(

        student_id=student_id,

        internship_id=internship_id,

        status="Applied"

    )

    db.add(application)

    db.commit()

    db.refresh(application)

    db.close()

    return {

        "message": "Application submitted successfully!",

        "application_id": application.id,

        "status": "Applied"

    }


# =========================================================
# GET STUDENT APPLICATIONS
# =========================================================

@app.get(
    "/student/{student_id}/applications"
)
def get_student_applications(
    student_id: int
):

    db = SessionLocal()

    applications = db.query(
        Application
    ).filter(
        Application.student_id == student_id
    ).all()

    result = []

    for application in applications:

        internship = db.query(
            Internship
        ).filter(
            Internship.id == application.internship_id
        ).first()

        result.append({

            "application_id": application.id,

            "internship_id": application.internship_id,

            "internship_title":
                internship.title
                if internship
                else None,

            "company":
                internship.company
                if internship
                else None,

            "status": application.status

        })

    db.close()

    return result


# =========================================================
# HELPER: GET STUDENT SKILLS
# =========================================================

def get_student_skills(student):

    student_skills = set()

    if student.selected_skills:

        student_skills.update(

            skill.strip().lower()

            for skill
            in student.selected_skills.split(",")

            if skill.strip()

        )

    if student.technical_skills:

        student_skills.update(

            skill.strip().lower()

            for skill
            in student.technical_skills.split(",")

            if skill.strip()

        )

    return student_skills


# =========================================================
# HELPER: SKILL OVERLAP
# =========================================================

def calculate_skill_overlap(
    student_skills,
    required_skills
):

    if not required_skills:

        return 0

    matched_skills = (
        student_skills & required_skills
    )

    return round(
        len(matched_skills)
        / len(required_skills)
        * 100
    )


# =========================================================
# HELPER: TF-IDF COSINE SIMILARITY
# =========================================================

def calculate_tfidf_similarity(
    student_text,
    target_text
):

    if not student_text.strip():
        return 0

    if not target_text.strip():
        return 0

    try:

        vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        vectors = vectorizer.fit_transform(
            [
                student_text,
                target_text
            ]
        )

        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

        return similarity * 100

    except Exception:

        return 0


# =========================================================
# HELPER: CREATE STUDENT PROFILE TEXT
# =========================================================

def create_student_profile_text(
    student
):

    parts = [

        student.name or "",

        student.branch or "",

        student.college or "",

        student.degree or "",

        student.technical_skills or "",

        student.selected_skills or "",

        student.interests or "",

        student.projects or "",

        student.certifications or ""

    ]

    return " ".join(parts)


# =========================================================
# AI INTERNSHIP RECOMMENDATIONS
# =========================================================

@app.get(
    "/student/{student_id}/recommendations"
)
def get_recommendations(
    student_id: int
):

    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student_skills = get_student_skills(
        student
    )

    student_text = create_student_profile_text(
        student
    )

    internships = db.query(
        Internship
    ).all()

    recommendations = []

    for internship in internships:

        required_skills = set()

        if internship.skills:

            required_skills = set(

                skill.strip().lower()

                for skill
                in internship.skills.split(",")

                if skill.strip()

            )

        skill_match = calculate_skill_overlap(
            student_skills,
            required_skills
        )

        internship_text = " ".join([

            internship.title or "",

            internship.company or "",

            internship.description or "",

            internship.skills or "",

            internship.location or "",

            internship.duration or ""

        ])

        tfidf_match = calculate_tfidf_similarity(
            student_text,
            internship_text
        )

        # Hybrid AI score
        #
        # 70% = skill matching
        # 30% = TF-IDF text similarity

        final_match = round(

            (
                skill_match * 0.70
            )
            +
            (
                tfidf_match * 0.30
            )

        )

        if final_match > 100:

            final_match = 100

        if final_match < 0:

            final_match = 0

        recommendations.append({

            "internship_id":
                internship.id,

            "title":
                internship.title,

            "company":
                internship.company,

            "skills":
                internship.skills,

            "duration":
                internship.duration,

            "location":
                internship.location,

            "match_percentage":
                final_match

        })

    recommendations.sort(

        key=lambda x:
            x["match_percentage"],

        reverse=True

    )

    db.close()

    return recommendations


# =========================================================
# GET ALL PROJECTS
# =========================================================

@app.get("/projects")
def get_projects():

    db = SessionLocal()

    projects = db.query(
        Project
    ).all()

    result = []

    for project in projects:

        result.append({

            "project_id":
                project.id,

            "title":
                project.title,

            "description":
                project.description,

            "skills":
                project.skills,

            "category":
                project.category

        })

    db.close()

    return result


# =========================================================
# AI PROJECT RECOMMENDATIONS
# =========================================================

@app.get(
    "/student/{student_id}/project-recommendations"
)
def get_project_recommendations(
    student_id: int
):

    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student_skills = get_student_skills(
        student
    )

    student_text = create_student_profile_text(
        student
    )

    projects = db.query(
        Project
    ).all()

    recommendations = []

    for project in projects:

        required_skills = set()

        if project.skills:

            required_skills = set(

                skill.strip().lower()

                for skill
                in project.skills.split(",")

                if skill.strip()

            )

        skill_match = calculate_skill_overlap(
            student_skills,
            required_skills
        )

        project_text = " ".join([

            project.title or "",

            project.description or "",

            project.skills or "",

            project.category or ""

        ])

        tfidf_match = calculate_tfidf_similarity(
            student_text,
            project_text
        )

        # Hybrid AI score
        #
        # 70% = skill matching
        # 30% = TF-IDF similarity

        final_match = round(

            (
                skill_match * 0.70
            )
            +
            (
                tfidf_match * 0.30
            )

        )

        if final_match > 100:

            final_match = 100

        if final_match < 0:

            final_match = 0

        recommendations.append({

            "project_id":
                project.id,

            "title":
                project.title,

            "description":
                project.description,

            "skills":
                project.skills,

            "category":
                project.category,

            "match_percentage":
                final_match

        })

    recommendations.sort(

        key=lambda x:
            x["match_percentage"],

        reverse=True

    )

    db.close()

    return recommendations


# =========================================================
# SAVE PROJECT
# =========================================================

@app.post(
    "/student/{student_id}/save-project/{project_id}"
)
def save_project(
    student_id: int,
    project_id: int
):

    db = SessionLocal()

    existing = db.query(
        SavedProject
    ).filter(

        SavedProject.student_id == student_id,

        SavedProject.project_id == project_id

    ).first()

    if existing:

        db.close()

        return {

            "message":
                "Project already saved"

        }

    saved_project = SavedProject(

        student_id=student_id,

        project_id=project_id

    )

    db.add(saved_project)

    db.commit()

    db.refresh(saved_project)

    db.close()

    return {

        "message":
            "Project saved successfully!",

        "saved_project_id":
            saved_project.id

    }


# =========================================================
# GET SAVED PROJECTS
# =========================================================

@app.get(
    "/student/{student_id}/saved-projects"
)
def get_saved_projects(
    student_id: int
):

    db = SessionLocal()

    saved_projects = db.query(
        SavedProject
    ).filter(

        SavedProject.student_id == student_id

    ).all()

    result = []

    for saved in saved_projects:

        project = db.query(
            Project
        ).filter(
            Project.id == saved.project_id
        ).first()

        if project:

            result.append({

                "saved_project_id":
                    saved.id,

                "project_id":
                    project.id,

                "title":
                    project.title,

                "description":
                    project.description,

                "skills":
                    project.skills,

                "category":
                    project.category

            })

    db.close()

    return result
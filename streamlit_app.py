import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Internship & Project Recommendation System",
    page_icon="🎓",
    layout="wide"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }

    .card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ddd;
        margin-bottom: 18px;
        background-color: #ffffff;
    }

    .match {
        font-size: 22px;
        font-weight: 700;
    }

    .skill {
        display: inline-block;
        padding: 6px 10px;
        margin: 4px;
        border-radius: 15px;
        background-color: #eef2ff;
        font-size: 13px;
    }

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SAMPLE INTERNSHIP DATA
# ---------------------------------------------------------
internships = [
    {
        "id": 1,
        "title": "Python Developer Intern",
        "company": "ABC Technologies",
        "description": "Build Python applications and work with APIs and databases.",
        "skills": ["python", "sql", "git"],
        "duration": "3-6 months",
        "location": "Remote"
    },
    {
        "id": 2,
        "title": "Machine Learning Intern",
        "company": "DataTech Solutions",
        "description": "Work on machine learning models, data analysis and AI projects.",
        "skills": ["python", "machine-learning", "data-science"],
        "duration": "3-6 months",
        "location": "Hybrid"
    },
    {
        "id": 3,
        "title": "Frontend Developer Intern",
        "company": "WebWorks Pvt Ltd",
        "description": "Build responsive web applications using HTML, CSS, JavaScript and React.",
        "skills": ["html-css", "javascript", "react"],
        "duration": "3-6 months",
        "location": "Remote"
    }
]


# ---------------------------------------------------------
# SAMPLE PROJECT DATA
# ---------------------------------------------------------
projects = [
    {
        "id": 1,
        "title": "AI Resume Analyzer",
        "description": "AI system that analyzes resumes and gives improvement suggestions.",
        "skills": ["python", "machine-learning", "nlp"],
        "category": "Artificial Intelligence"
    },
    {
        "id": 2,
        "title": "Machine Learning Prediction System",
        "description": "Machine learning project for predicting outcomes from student data.",
        "skills": ["python", "machine-learning", "data-science"],
        "category": "Machine Learning"
    },
    {
        "id": 3,
        "title": "Student Portfolio Website",
        "description": "Responsive portfolio website for students to showcase skills and projects.",
        "skills": ["html-css", "javascript", "react"],
        "category": "Web Development"
    }
]


# ---------------------------------------------------------
# AI MATCHING FUNCTIONS
# ---------------------------------------------------------
def normalize_skill(skill):
    return skill.strip().lower().replace(" ", "-")


def skill_overlap(student_skills, target_skills):
    student_set = set(normalize_skill(x) for x in student_skills)
    target_set = set(normalize_skill(x) for x in target_skills)

    if not target_set:
        return 0

    matched = student_set.intersection(target_set)

    return len(matched) / len(target_set)


def tfidf_score(student_text, target_text):
    try:
        vectorizer = TfidfVectorizer()
        matrix = vectorizer.fit_transform([student_text, target_text])
        score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
        return score
    except:
        return 0


def calculate_match(student_skills, student_text, target_skills, target_text):
    skill_score = skill_overlap(student_skills, target_skills)
    ai_score = tfidf_score(student_text, target_text)

    final_score = (0.70 * skill_score) + (0.30 * ai_score)

    return round(final_score * 100)


def get_matched_skills(student_skills, required_skills):
    student_set = set(normalize_skill(x) for x in student_skills)
    required_set = set(normalize_skill(x) for x in required_skills)

    return sorted(student_set.intersection(required_set))


def get_missing_skills(student_skills, required_skills):
    student_set = set(normalize_skill(x) for x in student_skills)
    required_set = set(normalize_skill(x) for x in required_skills)

    return sorted(required_set - student_set)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">🎓 AI-Powered Internship & Project Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-based career guidance using Skill Overlap + TF-IDF + Cosine Similarity</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
st.sidebar.title("🔎 Student Profile")

student_name = st.sidebar.text_input(
    "Student Name",
    "Triveni"
)

branch = st.sidebar.selectbox(
    "Branch",
    [
        "Computer Science Engineering",
        "Information Technology",
        "Artificial Intelligence",
        "Data Science",
        "Electronics"
    ]
)

skills_input = st.sidebar.text_area(
    "Technical Skills",
    "Python, SQL, JavaScript, HTML, CSS, Machine Learning"
)

interests_input = st.sidebar.text_area(
    "Interests",
    "Artificial Intelligence, Machine Learning, Web Development, Data Science"
)

certifications_input = st.sidebar.text_input(
    "Certifications",
    "Python Programming, Machine Learning Basics"
)

projects_input = st.sidebar.text_input(
    "Projects",
    "AI Resume Analyzer, Student Portfolio Website"
)


student_skills = [
    normalize_skill(x)
    for x in skills_input.split(",")
    if x.strip()
]

student_interests = [
    x.strip()
    for x in interests_input.split(",")
    if x.strip()
]

student_text = " ".join(
    student_skills
    + [x.lower() for x in student_interests]
    + [certifications_input.lower()]
    + [projects_input.lower()]
)


# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🏠 Dashboard",
        "💼 Internship Recommendations",
        "🚀 Project Recommendations",
        "📊 Skill Gap Analysis"
    ]
)


# ---------------------------------------------------------
# DASHBOARD
# ---------------------------------------------------------
with tab1:

    st.subheader(f"Welcome, {student_name}! 👋")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Branch", branch)

    with col2:
        st.metric("Technical Skills", len(student_skills))

    with col3:
        st.metric("Interests", len(student_interests))

    st.markdown("---")

    st.subheader("🧠 AI Matching Technology")

    st.info(
        "This system uses a Hybrid AI Matching approach: "
        "70% Skill Overlap + 30% TF-IDF Cosine Similarity."
    )

    st.subheader("⭐ Your Skills")

    for skill in student_skills:
        st.markdown(
            f'<span class="skill">{skill}</span>',
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# INTERNSHIP RECOMMENDATIONS
# ---------------------------------------------------------
with tab2:

    st.subheader("💼 Recommended Internships")

    recommendations = []

    for internship in internships:

        target_text = (
            internship["title"]
            + " "
            + internship["description"]
            + " "
            + " ".join(internship["skills"])
        )

        score = calculate_match(
            student_skills,
            student_text,
            internship["skills"],
            target_text
        )

        recommendations.append(
            (score, internship)
        )

    recommendations.sort(
        key=lambda x: x[0],
        reverse=True
    )

    for score, internship in recommendations:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(
                f"### {internship['title']}"
            )

            st.write(
                f"🏢 **Company:** {internship['company']}"
            )

            st.write(
                f"📍 **Location:** {internship['location']}"
            )

            st.write(
                f"⏳ **Duration:** {internship['duration']}"
            )

            st.write(
                internship["description"]
            )

            st.write("**Required Skills:**")

            for skill in internship["skills"]:
                st.markdown(
                    f'<span class="skill">{skill}</span>',
                    unsafe_allow_html=True
                )

        with col2:
            st.markdown(
                f'<div class="match">🤖 {score}%</div>',
                unsafe_allow_html=True
            )

            st.progress(
                score / 100
            )

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# PROJECT RECOMMENDATIONS
# ---------------------------------------------------------
with tab3:

    st.subheader("🚀 Recommended Projects")

    project_recommendations = []

    for project in projects:

        target_text = (
            project["title"]
            + " "
            + project["description"]
            + " "
            + " ".join(project["skills"])
        )

        score = calculate_match(
            student_skills,
            student_text,
            project["skills"],
            target_text
        )

        project_recommendations.append(
            (score, project)
        )

    project_recommendations.sort(
        key=lambda x: x[0],
        reverse=True
    )

    for score, project in project_recommendations:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([4, 1])

        with col1:

            st.markdown(
                f"### {project['title']}"
            )

            st.write(
                f"📂 **Category:** {project['category']}"
            )

            st.write(
                project["description"]
            )

            st.write("**Required Skills:**")

            for skill in project["skills"]:
                st.markdown(
                    f'<span class="skill">{skill}</span>',
                    unsafe_allow_html=True
                )

        with col2:

            st.markdown(
                f'<div class="match">🤖 {score}%</div>',
                unsafe_allow_html=True
            )

            st.progress(
                score / 100
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# SKILL GAP ANALYSIS
# ---------------------------------------------------------
with tab4:

    st.subheader("📊 Skill Gap Analysis")

    selected_internship = st.selectbox(
        "Select an Internship",
        internships,
        format_func=lambda x: x["title"]
    )

    required_skills = selected_internship["skills"]

    matched = get_matched_skills(
        student_skills,
        required_skills
    )

    missing = get_missing_skills(
        student_skills,
        required_skills
    )

    match_percentage = round(
        (len(matched) / len(required_skills)) * 100
    )

    st.metric(
        "Your Skill Match",
        f"{match_percentage}%"
    )

    st.progress(
        match_percentage / 100
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if matched:
            for skill in matched:
                st.success(skill)
        else:
            st.write("No matching skills yet.")

    with col2:

        st.subheader("📚 Skills to Learn")

        if missing:
            for skill in missing:
                st.warning(skill)
        else:
            st.success(
                "You have all required skills!"
            )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")

st.caption(
    "AI-Powered Internship & Project Recommendation System | "
    "B.Tech CSE Project | Hybrid AI Recommendation"
)

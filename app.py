import streamlit as st

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎤",
    layout="wide"
)

INTERVIEW_QUESTIONS = {
    "AI Engineer": [
        "What is Machine Learning?",
        "Difference between AI and ML?",
        "What is Deep Learning?",
        "What is Overfitting?",
        "Explain Neural Networks."
    ],
    "GenAI Developer": [
        "What is RAG?",
        "What is LangChain?",
        "What is LangGraph?",
        "What are Embeddings?",
        "What is Vector Database?"
    ],
    "Python Developer": [
        "What is OOP?",
        "Difference between List and Tuple?",
        "What are Decorators?",
        "What is Exception Handling?",
        "Explain Generators."
    ],
    "Data Scientist": [
        "What is Data Cleaning?",
        "What is Feature Engineering?",
        "Explain Regression.",
        "What is Classification?",
        "What is Cross Validation?"
    ],
    "Data Analyst": [
        "What is SQL?",
        "What is Power BI?",
        "What is Data Visualization?",
        "What is KPI?",
        "Explain Dashboard."
    ]
}

st.title("🎤 AI Interview Coach")

role = st.selectbox(
    "Select Job Role",
    list(INTERVIEW_QUESTIONS.keys())
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

st.subheader("Interview Questions")

questions = INTERVIEW_QUESTIONS[role]

answers = []

for i, question in enumerate(questions):

    st.write(f"Q{i+1}. {question}")

    answer = st.text_area(
        f"Answer {i+1}",
        key=i
    )

    answers.append(answer)

if st.button("Evaluate Interview"):

    total_score = 0

    feedback = []

    for answer in answers:

        word_count = len(answer.split())

        if word_count > 50:
            score = 10

        elif word_count > 25:
            score = 7

        elif word_count > 10:
            score = 5

        else:
            score = 2

        total_score += score

    percentage = int(
        (total_score / (len(questions) * 10))
        * 100
    )

    st.subheader("📊 Interview Score")

    st.progress(percentage)

    st.metric(
        "Interview Readiness",
        f"{percentage}%"
    )

    if percentage >= 80:

        st.success(
            "Excellent Interview Performance"
        )

    elif percentage >= 60:

        st.info(
            "Good Performance. Keep Practicing."
        )

    else:

        st.warning(
            "Needs Improvement."
        )

    st.subheader("🎯 Suggestions")

    st.write(
        "✅ Give more detailed answers"
    )

    st.write(
        "✅ Use real-world examples"
    )

    st.write(
        "✅ Improve technical depth"
    )

    st.write(
        "✅ Practice mock interviews"
    )

    st.subheader("📚 Learning Roadmap")

    if role == "AI Engineer":

        roadmap = [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "MLOps",
            "AWS"
        ]

    elif role == "GenAI Developer":

        roadmap = [
            "LangChain",
            "LangGraph",
            "RAG",
            "Vector DB",
            "Deployment"
        ]

    elif role == "Python Developer":

        roadmap = [
            "Python",
            "OOP",
            "FastAPI",
            "SQL",
            "Docker"
        ]

    elif role == "Data Scientist":

        roadmap = [
            "Python",
            "Statistics",
            "ML",
            "Visualization",
            "Deployment"
        ]

    else:

        roadmap = [
            "Excel",
            "SQL",
            "Power BI",
            "Python",
            "Dashboarding"
        ]

    for item in roadmap:

        st.write(f"📌 {item}")
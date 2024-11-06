import streamlit as st

# Sample course data
courses = {
    "Python Basics": {
        "description": "Learn the basics of Python programming.",
        "content": [
            "Introduction to Python",
            "Data Types and Variables",
            "Control Structures",
            "Functions",
            "Modules and Packages"
        ],
        "quiz": {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["8", "6", "9", "5"],
            "answer": "8"
        }
    },
    "Data Science with Python": {
        "description": "An introduction to Data Science using Python.",
        "content": [
            "Data Analysis with Pandas",
            "Data Visualization with Matplotlib",
            "Machine Learning Basics",
            "Model Evaluation"
        ],
        "quiz": {
            "question": "Which library is used for data manipulation?",
            "options": ["NumPy", "Pandas", "Matplotlib", "Scikit-learn"],
            "answer": "Pandas"
        }
    },
    "Web Development with Flask": {
        "description": "Build web applications using Flask.",
        "content": [
            "Introduction to Flask",
            "Routing and Views",
            "Templates",
            "Forms and User Input",
            "Deploying Flask Apps"
        ],
        "quiz": {
            "question": "What is Flask?",
            "options": ["A database", "A web framework", "A programming language", "A library"],
            "answer": "A web framework"
        }
    }
}

def display_course(course_name):
    """Display the selected course details."""
    st.header(course_name)
    st.write(courses[course_name]["description"])

    # Display course content
    st.subheader("Course Content")
    for item in courses[course_name]["content"]:
        st.write(f"- {item}")

def display_quiz(course_name):
    """Display the quiz for the selected course."""
    st.subheader("Quiz")
    quiz = courses[course_name]["quiz"]
    user_answer = st.radio(quiz["question"], quiz["options"])

    if st.button("Submit Answer"):
        if user_answer == quiz["answer"]:
            st.success("Correct!")
        else:
            st.error("Incorrect. Try again!")

def main():
    """Main function to run the Streamlit app."""
    st.title("Interactive Knowledge Training e-Course App")
    st.sidebar.title("Courses")

    # Course selection
    course_selection = st.sidebar.selectbox("Select a Course", list(courses.keys()))

    # Display selected course details
    display_course(course_selection)

    # Display quiz section
    display_quiz(course_selection)

if __name__ == "__main__":
    main()
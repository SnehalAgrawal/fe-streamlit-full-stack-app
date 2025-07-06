import streamlit as st
import requests

# Configuration
API_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="Add Student", page_icon="➕")

st.title("➕ Add New Student")

with st.form("student_form"):
    name = st.text_input("Name")
    student_class = st.selectbox("Class", [f"{i}th" for i in range(1, 13)])
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    optional_subjects = st.multiselect("Optional Subjects", ["Sample 1", "Sample 2", "Sample 3"])
    previous_score = st.number_input("Score in Last Class", min_value=0, max_value=100, step=1)

    submitted = st.form_submit_button("Submit")
    if submitted:
        student_data = {
            "Name": name,
            "Class": student_class,
            "Gender": gender,
            "Optional Subjects": optional_subjects,
            "Previous Score": previous_score
        }

        try:
            response = requests.post(f"{API_URL}/students", json=student_data)
            response.raise_for_status()
            st.success("Student added successfully!")
            st.json(student_data)
            # Navigate back to the All Students page after successful submission
            st.switch_page("pages/1_All_Students.py")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to add student: {e}")

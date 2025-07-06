import streamlit as st
import requests
import pandas as pd

# Configuration
API_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="All Students", page_icon="🧑‍🎓")

st.title("🧑‍🎓 All Students")

# Button to navigate to Add Student page
if st.button("➕ Add New Student"):
    st.switch_page("pages/2_Add_Student.py")

st.markdown("--- ")

# Fetch and display existing students
try:
    response = requests.get(f"{API_URL}/students")
    response.raise_for_status()
    students = response.json()
    if students:
        st.subheader("List of All Students")
        df = pd.DataFrame(students)
        st.dataframe(df)
    else:
        st.info("No students have been added yet.")
except requests.exceptions.RequestException as e:
    st.error(f"Could not fetch students: {e}")

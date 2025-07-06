import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Configuration
API_URL = "http://127.0.0.1:5000"

st.set_page_config(
    page_title="Student Dashboard",
    page_icon="📊",
)


st.title("📊 Student Dashboard")

# Fetch data from the Flask API
try:
    response = requests.get(f"{API_URL}/students")
    response.raise_for_status()  # Raise an exception for bad status codes
    students = response.json()

    if not students:
        st.warning("No student data available. Add students to see the dashboard.")
    else:
        df = pd.DataFrame(students)

        # Pie chart for number of students per class
        st.subheader("Number of Students per Class")
        class_counts = df['Class'].value_counts().reset_index()
        class_counts.columns = ['Class', 'Count']
        fig_pie = px.pie(class_counts, names='Class', values='Count', title='Distribution of Students by Class')
        st.plotly_chart(fig_pie)

        # Bar chart for average score per class
        st.subheader("Average Score per Class")
        avg_score_per_class = df.groupby('Class')['Previous Score'].mean().reset_index()
        fig_bar = px.bar(avg_score_per_class, x='Class', y='Previous Score', title='Average Score by Class')
        st.plotly_chart(fig_bar)

except requests.exceptions.RequestException as e:
    st.error(f"Could not connect to the backend: {e}")

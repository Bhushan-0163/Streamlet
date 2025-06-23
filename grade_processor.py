import streamlit as st
from functools import reduce

st.title("Student Grade Processor")
st.subheader("Using Map, Filter, and Reduce")

# Input section
st.header("Input Student Grades")
grades_input = st.text_area(
    "Enter student grades (comma-separated):",
    "85, 92, 78, 65, 90, 55, 88, 72, 95, 60"
)

# Convert input to list of integers
try:
    grades = [int(grade.strip()) for grade in grades_input.split(",")]
except ValueError:
    st.error("Invalid input! Please enter comma-separated numbers.")
    st.stop()

st.write(f"Original Grades: {grades}")

# Operations
st.header("Operations")

# Map: Grade adjustment
st.subheader("Map: Grade Adjustment")
curve = st.slider("Add curve to all grades:", -10, 20, 0)
curved_grades = list(map(lambda x: x + curve, grades))
st.write(f"Curved Grades: {curved_grades}")

# Filter: Passing grades
st.subheader("Filter: Passing Grades")
passing_threshold = st.slider("Passing threshold:", 0, 100, 60)
passing_grades = list(filter(lambda x: x >= passing_threshold, curved_grades))
st.write(f"Passing Grades: {passing_grades}")

# Reduce: Statistics
st.subheader("Reduce: Statistics")
if curved_grades:
    # Calculate average
    average = reduce(lambda a, b: a + b, curved_grades) / len(curved_grades)
    
    # Calculate max
    maximum = reduce(lambda a, b: a if a > b else b, curved_grades)
    
    # Calculate min
    minimum = reduce(lambda a, b: a if a < b else b, curved_grades)
    
    st.metric("Average Grade", f"{average:.2f}")
    st.metric("Highest Grade", maximum)
    st.metric("Lowest Grade", minimum)
else:
    st.warning("No grades to process")

# Footer
st.divider()
st.caption("Capstone Project: Functional Programming with Python")

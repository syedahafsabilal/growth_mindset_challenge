import streamlit as st
import pandas as pd  
import base64
import os


video_file_path = "workout.mp4"



if os.path.exists(video_file_path):
    with open(video_file_path, "rb") as video_file:
        st.video(video_file)
else:
    st.error("❌ File not found. Make sure it's in the same folder as app.py")


if "workouts" not in st.session_state:
    st.session_state.workouts =[]
 
st.markdown(
    """
    <style>
        html, body, .stApp {
            background-color:rgb(38, 216, 18) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
 )

st.title(" 🏋‍♀Fitness Tracker")

exercise = st.text_input("Exercise Name")
duration = st.number_input("Duration (mins):", min_value=1)
calories = st.number_input("Calories Burned:", min_value=1)

if st.button("Add Workout"):
    if exercise and duration and calories:
        st.session_state.workouts.append({
            "Exercise":exercise,
            "Duration (mins)": duration,
            "Calories Burned": calories
        })
        st.success("Workout Added! :)")
    else:
        st.warning("Please fill all the Fields.")    

if st.session_state.workouts:
    st.subheader("Workout History") 
    df = pd.DataFrame(st.session_state.workouts) 
    st.dataframe(df)

    total_calories = df["Calories Burned"].sum()   
    st.subheader(f"🔥Total Calories Burned: {total_calories} kcal")   

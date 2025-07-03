import streamlit as st
from utils import get_weather, get_news
from planner import generate_todo

st.title("🌤️ AI Daily Planner (100% Free)")

if st.button("Generate My Daily Plan"):
    weather = get_weather()
    news = get_news()
    context = f"Weather: {weather}\nNews:\n{news}"
    todo_list = generate_todo(context)
    
    st.subheader("📍 Weather Today:")
    st.write(weather)
    
    st.subheader("📰 Top News Headlines:")
    st.write(news)
    
    st.subheader("📝 Suggested To-Do List:")
    st.write(todo_list)

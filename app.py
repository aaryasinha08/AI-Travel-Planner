import random
import streamlit as st
from services.planner import generate_travel_plan
from assets.image_pool import IMAGE_POOL

st.set_page_config(page_title="Student AI Travel Planner", layout="wide")

# 🌍 Sidebar - Filters / Navigation
st.sidebar.title("🧭 Travel Preferences")

city = st.sidebar.text_input("📍 Destination City", "Varanasi")
days = st.sidebar.selectbox("🗓️ Trip Duration (Days)", [1,2,3,4,5,6,7])
budget = st.sidebar.selectbox("💸 Budget", ["Low", "Medium", "High"])

travel_style = st.sidebar.selectbox(
    "🧳 Travel Style",
    ["Road Tripper", "Slow Traveler", "Wellness", "Luxury", "Spiritual", "Cultural & Heritage", "Eco & Wildlife"]
)

interests = st.sidebar.multiselect(
    "🎯 Interests",
    ["Photography", "Nightlife", "Food", "History", "Nature", "Shopping"]
)

# 🏠 Main Page
st.title("✈️ Student AI Travel Planner")
st.write("Plan your trip smartly, beautifully, and on budget.")

if st.button("🚀 Generate My Travel Plan"):
    with st.spinner("Creating your personalized travel plan..."):
        plan = generate_travel_plan(
            city,
            days,
            budget,
            travel_style,
            ", ".join(interests)
        )

    st.success("Your travel plan is ready! 🌟")

    # 📝 Display AI Output Nicely
    sections = plan.split("\n\n")

    for section in sections:
        if section.startswith("TITLE"):
            st.header(section.replace("TITLE:", "").strip())
        elif section.startswith("OVERVIEW"):
            st.subheader("🌍 Overview")
            st.write(section.replace("OVERVIEW:", "").strip())
        elif section.startswith("DAY"):
            st.subheader(section.split(":")[0])
            st.write(section)
        elif section.startswith("BUDGET"):
            st.subheader("💡 Budget Tips")
            st.write(section)
        else:
            st.write(section)

    # 🖼️ City Image (No download, direct from web)
    # 📸 Random Image Gallery
    st.subheader("📸 Trip Gallery")

    selected_images = random.sample(IMAGE_POOL, 3)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(selected_images[0], use_container_width=True)

    with col2:
        st.image(selected_images[1], use_container_width=True)

    with col3:
        st.image(selected_images[2], use_container_width=True)



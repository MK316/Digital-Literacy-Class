import streamlit as st
from datetime import datetime
import pytz
from gtts import gTTS
from io import BytesIO
import random

# List of available time zones (City/Country)
timezones = {
    "Seoul, South Korea": "Asia/Seoul",
    "New York, USA": "America/New_York",
    "London, UK": "Europe/London",
    "Tokyo, Japan": "Asia/Tokyo",
    "Sydney, Australia": "Australia/Sydney",
    "Paris, France": "Europe/Paris",
    "Berlin, Germany": "Europe/Berlin",
    "Dubai, UAE": "Asia/Dubai",
    "Mumbai, India": "Asia/Kolkata",
}

# Create tabs
tabs = st.tabs(["🕒 Timezone", "🔹 Future Expansion"])

# 🕒 First Tab: Timezone App
with tabs[0]:
    st.markdown("#### 🌍 Saying World Time using TTS Generator")
    st.caption("Select a city or country to check the current time and hear it as audio.")

    # Dropdown for city selection
    selected_city = st.selectbox("Choose a City/Country:", list(timezones.keys()))

    # Get current time in the selected city's timezone
    timezone = pytz.timezone(timezones[selected_city])
    current_time_24 = datetime.now(timezone)

    # Convert time to 12-hour format with AM/PM
    current_time_12 = current_time_24.strftime("%I:%M %p")  # Example: "03:45 PM"

    # Extract only the city name for TTS output
    city_name = selected_city.split(",")[0]

    # Select a random city different from the selected one
    other_cities = [city for city in timezones.keys() if city != selected_city]
    random_city = random.choice(other_cities).split(",")[0]

    # Display the current time
    st.markdown("---")
    st.markdown(f"### 🕒 Current Time in {selected_city}: `{current_time_12}`")
    st.markdown("---")

    # Function to generate TTS audio
    def generate_tts(text):
        tts = gTTS(text=text, lang="en")
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer

    # Button to generate and play TTS in 12-hour format
    if st.button("🔊 Hear Time Announcement"):
        tts_text = f"The current time in {city_name} is {current_time_12}. What time is it in {random_city} now?"
        st.markdown("---")
        audio_file = generate_tts(tts_text)
        st.audio(audio_file, format="audio/mp3")

    # Footer
    st.caption("Note: This app fetches real-time data and generates spoken output.")

# 📌 Second Tab: Placeholder for Future Features
with tabs[1]:
    st.write("🚀 This tab can be used for additional features in future updates.")

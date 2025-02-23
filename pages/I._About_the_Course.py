import streamlit as st
import requests
import calendar
from datetime import datetime
import pandas as pd


# Include custom CSS to justify text in the markdown
# Include custom CSS to justify text in the markdown
st.markdown("""
<style>
.justify-text p {
    text-align: justify;
    text-justify: inter-word;
}
.calendar-table {
    margin-left: auto;
    margin-right: auto;
    border-collapse: collapse;
}
.calendar-table td, .calendar-table th {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Create tabs for different sections of the course
tabs = st.tabs(["🍐 Course Overview", "🍏 Evaluation", "🍒 Assignments", "🍋 QR Links", "📆 Calendar"])

# Content for the Course Overview tab
with tabs[0]:
    st.caption("🔎 Course Overview")
    
    # Display the text for the first passage
    st.markdown("""
    <div class="justify-text">
    This course is designed for pre-service English teachers to equip them with critical digital literacy skills and an understanding of technology's evolving role in language education. Recognizing the indispensability of digital tools in today’s educational landscape, the curriculum extends beyond traditional digital literacy to include basic coding skills essential for designing and developing learner-centered language apps. 
    </div>
    """, unsafe_allow_html=True)

    # Audio for the first passage
    st.audio('https://github.com/MK316/Digital-Literacy-Class/raw/main/audio/overview1.mp3', format='audio/mp3')

    # Display the text for the second passage
    st.markdown("""
    <div class="justify-text">
    Students will gain hands-on experience in coding, enabling them to create customized, interactive language learning tools. This approach aims to empower educators to not only navigate but also innovate within the digital era of language teaching. By the end of the course, participants will be adept at integrating coding skills in pedagogically sound ways, enhancing both their teaching practices and their students’ learning experiences.
    </div>
    """, unsafe_allow_html=True)

    # Audio for the second passage
    st.audio('https://github.com/MK316/Digital-Literacy-Class/raw/main/audio/overview2.mp3', format='audio/mp3')

        
# Content for the Evaluation tab
with tabs[1]:
    st.header("Evaluation")
    st.markdown("""
    - Attendance: 10%
    - Midterm: 30%
    - Final project: 30%
    - Assignments: 30%

    """)
# Content for the Assignments tab
with tabs[2]:
    st.markdown("### 📋 Assignments Details")

    # Define the assignment table with detail instruction links
    assignments_data = {
        "ID": ["1", "2", "3", "4", "5"],
        "Due Date": ["TBA", "TBA", "TBA", "TBA", "TBA"],
        "Topic": ["TBA", "TBA", "TBA", "TBA", "TBA"],
        "Instruction Link": [
            "[Instructions](https://github.com/yourusername/yourrepo/blob/main/A1.md)",
            "[Instructions](https://github.com/yourusername/yourrepo/blob/main/A2.md)",
            "[Instructions](https://github.com/yourusername/yourrepo/blob/main/A3.md)",
            "[Instructions](https://github.com/yourusername/yourrepo/blob/main/A4.md)",
            "[Instructions](https://github.com/yourusername/yourrepo/blob/main/A5.md)"
        ]
    }

    # Convert to DataFrame and display as a table
    df_assignments = pd.DataFrame(assignments_data)

    # Display table
    st.markdown(df_assignments.to_markdown(index=False), unsafe_allow_html=True)

    
# Content for the Links tab
with tabs[3]:
    st.header("QR Links")

    st.write("1. Padlet - sharing files inclass")
    st.image("https://github.com/MK316/Digital-Literacy-Class/raw/main/images/padlet-dl.jpg")
    st.markdown("---")
    
    st.write("2. MK316 Home - https://mk316.github.io")
    st.image("https://github.com/MK316/Digital-Literacy-Class/raw/main/images/mkhome.jpg")
    st.markdown("---")

    st.write("3. Class - Digital Literacy Home")
    st.image("https://github.com/MK316/Digital-Literacy-Class/raw/main/images/dl-qr.jpg")
    st.markdown("---")

# Content for the Calendar tab
with tabs[4]:
    # Dropdown for selecting a month
    month_option = st.selectbox("Select a Month", options=["March", "April", "May", "June"], index=0)
    # Dictionary to map month names to their corresponding numbers
    month_to_number = {"March": 3, "April": 4, "May": 5, "June": 6}
    # Get selected month number
    month_number = month_to_number[month_option]
    year = 2025  # Define the year

    # Define a list of holidays as tuples (day, month)
    holidays = [
        (1, 3),  # Example: March 1
        (3, 3),  # Example: May 25
        (5, 5),
        (6, 5),
        (6, 6)
        # Add more holidays as needed
    ]

    # Generate the calendar for the selected month
    cal = calendar.monthcalendar(year, month_number)

    # Display the calendar as a table using HTML
    cal_html = "<table class='calendar-table'><thead><tr>"
    cal_html += "".join(f"<th>{day}</th>" for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    cal_html += "</tr></thead><tbody>"

    for week in cal:
        cal_html += "<tr>"
        for day in week:
            if day == 0:  # Empty cell for days outside the month
                cal_html += "<td></td>"
            else:
                # Check if the day is a holiday
                if (day, month_number) in holidays:
                    cal_html += f"<td style='color: red; font-weight: bold;'>{day}</td>"
                else:
                    cal_html += f"<td>{day}</td>"
        cal_html += "</tr>"
    cal_html += "</tbody></table>"

    st.markdown(cal_html, unsafe_allow_html=True)

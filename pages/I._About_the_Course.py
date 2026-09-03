import streamlit as st
import requests
import calendar
from datetime import datetime
import pandas as pd


# Custom CSS
st.markdown("""
<style>
.justify-text p {
    text-align: justify;
    text-justify: inter-word;
}

/* Calendar */
.calendar-table {
    width: 90%;
    max-width: 950px;
    margin-left: auto;
    margin-right: auto;
    border-collapse: collapse;
    table-layout: fixed;
}

.calendar-table th {
    border: 1px solid #ccc;
    padding: 14px 8px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    background-color: #f5f5f5;
}

.calendar-table td {
    border: 1px solid #ccc;
    padding: 18px 8px;
    text-align: center;
    font-size: 20px;
    height: 60px;
}

/* Sunday header */
.calendar-table th:first-child {
    color: red;
}

/* Saturday header */
.calendar-table th:last-child {
    color: #1f5fbf;
}
</style>
""", unsafe_allow_html=True)


# Create tabs
tabs = st.tabs([
    "🍐 Course Overview",
    "🍏 Evaluation",
    "🍋 QR Links",
    "📆 Calendar"
])


# --------------------------------------------------
# Course Overview
# --------------------------------------------------
with tabs[0]:

    st.caption("🔎 Course Overview")
    
    st.markdown("""
    <div class="justify-text">
    This course is designed for pre-service English teachers to equip them with critical digital literacy skills and an understanding of technology's evolving role in language education. Recognizing the indispensability of digital tools in today’s educational landscape, the curriculum extends beyond traditional digital literacy to include basic coding skills essential for designing and developing learner-centered language apps. 
    </div>
    """, unsafe_allow_html=True)

    st.audio(
        'https://github.com/MK316/Digital-Literacy-Class/raw/main/audio/overview1.mp3',
        format='audio/mp3'
    )

    st.markdown("""
    <div class="justify-text">
    Students will gain hands-on experience in coding, enabling them to create customized, interactive language learning tools. This approach aims to empower educators to not only navigate but also innovate within the digital era of language teaching. By the end of the course, participants will be adept at integrating coding skills in pedagogically sound ways, enhancing both their teaching practices and their students’ learning experiences.
    </div>
    """, unsafe_allow_html=True)

    st.audio(
        'https://github.com/MK316/Digital-Literacy-Class/raw/main/audio/overview2.mp3',
        format='audio/mp3'
    )


# --------------------------------------------------
# Evaluation
# --------------------------------------------------
with tabs[1]:

    st.header("Evaluation")

    st.markdown("""
    - Attendance: 10%
    - Midterm: 30%
    - Final project: 30%
    - Assignments: 30%
    """)


# --------------------------------------------------
# QR Links
# --------------------------------------------------
with tabs[2]:

    st.header("QR Links")

    st.write("1. Padlet - sharing files in class")
    st.image(
        "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/padlet-dl.jpg"
    )

    st.markdown("---")
    
    st.write("2. MK316 Home - https://mk316.github.io")
    st.image(
        "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/mkhome.jpg"
    )

    st.markdown("---")

    st.write("3. Class - Digital Literacy Home")
    st.image(
        "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/dl-qr.jpg"
    )

    st.markdown("---")


# --------------------------------------------------
# Calendar
# --------------------------------------------------
with tabs[3]:

    st.subheader("📆 Calendar")

    # Start calendar on Sunday
    calendar.setfirstweekday(calendar.SUNDAY)

    # Year and Month selection
    col1, col2 = st.columns(2)

    with col1:
        year = st.selectbox(
            "Select a Year",
            options=[2025, 2026, 2027, 2028],
            index=1  # Default: 2026
        )

    with col2:
        month_option = st.selectbox(
            "Select a Month",
            options=[
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ],
            index=8  # Default: September
        )

    # Convert month name to number
    month_to_number = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    month_number = month_to_number[month_option]


    # Holidays
    # Format: (month, day)
    holidays = [
        (9, 24),
        (9, 25),
        (10, 1),
        (10, 5),
        (10, 9),
        (10, 20),
        (12, 25)
    ]


    # Generate calendar
    cal = calendar.monthcalendar(
        year,
        month_number
    )


    # Display selected year and month
    st.markdown(
        f"<h2 style='text-align:center;'>"
        f"{month_option} {year}"
        f"</h2>",
        unsafe_allow_html=True
    )


    # Create calendar table
    cal_html = "<table class='calendar-table'><thead><tr>"

    cal_html += "".join(
        f"<th>{day}</th>"
        for day in [
            "Sun",
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat"
        ]
    )

    cal_html += "</tr></thead><tbody>"


    # Calendar dates
    for week in cal:

        cal_html += "<tr>"

        for weekday_index, day in enumerate(week):

            if day == 0:

                cal_html += "<td></td>"

            else:

                is_holiday = (
                    month_number,
                    day
                ) in holidays

                is_sunday = weekday_index == 0
                is_saturday = weekday_index == 6


                # Holidays and Sundays: red
                if is_holiday or is_sunday:

                    cal_html += (
                        f"<td style='color:red; "
                        f"font-weight:bold;'>"
                        f"{day}"
                        f"</td>"
                    )

                # Saturdays: blue
                elif is_saturday:

                    cal_html += (
                        f"<td style='color:#1f5fbf;'>"
                        f"{day}"
                        f"</td>"
                    )

                else:

                    cal_html += f"<td>{day}</td>"


        cal_html += "</tr>"


    cal_html += "</tbody></table>"


    st.markdown(
        cal_html,
        unsafe_allow_html=True
    )

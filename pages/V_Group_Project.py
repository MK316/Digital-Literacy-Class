import streamlit as st

# Create three tabs
tabs = st.tabs(["📌 Instructions", "💻 GitHub IDs", "🖼️ Project Gallery"])

# First tab: Instructions
with tabs[0]:
    st.markdown("## 📌 Project Instructions")
    st.write("""
    Welcome to the project portal! Here’s what you need to know:
    
    1. Each group will work on a project and upload the code to GitHub.
    2. Add your GitHub repository links in the 'GitHub IDs' tab.
    3. Completed projects will be displayed in the 'Project Gallery' tab.
    4. Follow the guidelines provided in the course materials.
    
    **Deadline:** Please submit your project by the specified deadline.
    
    Good luck, and happy coding!
    """)

# Second tab: GitHub IDs
with tabs[1]:
    st.markdown("## 💻 GitHub IDs for Group Projects")

    # Group 1
    st.subheader("🔹 Group 1")
    github_id_1 = st.text_input("GitHub Link for Group 1", placeholder="Enter GitHub repository link...")

    # Group 2
    st.subheader("🔹 Group 2")
    github_id_2 = st.text_input("GitHub Link for Group 2", placeholder="Enter GitHub repository link...")

    # Group 3
    st.subheader("🔹 Group 3")
    github_id_3 = st.text_input("GitHub Link for Group 3", placeholder="Enter GitHub repository link...")

    if st.button("💾 Save Links"):
        st.success("GitHub links saved successfully!")

# Third tab: Project Gallery
with tabs[2]:
    st.markdown("## 🖼️ Project Gallery")
    st.write("Once the projects are submitted, they will be displayed below:")

    # Display GitHub links if available
    if github_id_1:
        st.markdown(f"**Group 1:** [View Project]({github_id_1})")
    if github_id_2:
        st.markdown(f"**Group 2:** [View Project]({github_id_2})")
    if github_id_3:
        st.markdown(f"**Group 3:** [View Project]({github_id_3})")

    # Optional: Placeholder for future gallery content
    st.image("https://via.placeholder.com/400", caption="Sample Project Thumbnail", width=300)

# Footer
st.markdown("---")
st.caption("📌 Note: Make sure to update your GitHub links and project files before the deadline.")

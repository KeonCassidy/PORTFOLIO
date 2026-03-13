import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="💻")

st.title("Welcome to My Portfolio")

st.write("Hello! I am a student passionate about technology and programming.")

st.header("About This Website")
st.write("""
This portfolio showcases my:
- Skills
- Resume
- Contact Information
""")


st.success("Use the sidebar to navigate through my portfolio pages.")

st.title("Contact Me")

st.write("You can contact me through the following:")

st.write("📧 Email: keoncassidy26@email.com")
st.write("📱 Phone: 09760654750")
st.write("💻 GitHub: https://github.com/KeonCassidy")

st.write("Thank you for visiting my portfolio!")

st.title("My Resume")

st.write("""
### Education
Bachelor of Science in Information Technology  
(Rizal Technological University)

### Certifications
- Basic Python Programming
- Networking Fundamentals

### Experience
- Academic Projects
- Group Research in Systems Integration
""")

import streamlit as st
import base64


st.set_page_config(page_title="Portfolio - Sandhya Tomar", layout="wide")


page_bg_img = f'''
<style>
[data-testid="stAppViewContainer"] {{
    background-color: #1E3A8A; /* Dark Blue */
    color: white;
}}
[data-testid="stSidebar"] {{
    background-color: #0F172A; /* Darker Blue */
    color: white;
}}
a {{
    color: #FFDD57;
    text-decoration: none;
}}
a:hover {{
    text-decoration: underline;
}}
</style>
'''











st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("Hi, I am Sandhya Tomar 👩‍💻")
st.subheader("B.Tech in Computer Science | Python & Web Development")


st.write("""
🚀 Passionate about Web Development and Robotics.
I enjoy building intelligent systems, web applications, and solving real-world problems using technology.
Check out my projects and feel free to connect!
""")


st.sidebar.title("📩 Contact Info")
st.sidebar.write("✉️ Email: sandhyatomar248@gmail.com")
st.sidebar.write("🔗 LinkedIn: [Sandhya Tomar](https://www.linkedin.com/in/sandhya-tomar-914920281)")
st.sidebar.write("💻 GitHub: [beingsandhya](https://github.com/beingsandhya)")


st.markdown("## 💡 Projects")

projects = {
    "📚 Django Library Management System": {
        "desc": "A web app to manage library books, users, and fines.",
        "link": "https://github.com/beingsandhya/Django-Library-Management-System"
    },
    "📈 Stock Price Predictor": {
        "desc": "A machine learning model predicting stock prices based on historical data.",
        "link": "https://github.com/beingsandhya/Stock-Price-Predictor"
    },
    "💰 Crypto Price Analysis": {
        "desc": "An AI-based system to analyze and predict cryptocurrency trends.",
        "link": "https://github.com/beingsandhya/Crypto-Price-Analysis"
    },
}

for project, details in projects.items():
    st.write(f"### {project}")
    st.write(details["desc"])
    st.write(f"🔗 [GitHub Repository]({details['link']})")
    st.markdown("---")


st.markdown("## 🚀 Technical Skills")
st.write("**Web Development:** HTML, CSS, Django, Streamlit")
st.write("**AI & Machine Learning:** OpenCV, Image Processing, Scikit-Learn, TensorFlow")
st.write("**Robotics:** Motion Control, Sensor Integration, ROS")
st.write("**CAD & Simulation:** Fusion 360, SolidWorks")
st.write("**Databases:** SQL")
st.write("**Languages:** C++, Python, SQL, JavaScript")


st.markdown("## 🎯 Additional Features")
st.write("✅ **Dark Mode Support** for better user experience.")
st.write("✅ **Interactive Charts & Visuals** for project insights.")
st.write("✅ **Live Deployment Links** for web-based projects.")
st.write("✅ **Custom Styling & Improved Readability.**")


import streamlit as st

st.title("💬 Chat with Me!")


faq_responses = {
    "hello": "Hello! How can I help you?",
    "who are you": "I am Sandhya's personal chatbot. How can I assist?",
    "projects": "Check out my projects on GitHub: https://github.com/beingsandhya",
    "contact": "You can contact me at sandhyatomar248@gmail.com or WhatsApp me !"
}

user_input = st.text_input("Ask me anything!")

if user_input:
    response = faq_responses.get(user_input.lower(), "I'm not sure. Try asking something else!")
    st.write("🤖 Chatbot:", response)
whatsapp_number = "9725956648"  
whatsapp_link = f"https://wa.me/{whatsapp_number}"

st.sidebar.markdown(f"[📱 Chat on WhatsApp]({whatsapp_link})", unsafe_allow_html=True)


st.markdown("""
---
🚀 *Let's build something amazing together!*
""")























































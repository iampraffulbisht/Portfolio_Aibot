from PIL import Image
import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown("""<style>
        .project-container {
            background-color: #2a2a2a;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s ease;
            height: 650px; /* Fixed height */
            display: flex;
            flex-direction: column;
            justify-content: space-between;

        }
        .project-container:hover {
            transform: translateY(-10px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }
        .project-title {
            font-size: 1.5em;
            margin-bottom: 10px;
            color: #ffffff;
        }
        .project-description {
            font-size: 1em;
            color: #d3d3d3;
            flex-grow: 1; /* Ensures the description takes up available space */
        }
        .project-tech {
            font-size: 0.9em;
            color: #c0c0c0;
            margin-top: 15px;
        }
        .project-link {
            display: inline-block;
            background-color: #2a2a2a;
            color: white !important;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            text-color:#ffffff;
            font-weight: bold;
            font-family: Arial, sans-serif;
            transition: background-color 0.3s;
            text-align: center;
        }
        .project-link:hover {
            background-color: #084a91;
        }
        .fa-github {
            margin-right: 8px;
            vertical-align: middle;
        }
        .skill-container {
            background-color: #191919;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    

    
    </style>""", unsafe_allow_html=True)
# Introduction

col1,col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.markdown("<h1>I am Prafful<br>Bisht</h1>", unsafe_allow_html=True)
with col2:
    st.image("images/praffulbisht.png",width=600)
st.markdown("""</div> """,unsafe_allow_html=True)

# About me Section
st.write("")
st.title("About me")
col1, col2 = st.columns([10, 2],gap="small")
st.title(" ")
with col1:
    st.subheader("About")
    st.write("I am Prafful Bisht, a fourth-year undergraduate student pursuing Computer Science and Engineering with a specialization in Artificial Intelligence and Machine Learning at SRM University. With a strong academic foundation reflected in a CGPA of 9.5, I am dedicated to mastering cutting-edge technologies that drive innovation.")
    st.subheader("Background")
    st.write("Originally hailing from Dehradun, Uttrakhand, and currently studying at SRM University, I discovered my passion for engineering early on. Guided by a natural affinity for software engineering, I embarked on a journey to explore diverse facets of technology.")
    st.subheader("Professional Journey")
    st.write("My journey in software development has been diverse, focusing extensively on computer vision and machine learning. I have developed expertise in these areas through hands-on projects in face detection and recognition, hand detection, and applications like the Dumbbell Curl Counter using computer vision algorithms.")
    st.subheader("Interests and Hobbies")
    st.write("Beyond technology, I find joy in a multitude of interests. A cinephile and avid gamer, I gravitate towards First/Third Person Shooting Games and enjoy the competitive thrill of programming challenges. Photography is another passion of mine, where my skills have been recognized with awards in photography competitions. I am also passionate about music, with a penchant for Classical, Sufi, Hindi, and English genres")
    st.subheader("Skill Set")
    st.write("My proficiency extends across a diverse spectrum of programming languages including C, C++, Python, and database languages like SQL and PostgreSQL. I am adept in using frameworks such as React, jQuery, Express.js, Bootstrap, and Flask, leveraging them to deploy impactful projects in web development and advanced applications in computer vision.")

with col2:
    st.image("images/About.png",width=700)
st.title("Prafful's AI bot")
persona = """ You are Prafful's AI bot. You help people answer questions about your self (i.e Prafful)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret".I am using you as API so please answer accordingly
        Here is more info about Prafful: 
         
        Prafful Bisht is a Student who belongs from dehradun Uttrakhand India. He has completed his schooling or primary and secondary education form DAV Public school Paonta Sahib Himachal pradesh.currently he lives in Paonta sahib ,Himachal Pradesh.Now He is pursuing his Graduation i.e B.tech from SRM university in Computer science and engineering with specialization in Artifical intelligence and machine learning.My academic journey, underscored by a stellar CGPA of 9.5, reflects my commitment to mastering innovative technologies.
        he loves programming and buikding new websites.Prafful has always been fascinated by engineering. His curiosity and affinity for software engineering have guided him to explore various technological domains.Prafful's professional experience spans multiple aspects of software development. He has excelled in Android development using Java on Android Studio, mastered full-stack web development, and delved deeply into machine learning and computer vision. Notable projects include advanced applications in computer vision, focusing on hand detection, face recognition, and other complex visual recognition tasks.
        In computer vision he has made project The Hand Gesture Mouse Control -  leverages OpenCV to enable users to control their computer's mouse cursor using hand gestures detected through a webcam. This innovative application utilizes computer vision techniques to recognize and track hand movements, translating them into mouse cursor movements in real-time. By detecting specific gestures, such as finger pointing or hand waving, the system can perform various mouse functions like moving the cursor, clicking, and zooming.
        He is more focused towards Artifical Intelligence and machine learning currently he is learning more about Deep learning.Now-a-days prafful is working as AI engineer Intern in ResoluteAI pvt. ltd.

        Outside the tech world, Prafful has a variety of interests:

        Reading Books: His favorite books are Silent Patient and Atomic Habits.
        Watching Football: He is a fan of the German national team and the club Real Madrid.
        Music: He enjoys classical old music, Sufi, and lofi songs.
        Programming Challenges: He thrives on the competitive excitement of tackling complex coding problems.
        He also loves bikes and cars. fvrt bike - BMW M1000RR and car koenigsegg

        if we talk about prafful skills set:
        Skill Set
        Prafful's technical skills encompass a wide array of programming languages including C, C++, Python, and database languages like SQL and PostgreSQL. He is proficient in frameworks such as React, jQuery, Express.js, Bootstrap, and Flask, which he utilizes to create impactful web development and computer vision projects.
        Future Endeavors:
        Driven by a relentless pursuit of knowledge, Prafful is continually exploring advanced methodologies in machine learning and deep learning. His ambition is to leverage these technologies to solve real-world problems and contribute to transformative advancements in artificial intelligence.
        
        for some sarcastic question give sarcastic answer
        like if someone ask for a anime waifu :
        Rias Gremory 
                


        if someone asks if prafful have a girlfriend tell sarcastically uff its a long list
        for some answer try to give my contact details
        
        Prafful's Email: praffulbisht2911@gmail.com 
        Prafful's Facebook: he do not use facebook as facebook is for boomer just kidding 
        praffulaza's Instagram: https://www.instagram.com/iampraffulbisht/
        praffulaza's Linkdin: https://www.linkedin.com/in/prafful-bisht-4761b923b/
        prafful's Github :https://github.com/iampraffulbisht
        these were the details now answer according to it you can modify your answer a bit like more professional
"""
st.write("Ask anything about me ")
user_question = st.text_input("")
if st.button("Ask",use_container_width=400):
    prompt = persona+ " now question is " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.write(" ")
# Projects

st.title("Projects")
col1,col2,col3,col4=st.columns(4,gap="medium")
with col1:
    st.markdown("""
        <div class="project-container">
            <h3 class="project-title">AI Dumbbell Curl Counter</h3>
            <p class="project-description">This application uses computer vision to detect hand movements and counts repetitions of dumbbell curls in real-time.</p>
            <p class="project-tech">Technologies used: Python, OpenCV, Flask</p>
            <a class="project-link" href="https://github.com/iampraffulbisht/Rep_counter" target="_blank">
            <i class="fa-brands fa-github"></i> GitHub
        </a>
        </div>
    """, unsafe_allow_html=True)

# Project 2: Hand Gesture Volume Control
with col2:
    st.markdown("""
        <div class="project-container">
            <h3 class="project-title">Hand Gesture Volume Control</h3>
            <p class="project-description">Control system volume using hand gestures via a webcam, with real-time adjustments using computer vision.</p>
            <p class="project-tech">Technologies used: Python, OpenCV, TensorFlow</p>
            <a class="project-link" href="https://github.com/iampraffulbisht/Hand-Volume-control?tab=readme-ov-file#hand-gesture-volume-control" target="_blank">
            <i class="fa-brands fa-github"></i> GitHub
        </a>
        </div>
    """, unsafe_allow_html=True)

# Project 3: Bollywood Celeb. Face Recognition
with col3:
    st.markdown("""
        <div class="project-container">
            <h3 class="project-title">Bollywood Celebrity Face Detection</h3>
            <p class="project-description">Recognizes celebrities in images or videos using computer vision algorithms to match faces from a curated database.</p>
            <p class="project-tech">Technologies used: Python, OpenCV, TensorFlow</p>
            <a class="project-link" href="https://github.com/iampraffulbisht/Bollywood_Face_Recognition" target="_blank">
            <i class="fa-brands fa-github"></i> GitHub
        </a>
        </div>
    """, unsafe_allow_html=True)

# Project 4: Virtual-PaintBrush
with col4:
    st.markdown("""
        <div class="project-container">
            <h3 class="project-title">AI Virtual Paint Brush</h3>
            <p class="project-description">A virtual painter that lets users draw on a digital canvas through hand gestures detected by a webcam in real-time.</p>
            <p class="project-tech">Technologies used: Python, OpenCV, TensorFlow</p>
            <a class="project-link" href="https://github.com/iampraffulbisht/Virtual-PaintBrush" target="_blank">
            <i class="fa-brands fa-github"></i> GitHub
        </a>
        </div>
    """, unsafe_allow_html=True)


st.write(" ")
st.title("My Skills")
st.slider("Programming",0,100,90)
st.slider("Computer Vision",0,100,85)
st.slider("Machine Learning",0,100,89)
st.slider("Web Development",0,100,80)
st.slider("Photography",0,100,95)
st.title("My Resume")
resume_file = "Prafful_s_Resume.pdf"

# Open the PDF file
resume_image = Image.open("Resume.png")
st.image(resume_image, caption="Preview of My Resume", width=None)

# Provide the download button for the PDF
col1, col2, col3 = st.columns([1, 1, 1])
with open(resume_file, "rb") as file:
    with col2:
        st.download_button(
            label="📄 Download My Resume",
            data=file,
            file_name="Prafful_s_Resume.pdf",
            mime="application/pdf"
        )
st.title("Gallery")
st.subheader(" Photography Skills")
num_photos = 9  # Total number of photos
num_cols = 3    # Number of columns
photos_per_col = num_photos // num_cols
col1,col2,col3 = st.columns(3)

for i in range(1,photos_per_col+1):
    img_path = f"images/photo-{i}.jpeg"
    with col1:
        st.image(img_path,width=None)
for i in range(photos_per_col+1,2*photos_per_col+1):
    img_path = f"images/photo-{i}.jpeg"
    with col2:
        st.image(img_path,width=None)
for i in range(2*photos_per_col+1,num_photos+1):
    img_path = f"images/photo-{i}.jpeg"
    with col3:
        st.image(img_path,width=None)


st.write("")
st.title("Contact Me")
st.markdown("<h3 style='text-align: center; margin-left:20px;'>Get in Touch </h3>", unsafe_allow_html=True)


st.markdown("<p style='text-align: center;'>Email: praffulbisht2911@gmail.com</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Phone: +91 8219144427</p>", unsafe_allow_html=True)

# Social Media Links
st.subheader("Connect on Social Media")
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    # Custom CSS for the LinkedIn button
    st.markdown("""
        <style>
        .linkedin-button {
            display: inline-block;
            background-color: #24292e;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            font-family: Arial, sans-serif;
            transition: background-color 0.3s;
            text-align: center;
        }
        .linkedin-button:hover {
            background-color: #084a91;
        }
        .fa-linkedin {
            margin-right: 8px;
            vertical-align: middle;
        }
        </style>
    """, unsafe_allow_html=True)

    # LinkedIn button with Font Awesome icon
    st.markdown('''
        <a class="linkedin-button" href="https://www.linkedin.com/in/prafful-bisht-4761b923b/" target="_blank">
            <i class="fa-brands fa-linkedin"></i> LinkedIn
        </a>
    ''', unsafe_allow_html=True)

with col2:
    # Custom CSS for the X (Twitter) button
    st.markdown("""
        <style>
        .x-button {
            display: inline-block;
            background-color: #24292e;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            font-family: Arial, sans-serif;
            transition: background-color 0.3s;
            text-align: center;
        }
        .x-button:hover {
            background-color: #084a91;
        }
        .fa-twitter {
            margin-right: 8px;
            vertical-align: middle;
        }
        </style>
    """, unsafe_allow_html=True)

    # X button with Font Awesome icon
    st.markdown('''
        <a class="x-button" href="https://x.com/prafullbisht" target="_blank">
            <i class="fa-brands fa-x-twitter"></i> Twitter
        </a>
    ''', unsafe_allow_html=True)

with col3:
    # Custom CSS for the GitHub button
    st.markdown("""
        <style>
        .github-button {
            display: inline-block;
            background-color: #24292e;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            font-family: Arial, sans-serif;
            transition: background-color 0.3s;
            text-align: center;
        }
        .github-button:hover {
            background-color: #084a91;
        }
        .fa-github {
            margin-right: 8px;
            vertical-align: middle;
        }
        </style>
    """, unsafe_allow_html=True)

    # GitHub button with Font Awesome icon
    st.markdown('''
        <a class="github-button" href="https://github.com/iampraffulbisht" target="_blank">
            <i class="fa-brands fa-github"></i> GitHub
        </a>
    ''', unsafe_allow_html=True)

# Add the Font Awesome script to load icons globally
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
""", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<p style='text-align: center;'>© 2024 Prafful Bisht. All rights reserved.</p>", unsafe_allow_html=True)

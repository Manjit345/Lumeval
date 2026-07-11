"""
MatchForge Test Cases: Sample inputs and expected outputs used to evaluate MatchForge's skills analyzer and resume rewriter using DeepEval.
"""

RESUME_TEXT = """Manjit Dey
Career Objective
To expand my knowledge and develop my skills in Data Science, Machine Learning, Deep Learning,
and GenAI. I aim to apply my knowledge and skills to solve real-world problems and prepare myself
for the industry.
Education
Heritage Institute of Technology, Kolkata
Bachelor of Technology in Computer Science Technology 2022-2026
Specialization: Data Science Overall GPA: 8.85 (as of 6th semester)
Projects
PDF Chatterbox
A RAG-based application built with Streamlit where users can upload PDF documents and ask
queries about the content.
HireGuru (Ongoing)
Started building with a team of four during the AIgnite 2025 Hackathon.
Developing a smart AI interview platform that summarizes candidate resumes and asks interview questions.
Video Game Recommender System
Created a recommendation system using Steam game dataset that suggests similar games based on user selections.
Skills
Programming Languages: Python, SQL, C, C++
Software & Frameworks: Git, GitHub, HuggingFace"""

JOB_DESCRIPTION = """Software Developer with Gen AI Expertise
We are seeking a motivated and innovative Software Developer with a strong foundation in 
Generative AI technologies.
Mandatory Skills:
- Strong knowledge of Generative AI concepts and frameworks
- Proficiency in at least one programming language (Python, Java, or JavaScript)
- Familiarity with software development methodologies (Agile, Scrum)
- Basic understanding of database management and APIs
Preferred Skills:
- Experience with machine learning libraries (TensorFlow, PyTorch)
- Knowledge of cloud platforms (AWS, Azure)
- Exposure to front-end technologies (HTML, CSS, React)"""

SKILLS_GAP_OUTPUT = """Present skills: Python, SQL, Generative AI concepts & frameworks, HuggingFace, RAG
Missing skills: Agile and Scrum methodologies, APIs, Machine learning libraries (TensorFlow, PyTorch), Cloud platforms (AWS, Azure, GCP), Front-end technologies (HTML, CSS, React)
Reasoning: The candidate is a strong fit for an entry-level Generative AI developer role, having built multiple projects leveraging LLMs, RAG, and HuggingFace. However, they lack experience with Agile/Scrum, front-end technologies, major cloud providers, and specific ML libraries like TensorFlow or PyTorch."""

REWRITTEN_RESUME = """Manjit Dey
Professional Summary
A motivated Computer Science Technology student specializing in Data Science with practical 
experience designing and developing Generative AI applications. Proven ability to build 
functional software solutions using Python, HuggingFace, and RAG architectures.
Technical Skills
Programming Languages: Python, SQL, C, C++
Software, Frameworks & Libraries: HuggingFace, Streamlit, Git, GitHub
Projects
PDF Chatterbox (GenAI / RAG Application)
Designed and built a Retrieval-Augmented Generation (RAG) software application using Python and Streamlit.
Integrated GenAI workflows allowing users to upload PDF documents and receive context-aware answers.
HireGuru (Smart AI Interview Platform) - AIgnite 2025 Hackathon
Collaborated in a team of four to design and develop an intelligent AI recruitment platform.
Developed features to parse and summarize candidate resumes and generate interview questions.
Video Game Recommender System
Developed a content-based recommendation application leveraging Python and a Steam games dataset."""
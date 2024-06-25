import streamlit as st
from src.review_page1 import sa_questions
from src.transcript_page2 import generate_transcript_questions
from src.reading_page3 import generate_reading_questions
from src.islr_long_form_questions_page5 import generate_open_questions
from src. image_questions_page4 import generate_image_questions

def intro():
    import streamlit as st

    st.write("# Welcome to the Graph Theory Prep App! 👋")
    st.sidebar.success("Choose a practice category to begin.")

    st.markdown("""
Streamlit powers this interactive test aid designed to support students in their preparation for exams on graph theory. The app tests your knowledge of lecture notes, Newman's book on networks, and any papers mentioned in the lectures. You will find a variety of question types including:

1. **Multiple Choice Questions**: Assess your understanding with multiple-choice questions based on the lecture notes and readings.
2. **Open-ended Questions**: Explore deeper thought questions that encourage comprehensive understanding of graph theory concepts.
3. **Chart & Graph Interpretation**: Test your skills in interpreting charts and graphs related to graph theory and network analysis.

Get started by selecting a practice category from the dropdown on the left and enhance your exam preparation.
    """)


def review_questions():
    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.write('Graph Theory Multiple Choice Questions')
    sa_questions()

# def reading_questions():
#     st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
#     st.write('multiple choice questions based on the readings')
#     generate_reading_questions()

# def transcript_questions():
#     st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
#     st.write('multiple choice questions based on lecture transcripts')
#     generate_transcript_questions()

def open_ended_questions():
    import streamlit as st
    st.markdown(f"# {list(page_names_to_funcs.keys())[4]}")
    st.write('Graph Theory Open Ended Questions')
    generate_open_questions()

# def chart_questions():
#     import streamlit as st
#     st.markdown(f"# {list(page_names_to_funcs.keys())[5]}")
#     st.write('Chart & Graph Intepretation')
#     generate_image_questions()

def reset_or_initialize_state():
    if 'token' in st.session_state:
        del st.session_state['token']

page_names_to_funcs = {
    "—": intro,
    "Multiple Choice Questions": review_questions,
    # "Course Readings": reading_questions,
    # "Lecture Videos": transcript_questions,
    "Open Ended Questions": generate_open_questions,
    # "Charts & Code": generate_image_questions
}

if 'current_demo' not in st.session_state:
    st.session_state['current_demo'] = None

# Sidebar selection box
demo_name = st.sidebar.selectbox("Choose Practice Type", list(page_names_to_funcs.keys()))

# Check if the demo has changed
if st.session_state['current_demo'] != demo_name:
    st.session_state['current_demo'] = demo_name  # Update the current demo
    reset_or_initialize_state()  # Reset or initialize state based on new demo

# Dynamically call the selected demo function
if demo_name in page_names_to_funcs:
    page_names_to_funcs[demo_name]()

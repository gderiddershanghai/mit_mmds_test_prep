def generate_open_questions():

    import streamlit as st
    from src.states import Token

    def apply_custom_css():
        custom_css = """
        <style>
            .question-style {
                font-size: 18px;

            }
            .textbox-style {
                font-size: 16px;
            }
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)

    def question_generator(label, question_key):
        answer = st.text_area(label, key=question_key, placeholder="Type your answer here...", height=100)
        return answer

    # Check if 'token' is already in the session state, otherwise initialize it
    if 'token' not in st.session_state:
        st.session_state.token = Token(STATE='open')
        st.session_state.token.initialize_open_questions()

    apply_custom_css()
    questions = st.session_state.token.mpc_questions

    for i, q in enumerate(questions, start=1):
        label = q['question']
        correct_answer = q['correct_answer']
        question_key = f"question_{i}"

        st.markdown('-------------------------------')
        st.markdown(f'<div class="question-style">Question {i}: {label}</div>', unsafe_allow_html=True)

        answer = question_generator(" ", question_key)

        if st.button('Compare Answers', key=f"submit_{i}"):
            st.info(f"{correct_answer}")

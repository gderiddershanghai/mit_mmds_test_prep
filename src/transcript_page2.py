
def generate_transcript_questions():

    import streamlit as st
    from src.states import Token

    def apply_custom_css():
        custom_css = """
        <style>
            .question-style {
                font-size: 20px; /* Customize the font size as needed */
                font-weight: bold; /* Optional: Make the question bold */
            }
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)

    def question_generator(label, options, question_key):
        # Display the question as a radio button
        question = st.radio(label='Please select the correct answer', options=options, key=question_key)
        return question

    # Check if 'token' is already in the session state, otherwise initialize it
    if 'token' not in st.session_state:
        st.session_state.token = Token(STATE='transcript')
        st.session_state.token.initialize_transcript_questions()

    apply_custom_css()
    questions = st.session_state.token.mpc_questions

    for i, q in enumerate(questions, start=0):
        label = q['question']
        options = q['options_list']
        correct_answer = q['correct_answer']
        question_key = f"question_{i}"

        print('question key', question_key)

        # Display the question with custom styling
        st.markdown('-------------------------------')
        st.markdown(f'<div class="question-style">{label}</div>', unsafe_allow_html=True)

        question = question_generator(label, options, question_key)

        # Use a unique key for each submit button to handle them individually
        if st.button('Submit', key=f"submit_{i}"):
            if question == correct_answer:
                st.success('Great work!')
            else:
                st.error(f"Ai, the correct answer was {correct_answer}")

            # Optionally, provide a way to review material related to the question
            if 'chapter_information' in q:
                st.write(f"You can review {q['chapter_information']}")

# if __name__ == "__main__":
#     main()

import streamlit as st
import random
import time

# Custom exception
class InvalidAnswerError(Exception):
    def __str__(self):
        return "Please enter a valid integer answer."

# Initialize session state
if 'name' not in st.session_state:
    st.session_state.name = ''
if 'started' not in st.session_state:
    st.session_state.started = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question' not in st.session_state:
    st.session_state.question = ''
if 'correct_answer' not in st.session_state:
    st.session_state.correct_answer = 0
if 'question_start' not in st.session_state:
    st.session_state.question_start = 0.0
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0.0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Title
st.title("🧠 Math Quiz Game")

# Step 1: Enter your name
if not st.session_state.started:
    name = st.text_input("Enter your name to start the game:")

    if st.button("Start Game") and name.strip():
        st.session_state.name = name.strip()
        st.session_state.started = True
        st.session_state.start_time = time.time()
        st.session_state.score = 0
        st.session_state.game_over = False
        st.success(f"Welcome {st.session_state.name}! Game started at {time.strftime('%H:%M:%S', time.localtime(st.session_state.start_time))}")

# Step 2: Ask questions
if st.session_state.started and not st.session_state.game_over:
    if st.session_state.question == '':
        question_type = random.choice(["square", "squareroot"])
        if question_type == "square":
            number = random.randint(1, 100)
            st.session_state.correct_answer = number ** 2
            st.session_state.question = f"What is the square of {number}?"
        else:
            answer = random.randint(1, 20)
            number = answer ** 2
            st.session_state.correct_answer = answer
            st.session_state.question = f"What is the square root of {number}?"
        st.session_state.question_start = time.time()

    st.subheader(f"{st.session_state.name}, your question:")
    st.write(st.session_state.question)

    user_input = st.text_input("Your answer:")

    if st.button("Submit Answer"):
        time_taken = round(time.time() - st.session_state.question_start, 2)
        try:
            if not user_input.strip().isdigit():
                raise InvalidAnswerError()
            user_answer = int(user_input)

            if user_answer == st.session_state.correct_answer:
                st.success("Correct!")
                st.session_state.score += 10
            else:
                st.error(f"Wrong! The correct answer was {st.session_state.correct_answer}")
                st.session_state.score -= 5
        except InvalidAnswerError as e:
            st.warning(f"Invalid input: {e}")
            st.session_state.score -= 5

        st.info(f"Time taken to answer: {time_taken} seconds")
        st.info(f"Current Score: {st.session_state.score}")

        # Check win condition
        if st.session_state.score >= 50:
            st.balloons()
            st.success("🎉 Congratulations, you are the winner! 🎉")
            st.session_state.game_over = True
        else:
            # Clear question for next round
            st.session_state.question = ''

    if st.button("End Game"):
        st.session_state.game_over = True

# Step 3: End game
if st.session_state.game_over:
    end_time = time.time()
    st.subheader("🎮 Game Over")
    st.write(f"Name: {st.session_state.name}")
    st.write(f"Final Score: {st.session_state.score}")
    st.write(f"Game started at: {time.strftime('%H:%M:%S', time.localtime(st.session_state.start_time))}")
    st.write(f"Game ended at: {time.strftime('%H:%M:%S', time.localtime(end_time))}")
    st.write(f"Total game time: {round(end_time - st.session_state.start_time, 2)} seconds")

    if st.button("Restart Game"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()

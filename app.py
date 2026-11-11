import streamlit as st

st.set_page_config(page_title="Happy Birthday Karismaa ! ♾", page_icon="♾️")

st.title("♾️ Happy Birthday ! To Infinity and Beyond! ♾️")

st.write("Just like an infinity loop, our friendship has no end, ok so dont overthink tooomuch be calm enjoy this .")

# Initialize st.session_state to track the phase, quiz step, and score
if "phase" not in st.session_state:
    st.session_state.phase = "puzzle phase"
if "puzzle_solved" not in st.session_state:
    st.session_state.puzzle_solved = False
if "step" not in st.session_state:
    st.session_state.step = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# Intro starter question (Phase 1 quiz)
questions = [
    {
        "question": "first of all happy birthday then if u want to start the quiz press anything u want:",
        "options": ["anyways it will start", "dont click on this", "error", "anything"],
    }
]

# Main quiz questions (Phase 2 quiz)
question = [
    {
        "question": "answer travel the world",
        "options": ["Travel the world", "Eat infinite snacks", "Binge-watch every movie", "Build a pillow fort"],
        "answer": "Travel the world"
    },
    {
        "question": "How long are we going to be best friends?",
        "options": ["few years", "till old.", "For infinity...", "tomorrow ?"],
        "answer": "For infinity..."
    },
]

# ==========================================
# PHASE 1: PUZZLE PHASE
# ==========================================
if st.session_state.phase == "puzzle phase":
    st.subheader("Phase 1: The Infinity Riddle 🧩")
    st.write("I have no beginning and I have no end. Turn me on my side, and I look like the number 8. What am I?")
    
    puzzle_guess = st.text_input("Type your answer below:")
    
    if st.button("Answer"):
        if puzzle_guess.strip().lower() == "infinity":
            st.session_state.puzzle_solved = True
        else:
            st.error("Not quite! Hint: Check the theme of this page!")
            
    if st.session_state.puzzle_solved:
        st.success("You unlocked the Infinity loop! ✨")
        st.image("img6.jpeg", caption="Infinite Memories Forever ♾️")
        
        if st.button("Proceed to the Birthday Quiz ➡️"):
            st.session_state.phase = "quiz phase1"
            st.rerun()

# ==========================================
# PHASE 1.5: STARTER QUESTION (ANY OPTION ADVANCES)
# ==========================================
elif st.session_state.phase == "quiz phase1":
    current_q = questions[0]
    
    st.subheader(current_q["question"])
    user_choice = st.radio(
        "Select your answer:",
        current_q["options"],
        key="starter_q"
    )

    if st.button("Submit"):
        # Clicking submit on any answer resets the question counter and advances to the main quiz
        st.session_state.step = 0
        st.session_state.phase = "quiz phase"
        st.rerun()

# ==========================================
# PHASE 2: MAIN QUIZ PHASE
# ==========================================
elif st.session_state.phase == "quiz phase":
    current_q = question[st.session_state.step]
    
    st.subheader(current_q["question"])

    user_choice = st.radio(
        "Select your answer:",
        current_q["options"],
        key=f"q_{st.session_state.step}"
    )

    if st.button("Submit"):
        if user_choice == current_q["answer"]:
            st.session_state.score += 1
            
        st.session_state.step += 1
        
        # Check against question list length
        if st.session_state.step >= len(question):
            st.session_state.phase = "completed phase"
            
        st.rerun()

# ==========================================
# PHASE 3: COMPLETED PHASE
# ==========================================
elif st.session_state.phase == "completed phase":
    st.subheader("Birthday Quiz Complete! 🥳🎂")
    st.write(f"Your final score is **{st.session_state.score} out of {len(question)}**!")
    
    passing_score = 2
    
    if st.session_state.score >= passing_score:
        st.balloons()
        st.success("You passed the quiz! Wishing you the happiest of birthdays filled with infinite joy, laughter, and love! Here are some of my favorite memories with you: 💖♾️")
        
        st.image("img3.jpeg", caption="Memory 1:✨")
        st.image("img2.jpeg", caption="Memory 2:😂")
        st.image("img4.jpeg", caption="Memory 3:♾️")
        st.image("img5.jpeg", caption=" ")
    else:
        st.warning("So close! Give the quiz another try to unlock your special birthday surprise! 🎈")

    if st.button("Replay Birthday Experience 🔄"):
        st.session_state.phase = "puzzle phase"
        st.session_state.puzzle_solved = False
        st.session_state.step = 0
        st.session_state.score = 0
        st.rerun()
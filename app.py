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

# Define the multiple-choice questions
questions = [
    {
        "question": "first of all happy birthday then if u want to start the quiz press anything u want:",
        "options": ["anyways it will start", "dont click on this", "error", "anything"],
        "answer": ["anyways it will start", "dont click on this", "error", "anything"]
    }
]

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
    # --- EDIT PUZZLE PHASE HEADER HERE ---
    st.subheader("Phase 1: The Infinity Riddle 🧩")
    
    # --- EDIT YOUR PUZZLE CLUE / RIDDLE TEXT HERE ---
    st.write("I have no beginning and I have no end. Turn me on my side, and I look like the number 8. What am I?")
    
    # --- EDIT PUZZLE INPUT PROMPT LABEL HERE ---
    puzzle_guess = st.text_input("Type your answer below:")
    
    # --- EDIT PUZZLE SUBMIT BUTTON TEXT HERE ---
    if st.button("Answer"):
        # --- EDIT PUZZLE CORRECT ANSWER HERE (USE LOWERCASE) ---
        if puzzle_guess.strip().lower() == "infinity":
            st.session_state.puzzle_solved = True
        else:
            # --- EDIT PUZZLE WRONG ANSWER HINT MESSAGE HERE ---
            st.error("Not quite! Hint: Check the theme of this page!")
            
    if st.session_state.puzzle_solved:
        # --- EDIT PUZZLE SOLVED SUCCESS MESSAGE HERE ---
        st.success("You unlocked the Infinity loop! ✨")
        
        # --- EDIT IMAGE FILENAME AND CAPTION HERE ---
        st.image("img6.jpg", caption="Infinite Memories Forever ♾️")
        
        # --- EDIT PROCEED TO QUIZ BUTTON TEXT HERE ---
        if st.button("Proceed to the Birthday Quiz ➡️"):
            st.session_state.phase = "quiz phase1"
            st.rerun()
            
elif st.session_state.phase == "quiz phase1":
    current_q = questions[st.session_state.step]
    
    st.subheader(current_q["question"])
    user_choice = st.radio(
        "Select your answer:",
        current_q["options"],
        key=f"q_{st.session_state.step}"
    )

    if st.button("Submit"):
        if user_choice == current_q["answer"]:
            st.session_state.phase == "quiz phase"

# ==========================================
# PHASE 2: QUIZ PHASE
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
        
        if st.session_state.step >= len(questions):
            st.session_state.phase = "completed phase"
            
        st.rerun()

# ==========================================
# PHASE 3: COMPLETED PHASE
# ==========================================
elif st.session_state.phase == "completed phase":
    # --- EDIT COMPLETED PHASE HEADER HERE ---
    st.subheader("Birthday Quiz Complete! 🥳🎂")
    
    # --- EDIT FINAL SCORE MESSAGE HERE ---
    st.write(f"Your final score is **{st.session_state.score} out of {len(questions)}**!")
    
    # --- EDIT PASSING SCORE THRESHOLD HERE (DEFAULT IS 2 OUT OF 3) ---
    passing_score = 2
    
    if st.session_state.score >= passing_score:
        st.balloons()
        
        # --- EDIT FINAL MESSAGE HERE ---
        st.success("You passed the quiz! Wishing you the happiest of birthdays filled with infinite joy, laughter, and love! Here are some of my favorite memories with you: 💖♾️")
        
        # --- EDIT MEMORY 1 IMAGE FILENAME AND CAPTION HERE ---
        st.image("img3.jpg", caption="Memory 1:✨")
        
        # --- EDIT MEMORY 2 IMAGE FILENAME AND CAPTION HERE ---
        st.image("img2.jpg", caption="Memory 2:😂")
        
        # --- EDIT MEMORY 3 IMAGE FILENAME AND CAPTION HERE ---
        st.image("img4.jpg", caption="Memory 3:♾️")
        st.image("img5.jpg", caption=" ")
    else:
        # --- EDIT DID NOT PASS MESSAGE HERE ---
        st.warning("So close! Give the quiz another try to unlock your special birthday surprise! 🎈")

    # --- EDIT RESTART BUTTON TEXT HERE ---
    if st.button("Replay Birthday Experience 🔄"):
        st.session_state.phase = "puzzle phase"
        st.session_state.puzzle_solved = False
        st.session_state.step = 0
        st.session_state.score = 0
        st.rerun()

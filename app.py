import streamlit as st

# --- EDIT PAGE TAB TITLE AND ICON HERE ---
st.set_page_config(page_title="Happy Birthday! ∞", page_icon="♾️")

# --- EDIT MAIN BIRTHDAY TITLE HERE ---
st.title("♾️ Happy Birthday! To Infinity and Beyond! ♾️")

# --- EDIT WELCOME MESSAGE HERE ---
st.write("Welcome to your special birthday experience! Just like an infinity loop, our friendship has no end. Let's start with a quick challenge!")

# Initialize st.session_state to track the phase, quiz step, and score
if "phase" not in st.session_state:
    st.session_state.phase = "puzzle phase"
if "puzzle_solved" not in st.session_state:
    st.session_state.puzzle_solved = False
if "step" not in st.session_state:
    st.session_state.step = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# Define the 3 multiple-choice questions
questions = [
    {
        # --- EDIT QUIZ QUESTION 1 HERE ---
        "question": "1. What is my favorite memory of us?",
        # --- EDIT QUIZ QUESTION 1 ANSWER CHOICES HERE ---
        "options": ["Our late-night talks", "That crazy road trip", "Laughing over nothing", "All of the above"],
        # --- EDIT QUIZ QUESTION 1 CORRECT ANSWER HERE (MUST MATCH ONE OF THE OPTIONS EXACTLY) ---
        "answer": "All of the above"
    },
    {
        # --- EDIT QUIZ QUESTION 2 HERE ---
        "question": "2. If we had infinite time together, what would we do first?",
        # --- EDIT QUIZ QUESTION 2 ANSWER CHOICES HERE ---
        "options": ["Travel the world", "Eat infinite snacks", "Binge-watch every movie", "Build a pillow fort"],
        # --- EDIT QUIZ QUESTION 2 CORRECT ANSWER HERE (MUST MATCH ONE OF THE OPTIONS EXACTLY) ---
        "answer": "Travel the world"
    },
    {
        # --- EDIT QUIZ QUESTION 3 HERE ---
        "question": "3. How long are we going to be best friends?",
        # --- EDIT QUIZ QUESTION 3 ANSWER CHOICES HERE ---
        "options": ["A few years", "Until we get old", "For infinity", "Until tomorrow"],
        # --- EDIT QUIZ QUESTION 3 CORRECT ANSWER HERE (MUST MATCH ONE OF THE OPTIONS EXACTLY) ---
        "answer": "For infinity"
    }
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
    if st.button("Check Answer"):
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
        st.image("infinity.jpg", caption="Infinite Memories Forever ♾️")
        
        # --- EDIT PROCEED TO QUIZ BUTTON TEXT HERE ---
        if st.button("Proceed to the Birthday Quiz ➡️"):
            st.session_state.phase = "quiz phase"
            st.rerun()

# ==========================================
# PHASE 2: QUIZ PHASE
# ==========================================
elif st.session_state.phase == "quiz phase":
    current_q = questions[st.session_state.step]
    
    st.subheader(current_q["question"])
    
    # --- EDIT RADIO BUTTON PROMPT LABEL HERE ---
    user_choice = st.radio(
        "Select your answer:",
        current_q["options"],
        key=f"q_{st.session_state.step}"
    )
    
    # --- EDIT QUIZ SUBMIT BUTTON TEXT HERE ---
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
        st.image("memory1.jpg", caption="Memory 1: Unforgettable times ✨")
        
        # --- EDIT MEMORY 2 IMAGE FILENAME AND CAPTION HERE ---
        st.image("memory2.jpg", caption="Memory 2: Always laughing together 😂")
        
        # --- EDIT MEMORY 3 IMAGE FILENAME AND CAPTION HERE ---
        st.image("memory3.jpg", caption="Memory 3: Friends to infinity and beyond ♾️")
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

import streamlit as st
import pages.sign_up as sign_up
import pages.sign_in as sign_in

# Set wide layout
st.set_page_config(layout="wide")
st.logo("images/LOGO.jpg")

st.markdown(
    """
<style>
    /* Style all buttons */
    div.stButton > button {
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }

    /* Hover effect */
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.2);
        background: linear-gradient(45deg, #FF416C, #FF4B2B);
        color: white;
    }

    /* Active/Clicked effect */
    div.stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Primary Button Style (Gold/Orange) */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: black;
        border: none;
    }
    
    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(45deg, #FFA500, #FFD700);
        color: black;
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }
</style>
""",
    unsafe_allow_html=True,
)

st.divider()

col1, col2 = st.columns(2)


with col1:
    sign_in_btn = st.button("Sign In", use_container_width=True)

with col2:
    sign_up_btn = st.button("Sign Up", use_container_width=True)

st.divider()

# Trigger dialogs based on query
if sign_in_btn:
    sign_in.sign_in_pop_up()
elif sign_up_btn:
    sign_up.sign_up_pop_up()

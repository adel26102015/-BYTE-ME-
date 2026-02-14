import streamlit as st
import pages.sign_up as sign_up
import pages.sign_in as sign_in
from data.styling import apply_standard_styling

st.set_page_config(layout="wide")
st.logo("./images/LOGO.jpg")

apply_standard_styling()

st.divider()

col1, col2 = st.columns(2)


with col1:
    sign_in_btn = st.button("Sign In", use_container_width=True)

with col2:
    sign_up_btn = st.button("Sign Up", use_container_width=True)

st.divider()

if sign_in_btn:
    sign_in.sign_in_pop_up()
elif sign_up_btn:
    sign_up.sign_up_pop_up()

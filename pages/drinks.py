import streamlit as st
from data.data import drink_categories
from data.styling import apply_standard_styling
import time


st.set_page_config(page_title="Drinks", layout="wide")
apply_standard_styling()

st.title("Drinks")

st.logo("images/LOGO.jpg")


st.session_state.is_signed_in = (
    st.session_state.is_signed_in if "is_signed_in" in st.session_state else False
)


if st.session_state.is_signed_in == False:
    st.error("Please Sign In before Any Operation !")

    time.sleep(3)
    st.switch_page("../Adel-V1/app.py")

else:
    col1, col2 = st.columns(2)

    with col1:
        st.image(
            drink_categories[0]["image"],
            caption=drink_categories[0]["title"],
            use_container_width=True,
        )
        cold_drinks_btn = st.button("Buy cold drinks", use_container_width=True)

        if cold_drinks_btn:
            st.switch_page("./pages/cold_drinks.py")

    with col2:
        st.image(
            drink_categories[1]["image"],
            caption=drink_categories[1]["title"],
            use_container_width=True,
        )
        hot_drinks_btn = st.button("Buy hot drinks", use_container_width=True)

        if hot_drinks_btn:
            st.switch_page("./pages/hot_drinks.py")

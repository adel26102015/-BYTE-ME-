import streamlit as st
from data.accounts_data import load_accounts


def valildate_sign_in_form(email_input, password_input):

    if email_input == "":
        st.warning("Type a valid email")
        return False

    elif password_input == "" or len(password_input) < 8:
        st.warning("Please enter a valid password")
        return False

    else:
        users_list = load_accounts()
        for user in users_list:
            if email_input == user["email"] and password_input == user["password"]:
                st.session_state.is_signed_in = True

                return True

        st.session_state.is_signed_in = False
        return False


@st.dialog("sign in")
def sign_in_pop_up():
    email_input2 = st.text_input("email")
    password_input2 = st.text_input("password")

    if st.button("submit"):
        validation_result = valildate_sign_in_form(email_input2, password_input2)

        if validation_result:
            st.success("OKAY!")
            st.snow()
            st.switch_page("./pages/home.py")

        else:
            st.error("chech your data")

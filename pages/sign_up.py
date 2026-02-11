import streamlit as st
from data.accounts_data import load_accounts, save_accounts


def valildate_sign_up_form(
    email_input, password_input, phone_number, birthday_date, user_name
):

    if email_input == "":
        st.warning("Type a valid email")
        return False

    elif password_input == "" or len(password_input) < 8:
        st.warning("Please enter a password more than 8 characters")
        return False

    elif phone_number == "" or len(phone_number) < 11 or phone_number is None:
        st.warning("enter a valid number")
        return False

    elif birthday_date == "" or birthday_date is None:
        st.warning("please enter a valid birthday date")
        return False

    elif user_name == "" or len(user_name) < 3 or user_name is None:
        st.warning("please enter a valid username")
        return False

    else:
        new_user = {
            "username": user_name,
            "phone": phone_number,
            "email": email_input,
            "password": password_input,
            "birthdate": str(birthday_date),
        }

        users_list = load_accounts()
        users_list.append(new_user)
        save_accounts(users_list)
        return True


@st.dialog("sign up")
def sign_up_pop_up():
    user_name = st.text_input("username")
    email_input = st.text_input("email")
    password_input = st.text_input("password")
    phone_number = st.text_input("phone number")
    birthday_date = st.date_input("birthday date")

    if st.button("submit", use_container_width=True):
        validation_result = valildate_sign_up_form(
            email_input, password_input, phone_number, birthday_date, user_name
        )

        if validation_result:
            st.snow()
            st.success("Account Registered successfully !")

        else:
            st.error("chech your data")

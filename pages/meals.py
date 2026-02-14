import streamlit as st
from data.data import meals_dict
from data.styling import get_base64_image, get_standard_css
import time
import os


st.set_page_config(page_title="MEALS", layout="wide")

st.title("Meals")

st.logo("images/LOGO.jpg")

st.session_state.orders_list = (
    st.session_state.orders_list if "orders_list" in st.session_state else []
)


st.session_state.is_signed_in = (
    st.session_state.is_signed_in if "is_signed_in" in st.session_state else False
)


if st.session_state.is_signed_in == False:
    st.error("Please Sign In before Any Operation !")

    time.sleep(3)
    st.switch_page("../Adel-V1/app.py")

else:
    # Apply standardized styling
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    bg_image_path = os.path.join(parent_dir, "images", "background.jpeg")
    bg_image = get_base64_image(bg_image_path)

    st.markdown(get_standard_css(bg_image), unsafe_allow_html=True)

    meals = meals_dict["items"]

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i, item in enumerate(meals):
        name = item["name"]

        price = item["price"]

        image = item["image"]
        with cols[i]:
            with st.container(key=f"meals_form_{item}"):
                st.subheader(name)
                st.subheader(price)

                st.image(image, width=200)

                col1, col2, col3 = st.columns(3)

                with col1:
                    if st.button("➕", key=f"{item}_add_btn", use_container_width=True):
                        st.session_state.orders_list.append(
                            {"name": name, "price": price}
                        )
                with col2:
                    if st.button(
                        "➖", key=f"{item}_remove_btn", use_container_width=True
                    ):
                        st.session_state.orders_list.remove(
                            {"name": name, "price": price}
                        )
                with col3:
                    if st.button(
                        "ℹ️", key=f"{item}details_btn", use_container_width=True
                    ):
                        st.session_state.selected_item = item
                        st.switch_page("./pages/item_details.py")

    if len(st.session_state.orders_list) > 30:
        st.error("Too much orders ")
        st.rerun()

    with st.sidebar:
        with st.expander("ORDER LIST 🛒"):
            for i in st.session_state.orders_list:
                col1, col2 = st.columns(2)

                with col1:
                    st.write(i["name"])

                with col2:
                    st.write(i["price"])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        go_to_home_btn = st.button("back home🔙", use_container_width=True)
        if go_to_home_btn:
            st.switch_page("./pages/home.py")

    with col2:
        checkout_btn = st.button("checkout", use_container_width=True)
        if checkout_btn:
            st.switch_page("./pages/checkout.py")

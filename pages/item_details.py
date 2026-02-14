import streamlit as st
import time
from data.styling import apply_standard_styling

st.set_page_config(page_title="Item Details", layout="wide")
apply_standard_styling()

st.title("Item Details")

st.logo("images/LOGO.jpg")

st.session_state.orders_list = (
    st.session_state.orders_list if "orders_list" in st.session_state else []
)

st.session_state.is_signed_in = (
    st.session_state.is_signed_in if "is_signed_in" in st.session_state else False
)

st.session_state.selected_item = (
    st.session_state.selected_item if "selected_item" in st.session_state else None
)


item = st.session_state.selected_item
item_name = item["name"]
item_price = item["price"]
item_image = item["image"]
item_rate = item["rate"]
item_calories = item["calories"]
item_ingredients = item["ingredients"]


if st.session_state.is_signed_in == False:
    st.error("Please Sign In before Any Operation !")

    time.sleep(3)
    st.switch_page("../Adel-V1/app.py")

else:
    st.header(item_name)
    c1, c2 = st.columns([2, 1])

    with c1:
        st.image(item_image)

    with c2:
        st.subheader(f"**price** : {item_price} LE")
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕", key=f"{item}_add_btn", use_container_width=True):
                st.session_state.orders_list.append(
                    {"name": item_name, "price": item_price}
                )
        with col2:
            if st.button("➖", key=f"{item}_remove_btn", use_container_width=True):
                st.session_state.orders_list.remove(
                    {"name": item_name, "price": item_price}
                )
        st.divider()

        mcol1, mcol2 = st.columns(2)
        with mcol1:
            st.metric(label="Rating", value=f"⭐ {item['rate']}")
        with mcol2:
            st.metric(label="calories", value=f"🔥 {item['calories']}")

        st.markdown("### Ingredients")
        item_ingredients = item["ingredients"]
        for ing in item_ingredients:
            st.write(f"- {ing}")


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

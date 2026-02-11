import streamlit as st
from data.data import desserts_dict
import time




st.set_page_config(page_title="DESSERTS", layout="wide")

st.title("Desserts")

st.logo("images/LOGO.jpg")


st.session_state.orders_list = st.session_state.orders_list if "orders_list" in st.session_state else []



st.session_state.is_signed_in = st.session_state.is_signed_in if "is_signed_in" in st.session_state else False


if st.session_state.is_signed_in == False:
    st.error("Please Sign In before Any Operation !")
    
    time.sleep(3)
    st.switch_page("../Adel-V1/app.py")
     
else : 
    
        
        
    st.markdown("""
        <style>
        [data-testid="stImage"] img {
            height: 300px;
            object-fit: cover;
            width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)


    desserts = desserts_dict["items"]


    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]


    for i, item in enumerate(desserts):
        name = item["name"]
        
        price = item["price"]
        
        image = item["image"]
        with cols[i]:
            with st.container(key=f"desserts_form_{item}"):
                st.subheader(name)
                st.subheader(price)            

                st.image(image, width=200)

                col1, col2, col3 = st.columns(3)

                with col1:
                    if st.button("➕", key=f"{item}_add_btn", use_container_width=True):
                        st.session_state.orders_list.append({"name": name, "price":price})
                with col2:
                    if st.button("➖", key=f"{item}_remove_btn", use_container_width=True):
                        st.session_state.orders_list.remove({"name": name,
                                                            "price":price})
                with col3 :
                    if st.button("ℹ️", key=f"{item}details_btn", use_container_width=True):
                        st.session_state.selected_item = item
                        st.switch_page("./pages/item_details.py")


    with st.sidebar:
            with st.expander("ORDER LIST 🛒"):
                for i in st.session_state.orders_list:
                    col1,col2 = st.columns(2)
                    
                    with col1:
                        st.write(i["name"])
                    
                    with col2 :
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

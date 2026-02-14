import streamlit as st
from data.styling import apply_standard_styling

st.set_page_config(page_title="About Us", page_icon="👨‍🍳", layout="wide")
apply_standard_styling()

st.title("👨‍🍳 About Adel's Kitchen")

c1, c2 = st.columns(2)

with c1:
    st.image(
        "https://images.unsplash.com/photo-1556910103-1c02745a30bf",
        caption="Our Kitchen",
        use_container_width=True,
    )
with c2:
    st.write("""
    ### Our Story
    Welcome to **Byte Me**! our website help to deliever all delious food write in your hand
    
    we always want you to eat the special food and we hope that you be always happy with our delicious food
    
    ### Our Promise
    - **Fresh Ingredients**: We always use the freshest ingredients.
    - **Fast Delivery**: From our kitchen to your table in minutes.
    - **Top Hygiene Standards**: Your safety is our priority.
    """)
st.info("Check out our menu to start ordering!")
if st.button("Go to Menu", use_container_width=True):
    st.switch_page("./pages/home.py")

st.divider()
st.success("📍 Located in Kafr EL Shiekh, Egypt | 📞 Contact: +20 100 946 6865")

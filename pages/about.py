import streamlit as st

st.set_page_config(page_title="About Us", page_icon="👨‍🍳", layout="wide")
st.title("👨‍🍳 About Adel's Kitchen")

st.markdown(
    """
<style>
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
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.2);
        background: linear-gradient(45deg, #FF416C, #FF4B2B);
        color: white;
    }
    div.stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""",
    unsafe_allow_html=True,
)

c1,c2 = st.columns(2)

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
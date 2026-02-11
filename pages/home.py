import streamlit as st
import pages.sign_up as sign_up
import pages.sign_in as sign_in
from data.data import categories

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

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
    
    [data-testid="stImage"] img {
        height: 300px;
        object-fit: cover;
        width: 100%;
        border-radius: 15px;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("🍔 BYTE ME")
st.logo("images/LOGO.jpg")


st.subheader("🔥 Trending Now")
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
            use_container_width=True,
        )
    with col2:
        st.write("### The Ultimate Burger")
        st.write(
            "Our signature beef patty topped with melted cheddar, caramelized onions, and secret sauce."
        )
        st.caption("⭐ 4.9 (120+ reviews)")
        if st.button("Order Now - 180 LE", key="featured_btn", type="primary"):
            st.switch_page("./pages/meals.py")

st.divider()

st.subheader("🍽️ Menu Categories")
col1, col2, col3, col4 = st.columns(4)
cols = [col1, col2, col3, col4]

for i, category in enumerate(categories):
    with cols[i]:
        st.image(
            category["image"],
            caption=category["title"],
            use_container_width=True,
        )
        if st.button(
            f"Order {category['title']} !",
            key=f"btn_{category['title']}",
            use_container_width=True,
        ):
            st.switch_page(f"./pages/{category['page']}")


st.divider()
st.subheader("💬 What our customers say")
reviews = [
    {
        "name": "Sarah M.",
        "text": "Best burger in town! Delivery was super fast.",
        "rating": "⭐⭐⭐⭐⭐",
    },
    {
        "name": "Ahmed K.",
        "text": "Love the cold drinks collection. Very refreshing.",
        "rating": "⭐⭐⭐⭐⭐",
    },
    {
        "name": "Laila O.",
        "text": "The packaging is excellent and food arrived hot.",
        "rating": "⭐⭐⭐⭐",
    },
]

cols = st.columns(3)
for i, review in enumerate(reviews):
    with cols[i]:
        st.markdown(f"**{review['name']}**")
        st.caption(review["rating"])
        st.info(f"_{review['text']}_")

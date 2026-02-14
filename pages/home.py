import streamlit as st
from data.data import categories
from data.styling import apply_standard_styling

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

apply_standard_styling()

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

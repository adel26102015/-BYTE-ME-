import streamlit as st
import time
st.set_page_config(page_title="Checkout", page_icon="🛒", layout="wide")

st.title("🛒 Checkout")
st.logo("images/LOGO.jpg")


st.session_state.orders_list = (
    st.session_state.orders_list if "orders_list" in st.session_state else []
)


st.session_state.is_signed_in = st.session_state.is_signed_in if "is_signed_in" in st.session_state else False


if st.session_state.is_signed_in == False:
    st.error("Please Sign In before Any Operation !")
    time.sleep(3)
    st.switch_page("../Adel-V1/app.py")
     
else : 
        


    st.subheader("📋 Order Summary")

    if st.session_state.orders_list:
        from collections import defaultdict

        item_counts = defaultdict(lambda: {"quantity": 0, "price": 0})

        for order_item in st.session_state.orders_list:
            name = order_item["name"]
            price = order_item["price"]
            item_counts[name]["quantity"] += 1
            item_counts[name]["price"] = price

        
        st.write("**Item**")
        st.divider()

        total = 0

        for item_name, item_data in item_counts.items():
            quantity = item_data["quantity"]
            price = item_data["price"]
            subtotal = price * quantity
            total += subtotal


            col1, col2, col3 = st.columns([3, 2, 1])

            with col1:
                st.write(f"**{item_name}**")
                st.caption(f"{price} LE × {quantity}")

            with col2:
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    if st.button(
                        "➕", key=f"{item_name}_add_btn", use_container_width=True
                    ):
                        st.session_state.orders_list.append(
                            {"name": item_name, "price": price}
                        )
                        st.rerun()
                with btn_col2:
                    if st.button(
                        "➖", key=f"{item_name}_remove_btn", use_container_width=True
                    ):
                        for i, order in enumerate(st.session_state.orders_list):
                            if order["name"] == item_name:
                                st.session_state.orders_list.pop(i)
                                break
                        st.rerun()

            with col3:
                st.write(f"**{subtotal} LE**")

            st.divider()

        col1, col2 = st.columns([5, 1])
        with col1:
            st.write("### Total:")
        with col2:
            st.write(f"### {total} LE")

        st.divider()

        
        st.subheader("📝 Delivery Information")

        with st.form("checkout_form"):
            col1, col2 = st.columns(2)

            with col1:
                name_input = st.text_input(
                    "Full Name *", placeholder="Enter your full name"
                )
                phone_input = st.text_input(
                    "Phone Number *", placeholder="+20 XXX XXX XXXX"
                )
                email_input = st.text_input("Email", placeholder="your.email@example.com")

            with col2:
                address_input = st.text_area(
                    "Delivery Address *", placeholder="Street, Building, Apartment"
                )
                city_input = st.text_input("City *", placeholder="Cairo")
                notes_input = st.text_area(
                    "Order Notes", placeholder="Any special instructions?"
                )

            st.subheader("💳 Payment Method")
            payment_method = st.radio(
                "Select payment method:",
                ["Cash on Delivery", "Credit/Debit Card", "Mobile Wallet"],
                horizontal=True,
            )

            if payment_method == "Credit/Debit Card":
                card_number = st.text_input(
                    "Card Number", placeholder="XXXX XXXX XXXX XXXX"
                )
                col1, col2 = st.columns(2)
                with col1:
                    expiry = st.text_input("Expiry Date", placeholder="MM/YY")
                with col2:
                    cvv = st.text_input("CVV", placeholder="XXX", type="password")

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                back_btn = st.form_submit_button("← Back to Menu", use_container_width=True)
                if back_btn:
                    st.switch_page("./pages/home.py")

            with col2:
                submit_btn = st.form_submit_button(
                    "Place Order 🎉", use_container_width=True, type="primary"
                )

                if submit_btn:
                
                    if (
                        not name_input
                        or not phone_input
                        or not address_input
                        or not city_input
                    ):
                        st.error("⚠️ Please fill in all required fields marked with *")
                    else:
                    
                        st.success("✅ Order placed successfully!")
                        st.balloons()

                        st.info(f"""
                        **Order Confirmation**
                        
                        Thank you, {name_input}! Your order has been confirmed.
                        
                        **Order Details:**
                        - Total Items: {len(st.session_state.orders_list)}
                        - Total Amount: {total} LE
                        - Payment Method: {payment_method}
                        - Delivery Address: {address_input}, {city_input}
                        
                        We'll contact you at {phone_input} shortly to confirm your delivery time.
                        
                        Estimated delivery: 30-45 minutes
                        """)

                        st.session_state.order_placed = True


        if st.session_state.get("order_placed", False):
            if st.button("Start New Order", use_container_width=True, type="primary"):
                st.session_state.orders_list = []
                st.session_state.order_placed = False
                st.switch_page("./pages/home.py")

    else:
        st.warning("🛒 Your cart is empty!")
        st.write("Add some items to your cart before checking out.")

        if st.button("← Back to Menu", use_container_width=True):
            st.switch_page("./pages/home.py")

import streamlit as st

# Title and Styling
st.title("⚡ Electricity Bill Calculator")
st.write("Calculate your monthly bill instantly.")

# User Inputs
user_name = st.text_input("Enter your name:", placeholder="e.g. John Doe")
electricity_consumed = st.number_input("Enter units consumed:", min_value=0.0, step=1.0)

# Calculation Logic
if st.button("Calculate Bill"):
    if user_name:
        bill_amount = electricity_consumed * 8
        
        # Applying the surcharge logic
        if bill_amount > 500:
            bill_amount += 50
            st.info("A surcharge of 50 has been applied for bills over 500.")

        # Displaying the result
        st.success(f"Hello {user_name}!")
        st.metric(label="Total Bill Amount", value=f"${bill_amount}")
    else:
        st.warning("Please enter your name to proceed.")   
    
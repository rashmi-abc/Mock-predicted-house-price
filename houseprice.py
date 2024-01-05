import streamlit as st

# Streamlit App
st.title("House Price Prediction App")

# Sidebar
st.sidebar.header("Input Features")

# Input features
overall_quality = st.sidebar.slider('Overall Quality', 1, 10, 5)
total_rooms_above_grade = st.sidebar.slider('Total Rooms Above Grade', 1, 15, 7)
year_built = st.sidebar.slider('Year Built', 1800, 2022, 2000)
total_basement_sf = st.sidebar.slider('Total Basement SF', 0, 3000, 1500)

# Display input features
st.sidebar.subheader("Selected Input Features")
st.sidebar.write(f"Overall Quality: {overall_quality}")
st.sidebar.write(f"Total Rooms Above Grade: {total_rooms_above_grade}")
st.sidebar.write(f"Year Built: {year_built}")
st.sidebar.write(f"Total Basement SF: {total_basement_sf}")

# Mock prediction (you should replace this with your actual model)
mock_predicted_price = overall_quality * 1000 + total_rooms_above_grade * 500 + (2022 - year_built) * 200 + total_basement_sf * 100

# Display the mock predicted house price
st.subheader("Mock Predicted House Price")
st.write(f"${mock_predicted_price:,.2f}")

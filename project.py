import streamlit as st

# Function to convert length
def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'inches': 39.3701,
        'feet': 3.28084
    }
    # Convert the input to meters first
    value_in_meters = value * length_units[from_unit]
    # Then convert from meters to the desired unit
    return value_in_meters / length_units[to_unit]

# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1,
        'grams': 1000,
        'milligrams': 1e6,
        'pounds': 2.20462,
        'ounces': 35.274
    }
    # Convert the input to kilograms first
    value_in_kg = value * weight_units[from_unit]
    # Then convert from kilograms to the desired unit
    return value_in_kg / weight_units[to_unit]

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # Same unit

# Streamlit UI elements
st.title("Unit Converter")

# Choose the type of conversion
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    # Length converter
    value = st.number_input("Enter value", value=1.0)
    from_unit = st.selectbox("From Unit", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet"])
    to_unit = st.selectbox("To Unit", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet"])
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
    
elif conversion_type == "Weight":
    # Weight converter
    value = st.number_input("Enter value", value=1.0)
    from_unit = st.selectbox("From Unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    to_unit = st.selectbox("To Unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
    
elif conversion_type == "Temperature":
    # Temperature converter
    value = st.number_input("Enter value", value=0.0)
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")



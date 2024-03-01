import streamlit as st
import difflib

# Dictionary mapping aliases to full names
alias_mapping = {
    "america": "US",
    "usa": "US",
    "united states": "US",
    "uk": "United Kingdom",
    # Add more aliases as needed
}

# List of items
items = list(alias_mapping.values()) + ["Canada", "Australia", "Germany", "France", "Japan", "China", "India", "Brazil"]

# Function to find the closest match
def find_closest_match(user_input):
    lower_input = user_input.lower()
    if lower_input in alias_mapping:
        return alias_mapping[lower_input]
    else:
        matches = difflib.get_close_matches(lower_input, items, n=1, cutoff=0.6)
        if matches:
            return matches[0]
        else:
            return "No match found"

# Streamlit app
def main():
    st.title("Closest Match Finder Country")

    # User input
    user_input = st.text_input("Enter a country or alias:", "")

    # Find closest match
    closest_match = find_closest_match(user_input)

    # Display result
    st.text(f"Closest match: {closest_match}")

if __name__ == "__main__":
    main()









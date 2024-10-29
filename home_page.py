import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="The Gathering",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to improve spacing and styling
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        text-align: center;
        padding: 2rem 0;
        font-weight: bold;
    }
    .event-title {
        font-size: 2rem;
        padding: 1rem 0;
        font-weight: bold;
    }
    .event-details {
        font-size: 1.2rem;
        padding: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<p class="main-title">The Gathering</p>', unsafe_allow_html=True)

# Event section
st.markdown('<p class="event-title">Example Event</p>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    # Placeholder for event image
    st.image("https://via.placeholder.com/400x300", caption="Event Image")

with col2:
    # Event details
    st.markdown('<p class="event-details">Time: [Event Time]</p>', unsafe_allow_html=True)
    st.markdown('<p class="event-details">Place: [Event Location]</p>', unsafe_allow_html=True)
    st.markdown('<p class="event-details">Entry Fee: [Fee Amount]</p>', unsafe_allow_html=True)

# Additional details section
st.markdown("---")
st.markdown("### Event Description")
st.write("Add your event description here. This can include multiple paragraphs and details about the event.")

# Optional: Add a registration button
if st.button("Register for Event"):
    st.success("Registration button clicked! Add your registration logic here.")
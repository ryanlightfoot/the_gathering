import streamlit as st
from PIL import Image

# Set page config with wider layout
st.set_page_config(
    page_title="Events | The Gathering",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load external CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Navigation bar
st.markdown("""
    <div class="nav-container">
        <nav class="nav-bar">
            <div class="nav-logo">The Gathering</div>
            <div class="nav-links">
                <a href="/" class="nav-link active">Events</a>
                <a href="/gatherings" class="nav-link">Gatherings</a>
            </div>
        </nav>
    </div>
""", unsafe_allow_html=True)

# Wrap content in container
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# Main title
st.markdown('<div class="main-title">The Gathering</div>', unsafe_allow_html=True)

# Event title
st.markdown('<div class="event-title">Featured Event</div>', unsafe_allow_html=True)

# Event image
st.image("https://via.placeholder.com/800x400", caption="Event Preview", use_column_width=True)

# Description section
st.markdown("""
    <div class="section">
        <div class="event-title">Event Details</div>
        <p>Join us for an extraordinary gathering where creativity meets community. 
        This exclusive event brings together artists, thinkers, and innovators for 
        an unforgettable experience. Perfect for both newcomers and regular attendees.</p>
    </div>
""", unsafe_allow_html=True)

# Event details
st.markdown("""
    <div class="section">
        <div class="section-label">Event Information</div>
        <div class="event-details">Time: Saturday, 2 PM EST</div>
        <div class="event-details">Place: Main Hall</div>
        <div class="event-details">Entry Fee: $25</div>
    </div>
""", unsafe_allow_html=True)

# Close container
st.markdown('</div>', unsafe_allow_html=True)
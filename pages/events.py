import streamlit as st
from PIL import Image

def show_events_page():
    # Main title
    st.markdown('<div class="main-title">Events</div>', unsafe_allow_html=True)

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
            an unforgettable experience. Perfect for both travelers and members of the community!</p>
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
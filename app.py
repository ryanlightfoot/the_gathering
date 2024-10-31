# app.py
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

def show_gatherings_page():
    # Main title
    st.markdown('<div class="main-title">Gatherings</div>', unsafe_allow_html=True)

    # Content specific to Gatherings page
    st.markdown("""
        <div class="section">
            <div class="event-title">Past Gatherings</div>
            <p>Explore our community's past gatherings and the memories we've created together. 
            Each gathering is a unique blend of creativity, connection, and celebration.</p>
        </div>
    """, unsafe_allow_html=True)

    # Example gatherings grid
    st.markdown("""
        <div class="gatherings-grid">
            <div class="gathering-card">
                <h3>Summer Gathering 2023</h3>
                <p>A celebration of art and music under the stars</p>
            </div>
            <div class="gathering-card">
                <h3>Winter Workshop 2023</h3>
                <p>Creative workshops and collaborative projects</p>
            </div>
            <div class="gathering-card">
                <h3>Spring Festival 2023</h3>
                <p>Community showcase and cultural exchange</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Set page config with wider layout
st.set_page_config(
    page_title="The Gathering",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load external CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'events'

# Create a container for the navigation bar
nav_container = st.container()

with nav_container:
    # Use columns for logo and navigation buttons
    logo_col, spacer, nav_col = st.columns([2, 3, 2])
    
    with logo_col:
        st.markdown('<div class="nav-logo">The Gathering</div>', unsafe_allow_html=True)
    
    with nav_col:
        # Create a container for the buttons
        st.markdown('<div class="nav-links">', unsafe_allow_html=True)
        button_col1, button_col2 = st.columns((1, 1), gap="large")
        
        with button_col1:
            events_clicked = st.button("Events", key="nav_events", 
                                     help="View all events",
                                     use_container_width=True)
            if events_clicked:
                st.session_state.current_page = 'events'
                st.rerun()
        
        with button_col2:
            gatherings_clicked = st.button("Gatherings", key="nav_gatherings",
                                         help="View past gatherings",
                                         use_container_width=True)
            if gatherings_clicked:
                st.session_state.current_page = 'gatherings'
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# Wrap content in container
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# Show the appropriate page based on navigation state
if st.session_state.current_page == 'events':
    show_events_page()
else:
    show_gatherings_page()

# Close container
st.markdown('</div>', unsafe_allow_html=True)
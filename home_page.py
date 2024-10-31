# app.py
import streamlit as st
from PIL import Image
from pages.events import show_events_page
from pages.gatherings import show_gatherings_page

# Set page config with wider layout
st.set_page_config(
    page_title="The Gathering",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={} 
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
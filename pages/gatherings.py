import streamlit as st
from PIL import Image

# Set page config with wider layout
st.set_page_config(
    page_title="Gatherings | The Gathering",
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
                <a href="/" class="nav-link">Events</a>
                <a href="/gatherings" class="nav-link active">Gatherings</a>
            </div>
        </nav>
    </div>
""", unsafe_allow_html=True)

# Wrap content in container
st.markdown('<div class="content-container">', unsafe_allow_html=True)

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

# Close container
st.markdown('</div>', unsafe_allow_html=True)
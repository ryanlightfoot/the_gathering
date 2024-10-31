import streamlit as st
from PIL import Image

def show_gatherings_page():
    # Main title
    st.markdown('<div class="main-title">Gatherings</div>', unsafe_allow_html=True)

    # Content specific to Gatherings page
    st.markdown("""
        <div class="section">
            <div class="event-title">Past Gatherings</div>
            <p>Explore our community's gatherings and see what experiences we have on offer
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
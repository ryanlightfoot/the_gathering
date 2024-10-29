import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="The Gathering",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS with paper texture
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap');
    
    /* Animation for entire page */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    .stApp {
        background: 
            linear-gradient(rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.05)),
            repeating-linear-gradient(
                -45deg,
                rgba(255, 255, 255, 0.02) 0px,
                rgba(255, 255, 255, 0.02) 1px,
                transparent 1px,
                transparent 3px
            ),
            linear-gradient(135deg, rgba(15, 15, 15, 0.95), rgba(25, 25, 25, 0.95));
        background-attachment: fixed;
        animation: fadeIn 1.5s ease-in;
    }
    
    /* Main Title Styling */
    .main-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3.5rem;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        padding: 3.5rem 0;
        transform: skew(-5deg);
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Event Card Styling */
    .event-card {
        background: linear-gradient(145deg, 
            rgba(44, 44, 44, 0.9), 
            rgba(31, 31, 31, 0.9)
        );
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .event-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        color: #ffffff;
        margin-bottom: 1rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    .event-details {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.2rem;
        color: #e0e0e0;
        background: linear-gradient(145deg, 
            rgba(51, 51, 51, 0.8), 
            rgba(38, 38, 38, 0.8)
        );
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        padding: 0.8rem 1.2rem;
        border-radius: 8px;
        margin: 0.8rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease;
    }
    
    .event-details:hover {
        transform: translateX(5px);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(145deg, 
            rgba(51, 51, 51, 0.9), 
            rgba(38, 38, 38, 0.9)
        ) !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 0.8rem 2rem !important;
        font-family: 'Space Grotesk', sans-serif !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transform: skew(-5deg);
        width: 100%;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
    }
    
    .stButton > button:hover {
        background: linear-gradient(145deg, 
            rgba(64, 64, 64, 0.9), 
            rgba(51, 51, 51, 0.9)
        ) !important;
        transform: skew(-5deg) scale(1.02);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }
    
    /* Custom text colors */
    p {
        color: rgba(204, 204, 204, 0.9);
        line-height: 1.6;
    }

    /* Image caption styling */
    .caption {
        color: rgba(153, 153, 153, 0.9);
        font-size: 0.9rem;
        text-align: center;
        margin-top: 0.5rem;
    }

    /* Success message styling */
    .stSuccess {
        background: linear-gradient(145deg, 
            rgba(51, 51, 51, 0.9), 
            rgba(38, 38, 38, 0.9)
        ) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
    }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<div class="main-title">The Gathering</div>', unsafe_allow_html=True)

# Event card with title
st.markdown("""
    <div class="event-card">
        <div class="event-title">Featured Event</div>
    </div>
""", unsafe_allow_html=True)

# Event image
st.image("https://via.placeholder.com/800x400", caption="Event Preview", use_column_width=True)

# Event details card
st.markdown("""
    <div class="event-card">
        <div class="event-details">Time: Saturday, 2 PM EST</div>
        <div class="event-details">Place: Main Hall</div>
        <div class="event-details">Entry Fee: $25</div>
    </div>
""", unsafe_allow_html=True)

# Description section
st.markdown("""
    <div class="event-card">
        <div class="event-title">Event Details</div>
        <p>Join us for an extraordinary gathering where creativity meets community. 
        This exclusive event brings together artists, thinkers, and innovators for 
        an unforgettable experience. Perfect for both newcomers and regular attendees.</p>
    </div>
""", unsafe_allow_html=True)

# Styled registration button
if st.button("Register Now"):
    st.success("Thank you for your interest! Registration details will be sent to your email.")
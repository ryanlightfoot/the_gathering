import streamlit as st
from PIL import Image

# Set page config with wider layout
st.set_page_config(
    page_title="The Gathering",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with responsive design
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@300;400;500;600;700&display=swap');
    
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
        background: #FDF3E5;
        animation: fadeIn 1.5s ease-in;
        min-height: 100vh;
    }

    /* Container for content centering */
    .content-container {
        max-width: min(90vw, 1200px);
        margin: 0 auto;
        padding: 0 clamp(1rem, 5vw, 2rem);
    }
    
    /* Main Title Styling */
    .main-title {
        font-family: 'Fredoka One', cursive;
        font-size: clamp(2.5rem, 8vw, 4.5rem);
        color: #FF6B1A;
        text-align: center;
        padding: clamp(2rem, 5vh, 3.5rem) 0;
        letter-spacing: 0.02em;
        text-shadow: 2px 2px 0px rgba(0,0,0,0.1);
        animation: float 6s ease-in-out infinite;
        line-height: 1.2;
    }

    @keyframes float {
        0% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
        100% {
            transform: translateY(0px);
        }
    }
    
    /* Event Title Styling */
    .event-title {
        font-family: 'Quicksand', sans-serif;
        font-size: clamp(1.5rem, 4vw, 2rem);
        color: #FF6B1A;
        margin: clamp(1rem, 3vh, 2rem) 0 clamp(0.5rem, 2vh, 1rem) 0;
        text-align: center;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    
    /* Event Details Styling */
    .event-details {
        font-family: 'Quicksand', sans-serif;
        font-weight: 600;
        font-size: clamp(1rem, 3vw, 1.3rem);
        color: #333333;
        padding: clamp(0.4rem, 2vh, 0.8rem) 0;
        margin: clamp(0.2rem, 1vh, 0.4rem) 0;
        transition: transform 0.3s ease;
    }
    
    @media (hover: hover) {
        .event-details:hover {
            transform: translateX(5px);
        }
    }
    
    /* Section Spacing */
    .section {
        margin: clamp(1.5rem, 4vh, 3rem) 0;
        text-align: center;
        width: 100%;
    }
    
    /* Button Styling */
    .stButton > button {
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 600 !important;
        background: #FF6B1A !important;
        color: #FFFFFF !important;
        border-radius: 25px !important;
        padding: clamp(0.6rem, 2vh, 0.8rem) clamp(1.5rem, 4vw, 3rem) !important;
        border: none !important;
        transform: skew(-5deg);
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 107, 26, 0.2);
        margin: clamp(1rem, 3vh, 2rem) 0;
        font-size: clamp(1rem, 2.5vw, 1.2rem) !important;
        letter-spacing: 0.5px;
        width: min(100%, 300px);
    }
    
    @media (hover: hover) {
        .stButton > button:hover {
            background: #FF8142 !important;
            transform: skew(-5deg) scale(1.02);
            box-shadow: 0 6px 20px rgba(255, 107, 26, 0.3);
        }
    }
    
    /* Custom text colors */
    p {
        font-family: 'Quicksand', sans-serif;
        color: #333333;
        line-height: 1.6;
        font-size: clamp(1rem, 2.5vw, 1.2rem);
        max-width: min(90vw, 600px);
        margin: clamp(0.5rem, 2vh, 1rem) auto;
        font-weight: 400;
        padding: 0 clamp(1rem, 3vw, 2rem);
    }

    /* Section Headings */
    .section-label {
        font-family: 'Quicksand', sans-serif;
        font-weight: 700;
        color: #FF6B1A;
        font-size: clamp(1.2rem, 3vw, 1.4rem);
        margin-bottom: clamp(0.5rem, 2vh, 1rem);
    }

    /* Success message styling */
    .stSuccess {
        font-family: 'Quicksand', sans-serif !important;
        background: none !important;
        color: #FF6B1A !important;
        border: none !important;
        text-align: center;
        font-weight: 600;
        font-size: clamp(0.9rem, 2.5vw, 1.1rem) !important;
        padding: clamp(0.5rem, 2vh, 1rem) !important;
    }

    /* Image caption styling */
    img + div.css-1offfwp {
        font-family: 'Quicksand', sans-serif !important;
        color: #333333 !important;
        text-align: center;
        font-weight: 500;
        font-size: clamp(0.8rem, 2vw, 1rem);
    }

    /* Image container */
    .stImage {
        margin: 0 auto;
        max-width: min(90vw, 800px);
    }

    /* Streamlit container overrides for mobile */
    .css-1d391kg {
        padding: 1rem 1rem;
    }

    @media screen and (max-width: 768px) {
        .css-1d391kg {
            padding: 0.5rem;
        }
    }
    </style>
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
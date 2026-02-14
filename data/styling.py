import base64
import os
import streamlit as st


def get_base64_image(image_path):
    """Convert image to base64 for CSS embedding"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def get_standard_css(bg_image_base64):
    """Return standardized CSS for all pages"""
    return f"""
<style>
/* Make Streamlit toolbar transparent */
[data-testid="stToolbar"] {{
    background-color: transparent !important;
}}

.stAppToolbar {{
    background-color: transparent !important;
    backdrop-filter: blur(10px);
}}

header {{
    background-color: transparent !important;
}}

/* Make toolbar buttons visible with white color */
[data-testid="stToolbar"] button {{
    color: white !important;
}}

[data-testid="stToolbar"] svg {{
    fill: white !important;
}}

/* Make sidebar transparent with glassmorphism */
[data-testid="stSidebar"] {{
    background-color: rgba(0, 0, 0, 0.3) !important;
    backdrop-filter: blur(10px);
}}

[data-testid="stSidebarContent"] {{
    background-color: transparent !important;
}}

/* Sidebar navigation styling */
[data-testid="stSidebarNav"] {{
    background-color: transparent !important;
}}

[data-testid="stSidebarNav"] a {{
    color: white !important;
}}

[data-testid="stSidebarNav"] span {{
    color: white !important;
}}

/* Sidebar buttons */
[data-testid="stSidebar"] button {{
    color: white !important;
}}

[data-testid="stSidebar"] svg {{
    fill: white !important;
}}

.stApp {{
    background-image: url("data:image/jpeg;base64,{bg_image_base64}");
    background-size: cover;
    background-position: center;
}}

/* Text contrast improvements */
.stApp {{
    color: white !important;
}}

h1, h2, h3, h4, h5, h6 {{
    color: white !important;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
}}

p, span, div {{
    color: white !important;
}}

/* Add semi-transparent background to main content for better readability */
.main .block-container {{
    background-color: rgba(0, 0, 0, 0.5);
    padding: 2rem;
    border-radius: 15px;
}}

/* Divider styling */
hr {{
    border-color: rgba(255, 255, 255, 0.3) !important;
}}

/* Card styling for better contrast */
.stMarkdown {{
    color: white !important;
}}

div.stButton > button {{
    background: linear-gradient(45deg, #FF4B2B, #FF416C);
    color: white;
    border: none;
    border-radius: 25px;
    padding: 0.5rem 1rem;
    font-weight: bold;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}}

div.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 8px rgba(0,0,0,0.2);
    background: linear-gradient(45deg, #FF416C, #FF4B2B);
    color: white;
}}

div.stButton > button:active {{
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}}

div.stButton > button[kind="primary"] {{
    background: linear-gradient(45deg, #FFD700, #FFA500);
    color: black;
    border: none;
}}

div.stButton > button[kind="primary"]:hover {{
    background: linear-gradient(45deg, #FFA500, #FFD700);
    color: black;
    box-shadow: 0 6px 12px rgba(0,0,0,0.3);
}}

[data-testid="stImage"] img {{
    height: 300px;
    object-fit: cover;
    width: 100%;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}}
</style>
"""


def apply_standard_styling():
    """
    Convenience function to apply standard styling to any page.
    Call this function at the beginning of your page after st.set_page_config().

    Example usage:
        from data.styling import apply_standard_styling

        st.set_page_config(page_title="My Page", layout="wide")
        apply_standard_styling()
    """
    # Get the current file's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Check if we're in the pages directory or root
    if os.path.basename(current_dir) == "data":
        # We're in data folder, go up one level to root
        parent_dir = os.path.dirname(current_dir)
    else:
        # We're in root, use current dir
        parent_dir = current_dir

    # Build path to background image
    bg_image_path = os.path.join(parent_dir, "images", "background.jpeg")

    # Get base64 encoded image
    bg_image = get_base64_image(bg_image_path)

    # Apply the CSS
    st.markdown(get_standard_css(bg_image), unsafe_allow_html=True)

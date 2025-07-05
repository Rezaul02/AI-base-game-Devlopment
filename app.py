import streamlit as st
from streamlit_extras.card import card
import time
from streamlit_js_eval import streamlit_js_eval

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS
st.markdown("""
<style>
    .header{
        font-size: 2.5rem;
        font-weight: 800;
        color: #FF4B4B;
        margin-bottom: 0.5rem;       
            
    }
    .subheader {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }        
    .chat-box {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 10px;
        max-height: 400px;
        overflow-y: auto;
        margin-bottom: 1rem;
        border: 1px solid #e6e6e6;
    }
    .message {
        padding: 0.5rem;
        margin-bottom: 0.5rem;
        border-radius: 5px;
    }
    .user-message {
        background-color: #dff0d8;
        text-align: right;
    }
    .ai-message {
        background-color: #f0f0f0;
        text-align: left;
    }
    .prompt-input {
        width: 100%;
        padding: 0.75rem;
        border-radius: 5px;
        border: 1px solid #ccc;
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Tools Panel
with st.sidebar:
    st.markdown("## 🛠️ Tools")
    st.selectbox("🧠 Model", ["GPT-4", "GPT-3.5", "Custom GameGen AI"])
    st.checkbox("Enable Creativity Boost", value=True)
    st.slider("Creativity Level", 0.0, 1.0, 0.7)
    st.selectbox("Game Type", ["2D", "3D", "Text-based", "VR"])
    st.selectbox("Interface Language", ["English", "Spanish", "Arabic", "Bengali"])
    st.button("Reset Chat", on_click=lambda: st.session_state.messages.clear())

# Header
#st.markdown('<div class="header">Not YouTube, it\'s YouWare.</div>', unsafe_allow_html=True)
#st.markdown('<div class="subheader">AI-Powered Game Development Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="header">AI Base Game Generate </div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">AI-Powered Game Development Platform</div>', unsafe_allow_html=True)

# Show message history
st.markdown('<div class="chat-box">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    role_class = "user-message" if msg["role"] == "user" else "ai-message"
    st.markdown(f'<div class="message {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input prompt box (like ChatGPT)
prompt = st.text_area("💬 Type your game idea", placeholder="Type your game concept here...", label_visibility="collapsed")
#Edition part 

#prompt = st.text_area("💬 Type your game idea", 
                     # value=voice_text if voice_text else "", 
                     # placeholder="Type your game concept here...", 
                     # label_visibility="collapsed", 
                     # key="game_prompt")

# Show mic icon as button
st.markdown("""
    <button class="voice-btn" onclick="window.location.reload()">
    voice
    </button>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 6])
with col1:
    send = st.button("➕ Add")
with col2:
    generate = st.button("✨ Generate Game")

# When "Add" is clicked
if send and prompt.strip():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.experimental_rerun()

# When "Generate Game" is clicked
if generate:
    with st.spinner("🧠 AI is generating your game..."):
        time.sleep(2)
        response = "Here’s a draft of your game logic, design, and flow! Check below for assets and code."
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "ai", "content": response})
        st.success("Game generated successfully!")
        st.balloons()
       # st.experimental_rerun()
        st.rerun()

st.markdown("## 🎮 Trending Game Projects")

# Category Tabs
st.markdown('<div class="category-tabs">', unsafe_allow_html=True)
categories = ["All", "Action", "Adventure", "Puzzle", "RPG", "Arcade", "Educational"]
selected_category = st.radio(
    "Filter by category:",
    categories,
    horizontal=True,
    key="category_tabs"
)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown(f"### {selected_category} Games")
cols = st.columns(3)
# This shown me this Inhance project 
projects = [
    {"title": "Zombie Survival", "category": "Action", "description": "2D platformer with zombie enemies", "likes": 245, "complexity": "Intermediate"},
    {"title": "Galaxy Explorer", "category": "Adventure", "description": "3D space exploration game", "likes": 189, "complexity": "Advanced"},
    {"title": "Math Quest", "category": "Educational", "description": "Learn math while fighting monsters", "likes": 132, "complexity": "Beginner"},
    {"title": "Puzzle Dimensions", "category": "Puzzle", "description": "Mind-bending spatial puzzles", "likes": 98, "complexity": "Intermediate"},
    {"title": "Dragon's Legacy", "category": "RPG", "description": "Epic fantasy role-playing game", "likes": 312, "complexity": "Advanced"},
    {"title": "Neon Racer", "category": "Arcade", "description": "Futuristic racing game", "likes": 176, "complexity": "Beginner"},
]

# Filter projects by selected category
filtered_projects = [p for p in projects if selected_category == "All" or p["category"] == selected_category]

# Display projects in a responsive grid
for i, project in enumerate(filtered_projects):
    with cols[i % 3]:
        with st.container():
            st.markdown(f"""
            <div class="project-card">
                <h3>{project['title']}</h3>
                <p><small>🏷️ {project['category']} | 🧩 {project['complexity']}</small></p>
                <p>{project['description']}</p>
                <p>❤️ {project['likes']} likes</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Use Template", key=f"try_{i}"):
                st.session_state['selected_template'] = project['title']
                st.rerun()

# AI Game Generator Section
if 'selected_template' in st.session_state or prompt:
    st.markdown("---")
    st.markdown("## 🧠 AI Game Generator")
    
    with st.expander("⚙️ Game Configuration", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            game_name = st.text_input("Game Name", "My Awesome Game")
            genre = st.selectbox("Genre", ["Platformer", "RPG", "Puzzle", "Adventure", "Shooter", "Simulation"])
            difficulty = st.slider("Difficulty Level", 1, 5, 3)
            
        with col2:
            art_style = st.selectbox("Art Style", ["Pixel Art", "Cartoon", "Realistic", "Minimalist", "Low Poly"])
            platform = st.multiselect("Target Platforms", ["Web", "Mobile", "Desktop", "Console"])
        
        # Advanced AI settings
        with st.expander("Advanced AI Settings"):
            creativity = st.slider("Creativity Level", 0.0, 1.0, 0.7, help="Higher values produce more original but potentially less predictable results")
            detail_level = st.select_slider("Detail Level", ["Basic", "Standard", "Detailed", "Very Detailed"])
            code_language = st.selectbox("Preferred Language", ["Python", "JavaScript", "C#", "C++"])
    
    if st.button("✨ Generate Game", type="primary"):
        with st.spinner("🧠 AI is generating your game... This may take a minute"):
            # Simulate AI processing time
            time.sleep(3)
            
            # Display results
            st.success("🎉 Game generated successfully!")
            st.balloons()
            
            st.markdown("### Generated Assets")
            tab1, tab2, tab3 = st.tabs(["📜 Code", "🖼️ Assets", "🎥 Preview"])
            
            with tab1:
                st.code("""
# Sample generated game code
import pygame

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        
    def update(self):
        # Movement logic here
        pass
        
    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 50, 50))
                """, language="python")
                st.download_button("Download Full Code", data="placeholder.py", file_name="game_code.py")
            
            with tab2:
                col1, col2 = st.columns(2)
                with col1:
                    st.image("https://via.placeholder.com/300x150?text=Character+Sprites", caption="Character Sprites")
                with col2:
                    st.image("https://via.placeholder.com/300x150?text=Environment+Tiles", caption="Environment Tiles")
                st.download_button("Download Assets Pack", data="placeholder.zip", file_name="game_assets.zip")
            
            with tab3:
                st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")
                st.caption("AI-generated gameplay preview")
            
            st.markdown("---")
            st.markdown("### Next Steps")
            st.write("1. Download the project files above")
            st.write("2. Customize the game to your liking")
            st.write("3. Share your creation with the community!")
            
            if st.button("🔄 Generate Another Game"):
                del st.session_state['selected_template']
                st.rerun()

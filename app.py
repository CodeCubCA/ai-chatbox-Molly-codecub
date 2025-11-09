import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Gemini client with API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Page configuration with gaming theme
st.set_page_config(
    page_title="Gaming Assistant",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS for gaming theme
st.markdown("""
    <style>
    .main {
        background-color: #0a0e27;
    }
    .stTextInput > div > div > input {
        background-color: #1a1f3a;
        color: #00ff88;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and description
st.title("🎮 Gaming Assistant")
st.markdown("""
### 👋 Welcome, Gamer!
I'm your personal gaming AI assistant, here to help you level up your gaming experience! Whether you need:
- 🎯 Game strategies and pro tips
- 🕹️ Game recommendations tailored to your taste
- 🏆 Help with difficult boss fights or puzzles
- 📰 Latest gaming news and trends
- 💬 Just a friendly chat about your favorite games

Let's get gaming! 🚀
""")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "personality" not in st.session_state:
    st.session_state.personality = "Friendly"

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about gaming..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Create messages for API call including system prompt with personality
        personality_prompts = {
            "Friendly": "You are a chill and friendly gaming buddy. Chat like you're talking to a friend - casual, supportive, and enthusiastic about games. Use a relaxed tone and share your excitement about gaming. Keep it conversational and fun!",
            "Professional": "You are a professional gaming consultant. Provide rigorous, accurate, and well-researched advice. Be precise with your recommendations, cite game mechanics accurately, and give detailed strategic analysis. Maintain a formal and expert tone.",
            "Humorous": "You are a humorous gaming companion with a great sense of humor. Keep things light, fun, and entertaining with witty remarks and gaming jokes. Make the conversation enjoyable while still being helpful. Don't be afraid to use gaming memes and references!"
        }

        system_prompt = f"{personality_prompts[st.session_state.personality]} You provide tips, strategies, game recommendations, and answer questions about video games."

        # Build conversation history for Gemini including system prompt
        conversation_history = []

        # Add system prompt as first user message if history is empty
        if len(st.session_state.messages) == 1:  # Only current message
            conversation_history.append({"role": "user", "parts": [system_prompt]})
            conversation_history.append({"role": "model", "parts": ["Understood! I'm ready to be your gaming assistant with that personality. What would you like to know about gaming?"]})

        for msg in st.session_state.messages[:-1]:  # Exclude the current user message
            if msg["role"] == "user":
                conversation_history.append({"role": "user", "parts": [msg["content"]]})
            else:
                conversation_history.append({"role": "model", "parts": [msg["content"]]})

        # Stream response from Gemini API
        try:
            # Initialize the model
            model = genai.GenerativeModel("gemini-2.0-flash")

            # Start chat with history
            chat = model.start_chat(history=conversation_history)

            # Send message and stream response
            response = chat.send_message(prompt, stream=True)

            # Display streaming response
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")

            # Display final response
            message_placeholder.markdown(full_response)

        except Exception as e:
            full_response = f"❌ Error: {str(e)}\n\nPlease check your GEMINI_API_KEY in the .env file."
            message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with personality selection and info
with st.sidebar:
    st.header("🎭 AI Personality")

    personality_options = {
        "😊 Friendly": "Friendly",
        "💼 Professional": "Professional",
        "😄 Humorous": "Humorous"
    }

    selected = st.radio(
        "Choose your AI's personality:",
        options=list(personality_options.keys()),
        index=list(personality_options.values()).index(st.session_state.personality),
        help="Select how you want the AI to interact with you"
    )

    # Update personality in session state
    st.session_state.personality = personality_options[selected]

    # Display personality description
    personality_descriptions = {
        "Friendly": "🤝 Chill and friendly - Chat like friends!",
        "Professional": "🎯 Rigorous and professional - Accurate advice!",
        "Humorous": "🎪 Relaxed and humorous - Interesting chat!"
    }
    st.info(personality_descriptions[st.session_state.personality])

    st.divider()

    st.header("ℹ️ About")
    st.markdown("""
    This is a gaming AI assistant powered by:
    - **Google Gemini API** (gemini-2.0-flash)
    - **Streamlit** for the interface

    Ask me about:
    - 🎯 Game strategies and tips
    - 🎮 Game recommendations
    - 📰 Gaming news and trends
    - 🕹️ Anything gaming-related!
    """)

    st.divider()

    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

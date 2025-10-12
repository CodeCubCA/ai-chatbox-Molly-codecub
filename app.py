import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page configuration with gaming theme
st.set_page_config(
    page_title="My gaming AI assistant",
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
st.title("🎮 My gaming AI assistant")
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

        api_messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        # Add chat history to API messages
        for msg in st.session_state.messages:
            api_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        # Stream response from Groq API
        try:
            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=api_messages,
                temperature=0.7,
                max_tokens=1024,
                stream=True
            )

            # Display streaming response
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            # Display final response
            message_placeholder.markdown(full_response)

        except Exception as e:
            full_response = f"❌ Error: {str(e)}\n\nPlease check your GROQ_API_KEY in the .env file."
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
    - **Groq API** (llama-3.3-70b-versatile)
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

# 🎮 Gaming Assistant - AI Chat Assistant

Your personal AI-powered gaming buddy for tips, strategies, and game recommendations!

---

## 📖 About

The **Gaming Assistant** is an intelligent AI chatbot designed specifically for gamers. Powered by Groq's advanced LLaMA 3.3 70B model, it provides personalized gaming advice, strategy tips, and game recommendations in real-time. Whether you need help with a difficult boss fight, want game suggestions, or just need a friendly gaming companion, this AI assistant has you covered with three distinct personality modes to match your vibe!

L'**Assistant Gaming** est un chatbot IA intelligent conçu spécialement pour les joueurs. Propulsé par le modèle avancé LLaMA 3.3 70B de Groq, il fournit des conseils de jeu personnalisés, des astuces stratégiques et des recommandations de jeux en temps réel.

**游戏助手**是一个专为玩家设计的智能 AI 聊天机器人。采用 Groq 先进的 LLaMA 3.3 70B 模型，实时提供个性化游戏建议、策略技巧和游戏推荐。

---

## ✨ Features

- 🤖 **AI-Powered Conversations** - Leverages Groq's LLaMA 3.3 70B model for intelligent, context-aware gaming discussions
- 🎭 **Multiple Personalities** - Choose from three AI personalities:
  - 😊 **Friendly** - Chill and casual gaming buddy
  - 💼 **Professional** - Expert gaming consultant with detailed analysis
  - 😄 **Humorous** - Fun and entertaining companion with gaming jokes
- ⚡ **Real-Time Streaming** - Watch responses appear in real-time with streaming API integration
- 🎯 **Gaming Expertise** - Specialized in:
  - Game strategies and pro tips
  - Personalized game recommendations
  - Boss fight help and puzzle solutions
  - Latest gaming news and trends
- 💬 **Chat History** - Maintains conversation context throughout your session
- 🎨 **Gaming Theme UI** - Dark mode interface with gaming-inspired design
- 🔄 **Easy Reset** - Clear chat history anytime to start fresh

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-00D4AA?style=for-the-badge&logo=ai&logoColor=white)

- **Python 3.9+** - Programming language
- **Streamlit** - Web application framework for rapid UI development
- **Groq API** - Ultra-fast AI inference platform
- **LLaMA 3.3 70B** - Advanced large language model by Meta
- **python-dotenv** - Environment variable management

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9 or higher
- Groq API key (free tier available)
- Git installed on your computer

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/CodeCubCA/ai-chatbox-Molly-codecub.git
   cd ai-chatbox-Molly-codecub
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:
   ```bash
   touch .env
   ```

   Add your Groq API key to the `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in your terminal

---

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy the app**
   - Click "New app"
   - Select your repository: `ai-chatbox-Molly-codecub`
   - Main file path: `app.py`
   - Click "Deploy"

4. **Add secrets**
   - In the Streamlit Cloud dashboard, go to app settings
   - Add your secrets:
     ```toml
     GROQ_API_KEY = "your_groq_api_key_here"
     ```

5. **Your app is live!** 🎉

---

## 🌟 Live Demo

**Try it now:** [https://ai-chatbox-molly-codecub.streamlit.app/](https://ai-chatbox-molly-codecub.streamlit.app/)

Experience the Gaming Assistant with all three personality modes and get instant gaming advice!

---

## 📸 Screenshots

> **Note:** Add screenshots to showcase the chatbot interface and features.

*Suggested screenshots:*
- 🎮 Main chat interface
- 🎭 Personality selection sidebar
- 💬 Sample conversation showing streaming responses
- 🎨 Dark mode gaming theme

---

## 🔑 API Key Setup

### How to Get Your Groq API Key

1. **Visit Groq Console**
   - Go to [console.groq.com](https://console.groq.com)

2. **Create an account**
   - Sign up with your email or GitHub account

3. **Generate API Key**
   - Navigate to "API Keys" section
   - Click "Create API Key"
   - Copy your key (save it securely!)

4. **Add to your project**
   - Paste the key in your `.env` file
   - Or add it to Streamlit Cloud secrets

**Note:** Keep your API key secret! Never commit it to GitHub.

---

## 🚧 Future Improvements

- [ ] 🎨 Add custom themes (light/dark mode toggle)
- [ ] 📊 Gaming statistics and recommendations based on chat history
- [ ] 🎯 Game-specific modes (FPS, RPG, Strategy, etc.)
- [ ] 🔊 Voice input/output for hands-free gaming assistance
- [ ] 🌍 Multi-language support for international gamers
- [ ] 📱 Mobile app version
- [ ] 💾 Save and export chat history
- [ ] 🏆 Integration with gaming platforms (Steam, Xbox, PlayStation)
- [ ] 📈 Track gaming goals and progress

---

## 👩‍💻 Author

**Molly**

Student & Chill Developer passionate about AI, gaming, and creating interactive applications.

- 🎮 **Gaming Enthusiast** - Loves creating AI-powered gaming tools
- 🤖 **AI Explorer** - Experimenting with LLMs and creative AI applications
- 💡 **Tech Stack:** Python, Streamlit, AI/ML, Web Development
- 🌟 **GitHub:** [CodeCubCA](https://github.com/CodeCubCA)

### Connect with me:
- 💼 Portfolio: [molly.codecub.org](https://molly.codecub.org)
- 🐙 GitHub: [@CodeCubCA](https://github.com/CodeCubCA)
- 🎮 Try my projects: [Gaming Assistant](https://ai-chatbox-molly-codecub.streamlit.app/)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- **Groq** - For providing ultra-fast AI inference
- **Meta** - For the powerful LLaMA 3.3 70B model
- **Streamlit** - For the amazing web framework
- **Gaming Community** - For inspiration and feedback

---

## 💡 Tips for Best Experience

1. **Choose your vibe** - Select the personality that matches your gaming style
2. **Be specific** - The more details you provide, the better the recommendations
3. **Explore features** - Try asking about different games, genres, and strategies
4. **Clear chat** - Use the "Clear Chat History" button to start fresh conversations

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with 💙 and 🎮 by Molly

*Level up your gaming with AI!*

</div>

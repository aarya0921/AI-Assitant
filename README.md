
# GroqTalk:AI Powered Assistant


GroqTalk is a single-query AI assistant that provides instant, intelligent responses using LLaMA 3 on Groq's lightning-fast infrastructure. 

Live demo:-https://acvwpvnfueux9kcdsnu6nw.streamlit.app/




## Features

-  Natural Language Chat: Human-like conversation powered by LLaMA 3
- LLaMA 3-8B model for intelligent, contextual answers
- Secure API Key Handling: Uses Streamlit's secrets system
- Streamlit UI: Easy-to-use chat interface


## Requirements
Before running the application, ensure you have the following dependencies installed:

-streamlit

-groq
## Installation
#### 1. Clone the repository:
 ```bash
 git clone https://github.com/aarya0921/AI-Assitant.git
 cd AI-Assitant
 ```

#### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
#### 3. Install the dependencies
```bash
pip install -r requirements.txt
```
#### 4. Add your Groq API key
Create a file .streamlit/secrets.toml and paste:
```bash
GROQ_API_KEY = "your_groq_api_key_here"
```

#### 5. Running the App Locally
```bash
streamlit run app.py
```


## Project Structure
```
├── app.py                  # Main Streamlit app
├── requirements.txt        # Required dependencies
├── .streamlit/
│   └── secrets.toml        # Groq API Key (not to be committed)
└── README.md               # This file
```

## Future Enhancements
-Add regional language routing (Hindi, Marathi, etc.)

-Integrate PDF reading and RAG-style question answering

-Session history or chat logs

 -Advanced Streamlit UI (avatars, themes)
## Acknowledgements

 - [Groq API](https://console.groq.com/home)
 - [ Streamlit](https://streamlit.io/)
 - [ Meta LLaMA 3](https://www.llama.com/)


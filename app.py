from groq import Groq
import streamlit as st

st.set_page_config(page_title="LLaMA 3 on Groq", page_icon=":robot_face:")  
st.title("AI Powered Assistant!! ")
# Load your API key securely
api_key = st.secrets["GROQ_API_KEY"]

# Initialize Groq client
client = Groq(api_key=api_key)

# Define your prompt
user_input = st.text_input("Ask Me:")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Use "llama3-70b-8192" for more powerful model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success("Response:")
        st.write(response.choices[0].message.content)


import streamlit as st
from download_video import download
from utils import base64_converter, prompting
from chat_retreival import retrieverSetup, chat
import os

OPENAI_KEY =os.environ["OPENAI_API_KEY"]

@st.cache_data
def video_data_retreival(url):
    #download video
    video_path = download(url)
    #convert video frames into base64
    base64Frames = base64_converter(video_path)
    #using GPT4 vision for description generation
    prompt_output = prompting(base64Frames, OPENAI_KEY)
    return retrieverSetup(prompt_output, OPENAI_KEY)


st.header('Talk with Youtube Videos', divider='rainbow')

if url := st.text_input('Youtube Link'):
    st.video(url)
    qa = video_data_retreival(url)


if prompt := st.chat_input("Talk with Video"):
    st.write(f"{prompt}")
    #chat using retreiver
    answer = chat(qa, prompt)
    st.write(f"{answer}")
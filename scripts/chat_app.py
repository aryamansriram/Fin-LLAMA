import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
from hugchat.login import Login
import random

if 'user_responses' not in st.session_state:
    st.session_state['user_responses'] = []

if 'bot_responses' not in st.session_state:
    st.session_state['bot_responses'] = [
        "Hello how's it going, I'm your neighborhood friendly assistant."
    ]


if 'cur_user' not in st.session_state:
    st.session_state['cur_user'] = ''

if 'cur_bot' not in st.session_state:
    st.session_state['cur_bot'] = ''

def u_callback():
    if st.session_state.user_input:
       st.session_state['user_responses'].append(
           st.session_state.user_input
       )

def b_callback():
    if st.session_state.user_input:
       st.session_state['bot_responses'].append(
           st.session_state.bot_input
       )

if __name__=="__main__":
    st.title('Example Chat')
    response = st.text_input('Enter your response',on_change=u_callback,key='user_input')
    bot_response = st.text_input("Enter bot's response",on_change=b_callback,key='bot_input')
    
    
    print("U: ",st.session_state['user_responses'])
    print("B: ",st.session_state["bot_responses"])
    if st.session_state['user_responses'] or st.session_state['bot_responses']:
        k=0
        for i,(u,b) in enumerate(zip(st.session_state['user_responses'],
                        st.session_state['bot_responses'])):
            if b:
                st.chat_message("ASSISTANT").write(b)
            if u:
                st.chat_message("USER").write(u)
            
            k+=1

        if k<len(st.session_state['user_responses']):
            st.chat_message("USER").write(st.session_state['user_responses'][k])
        
        if k<len(st.session_state['bot_responses']):
            st.chat_message("ASSISTANT").write(st.session_state['bot_responses'][k])
    # print("U: ",st.session_state['user_responses'])
    # print("B: ",st.session_state['bot_responses'])
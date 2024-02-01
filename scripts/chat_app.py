import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from llama_cpp import Llama
from langchain_community.llms import LlamaCpp


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

llm = LlamaCpp(
    model_path='models/fin_llama_q8.gguf',
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    )


if __name__=="__main__":
    st.title('Llama-Chat')
    response = st.chat_input('Enter your response',key='user_input')
    if response:
       
        u_callback()
    if len(st.session_state['bot_responses'])==1 and len(st.session_state['user_responses'])==0:
        st.chat_message("ASSISTANT").write(st.session_state['bot_responses'][0])
    
    if st.session_state['user_responses'] or st.session_state['bot_responses']:
        k=0
        for i,(u,b) in enumerate(zip(st.session_state['user_responses'],
                        st.session_state['bot_responses'])):
            
            st.chat_message("ASSISTANT").write(b)
            st.chat_message("USER").write(u)
          

    if response:
        
        bot_response = llm.stream(
            '<s>[INST] '+response+' [/INST]'
        )

        bot_res = ''
        with st.chat_message("ASSISTANT"):
            placeholder = st.empty()
            for chunk in bot_response:
                bot_res = bot_res+chunk
                placeholder.markdown(bot_res)

        st.session_state["bot_responses"].append(bot_res)



        
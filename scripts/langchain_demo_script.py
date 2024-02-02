from langchain_community.llms import LlamaCpp
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory,ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    
)

if __name__=="__main__":
    llm = LlamaCpp(
    model_path='models/fin_llama_q8.gguf',
    temperature=0.75,
    max_tokens=2000,
    max_length=100,
    top_p=1,
    )

    prompt = ChatPromptTemplate.from_messages(
    messages=[
        
        
        MessagesPlaceholder(variable_name="chat_history"),
        ("human",'<s>[INST] {input} [/INST]')
    ]
    )

    
    conversation = ConversationChain(
        llm = llm,
        prompt=prompt,
        verbose=False,
        memory=ConversationBufferMemory(memory_key='chat_history',return_messages=True)  
    )

    conversation.memory.save_context(
        {'input':'Hi'},{'output':'Hello'}
    )
    conversation.memory.save_context(
        {'input':'How are you'},{'output':'good'}
    )

    print(conversation.memory.load_memory_variables({}))

    
    # print('Start chatting')
    # while True:
    #     inp = input()
    #     if inp == 'close':
    #         break
    #     # response = llm.invoke(inp)
    #     response = conversation({"input":inp})['response']
    #     #response = conversation.predict(input='<s>[INST] '+inp+' [/INST]')
    #     print("ASSISTANT: "+response)
    
    # print(conversation.memory.load_memory_variables({}))
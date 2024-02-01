from langchain_community.llms import LlamaCpp
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

if __name__=="__main__":
    llm = LlamaCpp(
    model_path='models/fin_llama_q8.gguf',
    temperature=0.75,
    max_tokens=2000,
    max_length=100,
    top_p=1,
    )

    conversation = ConversationChain(
        llm = llm,
        verbose=True,
        memory=ConversationBufferWindowMemory(k=2)  
    )

    print('Start chatting')
    while True:
        inp = input()
        if inp == 'close':
            break
        # response = llm.invoke(inp)
        response = conversation.predict(input='<s>[INST] '+inp+' [/INST]')
        print("ASSISTANT: "+response)

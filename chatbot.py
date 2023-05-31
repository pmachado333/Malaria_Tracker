import openai
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate


### App Key for openai ###
load_dotenv()
OPENAI_API_KEY = os.getenv('APP_KEY')
openai.api_key = OPENAI_API_KEY


### Header ###
col1, col2 = st.columns([11,7])
with col1:
    st.markdown("# Doctorbot")
with col2:
    st.image('doctor.jpg')


### Chatbot ###
st.session_state['init'] = False

#@st.cache(allow_output_mutation=True)
@st.cache_resource()
def init():

    st.session_state['init'] = True
    template = """You are a chatbot having a conversation with a human.

        {chat_history}
        Human: {human_input}
        Chatbot:"""

    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"],
        template=template
    )

    memory = ConversationBufferMemory(memory_key="chat_history")

    llm_chain = LLMChain(
        llm=OpenAI(model_name='gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY),
        prompt=prompt,
        verbose=True,
        memory=memory,
        )

    return llm_chain

def response(llm_chain, text):
   return llm_chain.predict(human_input=text)


if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input('You:', value='', key='input')
    return input_text



user_input = get_text()

if st.session_state['init'] == False:
    llm_chain = init()


if user_input:
    output = response(llm_chain, user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


### Chat UI ###

def chat_interface_v1():
    chat_columns[0].write(
        f'<span style="font-size: 18px"></i> {st.session_state["past"][i]}</span>',
        unsafe_allow_html=True,
    )
    chat_columns[1].write(
        f'<span style="color: blue; font-size: 18px;">{st.session_state["generated"][i]}</span>',
        unsafe_allow_html=True,
        key=str(i)
    )


def chat_interface_v2():
    message(st.session_state["past"][i], is_user=False,
            avatar_style="adventurer",
            #avatar_style="personas",
            )
    message(st.session_state["generated"][i], is_user=True,
            avatar_style="bottts",
            )


if st.session_state['generated']:
    num_messages = len(st.session_state['generated'])
    chat_columns = st.columns(2)

    for i in range(num_messages):

        #chat_interface_v1()
        chat_interface_v2()

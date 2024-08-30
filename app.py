import openai
import streamlit as st
from streamlit_chat import message
from generate_vdb import vdb
from workflow import create_workflow
import os
from streamlit_extras.stylable_container import stylable_container 

# Setting page title and header
st.set_page_config(page_title="LAW", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'> An Adaptive RAG system for lawyers</h1>", unsafe_allow_html=True)

# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []
if 'cost' not in st.session_state:
    st.session_state['cost'] = []
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = []
if 'total_cost' not in st.session_state:
    st.session_state['total_cost'] = 0.0


# Initialize VDB
retriever = vdb()
app = create_workflow(retriever)

# generate a response
def generate_response(prompt):
    print(prompt)
    st.session_state['messages'].append({"role": "user", "content": prompt})

    inputs = {"question": prompt}
    for output in app.stream(inputs):
        for key, value in output.items():
            # Node
            print(f"Node '{key}':")
            # Optional: print full state at each node
            # print.print(value["keys"], indent=2, width=80, depth=None)
        print("\n---\n")

    response = value['generation']
    st.session_state['messages'].append({"role": "assistant", "content": response})
    print(response)
    return response#, total_tokens, prompt_tokens, completion_tokens

Pagex = st.container(border=True)
Pagex = stylable_container(key="Pagex", css_styles=[""" {box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 25px;
  height:60px;z-index: 1000;}"""])

c = Pagex.columns([1])
# container for chat history
response_container = Pagex.container()
# container for text box
container = Pagex.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("You: Enter question to ask the bot", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        #output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
        output = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))

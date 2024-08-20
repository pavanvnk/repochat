import streamlit as st
from repochat.db import vector_db, load_to_db
from repochat.models import hf_embeddings, code_llama
from repochat.chain import response_chain
import os

# Load the openai key
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize session state keys
if "db_name" not in st.session_state:
    st.session_state["db_name"] = "default_db_name"  # Set a default name if needed
if "db_loaded" not in st.session_state:
    st.session_state["db_loaded"] = False
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Set up the page
st.set_page_config(
    page_title="RepoChat",
    page_icon="💻",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "https://github.com/pnkvalavala/repochat/issues",
        'About': "No need to worry if you can't understand GitHub code or repositories anymore! Introducing RepoChat, where you can effortlessly chat and discuss all things related to GitHub repositories."
    }
)

st.markdown(
    "<h1 style='text-align: center;'>RepoChat</h1>",
    unsafe_allow_html=True
)

# Allow the user to input the repository path
repo_path = st.text_input("Enter the path to your local repository:", "")

if repo_path:
    if os.path.exists(repo_path):
        st.session_state["repo_path"] = repo_path
        st.session_state["db_name"] = os.path.basename(repo_path)  # Set db_name based on repo path
        
        try:
            with st.spinner('Loading the contents to database. This may take some time...'):
                st.session_state["chroma_db"] = vector_db(
                    hf_embeddings(),
                    load_to_db(st.session_state['repo_path'])
                )
            with st.spinner('Loading model to memory'):
                st.session_state["qa"] = response_chain( 
                    db=st.session_state["chroma_db"],
                    llm=code_llama()
                )

            st.session_state["db_loaded"] = True
        except TypeError:
            st.error("An error occurred while processing the repository.")
    else:
        st.error("The provided path does not exist. Please enter a valid path.")

if st.session_state.get("db_loaded"):
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter your query"):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            with st.spinner("Generating response..."):
                result = st.session_state["qa"](prompt)
            for chunk in result['answer'].split():
                full_response += chunk + " "
                st.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state["messages"].append({"role": "assistant", "content": full_response})


import os
import streamlit as st 
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage, Settings
from embedding import Settings

import warnings
warnings.filterwarnings("ignore")

def create_vector_store_index(pdf_nodes):
    index = VectorStoreIndex(pdf_nodes, embed_model=Settings.embed_model)
    index.storage_context.persist(persist_dir=r'F:\QnApdf\vector_db')
    
    loaded_index  = load_index_from_storage(
    StorageContext.from_defaults(persist_dir=r'F:\QnApdf\vector_db'),
    )
    return loaded_index

def create_vector_store_index(pdf_nodes, file_name):
    # Use a unique directory for each PDF file's vector store
    persist_dir = f'F:/QnApdf/vector_db/{file_name}'
    
    if os.path.exists(persist_dir):
        # Load existing index
        print("Vector store already exists for this file. Loading existing index.")
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=persist_dir))

    else:
        # Create new index
        print("Vector store does not exist for this file. Creating a new index.")
        index = VectorStoreIndex(pdf_nodes, embed_model=Settings.embed_model)
        os.makedirs(persist_dir, exist_ok=True)  # Ensure the directory exists
        st.success("File processed and index created successfully")
        index.storage_context.persist(persist_dir=persist_dir)
    
    return index

# @st.cache(allow_output_mutation=True)
@st.cache_resource(hash_funcs={VectorStoreIndex: lambda _: None})
def load_vector_store_index(file_name):
    persist_dir = f'F:/QnApdf/vector_db/{file_name}'
    index = load_index_from_storage(StorageContext.from_defaults(persist_dir=persist_dir))
    st.success("Vector store index loaded successfully") 
    return index


import os
import streamlit as st
from preprocessed import parse_pdf_documents
from vector_store import create_vector_store_index, load_vector_store_index
from postprocessing import query_index
from utils import save_uploaded_file
from logging_config import setup_logging 
setup_logging()


# Streamlit application 
st.title('RAG') #PDF Document Parser and Query

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file using the utility function
    file_path = save_uploaded_file(uploaded_file)
    
    # Extract file name without extension
    file_name = os.path.splitext(uploaded_file.name)[0]
    
  # Parse the PDF document
    pdf_nodes = parse_pdf_documents(file_path)
    
    # Create the vector store index
    index = create_vector_store_index(pdf_nodes, file_name)
    
    # Load the preprocessed vector store index
    index = load_vector_store_index(file_name)

    # Query input
    query = st.text_input("Enter your query:")
    
    try: 
      if query:
          # Perform the query
          results = query_index(query, index)
    except Exception as e:
      print(e)
      

# Ensure the uploads directory exists
os.makedirs('uploads', exist_ok=True)

















# import streamlit as st
# import os
# import sys
# from llama_index.core import SimpleDirectoryReader
# from llama_index.llms.huggingface import HuggingFaceLLM
# from llama_index.core import Settings
# from llama_index.core.node_parser import SimpleNodeParser
# from llama_index.core import VectorStoreIndex, ServiceContext, load_index_from_storage

# from llama_index.core import StorageContext
# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline ,AutoModel


# # os.environ['HUGGINGFACE_HUB_CACHE'] = r'F:\QnApdf\HuggignFaceHubModels\lamma_2'
# # model_name = "meta-llama/Llama-2-7b-chat-hf"

# # # Load the tokenizer and model
# # tokenizer = AutoTokenizer.from_pretrained(model_name)
# # model = AutoModel.from_pretrained(model_name)

# # # Verify the model is loaded
# # print(f"Model loaded and cached at: {os.environ['HUGGINGFACE_HUB_CACHE']}")

# # Set up parser and embedding model
# parser = SimpleNodeParser.from_defaults(
#     chunk_size=250,
#     chunk_overlap=20,
#     separator=' ',
#     paragraph_separator='\n\n\n',
#     secondary_chunking_regex='[^,.;。？！]+[,.;。？！]?'
# )

# embed_model = r'F:\QnApdf\HuggignFaceHubModels\embedding\models--sentence-transformers--all-mpnet-base-v2\models--sentence-transformers--all-mpnet-base-v2'
# # embed_model = "local:BAAI/bge-small-en-v1.5"
# service_context = ServiceContext.from_defaults(
#     llm=None,
#     embed_model=embed_model,
# )

# # Function to parse PDF documents
# def parse_pdf_documents(input_file):
#     reader = SimpleDirectoryReader(input_files=[input_file])
#     pdf_documents = reader.load_data()
#     pdf_nodes = parser.get_nodes_from_documents(pdf_documents)
#     return pdf_nodes

# def create_vector_store_index(pdf_nodes):
#     index = VectorStoreIndex(pdf_nodes, embed_model=embed_model)
#     index.storage_context.persist(persist_dir='F:/QnApdf/vector_db')
    
#     loaded_index = load_index_from_storage(
#         StorageContext.from_defaults(persist_dir='F:/QnApdf/vector_db'),
#         service_context=service_context
#     )
    
#     return loaded_index

# # Streamlit application 
# st.title('') #PDF Document Parser and Query

# uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# if uploaded_file is not None:
#     # Save the uploaded file
#     with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     st.write(f"Uploaded file: {uploaded_file.name}")

#     # Parse the PDF document
#     pdf_nodes = parse_pdf_documents(os.path.join("uploads", uploaded_file.name))
    
#     # Create the vector store index
#     index = create_vector_store_index(pdf_nodes)
#     st.success("File processed and index created successfully")

#     # Query input
#     query = st.text_input("Enter your query:")
    
#     if query:
#         # Perform the query
#         index = load_index_from_storage(
#             StorageContext.from_defaults(persist_dir='F:/QnApdf/vector_db'),
#             service_context=service_context
#         )
#         # def format_response(response):
#         #     content = getattr(response, 'content', '')
#         #     page_label = getattr(response, 'page_label', '')
#         #     file_path = getattr(response, 'file_path', '')
                    
#         #     # Combine content and metadata into a single formatted string
#         #     formatted_response = f"{content}\n\npage_label: {page_label}\nfile_path: {file_path}"
#         #     return formatted_response
#         # retriever = index.as_retriever(persist_dir='F:/QnApdf/vector_db')
#         # response = retriever.retrieve(query)
        
#         query_engine = index.as_query_engine(search_kwargs = {"k": 5, })
#         response = query_engine.query(query)
#         # disp_resp = format_response(response)
#         st.write("Response:", str(response))

# # Ensure the uploads directory exists
# os.makedirs('uploads', exist_ok=True)

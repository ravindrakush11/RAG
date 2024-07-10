
import streamlit as st
from llama_index.core import VectorStoreIndex


@st.cache_resource(hash_funcs={VectorStoreIndex: lambda _: None})
def process_retrieval_results(query, index):
    retriever = index.as_retriever(vector_store_query_mode="mmr",
    similarity_top_k=5,
    vector_store_kwargs={"mmr_threshold": 0.1},)
    result = retriever.retrieve(query)
    
    # query_engine = index.as_query_engine(streaming=True)
    # result = query_engine.query(query)
    # streaming_result.print_response_stream()
    
    count = 1
    for node_with_score in result:
            text_node = node_with_score.node
            score_node = node_with_score.score
            
            node_dict = {
            # "ID": text_node.id_,
            # "Embedding": text_node.embedding,
            # "Metadata": text_node.metadata,
            # "Excluded Embed Metadata Keys": text_node.excluded_embed_metadata_keys,
            # "Excluded LLM Metadata Keys": text_node.excluded_llm_metadata_keys,
            # "Relationships": {
            #     relationship.name: {
            #         "Node ID": related_node_info.node_id,
            #         "Node Type": related_node_info.node_type.name,
            #         "Metadata": related_node_info.metadata,
            #         "Hash": related_node_info.hash,
            #     } for relationship, related_node_info in text_node.relationships.items()
            # },
            "Text": text_node.text,
            # "Node Score": score_node
            # "Start Character Index": text_node.start_char_idx,
            # "End Character Index": text_node.end_char_idx,
            # "Text Template": text_node.text_template,
            # "Metadata Template": text_node.metadata_template,
            # "Metadata Separator": text_node.metadata_seperator,
            
        }
            
            st.markdown(f"<b>Similarity Text {count}</b>: {text_node.text}", unsafe_allow_html=True)
            count+=1
            # st.write(f"Node Score: {score_node}")
            # st.write(f"Node Dict {node_dict}")
    return result

def query_index(query, index):
    """
    Perform the query on the vector store index.

    Parameters:
    query (str): The query string
    index: The vector store index object

    Returns:
    list: The retrieval results
    """
    # Assuming process_retrieval_results is a function that processes the query
    results = process_retrieval_results(query, index)
    return results

from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core import SimpleDirectoryReader


def parse_pdf_documents(input_file):
    
    parser = SimpleNodeParser.from_defaults(
    chunk_size=250,
    chunk_overlap=20,
    separator=' ',
    paragraph_separator='\n\n\n',
    secondary_chunking_regex='[^,.;。？！]+[,.;。？！]?'
)
    reader = SimpleDirectoryReader(input_files=[input_file])
    pdf_documents = reader.load_data()
    pdf_nodes = parser.get_nodes_from_documents(pdf_documents)
    return pdf_nodes
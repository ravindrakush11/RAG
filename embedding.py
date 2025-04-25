from llama_index.core import Settings

from llama_index.llms.huggingface import HuggingFaceLLM

model_name = r'F:\QnApdf\HuggignFaceHubModels\models--HuggingFaceH4--zephyr-7b-alpha\snapshots\2ce2d025864af849b3e5029e2ec9d568eeda892d'
llm = HuggingFaceLLM(model_name=model_name,
                     tokenizer_name=model_name,
                      context_window=1024,
                      max_new_tokens=256,
                      device_map="auto",
                       tokenizer_kwargs={"max_length": 1024},
                    #    model_kwargs={"torch_dtype": torch.float16}
                       )

# from llama_index.llms.ollama import Ollama

# model_name = r'C:\Users\Admin\.ollama\models\blobs\sha256-ef311de6af9db043d51ca4b1e766c28e0a1ac41d60420fed5e001dc470c64b77'
# llm = Ollama(model="gemma:2b", request_timeout=30.0)

embed_model="local:BAAI/bge-small-en-v1.5"
# # Set settings
Settings.chunk_size = 512
Settings.embed_model = embed_model
Settings.llm = None 

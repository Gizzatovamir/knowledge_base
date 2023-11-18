from ollama/ollama
RUN mkdir /llama_root
WORKDIR /llama_root
ENTRYPOINT ollama serve && ollama pull llama2
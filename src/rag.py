from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma


# 1. Load PDF
loader = PyPDFLoader("documents/sample.pdf")
documents = loader.load()


# 2. Split PDF into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)


# 3. Create embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# 4. Store documents in Chroma
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)


# 5. Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


# 6. Create local LLM
llm = ChatOllama(
    model="llama3.2"
)


# 7. Ask a question
question = "What is this document about?"


# 8. Retrieve relevant chunks
results = retriever.invoke(question)


# 9. Combine retrieved information
context = "\n\n".join(
    document.page_content
    for document in results
)


# 10. Create prompt
prompt = f"""
Answer the question using only the information provided below.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
"I could not find this information in the document."
"""


# 11. Ask Llama
response = llm.invoke(prompt)


# 12. Print answer
print("\nAnswer:")
print(response.content)
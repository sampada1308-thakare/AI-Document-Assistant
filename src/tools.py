from langchain_core.tools import tool


@tool
def search_documents(question: str) -> str:
    """Search the uploaded PDF and return relevant information."""

    from langchain_chroma import Chroma
    from langchain_ollama import OllamaEmbeddings

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_store = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    results = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in results
    )

    return context

@tool
def calculator(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
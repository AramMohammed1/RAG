from langchain_community.document_loaders import PyPDFLoader

def pdf_to_string(file_path: str) -> str:

    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return "\n".join([doc.page_content for doc in documents])

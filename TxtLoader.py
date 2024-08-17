from langchain_community.document_loaders import TextLoader

def txt_to_string(file_path: str) -> str:
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents[0].page_content

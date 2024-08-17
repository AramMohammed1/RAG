from llama_index.embeddings.ollama import OllamaEmbedding
from PyPDF2 import PdfReader
from PDFLoader import PDFLoader

pdf_loader = PDFLoader(file_path="abc.pdf")  
documents = pdf_loader.load()




embeddings = OllamaEmbedding(
    model_name="llama3",
    base_url="http://172.25.1.141:11434",
)



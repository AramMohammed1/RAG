from PDFLoader import pdf_to_string
from DocxLoader import docx_to_string
from TxtLoader import txt_to_string



def converter(file_path: str) -> str:
  
    # Extract the last three characters of the file extension
    ext = file_path[-3:].lower()

    # Choose the appropriate function based on the extension
    if ext == 'txt':
        return txt_to_string(file_path)
    elif ext == 'pdf':
        return pdf_to_string(file_path)
    elif ext == 'ocx' or 'doc':  # Checking for 'docx' but using the last three chars
        return docx_to_string(file_path)
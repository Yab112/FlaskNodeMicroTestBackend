import pdfplumber

def extract_pdf_content(file_path):
    content = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            content += page.extract_text()
    return content

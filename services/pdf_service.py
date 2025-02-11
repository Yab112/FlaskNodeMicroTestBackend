import pdfquery
import fitz

def extract_pdf_content(file_path):
    """
    Extracts all text from a PDF file using PyMuPDF.
    """
    text = ""
    with fitz.open(file_path) as doc:
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  
            text += page.get_text()  
    return text


def extract_metadata(file_path):
    pdf = pdfquery.PDFQuery(file_path)
    pdf.load()
    metadata = pdf.tree.getroot().attrib
    return metadata

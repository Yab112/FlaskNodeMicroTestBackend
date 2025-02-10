from flask import Blueprint, request, jsonify
from services.pdf_service import extract_pdf_content
from models.pdf_data import PdfData
from config.db import get_db
import os
import tempfile

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file.save(temp_file.name)
        temp_file.close()  # Close the file before processing
        extracted_content = extract_pdf_content(temp_file.name)
        
        # Store extracted content in MongoDB
        db = get_db()
        collection = db['pdf_data']
        pdf_data = PdfData(content=extracted_content)
        collection.insert_one(pdf_data.to_dict())
        
        time.sleep(1)
        try:
            os.remove(extracted_content)
        except PermissionError:
            return f"Error: Unable to delete the file {extracted_content}. It might be in use.", 500

        
        return jsonify({'message': 'PDF extracted and stored successfully'}), 200

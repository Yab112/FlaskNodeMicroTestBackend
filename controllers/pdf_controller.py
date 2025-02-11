from flask import Blueprint, request, jsonify
from services.pdf_service import extract_pdf_content, extract_metadata
from utils.data_preprocess import preprocess_and_store_data
from utils.error_handler import handle_db_errors
from utils.db_utils import store_data
import os
import tempfile
import logging
import time

pdf_bp = Blueprint('pdf', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@pdf_bp.route('/upload', methods=['POST'])
@handle_db_errors
def upload_pdf():
    if 'files' not in request.files:
        return jsonify({'error': 'No files part'}), 400

    files = request.files.getlist('files')
    if not files:
        return jsonify({'error': 'No selected files'}), 400

    responses = []

    for file in files:
        if file.filename == '':
            continue

        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                file.save(temp_file.name)
                temp_file.close()  # Close the file before processing
                extracted_content = extract_pdf_content(temp_file.name)
                metadata = extract_metadata(temp_file.name)

                # Preprocess and store data
                if preprocess_and_store_data(extracted_content,metadata):
                    logging.info(f"Data from {file.filename} processed and stored successfully")
                else:
                    logging.error(f"Failed to process data from {file.filename}",)
                
                time.sleep(1)       
                os.remove(temp_file.name)  # Delete the temporary file

                responses.append({
                    'filename': file.filename,
                    'message': 'PDF extracted and stored successfully',
                    'metadata': metadata
                })
        except Exception as e:
            logging.error(f"Error processing file {file.filename}: {e}")
            return jsonify({'error': f"Error processing file {file.filename}"}), 500

    return jsonify(responses), 200

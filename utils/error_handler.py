import logging
from flask import jsonify
from pymongo.errors import (
    ConfigurationError, NetworkTimeout, ServerSelectionTimeoutError,
    OperationFailure, InvalidURI, InvalidName, PyMongoError
)

# Configure logging
logging.basicConfig(level=logging.INFO)

def handle_db_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConfigurationError as e:
            logging.error(f"Database configuration error: {e}")
            return jsonify({'error': 'Database configuration error'}), 500
        except NetworkTimeout as e:
            logging.error(f"Database network timeout error: {e}")
            return jsonify({'error': 'Database network timeout error'}), 500
        except ServerSelectionTimeoutError as e:
            logging.error(f"Database server selection timeout error: {e}")
            return jsonify({'error': 'Database server selection timeout error'}), 500
        except OperationFailure as e:
            logging.error(f"Database operation failure: {e}")
            return jsonify({'error': 'Database operation failure'}), 500
        except InvalidURI as e:
            logging.error(f"Invalid MongoDB URI: {e}")
            return jsonify({'error': 'Invalid MongoDB URI'}), 500
        except InvalidName as e:
            logging.error(f"Invalid database name: {e}")
            return jsonify({'error': 'Invalid database name'}), 500
        except PyMongoError as e:
            logging.error(f"General PyMongo error: {e}")
            return jsonify({'error': 'General database error'}), 500
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return jsonify({'error': 'An unexpected error occurred'}), 500
    return wrapper

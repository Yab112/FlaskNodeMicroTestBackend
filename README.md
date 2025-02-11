# Flask App for AccaciaTech

## Overview

This project is a Flask application designed for AccaciaTech. It includes various utilities and configurations to facilitate development and deployment.

## Features

- MongoDB integration
- Environment variable management
- Logging configuration
- Data storage utilities

## Setup

### Prerequisites

- Python 3.x
- MongoDB
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Yab112/FlaskNodeMicroTestBackend.git
   cd FlaskNodeMicroTestBackend
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your MongoDB URI:
   ```env
   MONGO_URI=mongodb://your_mongo_uri
   ```

## Usage

1. Activate the virtual environment:

   ```sh
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Run the Flask application:

   ```sh
   flask run
   ```

3. Access the application at `http://127.0.0.1:5000`.

## Project Structure

```
flask_app/
│
├── venv/                   # Virtual environment
├── flask_app/
│   ├── __init__.py         # Flask app initialization
│   ├── utils/
│   │   ├── db_utils.py     # Database utilities
│   │   └── ...
│   ├── services/
│   │   ├── __init__.py     # Route initialization
│   │   └── pdf_service.py      # Example route
    ├── Controllers/
│   │   ├── pdf_controller.py     # Route initialization
│   │   └── ex
│   ├── models/
│   │   ├── __init__.py     # Model initialization
│   │   └── pdf_data.py      # Example model
│   └── ...
├── app.py
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.

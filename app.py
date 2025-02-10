from flask import Flask
from controllers.pdf_controller import pdf_bp

app = Flask(__name__)
app.register_blueprint(pdf_bp)

if __name__ == '__main__':
    app.run(debug=True)

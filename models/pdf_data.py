from datetime import datetime

class PdfData:
    def __init__(self, content, extracted_on=None):
        self.content = content
        self.extracted_on = extracted_on or datetime.utcnow()

    def to_dict(self):
        return {
            'content': self.content,
            'extracted_on': self.extracted_on
        }

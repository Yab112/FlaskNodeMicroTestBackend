from datetime import datetime

class PdfData:
    def __init__(self, content, metadata=None, extracted_on=None):
        self.content = content
        self.metadata = metadata or {}
        self.extracted_on = extracted_on or datetime.utcnow()

    def to_dict(self):
        return {
            'content': self.content,
            'metadata': {
                'extracted_on': self.extracted_on.isoformat(),
                **self.metadata
            }
        }

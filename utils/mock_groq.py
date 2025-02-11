class GroqClient:
    def __init__(self, api_key):
        self.api_key = api_key

    class Chat:
        def completions(self, messages, model):
            return {"choices": [{"message": {"content": "Mocked response"}}]}  

    @property
    def chat(self):
        return self.Chat()

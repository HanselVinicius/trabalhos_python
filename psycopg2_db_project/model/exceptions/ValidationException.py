class ValidationException(Exception):
    def __init__(self, message="A validation error occurred"):
        self.message = message
        super().__init__(self.message)
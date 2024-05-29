class TaskValidationError(Exception):
    """Exception"""

    def __init__(self, message, status_code=400):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)
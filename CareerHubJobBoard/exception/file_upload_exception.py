# file_upload_exception.py
class FileUploadException(Exception):
    def __init__(self, message="Error occurred while uploading the file."):
        self.message = message
        super().__init__(self.message)

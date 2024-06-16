class BraipyException(Exception):
  def __init__(self, error_message: str):
    self.error_message = error_message

class NotTenjiError(BraipyException):
  def __str__(self):
    return self.error_message

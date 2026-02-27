class CNPError(Exception):
    """Base exception for CNP related errors."""
    pass

class CNPInvalidLengthError(CNPError):
    """Raised when the CNP does not have exactly 13 characters."""
    def __init__(self, message="CNP must be exactly 13 characters."):
        self.message = message
        super().__init__(self.message)

class CNPInvalidCharacterError(CNPError):
    """Raised when the CNP contains non-numeric characters."""
    def __init__(self, message="CNP must only contain Arabic numerals (0-9)."):
        self.message = message
        super().__init__(self.message)

class CNPInvalidDateError(CNPError):
    """Raised when a date is not valid for a CNP."""
    def __init__(self, message="Date is not valid (must be between January 1st, 1800 - December 31st, 2099)."):
        self.message = message
        super().__init__(self.message)

from client import status_codes

class AddressException(Exception):
    status_code = status_codes.HTTP_400_BAD_REQUEST
    default_message = ('Address is missing required fields')

    def __init__(self, status_code=status_code, message=default_message):
        self.status_code = status_code
        self.message = message

class EffectiveDateException(Exception):
    status_code = status_codes.HTTP_400_BAD_REQUEST
    default_message = ('Policy is missing effective date')

    def __init__(self, status_code=status_code, message=default_message):
        self.status_code = status_code
        self.message = message

class InvalidQuoteRequestException(Exception):
    status_code = status_codes.HTTP_400_BAD_REQUEST
    default_message = ('Quote request is missing required fields')

    def __init__(self, status_code=status_code, message=default_message):
        self.status_code = status_code
        self.message = message

class ClientUnauthorizedException(Exception):
    status_code = status_codes.HTTP_401_UNAUTHORIZED
    default_message = ('Client is unauthorized')

    def __init__(self, status_code=status_code, message=default_message):
        self.status_code = status_code
        self.message = message
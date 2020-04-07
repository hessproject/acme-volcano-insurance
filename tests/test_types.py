import pytest
from client.types import *

def test_malformed_address_raises_exception():
    with pytest.raises(AddressException):
        Address(None, None, None, None, line2=None)

def test_policy_missing_effective_date_raises_exception():
    with pytest.raises(EffectiveDateException):
        PolicyInformation(None, True, 100, True, 2)

def test_quote_request_missing_policy_raises_exception():
    with pytest.raises(InvalidQuoteRequestException):
        address = Address('123 Test Lane', 'Cityville', 'State', '11111')
        QuoteRequest(None, address, address)
import pytest
import json
from client.utils import *
from client.types import PolicyInformation, Address, QuoteRequest

def test_clean_none_keys():
    testobj = {
        'testfieldpersists': 'some data',
        'testfieldremoved': None
    }
    testobj = clean_none_keys(testobj)
    assert 'testfieldremoved' not in testobj
    assert 'testfieldpersists' in testobj

def test_create_request_object():
    policy = PolicyInformation('2020-04-25', False, 100, True, 2)
    address = Address('123 Test Ln', 'Fakestown', 'CA', '12345', line2='line2 test')
    request = QuoteRequest(policy, address, address)
    data = create_request_object(request)
    
    for data_point in data:
        assert data_point is not None


    
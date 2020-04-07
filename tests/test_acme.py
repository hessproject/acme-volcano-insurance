import pytest
from client.acme import AcmeClient
from client.exceptions import ClientUnauthorizedException
from client.types import QuoteRequest, Address, PolicyInformation

#Reusable Valid Quote Request
address = Address('123 E Main St.', 'Seattle', 'WA', '98112')
policy = PolicyInformation('2020-04-25', False, 100, True, 2)
test_request = QuoteRequest(policy, address, address)

#Valid Login Creds
user = 'acme_user'
pwd = 'super-secret'

def test_login_success():
    client = AcmeClient()
    client.login(user, pwd)
    assert client.access_token is not None

def test_login_fails_with_wrong_info():
    client = AcmeClient()
    with pytest.raises(ClientUnauthorizedException):
        client.login('baduser', 'badpassword')

def test_refresh_token_success():
    client = AcmeClient()
    client.login(user, pwd)
    data = client.refresh_token(client.refresh_token_value)
    assert 'access_token' in data and 'access_token_expires' in data

def test_refresh_token_fails_no_auth():
    client = AcmeClient()
    with pytest.raises(ClientUnauthorizedException):
        client.refresh_token(None)

def test_fetch_all_plans_fails_no_auth():
    client = AcmeClient()
    with pytest.raises(ClientUnauthorizedException):
        client.fetch_all_plans()

def test_fetch_all_plans_success():
    client = AcmeClient()
    client.login(user, pwd)
    res = client.fetch_all_plans()
    assert 'plans' in res['response']

def test_fetch_one_plan_fails_no_auth():
    client = AcmeClient()
    with pytest.raises(ClientUnauthorizedException):
        client.fetch_one_plan(1)

def test_fetch_one_plan_success():
    client = AcmeClient()
    client.login(user, pwd)
    res = client.fetch_one_plan(1)
    assert 'id' in res['response'] and 'name' in res['response']

def test_create_quote_fails_no_auth():
    client = AcmeClient()
    with pytest.raises(ClientUnauthorizedException):
        client.create_quote(test_request)

def test_create_quote_success():
    client = AcmeClient()
    client.login(user, pwd)
    res = client.create_quote(test_request)
    assert 'quote_number' in res

def test_update_quote_fails_no_auth():
    client = AcmeClient()
    with pytest.raises(ClientUnauthorizedException):
        client.update_quote(test_request, 1)

def test_update_quote_success():
    client = AcmeClient()
    client.login(user, pwd)
    res = client.create_quote(test_request)
    quote_number = res['quote_number']
    client.update_quote(test_request, quote_number)
    assert 'quote_number' in res

def test_get_quote_fails_no_auth():
    client = AcmeClient()
    with pytest.raises(ClientUnauthorizedException):
        client.get_quote(1)

def test_get_quote_success():
    client = AcmeClient()
    client.login(user, pwd)
    res1 = client.create_quote(test_request)
    quote_number = res1['quote_number']
    res2 = client.get_quote(quote_number)
    assert 'quote_number' in res2
    assert 'effective_date' in res2

def test_get_checkout_data_fails_no_auth():
    client = AcmeClient()
    with pytest.raises(ClientUnauthorizedException):
        client.get_checkout_data(1)

def test_get_checkout_data_success():
    client = AcmeClient()
    client.login(user, pwd)
    res1 = client.create_quote(test_request)
    quote_number = res1['quote_number']
    res2 = client.get_checkout_data(quote_number)
    assert 'rates' in res2
    assert 'total' in res2

def test_purchase_quote_fails_no_auth():
    client = AcmeClient()
    with pytest.raises(ClientUnauthorizedException):
        client.purchase_quote(1)

def test_purchase_quote_success():
    client = AcmeClient()
    client.login(user, pwd)
    res1 = client.create_quote(test_request)
    quote_number = res1['quote_number']
    res2 = client.purchase_quote(quote_number)
    assert 'policy_number' in res2
from client import utils
from client.types import QuoteRequest, Address
from client.exceptions import ClientUnauthorizedException, InvalidQuoteRequestException
import requests
import json
import xmltodict

class AcmeClient:

    base_url = 'http://surely.surepre.me'

    access_token = None
    access_token_expires = None
    refresh_token_value = None

    def login(self, username: str, password: str):
        """
        Login to client

        Returns: access token, expiry, and refresh token
        """
        url = self.base_url + '/auth'
        r = requests.post(url, json={'username': username, 'password': password})
        auth_data = r.json()
        #Make sure response includes cred data
        access_cred_data = {'access_token', 'access_token_expires', 'refresh_token'}
        if any(cred not in auth_data for cred in access_cred_data):
            raise ClientUnauthorizedException(message="Invalid credentials")
        else:
            self.access_token = auth_data['access_token']
            self.access_token_expires = auth_data['access_token_expires']
            self.refresh_token_value = auth_data['refresh_token']
        return auth_data


    def refresh_token(self, refresh_token: str):
        """
        Refresh expired access token

        Returns: access token, expiry
        """
        if self.refresh_token_value is None:
            raise ClientUnauthorizedException(message="Client is not logged in")
        url = self.base_url + '/token_refresh'
        headers = {'Authorization': 'Bearer {}'.format(self.refresh_token_value)}
        r = requests.post(url, json={}, headers=headers)
        auth_data = r.json()
        self.access_token = auth_data['access_token']
        self.access_token_expires = auth_data['access_token_expires']
        return auth_data

    def fetch_all_plans(self):
        """
        Fetch all available insurance plans. 
        Transforms APIs XML response to JSON for easier dict manipulation

        Returns: JSON list of insurance information
        """
        if self.access_token == None:
            raise ClientUnauthorizedException
        url = self.base_url + '/plans'
        headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        r = requests.get(url, headers=headers)
        return xmltodict.parse(r.content)

    def fetch_one_plan(self, plan_id: str):
        """
        Fetch a single insurance plan
        Transforms APIs XML response to JSON for easier dict manipulation

        Returns: JSON data of single insurance plan
        """
        if self.access_token == None:
            raise ClientUnauthorizedException
        url = self.base_url + '/plans/{}'.format(plan_id)
        headers = {
            'Authorization': 'Bearer {}'.format(self.access_token)}
        r = requests.get(url, headers=headers)
        return xmltodict.parse(r.content)

    def create_quote(self, request: QuoteRequest):
        """
        Create a quote from a quote request object

        Returns: JSON data about created quote
        """
        if self.access_token == None:
            raise ClientUnauthorizedException
        if request is None:
            raise InvalidQuoteRequestException
        url = self.base_url + '/quotes'
        headers = {
            'Authorization': 'Bearer {}'.format(self.access_token),
            'Content-Type': 'application/json'
            }
        data = utils.create_request_object(request)
        r = requests.post(url, data=json.dumps(data), headers=headers)
        return r.json()

    def update_quote(self, request: QuoteRequest, quote_number: str):
        """
        Update an existing quote from a quote request object

        Returns: JSON data about updated quote
        """
        if self.access_token == None:
            raise ClientUnauthorizedException
        if request is None:
            raise InvalidQuoteRequestException
        url = self.base_url + '/quotes/{}'.format(quote_number)
        headers = {
            'Authorization': 'Bearer {}'.format(self.access_token),
            'Content-Type': 'application/json'
            }
        data = utils.create_request_object(request)
        r = requests.put(url, data=json.dumps(data), headers=headers)
        return r.json()

    def get_quote(self, quote_number: str):
        """
        Get an existing quote

        Returns: JSON data about requested quote
        """
        if self.access_token == None:
            raise ClientUnauthorizedException
        url = self.base_url + '/quotes/{}'.format(quote_number)
        headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        r = requests.get(url, headers=headers)
        return r.json()

    def get_checkout_data(self, quote_number: str):
        """
        Get price breakdown and total cost of plan

        Returns: JSON data about cost and breakdown
        """
        if self.access_token == None:
            raise ClientUnauthorizedException
        url = self.base_url + '/quotes/{}/checkout'.format(quote_number)
        headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        r = requests.get(url, headers=headers)
        return r.json()

    def purchase_quote(self, quote_number:str):
        """
        Purchase a plan with provided quote number

        Returns: JSON data about policy number
        """
        if self.access_token == None:
            raise ClientUnauthorizedException
        url = self.base_url + '/quotes/{}/purchase'.format(quote_number)
        headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        r = requests.post(url, headers=headers)
        return r.json()
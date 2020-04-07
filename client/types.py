from client.exceptions import EffectiveDateException, AddressException, InvalidQuoteRequestException

class Address:
    def __init__(self, line1, city, state, zipcode, line2=None):
        
        if None in (line1, city, state, zipcode):
            raise AddressException
        
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.zipcode = zipcode

class PolicyInformation:
    def __init__(self, effective_date, previous_policy_cancelled, mileage_to_volcano, owns_property, plan_id):

        if effective_date == None:
            raise EffectiveDateException

        self.effective_date = effective_date
        self.previous_policy_cancelled = previous_policy_cancelled
        self.mileage_to_volcano = mileage_to_volcano
        self.owns_property = owns_property
        self.plan_id = plan_id

class QuoteRequest:
    def __init__(self, policy_information: PolicyInformation, mailing_address: Address, property_address: Address):

        if policy_information == None:
            raise InvalidQuoteRequestException

        self.policy_information = policy_information
        self.mailing_address = mailing_address
        self.property_address = property_address
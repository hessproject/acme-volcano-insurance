import json
from client.types import QuoteRequest

def clean_none_keys(obj):
    return {k:v for k,v in obj.items() if v is not None}

def create_request_object(req:QuoteRequest):
    data = {
        "effective_date": req.policy_information.effective_date,
        "previous_policy_cancelled": req.policy_information.previous_policy_cancelled,
        "property_mileage_to_nearest_volcano": req.policy_information.mileage_to_volcano,
        "owns_property_to_be_insured": req.policy_information.owns_property,
        "plan_id": req.policy_information.plan_id,
        "mailing_address": {
            "line1": req.mailing_address.line1,
            "city": req.mailing_address.city,
            "state": req.mailing_address.state,
            "zip_code": req.mailing_address.zipcode
        },
        "property_address": {
            "line1": req.property_address.line1,
            "city": req.property_address.city,
            "state": req.property_address.state,
            "zip_code": req.property_address.zipcode
        }
    }
    if req.mailing_address.line2 is not None:
        data["mailing_address"]["line2"] = req.mailing_address.line2
    if req.property_address.line2 is not None:
        data["property_address"]["line2"] = req.property_address.line2
    return data

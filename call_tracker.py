import requests
from twilio.rest import Client

# Twilio configuration
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
client = Client(account_sid, auth_token)

# numverify configuration
numverify_api_key = 'your_numverify_api_key'
numverify_url = 'http://apilayer.net/api/validate'

def get_location(phone_number):
    params = {
        'access_key': numverify_api_key,
        'number': phone_number
    }
    response = requests.get(numverify_url, params=params)
    data = response.json()
    if data['valid']:
        return data['location']
    else:
        return 'Unknown location'

def list_calls():
    calls = client.calls.list(limit=20)
    for call in calls:
        location = get_location(call.from_)
        print(f"From: {call.from_}, To: {call.to}, Status: {call.status}, Start Time: {call.start_time}, Duration: {call.duration}, Location: {location}")

def track_call(call_sid):
    call = client.calls(call_sid).fetch()
    location = get_location(call.from_)
    print(f"From: {call.from_}, To: {call.to}, Status: {call.status}, Start Time: {call.start_time}, Duration: {call.duration}, Location: {location}")

if __name__ == '__main__':
    print("Listing recent calls:")
    list_calls()

    # Example: Track a specific call by its SID
    # Replace 'your_call_sid' with an actual call SID from your Twilio account
    call_sid = 'your_call_sid'
    print("\nTracking specific call:")
    track_call(call_sid)

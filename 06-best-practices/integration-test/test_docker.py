# pylint: disable=line-too-long

import json

import requests
from deepdiff import DeepDiff

with open('event.json', 'rt', encoding='utf-8') as f_in:
    event = json.load(f_in)

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# response = requests.post(url, json=event)
# print(response.json())
actual_response = requests.post(url, json=event, timeout=10).json()
print(json.dumps(actual_response, indent=2))
expected_response = {
    'predictions': [
        {
            'model': 'ride_duration_prediction_model',
            'version': 'Test123',
            'prediction': {'ride_duration': 18.1, 'ride_id': 156},
        }
    ]
}

diff = DeepDiff(actual_response, expected_response, significant_digits=0)

print(f'diff={diff}')

assert 'type_changes' not in diff
assert 'values_changed' not in diff

# print(json.dumps(expected_response, indent=2))
# assert actual_response == expected_response

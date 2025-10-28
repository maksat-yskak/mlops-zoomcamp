import json
import requests

from deepdiff import DeepDiff

event = {
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49668304959240208419583667446471616242820364806463160322",
                "data": "ewogICAgICAgICJyaWRlIjogewogICAgICAgICAgICAiUFVMb2NhdGlvbklEIjogMTMwLAogICAgICAgICAgICAiRE9Mb2NhdGlvbklEIjogMjA1LAogICAgICAgICAgICAidHJpcF9kaXN0YW5jZSI6IDMuNjYKICAgICAgICB9LCAKICAgICAgICAicmlkZV9pZCI6IDE1NgogICAgfQ==",
                "approximateArrivalTimestamp": 1761315953.448
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000000:49668304959240208419583667446471616242820364806463160322",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::848474832112:role/lambda-kinesis-role",
            "awsRegion": "eu-north-1",
            "eventSourceARN": "arn:aws:kinesis:eu-north-1:848474832112:stream/ride_events"
        }
    ]
}

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# response = requests.post(url, json=event)
# print(response.json())
actual_response = requests.post(url, json=event).json()
print(json.dumps(actual_response, indent=2))
expected_response = {
    'predictions': [{
        'model': 'ride_duration_prediction_model',
        'version': 'Test123',
        'prediction':
        {
            'ride_duration': 18.16894572640533,
            'ride_id': 156
        }
    }]
}

diff = DeepDiff(actual_response, expected_response, significant_digits=5)

print(f'diff={diff}')

assert 'type_changes' not in diff
assert 'values_changed' not in diff

# print(json.dumps(expected_response, indent=2))
# assert actual_response == expected_response
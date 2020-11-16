import boto3
import json
from datetime import datetime
import calendar
import random
import time


my_stream_name = 'OrdersStream'
kinesis_client = boto3.client('kinesis', region_name='us-west-2')

payload = {
    'prop': str(1),
    'timestamp': str(time.time()),
    'thing_id': 1
}

print(payload)

put_response = kinesis_client.put_record(
    StreamName=my_stream_name,
    Data=json.dumps(payload),
    PartitionKey=str(1))

payload = {
    'prop': str(2),
    'timestamp': str(time.time()),
    'thing_id': 232
}

put_response = kinesis_client.put_record(
    StreamName=my_stream_name,
    Data=json.dumps(payload),
    PartitionKey=str(2))


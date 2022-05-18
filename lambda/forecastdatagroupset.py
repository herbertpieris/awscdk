import json
import boto3

def lambda_handler(event, context):
  forecast = boto3.client(forecast)
  response = forecast.create_dataset_group(
    DatasetGroupName='hapcustforecast',
    Domain='INVENTORY_PLANNING'
)
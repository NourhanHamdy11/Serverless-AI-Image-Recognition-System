import boto3
import json

def lambda_handler(event, context):

    rek = boto3.client('rekognition')

    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        print(f"Trigger received! Analyzing image: {key} from bucket: {bucket}")

        response = rek.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=3
        )

        print("Analysis Successful:")
        for label in response['Labels']:
            print(f"- {label['Name']}")

    except Exception as e:

        print(f"Connection established, but permission denied by Lab Policy: {str(e)}")

    return {'statusCode': 200}

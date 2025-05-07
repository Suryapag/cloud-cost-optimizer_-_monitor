import boto3
import os
from dotenv import load_dotenv
# Load environment variables from .env file
# Ensure you have a .env file with AWS_ACCESS_KEY and AWS_SECRET_KEY
load_dotenv()

def list_instances():
    ec2 = boto3.client('ec2', 
                       aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                       aws_secret_access_key=os.getenv('AWS_SECRET_kEY'))
    
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

if __name__ == "__main__":
    list_instances()
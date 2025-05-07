import boto3
import sys
import os
from email.mime.text import MIMEText
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared.notifier import send_error_email
from dotenv import load_dotenv
# Load environment variables from .env file
# Ensure you have a .env file with AWS_ACCESS_KEY and AWS_SECRET_KEY
load_dotenv()

def list_instances():
    ec2 = boto3.client('ec2', 
                       aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                       aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    data = []
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
            data.append({
                'InstanceId': instance['InstanceId'],
                'State': instance['State']['Name'],
                'InstanceType': instance['InstanceType'],
                'LaunchTime': instance['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S"),
                'CPUOptions': instance.get('CpuOptions', {}).get('CoreCount', 'N/A'),
                'Memory': instance.get('MemoryInfo', {}).get('SizeInMiB', 'N/A')
            })
            subject = f"Instance ID: {instance['InstanceId']}"

    return send_error_email(subject, data)

if __name__ == "__main__":
    list_instances()
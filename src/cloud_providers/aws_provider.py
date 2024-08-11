import boto3

class AWSProvider:
    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.s3 = boto3.client('s3')

    def list_ec2_instances(self):
        response = self.ec2.describe_instances()
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'InstanceId': instance['InstanceId'],
                    'InstanceType': instance['InstanceType'],
                    'State': instance['State']['Name']
                })
        return instances

    def list_s3_buckets(self):
        response = self.s3.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]

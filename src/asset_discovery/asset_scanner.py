from src.cloud_providers.aws_provider import AWSProvider

class AssetScanner:
    def __init__(self):
        self.aws_provider = AWSProvider()

    def scan_assets(self):
        assets = {
            'ec2_instances': self.aws_provider.list_ec2_instances(),
            's3_buckets': self.aws_provider.list_s3_buckets()
        }
        return assets

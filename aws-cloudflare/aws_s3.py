import os
from tinys3 import Connection
from tinys3.request_factory import S3Request

access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret = os.environ.get('AWS_ACCESS_KEY_SECRET')
region = os.environ.get('AWS_REGION')
bucket = os.environ.get('AWS_BUCKET')
if access_key is None or secret is None:
	raise Exception('Amazon S3 credentials are not available')


conn = Connection(access_key,secret, default_bucket=bucket, tls=True)

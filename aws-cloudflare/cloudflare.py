import os
from pyflare import PyflareClient


email = os.environ.get('CLOUDFLARE_EMAIL')
api_key = os.environ.get('CLOUDFLARE_API_KEY')
if email is None or api_key is None:
	raise Exception('CloudFlare credentials are not available')


client = PyflareClient(email, api_key)

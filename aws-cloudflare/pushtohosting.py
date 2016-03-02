import argparse
import tinys3
from cloudflare import client as cf_client
from aws_s3 import conn as aws_client
import os
import logging

domain = 'cdn.redditenhancementsuite.com'
base_url = 'https://{domain}/{filename}'

logging.basicConfig(level=logging.DEBUG)

class AmazonS3_Cloudflare_Pusher(object):
	def __init__(self, filenames):
		super(self.__class__, self).__init__()
		if isinstance(filenames, basestring):
			self.filenames = [ filenames ]
		else:
			self.filenames = filenames

	def main(self):

		for filename in self.filenames:
			self.push(filename)

	def push(self, filename):
		with open(filename,'rb') as f:
			logging.debug("{}:\n{}".format(filename, f))
			logging.info('Uploading {} to AWS'.format(filename))
			aws_client.upload(os.path.basename(filename),f)
		url = base_url.format(domain=domain, filename=filename)
		logging.info('Purging {} on Cloudflare'.format(filename))
		#cf_response = cf_client.zone_file_purge(z=domain, url=url) # Todo: catch ratelimit exception and wait


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("src_path", metavar="path", type=str,
	    help="Path to file")

	args = parser.parse_args()
	filename = args.src_path

	logging.debug('Pushing to hosting: {}'.format(filename))
	bot = AmazonS3_Cloudflare_Pusher(filename)
	bot.main()


import requests
import time
from itertools import islice
class Push():
	def sms_push(self):
		n = 5
		with open('/home/aakinduko/sms/uba.txt') as f:
		     for lines in iter(lambda: tuple(islice(f, n)), ()):  
		        #process(n_lines)
		       	id=(lines)
		       	num = [s.replace('\n','') for s in id]
		       	message='hello'
		       	for msisdn in num:

		       		url = 'http://google.com/mtn/sms?from_addr=*904&to_addr=%2B{0}&content={1}'.format(msisdn,message)
		           	r=requests.get('{0}'.format(url), verify=False)
		           	print(r.status_code)
		           	print(r.url)
		      	if True:
		      		time.sleep(5)
start=Push()
start.sms_push()
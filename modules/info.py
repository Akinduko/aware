import argparse
import BaseHTTPServer
import cgi
import urllib2
from BeautifulSoup import BeautifulSoup
import logging
import os
import sys
import requests
import time
import json
from itertools import islice
from lxml.etree import tostring
from lxml.builder import E
def live_agent(self):
    logging.info('GET %s' % (self.path))
    args = {}
    idx = self.path.find('?')
    if idx >= 0:
        rpath = self.path[:idx]
        args = cgi.parse_qs(self.path[idx+1:])
    else:
        rpath = self.path
    # Print out logging information about the path and args.
    if 'content-type' in self.headers:
        ctype, _ = cgi.parse_header(self.headers['content-type'])
        logging.debug('TYPE %s' % (ctype))
        logging.debug('PATH %s' % (rpath))
        logging.debug('ARGS %d' % (len(args)))
        print('TYPE %s' % (ctype))
        print('PATH %s' % (rpath))
        print('ARGS %d' % (len(args)))
    if len(args):
        i = 0
        for key in sorted(args):
            logging.debug('ARG[%d] %s=%s' % (i, key, args[key]))
            i += 1
    self.send_response(200)  # OK
    self.send_header('Content-type', 'text/html')
    self.end_headers()
     # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server GET Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    self.wfile.write('    <p>Message received</p>')
    self.wfile.write('  </body>')
    self.wfile.write('</html>') 
    message = args['message']
    msisdn = args['msisdn']    
    url = 'http://192.168.2.204:12003/mtn/sms?from_addr=*904&&to_addr=%2B{0}&content={1}'.format(msisdn[0],message[0])
    r=requests.get('{0}'.format(url), verify=False)
    print(r.status_code)
    print(r.url)    
    #request = urllib2.Request(url) 
    #request.add_header('Accept-Encoding', 'utf-8')
    #response = urllib2.urlopen(request)
    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
    if r.status_code == 200 :
        print(r.status_code)
        #self.send_response(200)  # generic server error for now
        #self.send_header('Content-type', 'text/html')
        #self.end_headers()
        #response = requests.get(...)
        #json_data = json.loads(response.text)
        self.wfile.write('<html>')
        self.wfile.write('  <head>')
        self.wfile.write('    <title>RESPONSE</title>')
        self.wfile.write('  </head>')
        self.wfile.write('  <body>')
        self.wfile.write('    <p>Passed</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
    else:
        self.wfile.write('<html>')
        self.wfile.write('  <head>')
        self.wfile.write('    <title>Server Access Error</title>')
        self.wfile.write('  </head>')
        self.wfile.write('  <body>')
        self.wfile.write('    <p>Server access error.</p>')
        self.wfile.write('  </body>')   
        self.wfile.write('</html>')

def send_json(self):
    logging.info('GET %s' % (self.path))
    args = {}
    idx = self.path.find('?')
    if idx >= 0:
        rpath = self.path[:idx]
        args = cgi.parse_qs(self.path[idx+1:])
    else:
        rpath = self.path
    # Print out logging information about the path and args.
    if 'content-type' in self.headers:
        ctype, _ = cgi.parse_header(self.headers['content-type'])
        logging.debug('TYPE %s' % (ctype))
        logging.debug('PATH %s' % (rpath))
        logging.debug('ARGS %d' % (len(args)))
        print('TYPE %s' % (ctype))
        print('PATH %s' % (rpath))
        print('ARGS %d' % (len(args)))
    if len(args):
        i = 0
        for key in sorted(args):
            logging.debug('ARG[%d] %s=%s' % (i, key, args[key]))
            i += 1
    self.send_response(200)  # OK
    self.send_header('Content-type', 'text/html')
    self.end_headers()
     # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server GET Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    self.wfile.write('    <p>Message received</p>')
    self.wfile.write('  </body>')
    self.wfile.write('</html>') 
    url='http://192.168.2.203:3002/receive_json'
    data = {'key1':'val1','key2':'val2'}
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=data_json, headers=headers)
    #print(data_json)

    '''message = args['message']
    msisdn = args['msisdn']    
    url = 'http://192.168.2.204:12003/mtn/sms?from_addr=*904&&to_addr=%2B{0}&content={1}'.format(msisdn[0],message[0])
    r=requests.get('{0}'.format(url), verify=False)
    print(r.status_code)
    print(r.url)    
    #request = urllib2.Request(url) 
    #request.add_header('Accept-Encoding', 'utf-8')
    #response = urllib2.urlopen(request)
    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
    if r.status_code == 200 :
        print(r.status_code)
        #self.send_response(200)  # generic server error for now
        #self.send_header('Content-type', 'text/html')
        #self.end_headers()
        #response = requests.get(...)
        #json_data = json.loads(response.text)
        response = requests.get(...)
        data = response.json()
        self.wfile.write('<html>')
        self.wfile.write('  <head>')
        self.wfile.write('    <title>RESPONSE</title>')
        self.wfile.write('  </head>')
        self.wfile.write('  <body>')
        self.wfile.write('    <p>Passed</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
    else:
        self.wfile.write('<html>')
        self.wfile.write('  <head>')
        self.wfile.write('    <title>Server Access Error</title>')
        self.wfile.write('  </head>')
        self.wfile.write('  <body>')
        self.wfile.write('    <p>Server access error.</p>')
        self.wfile.write('  </body>')   
        self.wfile.write('</html>')'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
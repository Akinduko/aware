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
sys.path.insert(0, '/home/aakinduko/Downloads/python/modules')
from check import check
from info import info
def do_POST(self):
    '''
    Handle POST requests.
    '''
    logging.debug('POST %s' % (self.path))

     # CITATION: http://stackoverflow.com/questions/4233218/python-basehttprequesthandler-post-variables
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['content-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    
    msisdn = postvars['msisdn']
    message = postvars['message']
    print(msisdn[0])
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]

     # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    if len(postvars):
        i = 0
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
     # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('Content-type', 'text/html')
    self.end_headers()
     # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        # Write out the POST variables in 3 columns.

         #url = 'http://appzone.qrios.com/ussd/multi/menu/index.xml'
        #url = 'http://127.0.0.1/mtn/sms?from_addr=*904&to_addr=%2B{0}&content={1}'.format(msisdn[0],message[0])
        #r=requests.get('{0}'.format(url), verify=False)
        '''The 5 lines of code below curls a url and get its response in xml'''
        #request = urllib2.Request(url) 
        #request.add_header('Accept-Encoding', 'utf-8')
                 #response = urllib2.urlopen(request)
                 #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                 #print (repr(soup))
                 #print(r.status_code)
                 #print(r.url)
                 #self.wfile.write(r.status_code)
                 #self.wfile.write(r.url)
                 #self.send_response (tostring(E.results(E.Country(name='Germany',Code='DE',Storage='Basic',Status='Fresh',Type='Photo')), xml_declaration=True, encoding='UTF-8'))
        print (tostring(E.results(E.Country(name='Germany',Code='DE',Storage='Basic',Status='Fresh',Type='Photo')), xml_declaration=True, encoding='UTF-8'))
        self.wfile.write('    <p><a href="%s">Back</a></p>' % (back))
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        xml=tostring(E.results(E.Country(name='Germany',Code='DE',Storage='Basic',Status='Fresh',Type='Photo')), xml_declaration=True, encoding='UTF-16')
        self.wfile.write ('{0}'.format(xml))
 
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
def fbn_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/fbn.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)
def uba_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/uba.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)

def diamond_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/diamond.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)
def stanbic_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/stanbic.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)
def fcmb_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/fcmb.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)
def access_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/access.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)
def fidelity_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/fidelity.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)
def zenith_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/zenith.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)
def mtn_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/mtn.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)
def union_push(self):
    ctype, pdict = cgi.parse_header(self.headers['message-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(self.headers['message-length'])
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    message = postvars['message']
    print(message[0])
    # Get the "Back" link.
    back = self.path if self.path.find('?') < 0 else self.path[:self.path.find('?')]
    # Print out logging information about the path and args.
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (self.path))
    logging.debug('ARGS %d' % (len(postvars)))
    i=0
    if len(postvars):
        for key in (postvars):
            logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
            i += 1
    # Tell the browser everything is okay and that there is
    # HTML to display.
    self.send_response(200)  # OK
    self.send_header('message-type', 'text/html')
    self.end_headers()
    # Display the POST variables.
    self.wfile.write('<html>')
    self.wfile.write('  <head>')
    self.wfile.write('    <title>Server POST Response</title>')
    self.wfile.write('  </head>')
    self.wfile.write('  <body>')
    if len(postvars):
        self.wfile.write('    <p>Message received</p>')
        self.wfile.write('  </body>')
        self.wfile.write('</html>')
        n = 5
        with open('/home/python/txt/union.txt') as f:
             for lines in iter(lambda: tuple(islice(f, n)), ()):  
                #process(n_lines)
                id=(lines)
                num = [s.replace('\n','') for s in id]

                for msisdn in num:
                    url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message[0])
                    r=requests.get('{0}'.format(url), verify=False)
                    print(r.status_code)
                    print(r.url)
                    #request = urllib2.Request(url) 
                    #request.add_header('Accept-Encoding', 'utf-8')
                    #response = urllib2.urlopen(request)
                    #soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
                    if r.status_code == 200 :
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server POST Response</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Message sent</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message Sent')
                    else:
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                        print ('Message failed')
                if True:
                   time.sleep(5)

def receive_json(self):

    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
    else:
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print(postvars)
        #message=postvars.values()[0].keys()[0]
        print('success')
        #print "postvars['key1']: ", postvars[0]
        for key, value in postvars.items():
            strip=(postvars.items())[0]
            first=strip[0] + '"}'
            loadsms=json.loads(first)
            sms = loadsms['message']
            print sms
            second='{"nothing":"' + (strip[1])[0]
            loadstate=json.loads(second)
            state = loadstate['state']
            print state
            message='{0} Current state is:{1}'.format(sms,state)
            print message

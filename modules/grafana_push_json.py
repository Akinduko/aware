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
n=5
def mtn_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/mtn.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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
def zenith_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/zenith.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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
def diamond_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/diamond.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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
def fbn_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/fbn.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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

def access_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/access.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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
def union_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/union.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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
def uba_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/uba.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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

def fidelity_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/fidelity.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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
def qrios_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/qrios.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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
def stanbic_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/stanbic.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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
def fcmb_push_json(self):
    ctype, pdict = cgi.parse_header(self.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(self.rfile, pdict)
        print (postvars)
        #if content type is not form, do below
    else:
        #parse all variable json into postvars.
        postvars = cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])), keep_blank_values=1)
        print("HEADERS: ", self.headers)
        print (postvars)
        print('success')
        #parse postvars into string and save the needed contents for grafana
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

            #read msisdns for each bank stored in the path below
            with open('/home/sms/txt/fcmb.txt') as f:
                 for lines in iter(lambda: tuple(islice(f, n)), ()):  
                    id=(lines)
                    num = [s.replace('\n','') for s in id]
                    #for each sms send alert
                    for msisdn in num:
                        url = 'http://192.168.2.212:12302/push?service=simpleGeneral&subscriber={0}&message={1}'.format(msisdn,message)
                        r=requests.get('{0}'.format(url), verify=False)
                        print(r.status_code)
                        print(r.url)
                        #log message delivery status
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



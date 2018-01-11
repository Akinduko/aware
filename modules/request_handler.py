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
sys.path.insert(0, '/home/python/modules')
from grafana_sms import fbn_sms
from grafana_sms import zenith_sms
from grafana_sms import access_sms
from grafana_sms import union_sms
from grafana_sms import diamond_sms
from grafana_sms import uba_sms
from grafana_sms import fidelity_sms
from grafana_sms import fcmb_sms
from grafana_sms import stanbic_sms
from grafana_sms import mtn_sms
from grafana_push import fbn_push  
from grafana_push import zenith_push
from grafana_push import access_push
from grafana_push import union_push
from grafana_push import diamond_push
from grafana_push import uba_push
from grafana_push import fidelity_push
from grafana_push import fcmb_push
from grafana_push import stanbic_push
from grafana_push import mtn_push
from grafana_push import receive_json
from grafana_sms_json import fbn_sms_json
from grafana_sms_json import zenith_sms_json
from grafana_sms_json import access_sms_json
from grafana_sms_json import union_sms_json
from grafana_sms_json import diamond_sms_json
from grafana_sms_json import uba_sms_json
from grafana_sms_json import fidelity_sms_json
from grafana_sms_json import fcmb_sms_json
from grafana_sms_json import stanbic_sms_json
from grafana_sms_json import mtn_sms_json
from grafana_sms_json import qrios_sms_json
from grafana_push_json import fbn_push_json
from grafana_push_json import zenith_push_json
from grafana_push_json import access_push_json
from grafana_push_json import union_push_json
from grafana_push_json import diamond_push_json
from grafana_push_json import uba_push_json
from grafana_push_json import fidelity_push_json
from grafana_push_json import fcmb_push_json
from grafana_push_json import stanbic_push_json
from grafana_push_json import mtn_push_json
from grafana_push_json import qrios_push_json
from info import send_json
from info import live_agent
def make_request_handler_class(opts):
    '''
    Factory to make the request handler and add arguments to it.

    It exists to allow the handler to access the opts.path variable
    locally.
    '''
    class MyRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        '''
        Factory generated request handler class that contain
        additional class variables.
        '''
        m_opts = opts

        def do_HEAD(self):
            '''
            Handle a HEAD request.
            '''
            logging.debug('HEADER %s' % (self.path))
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_POST(self):
            '''
            Handle POST requests.
            '''
            logging.debug('POST %s' % (self.path))
            # Check to see whether the file is stored locally,
            # if it is, display it.
            # There is special handling for http://127.0.0.1/info. That URL
            # displays some internal information.
            posturl = self.path
            if posturl == '/fbn_sms' or posturl == '/fbn_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fbn_sms(self)
            elif posturl == '/access_sms' or posturl == '/access_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 access_sms(self)
            elif posturl == '/diamond_sms' or posturl == '/diamond_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 diamond_sms(self)
            elif posturl == '/union_sms' or posturl == '/union_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 union_sms(self)
            elif posturl == '/zenith_sms' or posturl == '/zenith_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 zenith_sms(self)
            elif posturl == '/fidelity_sms' or posturl == '/fidelity_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fidelity_sms(self)                 
            elif posturl == '/uba_sms' or posturl == '/uba_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 uba_sms(self)
            elif posturl == '/fcmb_sms' or posturl == '/fcmb_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fcmb_sms(self)
            elif posturl == '/stanbic_sms' or posturl == '/stanbic_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 stanbic_sms(self)
            elif posturl == '/mtn_sms' or posturl == '/mtn_sms/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 mtn_sms(self) 
            elif posturl == '/fbn_push' or posturl == '/fbn_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fbn_push(self)
            elif posturl == '/access_push' or posturl == '/access_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 access_push(self)
            elif posturl == '/diamond_push' or posturl == '/diamond_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 diamond_push(self)
            elif posturl == '/union_push' or posturl == '/union_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 union_push(self)
            elif posturl == '/zenith_push' or posturl == '/zenith_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 zenith_push(self)
            elif posturl == '/fidelity_push' or posturl == '/fidelity_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fidelity_push(self)                 
            elif posturl == '/uba_push' or posturl == '/uba_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 uba_push(self)
            elif posturl == '/fcmb_push' or posturl == '/fcmb_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fcmb_push(self)
            elif posturl == '/stanbic_push' or posturl == '/stanbic_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 stanbic_push(self)
            elif posturl == '/mtn_push' or posturl == '/mtn_push/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 mtn_push(self)                                  
            elif posturl == '/receive_json' or posturl == '/receive_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 receive_json(self)     
            elif posturl == '/fbn_sms_json' or posturl == '/fbn_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fbn_sms_json(self)
            elif posturl == '/access_sms_json' or posturl == '/access_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 access_sms_json(self)
            elif posturl == '/diamond_sms_json' or posturl == '/diamond_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 diamond_sms_json(self)
            elif posturl == '/union_sms_json' or posturl == '/union_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 union_sms_json(self)
            elif posturl == '/zenith_sms_json' or posturl == '/zenith_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 zenith_sms_json(self)
            elif posturl == '/fidelity_sms_json' or posturl == '/fidelity_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fidelity_sms_json(self)
            elif posturl == '/uba_sms_json' or posturl == '/uba_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 uba_sms_json(self)
            elif posturl == '/fcmb_sms_json' or posturl == '/fcmb_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fcmb_sms_json(self)
            elif posturl == '/stanbic_sms_json' or posturl == '/stanbic_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 stanbic_sms_json(self)
            elif posturl == '/mtn_sms_json' or posturl == '/mtn_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 mtn_sms_json(self)
            elif posturl == '/fbn_push_json' or posturl == '/fbn_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fbn_push_json(self)
            elif posturl == '/access_push_json' or posturl == '/access_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 access_push_json(self)
            elif posturl == '/diamond_push_json' or posturl == '/diamond_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 diamond_push_json(self)
            elif posturl == '/union_push_json' or posturl == '/union_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 union_push_json(self)
            elif posturl == '/zenith_push_json' or posturl == '/zenith_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 zenith_push_json(self)
            elif posturl == '/fidelity_push_json' or posturl == '/fidelity_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fidelity_push_json(self)
            elif posturl == '/uba_push_json' or posturl == '/uba_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 uba_push_json(self)
            elif posturl == '/fcmb_push_json' or posturl == '/fcmb_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 fcmb_push_json(self)
            elif posturl == '/stanbic_push_json' or posturl == '/stanbic_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 stanbic_push_json(self)
            elif posturl == '/mtn_push_json' or posturl == '/mtn_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 mtn_push_json(self)
            elif posturl == '/qrios_push_json' or posturl == '/qrios_push_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 qrios_push_json(self)
            elif posturl == '/qrios_sms_json' or posturl == '/qrios_sms_json/':
                 self.send_response(200)  # OK
                 self.send_header('Content-type', 'text/html')
                 self.end_headers()
                 qrios_sms_json(self)


            else:
                # Get the file path.
                path = MyRequestHandler.m_opts.rootdir + posturl
                dirpath = None
                logging.debug('FILE %s' % (path))

                # Allow the user to type "///" at the end to see the
                # directory listing.
                if os.path.exists(path) and os.path.isfile(path):
                    # This is valid file, send it as the response
                    # after determining whether it is a type that
                    # the server recognizes.
                    _, ext = os.path.splitext(path)
                    ext = ext.lower()
                    content_type = {
                        '.css': 'text/css',
                        '.gif': 'image/gif',
                        '.htm': 'text/html',
                        '.html': 'text/html',
                        '.jpeg': 'image/jpeg',
                        '.jpg': 'image/jpg',
                        '.js': 'text/javascript',
                        '.png': 'image/png',
                        '.text': 'text/plain',
                        '.txt': 'text/plain',
                    }

                    # If it is a known extension, set the correct
                    # content type in the response.
                    if ext in content_type:
                        self.send_response(200)  # OK
                        self.send_header('Content-type', content_type[ext])
                        self.end_headers()

                        with open(path) as ifp:
                            self.wfile.write(ifp.read())    
                    else:
                        # Unknown file type or a directory.
                        # Treat it as plain text.
                        self.send_response(200)  # OK
                        self.send_header('Content-type', 'text/plain')
                        self.end_headers()

                        with open(path) as ifp:
                            self.wfile.write(ifp.read())
                    

                else:
                    if dirpath is None or self.m_opts.no_dirlist == True:
                        # Invalid file path, respond with a server access error
                        self.send_response(500)  # generic server error for now
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()

                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('    <p>%r</p>' % (repr(self.path)))
                        self.wfile.write('    <p><a href="%s">Back</a></p>' % (rpath))
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                    
        def do_GET(self):
            '''
            Handle a GET request.
            '''
            logging.debug('GET %s' % (self.path))

            # Parse out the arguments.
            # The arguments follow a '?' in the URL. Here is an example:
            #   http://example.com?arg1=val1
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
            if len(args):
                i = 0
                for key in sorted(args):
                    logging.debug('ARG[%d] %s=%s' % (i, key, args[key]))
                    i += 1

            # Check to see whether the file is stored locally,
            # if it is, display it.
            # There is special handling for http://127.0.0.1/info. That URL
            # displays some internal information.
                # Get the file path.
            getpath = MyRequestHandler.m_opts.rootdir + rpath
            logging.debug('FILE %s' % (getpath))
            if rpath == '/info' or rpath == '/info/':
               self.send_response(200)  # OK
               self.send_header('Content-type', 'text/html')
               self.end_headers()
               live_agent(self)            
            elif rpath == '/send_json' or rpath == '/send_json/':
               self.send_response(200)  # OK
               self.send_header('Content-type', 'text/html')
               self.end_headers()
               send_json(self)            
            
            else:
                # Get the file path.
                path = MyRequestHandler.m_opts.rootdir + rpath
                dirpath = None
                logging.debug('FILE %s' % (path))

                # If it is a directory look for index.html
                # or process it directly if there are 3
                # trailing slashed.
                if rpath[-3:] == '///':
                    dirpath = path
                elif os.path.exists(path) and os.path.isdir(path):
                    dirpath = path  # the directory portion
                    index_files = ['/index.html', '/index.htm', ]
                    for index_file in index_files:
                        tmppath = path + index_file
                        if os.path.exists(tmppath):
                            path = tmppath
                            break

                # Allow the user to type "///" at the end to see the
                # directory listing.
                if os.path.exists(path) and os.path.isfile(path):
                    # This is valid file, send it as the response
                    # after determining whether it is a type that
                    # the server recognizes.
                    _, ext = os.path.splitext(path)
                    ext = ext.lower()
                    content_type = {
                        '.css': 'text/css',
                        '.gif': 'image/gif',
                        '.htm': 'text/html',
                        '.html': 'text/html',
                        '.jpeg': 'image/jpeg',
                        '.jpg': 'image/jpg',
                        '.js': 'text/javascript',
                        '.png': 'image/png',
                        '.text': 'text/plain',
                        '.txt': 'text/plain',
                    }

                    # If it is a known extension, set the correct
                    # content type in the response.
                    if ext in content_type:
                        self.send_response(200)  # OK
                        self.send_header('Content-type', content_type[ext])
                        self.end_headers()

                        with open(path) as ifp:
                            self.wfile.write(ifp.read())
                    else:
                        # Unknown file type or a directory.
                        # Treat it as plain text.
                        self.send_response(200)  # OK
                        self.send_header('Content-type', 'text/plain')
                        self.end_headers()

                        with open(path) as ifp:
                            self.wfile.write(ifp.read())
                else:
                    if dirpath is None or self.m_opts.no_dirlist == True:
                        # Invalid file path, respond with a server access error
                        self.send_response(500)  # generic server error for now
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()

                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>Server Access Error</title>')
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <p>Server access error.</p>')
                        self.wfile.write('    <p>%r</p>' % (repr(self.path)))
                        self.wfile.write('    <p>%r</p>' % (repr(rpath)))
                        self.wfile.write('    <p><a href="%s">Back</a></p>' % (rpath))
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')
                    else:
                        # List the directory contents. Allow simple navigation.
                        logging.debug('DIR %s' % (dirpath))

                        self.send_response(200)  # OK
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        
                        self.wfile.write('<html>')
                        self.wfile.write('  <head>')
                        self.wfile.write('    <title>%s</title>' % (dirpath))
                        self.wfile.write('  </head>')
                        self.wfile.write('  <body>')
                        self.wfile.write('    <a href="%s">Home</a><br>' % ('/'));

                        # Make the directory path navigable.
                        dirstr = ''
                        href = None
                        for seg in rpath.split('/'):
                            if href is None:
                                href = seg
                            else:
                                href = href + '/' + seg
                                dirstr += '/'
                            dirstr += '<a href="%s">%s</a>' % (href, seg)
                        self.wfile.write('    <p>Directory: %s</p>' % (dirstr))

                        # Write out the simple directory list (name and size).
                        self.wfile.write('    <table border="0">')
                        self.wfile.write('      <tbody>')
                        fnames = ['..']
                        fnames.extend(sorted(os.listdir(dirpath), key=str.lower))
                        for fname in fnames:
                            self.wfile.write('        <tr>')
                            self.wfile.write('          <td align="left">')
                            path = rpath + '/' + fname
                            fpath = os.path.join(dirpath, fname)
                            if os.path.isdir(path):
                                self.wfile.write('            <a href="%s">%s/</a>' % (path, fname))
                            else:
                                self.wfile.write('            <a href="%s">%s</a>' % (path, fname))
                            self.wfile.write('          <td>&nbsp;&nbsp;</td>')
                            self.wfile.write('          </td>')
                            self.wfile.write('          <td align="right">%d</td>' % (os.path.getsize(fpath)))
                            self.wfile.write('        </tr>')
                        self.wfile.write('      </tbody>')
                        self.wfile.write('    </table>')
                        self.wfile.write('  </body>')
                        self.wfile.write('</html>')

    return MyRequestHandler

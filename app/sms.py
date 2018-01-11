#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Simple web server that demonstrates how browser/server interactions
work for GET and POST requests. Use it as a starting point to create a
custom web server for handling specific requests but don't try to use
it for any production work.

You start by creating a simple index.html file in web directory
somewhere like you home directory: ~/www.

You then add an HTML file: ~/www/index.html. It can be very
simple. Something like this will do nicely:

   <!DOCTYPE html>
   <html>
     <head>
       <meta charset="utf-8">
       <title>WebServer Test</title>
     </head>
     <body>
       <p>Hello, world!</p>
     </body>
   </html>

At this point you have a basic web infrastructure with a single file
so you start the server and point to the ~/www root directory:

   $ webserver.py -r ~/www

This will start the web server listening on your localhost on port
8080. You can change both the host name and the port using the --host
and --port options. See the on-line help for more information (-h,
--help).

If you do not specify a root directory, it will use the directory that
you started the server from.

Now go to your browser and enter http://0.0.0.0:8080 on the command
line and you will see your page.

Try entering http://0.0.0.0:8080/info to see some server information.

You can also use http://127.0.0.1.

By default the server allows you to see directory listings if there is
no index.html or index.htm file. You can disable this by specifying
the --no-dirlist option.

If you want to see a directory listing of a directory that contains a
index.html or index.htm directory, type three trailing backslashes in
the URL like this: http://foo/bar/spam///. This will not work if the
--no-dirlist option is specified.

The default logging level is "info". You can change it using the
"--level" option.

The example below shows how to use a number of the switches to run a
server for host foobar on port 8080 with no directory listing
capability and very little output serving files from ~/www:

  $ hostname
  foobar
  $ webserver --host foobar --port 8080 --level warning --no-dirlist --rootdir ~/www

To daemonize a process, specify the -d or --daemonize option with a
process directory. That directory will contain the log (stdout), err
(stderr) and pid (process id) files for the daemon process. Here is an
example:

  $ hostname
  foobar
  $ webserver --host foobar --port 8080 --level warning --no-dirlist --rootdir ~/www --daemonize ~/www/logs
  $ ls ~/www/logs
  webserver-foobar-8080.err webserver-foobar-8080.log webserver-foobar-8080.pid
'''

# LICENSE
#   Copyright (c) 2015 Joe Linoff
#   
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#   
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#   
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.

# VERSIONS
#   1.0  initial release
#   1.1  replace req with self in request handler, add favicon
#   1.2  added directory listings, added --no-dirlist, fixed plain text displays, logging level control, daemonize
VERSION = '1.2'

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
from itertools import islice
from lxml.etree import tostring
from lxml.builder import E
sys.path.insert(0, '/home/sms/modules')
from request_handler import make_request_handler_class
from err import err
from get_logging_level import get_logging_level

def daemonize(opts):
    '''
    Daemonize this process.

    CITATION: http://stackoverflow.com/questions/115974/what-would-be-the-simplest-way-to-daemonize-a-python-script-in-linux
    '''
    if os.path.exists(opts.daemonize) is False:
        err('directory does not exist: ' + opts.daemonize)

    if os.path.isdir(opts.daemonize) is False:
        err('not a directory: ' + opts.daemonize)

    bname = 'sms-%d' % (opts.port)
    outfile = os.path.abspath(os.path.join(opts.daemonize, bname + '.log'))
    errfile = os.path.abspath(os.path.join(opts.daemonize, bname + '.err'))
    pidfile = os.path.abspath(os.path.join(opts.daemonize, bname + '.pid'))

    if os.path.exists(pidfile):
        err('pid file exists, cannot continue: ' + pidfile)
    if os.path.exists(outfile):
        os.unlink(outfile)
    if os.path.exists(errfile):
        os.unlink(errfile)

    if os.fork():
        sys.exit(0)  # exit the parent

    os.umask(0)
    os.setsid()
    if os.fork():
        sys.exit(0)  # exit the parent

    print('daemon pid %d' % (os.getpid()))

    sys.stdout.flush()
    sys.stderr.flush()

    stdin = file('/dev/null', 'r')
    stdout = file(outfile, 'a+')
    stderr = file(errfile, 'a+', 0)

    os.dup2(stdin.fileno(), sys.stdin.fileno())
    os.dup2(stdout.fileno(), sys.stdout.fileno())
    os.dup2(stderr.fileno(), sys.stderr.fileno())

    with open(pidfile, 'w') as ofp:
        ofp.write('%i' % (os.getpid()))


def httpd(opts):
    '''
    HTTP server
    '''
    RequestHandlerClass = make_request_handler_class(opts)
    server = BaseHTTPServer.HTTPServer((opts.host, opts.port), RequestHandlerClass)
    logging.info('Server starting %s:%s (level=%s)' % (opts.host, opts.port, opts.level))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    logging.info('Server stopping %s:%s' % (opts.host, opts.port))


def getopts():
    '''
    Get the command line options.
    '''

    # Get the help from the module documentation.
    this = os.path.basename(sys.argv[0])
    description = ('description:%s' % '\n  '.join(__doc__.split('\n')))
    epilog = ' '
    rawd = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=rawd,
                                     description=description,
                                     epilog=epilog)

    parser.add_argument('-d', '--daemonize',
                        action='store',
                        type=str,
                        default='.',
                        metavar='DIR',
                        help='daemonize this process, store the 3 run files (.log, .err, .pid) in DIR (default "%(default)s")')

    parser.add_argument('-H', '--host',
                        action='store',
                        type=str,
                        default='192.168.2.203',
                        help='hostname, default=%(default)s')

    parser.add_argument('-l', '--level',
                        action='store',
                        type=str,
                        default='info',
                        choices=['notset', 'debug', 'info', 'warning', 'error', 'critical',],
                        help='define the logging level, the default is %(default)s')

    parser.add_argument('--no-dirlist',
                        action='store_true',
                        help='disable directory listings')

    parser.add_argument('-p', '--port',
                        action='store',
                        type=int,
                        default=3003,
                        help='port, default=%(default)s')

    parser.add_argument('-r', '--rootdir',
                        action='store',
                        type=str,
                        default=os.path.abspath('.'),
                        help='web directory root that contains the HTML/CSS/JS files %(default)s')

    parser.add_argument('-v', '--verbose',
                        action='count',
                        help='level of verbosity')

    parser.add_argument('-V', '--version',
                        action='version',
                        version='%(prog)s - v' + VERSION)

    opts = parser.parse_args()
    opts.rootdir = os.path.abspath(opts.rootdir)
    if not os.path.isdir(opts.rootdir):
        err('Root directory does not exist: ' + opts.rootdir)
    if opts.port < 1 or opts.port > 65535:
        err('Port is out of range [1..65535]: %d' % (opts.port))
    return opts

def main():
    ''' main entry '''
    opts = getopts()
    if opts.daemonize:
        daemonize(opts)
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=get_logging_level(opts))
    httpd(opts)


if __name__ == '__main__':
    main()  # this allows library functionality

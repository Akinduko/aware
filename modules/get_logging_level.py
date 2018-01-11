VERSION = '1.2'
import argparse
import BaseHTTPServer
import cgi
import logging
import os
import sys
def get_logging_level(opts):
    '''
    Get the logging levels specified on the command line.
    The level can only be set once.
    '''
    if opts.level == 'notset':
        return logging.NOTSET
    elif opts.level == 'debug':
        return logging.DEBUG
    elif opts.level == 'info':
        return logging.INFO
    elif opts.level == 'warning':
        return logging.WARNING
    elif opts.level == 'error':
        return logging.ERROR
    elif opts.level == 'critical':
        return logging.CRITICAL
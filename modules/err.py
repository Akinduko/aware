import os
import sys

def err(msg):
    '''
    Report an error message and exit.
    '''
    print('ERROR: %s' % (msg))
    sys.exit(1)
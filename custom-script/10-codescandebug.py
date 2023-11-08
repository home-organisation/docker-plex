#!/usr/bin/python3
import sys
import os
import logging

###########################################################
# SET STATIC CONFIG
###########################################################
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

###########################################################
# INIT CONFIG
###########################################################
if __name__ == '__main__':
    TEST_USER = os.environ.get('TEST_USER')
    TEST_PASSWORD = os.environ.get('TEST_PASSWORD')
    if TEST_USER is None or TEST_PASSWORD is None:
        logging.warning("TEST_USER or TEST_PASSWORD with no value, nothing to do")
        sys.exit(0)


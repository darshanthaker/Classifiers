import sys
import os
import logging

logging_level = logging.DEBUG
log = logging.getLogger(__name__)
if not os.path.exists('../logs'):
    os.makedirs('../logs')
else:
    os.remove('../logs/linearregression.log')
logging.basicConfig(filename='../logs/linearregression.log', level=logging_level)

def main():

if __name__=="__main__":
    main()

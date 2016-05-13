import sys
import os
import logging
import pandas as pd
import numpy as np

REGRESSION_DIR = '../data/lin_regression'
logging_level = logging.DEBUG
log = logging.getLogger(__name__)
if not os.path.exists('../logs'):
    os.makedirs('../logs')
else:
    os.remove('../logs/linearregression.log')
logging.basicConfig(filename='../logs/linearregression.log', level=logging_level)

def read_data(file_name):
    f = open(file_name, 'r')
    for line in f:
        pass  

def main():
    if not os.path.exists(REGRESSION_DIR):
        log.error("Directory {} doesn't exist".format(REGRESSION_DIR))
    for file_name in os.listdir(REGRESSION_DIR):
        data_frame = read_data(file_name) 
        

if __name__=="__main__":
    main()

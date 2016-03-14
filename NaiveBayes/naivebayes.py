import sys
import os
import logging

SPAM_DIR = '../data/spam'
HAM_DIR = '../data/easy_ham'
TEST_DIR = '../data/test'
logging_level = logging.DEBUG
log = logging.getLogger(__name__)
if not os.path.exists('../logs'):
    os.makedirs('../logs')
logging.basicConfig(filename='../logs/naivebayes.log', level=logging_level)

def preprocessData(directory):
    log.debug("Preprocessing directory {}".format(directory))
    if not os.path.exists(directory):
        log.error("Directory {} doesn't exist".format(directory))
        return

    for f in os.listdir(directory):
        print f

def main():
    preprocessData(SPAM_DIR)
    preprocessData(HAM_DIR)
    preprocessData(TEST_DIR)

if __name__ =="__main__":
    main()

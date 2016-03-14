#!/usr/bin/env python3
import sys
import os
import logging

SPAM_DIR = '../data/spam'
HAM_DIR = '../data/easy_ham'
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

    ignore_lines = ['From', 'Return-Path', 'Delivered-To', 'Received', 'Message-Id',
                    'To', 'Date', 'Content-Type', 'X-Spam', 'URL', 'Date']

    for file_name in os.listdir(directory):
        file_name = os.path.join(directory, file_name)
        f = open(file_name, 'r') 
        body = dict()
        # For simplification, ignore lines that do not parse through UnicodeDecode
        try:
            for line in f:
                # Remove trailing whitespaces
                line = line.rstrip(' ')
                # Check that line does not start with any word from ignore_lines
                # AND that line is nonempty
                if not any([line.startswith(i) for i in ignore_lines]) and \
                   line != "\n":
                    # Convert to bag of words representation
                    stoplist = set(("for a an this under through are them with" +
                                "got we that be as our have your of what is his" + 
                                "her on at and or to in not aren't when \r \n \t") \
                                .split())
                    bow = [word for word in line.lower().split() if word not in stoplist]
                    for word in bow:
                        if word in body:
                            body[word] += 1
                        else:
                            body[word] = 1
        except UnicodeDecodeError:
            pass

def main():
    preprocessData(SPAM_DIR)
    preprocessData(HAM_DIR)

if __name__ =="__main__":
    main()

#!/usr/bin/env python3
import sys
import os
import logging
import pandas as pd
import numpy as np

SPAM_DIR = '../data/spam'
HAM_DIR = '../data/easy_ham'
DATA_DIRS = [(HAM_DIR, 0), (SPAM_DIR, 1)]
logging_level = logging.DEBUG
log = logging.getLogger(__name__)
if not os.path.exists('../logs'):
    os.makedirs('../logs')
else:
    os.remove('../logs/naivebayes.log')
logging.basicConfig(filename='../logs/naivebayes.log', level=logging_level)

def preprocessData(directory, category):
    if not os.path.exists(directory):
        log.error("Directory {} doesn't exist".format(directory))
        return
    log.debug("Preprocessing directory {}".format(directory))

    data = pd.DataFrame()

    for file_name in os.listdir(directory):
        file_name = os.path.join(directory, file_name)
        tmp = pd.DataFrame([[file_name, category]], columns=['Name', 'Label'])
        data = data.append(tmp, ignore_index=True)
    return data

def train(train_set):
    log.debug("Training on the training set")
    ignore_lines = ['From', 'Return-Path', 'Delivered-To', 'Received', 'Message-Id',
                    'To', 'Date', 'Content-Type', 'X-Spam', 'URL', 'Date']

    log.debug("Creating training set vocabulary")
    vocab = dict()

    for file_name in train_set['Name']:
        f = open(file_name, 'r') 
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
                        if word in vocab:
                            vocab[word] += 1
                        else:
                            vocab[word] = 1
        except UnicodeDecodeError:
            #log.info("Found an UnicodeDecodeError...ignoring")
            pass

def split(dataset, TRAIN=0.8):
    index = int(TRAIN*len(dataset.index))
    log.debug("Length of dataset = {}".format(len(dataset.index)))
    log.debug("Splitting dataset on index {}".format(index))
    train = dataset.ix[0:index, :]
    test = dataset.ix[index:, :]
    return train, test

def main():
    dataset = pd.DataFrame()
    for (directory, category) in DATA_DIRS:
        data = preprocessData(directory, category)
        dataset = dataset.append(data, ignore_index=True)
    dataset = dataset.reindex(np.random.permutation(dataset.index))
    train_set, test_set = split(dataset)
    train(train_set)

if __name__ =="__main__":
    main()

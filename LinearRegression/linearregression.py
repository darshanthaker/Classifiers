#!/usr/bin/env python3
import sys
import argparse
import os
import logging
import numpy as np
from constants import REGRESSION_DIR, logging_level, log_filename


log = logging.getLogger(__name__)
if not os.path.exists('../logs'):
    os.makedirs('../logs')
elif os.path.exists('../logs/linearregression.log'):
    os.remove('../logs/linearregression.log')
logging.basicConfig(filename=log_filename, level=logging_level)

def read_data(file_name):
    xpoints = list()
    ypoints = list()
    file_path = os.path.join(REGRESSION_DIR, file_name)
    f = open(file_path, 'r')
    for line in f:
        x, y = map(float, line.rstrip().split())
        xpoints.append(x)
        ypoints.append(y)
    points = (xpoints, ypoints)
    return points

def fit_least_squares(points):
    xbar = np.mean(points[0])
    ybar = np.mean(points[1])
    transform_x = [x - xbar for x in points[0]]
    transform_y = [y - ybar for y in points[1]]
    b1 = np.dot(transform_x, transform_y)
    b0 = ybar - b1*xbar
    return b1, b0

def main(file_name):
    if not os.path.exists(REGRESSION_DIR):
        log.error("Directory {} doesn't exist".format(REGRESSION_DIR))
        return
    points = read_data(file_name) 
    b1, b0 = fit_least_squares(points)
    log.debug("Fitted slope (beta1hat) is {}".format(b1))
    log.debug("Fitted intercept (beta0hat) is {}".format(b0))
    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Linear Regression Argument Parser")
    parser.add_argument('file_name', type=str, help="File Name for DataFile")
    args = parser.parse_args()
    main(args.file_name)

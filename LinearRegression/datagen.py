#!/usr/bin/env python3
import argparse
import os
import sys
import random
from constants import REGRESSION_DIR


def main(file_name, num_points, x_range, y_range):
    if not os.path.exists(REGRESSION_DIR):
        os.makedirs(REGRESSION_DIR)
    file_path = os.path.join(REGRESSION_DIR, file_name)
    if os.path.exists(file_path):
        yn = input("File already exists! Do you wish to overwrite? [y/n]").lower()
        if yn != 'y':
            print("Aborting!")
            return
    file_handler = open(file_path, 'w')
    for i in range(num_points):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        file_handler.write("{} {}\n".format(x, y))

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="DataGen Argument Parser")
    parser.add_argument('file_name', type=str, help="File Name for DataFile")
    parser.add_argument('num_points', type=int, help="# of Data Points to Generate")
    parser.add_argument('x_low', type=float, help="X coordinates low range")
    parser.add_argument('x_high', type=float, help="X coordinates high range")
    parser.add_argument('y_low', type=float, help="Y coordinates low range")
    parser.add_argument('y_high', type=float, help="Y coordinates high range")
    args = parser.parse_args()
    main(args.file_name, args.num_points, (args.x_low, args.x_high), \
                                          (args.y_low, args.y_high))

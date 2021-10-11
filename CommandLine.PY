## My Sample Python  FIle in MASTER Branch ONly
#! /usr/bin/python
# Use dir(__builtins__) to get all List of Builot n errors

print ("command line aruemnt")
#execute like this => python clineExample2.py 10 20 wipro 25

print ("argv import from sys ")

from sys import argv

print ("total parameter given at command line : ",len(argv))
print ("total parameter given at command line : ",argv)
print ("total parameter given at command line : ",argv[0])
print ("total parameter given at command line : ",argv[1])
print ("total parameter given at command line : ",type(argv[1]))

print ("\n\n\nnow with sys import")

import sys

print ("total parameter given at command line : ",len(sys.argv))
print ("total parameter given at command line : ",sys.argv)
print ("total parameter given at command line : ",sys.argv[0])
print ("total parameter given at command line : ",sys.argv[1])
print ("total parameter given at command line : ",type(sys.argv[1]))


#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from urlparse import urlparse

for line in sys.stdin:
    data = line.strip().split()

    if len(data) == 10:
        ip_addr,identity,username, ts1, ts2, method, path_query_str,protocol,status,size = data
        ts = ts1+" "+ts2
        method =  method.replace('"','')
        protocol = protocol.replace('"','')
	path_query_str = path_query_str.replace("http://www.the-associates.co.uk","")
	path_query_str = urlparse(path_query_str)
        print "{0}\t{1}".format(path_query_str.path, 1)


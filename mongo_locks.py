#!/usr/bin/env python
import sys
from pymongo import MongoClient


def get_status(topic=None):
    mc = MongoClient()
    status = mc.local.command('serverStatus')
    return status[topic] if topic else status


# def get_config():
#     print "graph_title MongoDB network stats"
#     print "graph_args --base 1000"
#     # print "graph_args --base 1000 -l 0"
#     # print "graph_vlabel mb ${graph_period}"
#     print "graph_category MongoDB_WT"
#     print "graph_vlabel bytes in (-) / out (+) per ${graph_period}"
#
#     print "bytesIn.label In"
#     print "bytesIn.type COUNTER"
#     print "bytesIn.cdef 0,bytesIn,-"
#
#     print "bytesOut.label Out"
#     print "bytesOut.type COUNTER"
#
#     # print key + ".min 0"
#     # print key + ".max 500000"
#     # print key + ".draw LINE1"


def get_data():
    data = get_status("locks")
    print data
    # print "bytesIn.value " + str(data["bytesIn"])
    # print "bytesOut.value " + str(data["bytesOut"])


get_config() if sys.argv[-1] == "config" else get_data()

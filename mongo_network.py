#!/usr/bin/env python
import sys
from pymongo import MongoClient


def get_status(topic=None):
    mc = MongoClient()
    status = mc.local.command('serverStatus')
    return status[topic] if topic else status


def get_config():
    print "graph_title MongoDB network stats"
    print "graph_args --base 1000 --lower-limit 0"
    print "graph_category MongoDB"
    print "graph_vlabel bytes in (-) / out (+) per ${graph_period}"

    print "bytesOut.label Out"
    print "bytesOut.type COUNTER"
    print "bytesOut.draw AREA"

    print "bytesIn.label In"
    print "bytesIn.type COUNTER"
    print "bytesIn.draw LINE1"
    # print "bytesIn.cdef 0,bytesIn,-"


def get_data():
    data = get_status("network")
    print "bytesIn.value " + str(data["bytesIn"])
    print "bytesOut.value " + str(data["bytesOut"])


get_config() if sys.argv[-1] == "config" else get_data()

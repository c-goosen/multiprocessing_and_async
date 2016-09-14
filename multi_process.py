#!/usr/bin/env python

#title           :multi_process.py
#description     :Requests with async threads and multiprocess
#author          :Christo Goosen
#date            :20160914
#version         :0.1
#usage           :python multi_process.py
#notes           :
#python_version  :2.7.12
#==============================================================================
import unittest
import time
import requests
from multiprocessing import Pool, Manager, cpu_count
from functools import partial





def exec_async(x):
    r = requests.get("http://{}".format(x))
    return r.text

if __name__ == "__main__":
    print "CPU count"
    print (cpu_count() - 1)
    work_list = ["www.google.com", "www.news24.com", "www.ewn.co.za", "www.facebook.com"]
    ##############################
    # Start of Blocking code
    ##############################
    result_1 = []
    time1 = time.time()
    for x in work_list:
        r =requests.get("http://{}".format(x))
        result_1.append(r.text)
    time2 = time.time()
    print "\n\n Length of results {}".format(len(result_1))
    print 'code took %s ms' % ((time2 - time1) * 1000.0)

    ##############################
    # End of Blocking code
    ##############################

    ##############################
    # Start of non-Blocking code
    # This spawns child processes equal to cpu_count() - 1
    # So if you have a 4 core CPU, you will have 3 processes
    # Also function calls are done through p.map_async (async calls waiting for response)
    ##############################
    result_2 = []
    time1 = time.time()

    p = Pool(cpu_count() - 1)
    m = Manager()
    q = m.Queue()
    #e_async = partial(exec_async, work_list)
    #async_calls = p.map_async(e_async, work_list, callback=result_2.append)
    async_calls = p.map_async(exec_async, work_list)#, callback=result_2.append)

    while True:
        if async_calls.ready():
            break
        else:
            size = q.qsize()
            time.sleep(0.1)
    outputs = async_calls.get()

    time2 = time.time()
    print "\n\n Length of results {}".format(len(outputs))
    print 'Code took %s ms' % ((time2 - time1) * 1000.0)

#@timing
#non_blocking()
#blocking()


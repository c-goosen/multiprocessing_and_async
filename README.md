# multiprocessing_and_async
Repo created to document/work/learn the fundamentals of concurrency, multiprocessing and multithreading in python

Done: 
Multiprocessing requests

To do:
Multiprocessing paramiko
Gevent requests from scratch (not using grequests)
Geven with paramiko
Script choosing best multiprocessing vs threading based on cpu count & resources
Create a paramiko with multprocessing library


multiprocess.py
A script that spawns processes equal to cpu_count -1. Each process then async fires of requests and returns results to original process

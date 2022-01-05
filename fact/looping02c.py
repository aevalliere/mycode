#!/usr/bin/env python3

#open file read
with open("dnsservers.txt", "r") as dnsfile:
    #loop
    for svr in dnsfile:
        print(svr, end="")


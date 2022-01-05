#!/usr/bin/env python3

#Open file in read
dnsfile = open("dnsservers.txt", "r")
#create list of lines
dnslist = dnsfile.readlines()
#loop lines
for svr in dnslist:
    print(svr, end="")
#Close file
dnsfile.close()

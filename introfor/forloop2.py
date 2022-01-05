#!/usr/bin/env python3

# create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]

#loop across vendor list
for x in vendors:
    print("\nThe vendor is " + x, end="")
    if x not in approved_vendors:
        print("- NOT AN APPROVED VENDOR!", end="")
print("\nOUR loop has ended.")


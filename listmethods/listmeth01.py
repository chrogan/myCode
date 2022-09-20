#!/usr/bin/env python3

"""In this script we will be practicing working with LISTS"""


proto = ["ssh","http", "https"]
protoa = ["ssh", "http", "https"]

print(f"{proto} no change")
protoa.append("dns")

proto.append("dns")
print(proto)

proto2 = [22,80,443,53]

#practicing list.extend()
proto.extend(proto2)
print(f"{proto} with extending a list")

#practicing list.append()
protoa.append(proto2)
print(f"{protoa} with appending a list")

#practicing list.insert()
insert_list = ["hey Im the insert"]
proto.insert(2,insert_list)
print(proto)

#practing list.remove()
proto.remove(22)
print(proto)

#practicing list.pop([i])
protoa.pop()
print(protoa)


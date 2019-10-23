import pymongo
import random
import sys
import time

n = int(sys.argv[1])

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["db_stress_test"]

col = db["col_stress_test"]
col.remove({})
start_time = time.time()
for i in range(n):
    col.insert({'val1': random.randint(0, 100),'val2':random.randint(0, 100)})

print("--- %s insertion time in seconds" % (time.time() - start_time))
start_time = time.time()
resp =  col.find({"val1":{"$gt": -1}})
for i in resp:
   pass
print("--- %s search time in seconds" % (time.time() - start_time))
col.create_index([ ("val1", -1) ])
start_time = time.time()
resp =  col.find({"val1":{"$gt": -1}})
for i in resp:
   pass
print("--- %s search time with index in seconds" % (time.time() - start_time))
resp =  col.find({"val1":{"$gt": -1}} ,{"val1":1})
for i in resp:
    pass
print("--- %s search time with index for only val1 in seconds" % (time.time() - start_time))
col.remove({})
start_time = time.time()
for i in range(n):
    col.insert({'val1': random.randint(0, 100),'val2':random.randint(0, 100)})
print("--- %s insertion time with index in seconds" % (time.time() - start_time))

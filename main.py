import pymongo
import random
import sys
import time
from datetime import datetime

n = int(sys.argv[1])
num_test = int(sys.argv[2])

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["db_stress_test"]
col = db["col_stress_test"]
time_test = 0
for k in range(num_test):
    f = open("tests_file.txt", "a")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.write("------------------ test performed on  " +dt_string+" with "+str(n)+ " iterations ------------------"+'\n')
    col.delete_many({})
    col.drop_indexes()
    start_time = time.time()
    for i in range(n):
        col.insert_one({'val1': random.randint(0, 100),'val2':random.randint(0, 100)})
    time_test = (time.time() - start_time)
    print("--- %s insertion time in seconds" % time_test)
    f.write("--- %s insertion time in seconds" % time_test+ '\n')
    start_time = time.time()
    resp =  col.find({"val1":{"$gt": -1}})
    for i in resp:
        pass
    time_test = (time.time() - start_time)
    print("--- %s search time in seconds" % time_test)
    f.write("--- %s search time in seconds" % time_test+ '\n')
    col.create_index([ ("val1", -1) ])
    start_time = time.time()
    resp =  col.find({"val1":{"$gt": -1}})
    for i in resp:
        pass
    time_test = (time.time() - start_time)
    print("--- %s search time with index in seconds" % time_test)
    f.write("--- %s search time with index in seconds" % time_test+ '\n')
    resp =  col.find({"val1":{"$gt": -1}} ,{"val1":1})
    for i in resp:
        pass
    time_test = (time.time() - start_time)
    print("--- %s search time with index for only val1 in seconds" % time_test)
    f.write("--- %s search time with index for only val1 in seconds" % time_test+ '\n')
    col.delete_many({})
    start_time = time.time()
    for i in range(n):
        col.insert_one({'val1': random.randint(0, 100),'val2':random.randint(0, 100)})
    time_test = (time.time() - start_time)
    print("--- %s insertion time with index in seconds" % time_test)
    f.write("--- %s insertion time with index in seconds" % time_test+ '\n'),
f.close()


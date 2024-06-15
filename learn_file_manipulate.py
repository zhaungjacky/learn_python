import os
import json


with open("/home/zxl/dev/projects/python/learn_test/json.json",'r') as local_file:
    data = json.load(local_file)
    for x in data:
        print(type(x))

local_file.close()
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#   To delete an entire folder, use the os.rmdir() method:
os.rmdir("myfolder")
import os
from datetime import datetime



file_path = (os.path.join(os.getcwd(),"os.txt"))
print(os.path.dirname(file_path))
print(os.path.basename(file_path))

if os.path.exists(file_path):
    print("exists")

print(dir(datetime))

# print(file_path)
# with open(file_path,'r') as f:
#     lines = f.readline()
#     print(lines)
# os.chdir("/home/zxl/dev/projects/python")
# print(os.getcwd())

# for dirpath, dirnames, filenames in os.walk("/home/zxl/dev/projects/python"):
# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print(f"current dir path: {dirpath}")
#     print(f"current dirnames: {dirnames}")
#     print(f"current filenames: {dirnames}")
#     print("_______________________________________")
 
# mod_time = os.stat("os.txt").st_mtime


# print(os.getcwd())
# print(datetime.fromtimestamp(mod_time))
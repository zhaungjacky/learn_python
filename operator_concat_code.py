import os

new_file_name = "/home/zxl/dev/projects/python/learn_test/all_code.txt"

os.chdir("/home/zxl/dev/projects/python/learn_test")

for f in os.listdir():
    file_name,file_ext = os.path.splitext(f)
    # print(file_name)
    # print(file_ext)
  
    if file_ext == ".py" and file_name.startswith("learn"):
        print(f)
        data_size = 4096
        with open(new_file_name,"a") as new_code_file:
            with open(f) as source_file:
                new_code_file.write('\n')
                new_code_file.write(f)
                new_code_file.write('\n')
                file_data = source_file.read(data_size)
                while len(file_data) > 0:
                    new_code_file.write(file_data)
                    file_data = source_file.read(data_size)
                
                new_code_file.write('\n')
                new_code_file.write('\n')
                



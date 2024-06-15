
# f = open("os.txt",'r') 

# print(f.mode)

# f.close()

# with open("os.txt",'r') as f: # when finish code  automatic close the file
#     # f_content = f.readlines() # list
#     # f_content = f.readline() # each line

#     # for line in f_content:
#     #     print(line)
#     # print(f_content)
#     # for line in f:
#     #     print(line,end = " ")
#     size_to_read = 50

#     f_content = f.read(size_to_read)
#     f.seek(0)
#     while len(f_content) > 0:
#         print(f_content, end="*")
#         f_content = f.read(size_to_read)

    # f_content = f.read(100)
    # print(f_content,end = " ")
    # f_content = f.read(100)
    # print(f_content,end = " ")
    # f_content = f.read(100)
    # print(f_content,end = " ")
# print(f.closed)

# with open("test2.txt","a") as f:
#     f.seek(0)
#     f.write("hello + 1")

# with open("os.txt","r") as rf:
#     with open("test_copy.txt",'w') as wf:
#         for line in rf:
#             wf.write(line)

#binary mode
with open("issue.png",'rb') as rf:
    with open("issue_copy.png","wb") as wf:
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)
                  
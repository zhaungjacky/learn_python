import os

os.chdir("/home/zxl/dev/projects/python/learn_test/files")

for f in os.listdir():
    file_name,file_ext = os.path.splitext(f)
    category,name = file_name.split("_")
    fname,uid = name.split("-")
    uid = uid.strip().zfill(2)
    category = category.strip()
    fname = fname.strip()
    new_name = f"{uid}-{fname}-{category}{file_ext}"
    os.rename(f,new_name)
    # print(category)
    # print(fname)
    # print(uid)
    # print(file_ext)
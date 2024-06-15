import csv
import os

ori_csv_file = "/home/zxl/dev/projects/python/learn_test/assets/names.csv"

file_dir = os.path.dirname(ori_csv_file)
new_csv_file = os.path.join(file_dir,"new_names.csv")
# print(new_csv_file)


# with open(new_csv_file,"r") as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter="\t")
#     for line in csv_reader:
#         print(line)

with open(ori_csv_file,"r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # next(csv_reader)

    with open(new_csv_file,"w") as new_file:

        fields_names = ['first_name','last_name','email']
        # fields_names = ['first_name','last_name']

        csv_writer = csv.DictWriter(
            new_file,
            delimiter="\t",
            fieldnames=fields_names,
        )

        csv_writer.writeheader()

        for line in csv_reader:
            # del line['email']
            csv_writer.writerow(line)

    # with open(new_csv_file,"w") as new_file:
    #     csv_writer = csv.writer(new_file,delimiter="\t")

    #     for line in csv_reader:
    #         csv_writer.writerow(line)

# #     # csv_reader.__next__()
# #     for line in csv_reader:
# #         print(line[2])

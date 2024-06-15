import csv

csv_file = "/home/zxl/dev/projects/python/learn_test/assets/patrons.csv"

new_file = "/home/zxl/dev/projects/python/learn_test/assets/new_patrons.csv"

html_output=""
names=[]

with open(csv_file,"r") as data_file:
    # csv_data = csv.reader(data_file)
    csv_data = csv.DictReader(data_file,delimiter=",")

    next(csv_data) # do not want the first line
    # next(csv_data) # do not want the second line
    # print(list(csv_data))
    # field_names = ["FirstName","LastName"]
    for line in csv_data:
        if line["FirstName"] == "No Reward":
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

    # with open(new_file,"w") as new_csv:
    #     pass 

html_output += f'<p>There are currently {len(names)} public contributors. Thank you</p>'
html_output  += "\n<ul>"
for name in names:
    html_output += f"\n\t<li>{name}<\li>"
html_output  += "\n</ul>"
# for name in names:
#     print(name)

print(html_output)
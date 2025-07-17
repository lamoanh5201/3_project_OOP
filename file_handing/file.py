# import csv
# #open and read file
# f = open("example.txt", "r", encoding="utf-8")
# content = f.readlines()
# print(content)
# f.close()


# # Small test for u
# # Creat a file hello.txt and then write 2 lines:
# # Hello Oanh!
# # Welcome to file handling in Python.
# # Read the file hello.txt content and then print 

# f = open("hello.txt", "w")
# f.write("Hello Oanh!\n")
# f.write("Welcome to file handling in Python.")
# f.close()

# f1 = open("hello.txt", "r", encoding="utf-8")
# content1 = f1.read()
# f1.close()
# print(content1)

# with open("log.txt", "a", encoding = "utf-8") as f:
#     f.write("\nWow Iam so beautiful")
    
# with open("log.txt", "r", encoding = "utf-8") as f:
#     content2 = f.read()
#     print(content2)

# with open("log.txt", "r", encoding = "utf8") as f:
#     list_line = f.readlines()
#     print(" The number of line in log file: ", len(list_line))
#     for i in range(len(list_line)):
#         print("Dòng", i + 1, " : ", list_line[i].strip())

# with open("my_friends.csv", "r", newline = '', encoding = "utf8") as f: #
#     content3 = csv.reader(f)
#     for row in content3:
#      print(row)


# with open("my_friends.csv", "r", newline = '', encoding = "utf8") as f: #
#      content4 = csv.DictReader(f)     
#      for row in content4:
#         print (row["Name"], "is", row["Age"], "years old and loves", row["Hobby"] )


# import csv
# data = [
#     {"Name": "Oanh", "Age": 22, "School": "HUST"},
#     {"Name": "Chung", "Age": 23, "School": "HUSTT"},
#     {"Name": "Dung", "Age": 23, "School": "HUST"}
# ]
# with open("my_best_friends.csv", "w", newline = '', encoding = "utf8") as f:
#     fiedname = ["Name", "Age", "School"]
#     content5 = csv.DictWriter(f, fieldnames = fiedname)
#     content5.writeheader()
#     content5.writerows(data)

# with open("my_best_friends.csv", "r", newline = '', encoding = "utf8") as f:
#     content6 = csv.reader(f)
#     for row in content6:
#         print(row)

# JSON

# import json

# data = {
#   "Name": "Oanh",
#   "Age": 22,
#   "School": "HUST",
#   "Skills": ["Python", "Machine Learning", "Testing"]
# }
# with open("oanh_profile.json", "w", encoding = "utf-8") as f:
#     json.dump(data, f, ensure_ascii = False, indent = 4)
#     #Oanh học ở HUST, 22 tuổi. Kỹ năng gồm: Python, Machine Learning, Testing.
# with open("oanh_profile.json", "r", encoding = "utf-8") as f:
#     content6 = json.load(f)
#     name = content6["Name"]
#     age = content6["Age"]
#     school = content6["School"]
#     skill = content6["Skills"]
#     skills = ", ".join(skill)
#     print(f"{name} học ở {school}, {age} tuổi. Kỹ năng gồm: {skills}.")

# from dotenv import load_dotenv
# import os

# with open(".env", "w", encoding = "utf-8") as f:
#     f.write("USERNAME=oanh\n")
#     f.write("PASSWORD=123456")

# load_dotenv()

# content7 = os.getenv("USERNAME")
# content8 = os.getenv("PASSWORD")
# print(f"{content7}\n{content8}")
    
#làm việc với .yaml
import yaml

training_config = {
        "training": {
            "batch_size": 64,
            "device": "cuda",
            "epochs": 20,
            "lr": 0.001,
            "model": "mobilenetv2"
        }
    }
with open ("my_training_config.yaml", "w", encoding = "utf-8") as f:
    yaml.dump(training_config, f)

with open ("my_training_config.yaml", "r", encoding = "utf-8") as f:
    content8 = yaml.safe_load(f)
    print(content8)
    epochs = content8["training"]["epochs"]
    batch_size = content8["training"]["batch_size"]
    lr = content8["training"]["lr"]
    print("ẽ huấn luyện mô hình mobilenetv2 trên cuda với:\n")
    print(f"Số epochs: {epochs}, Batch size: {batch_size}, Learning rate: {lr}")
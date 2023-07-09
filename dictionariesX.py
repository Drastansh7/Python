user_info = {"id": 5, "Name": "Drastansh", "Age": 20}

# print(user_info)
# print(user_info["Name"])

# for info in user_info:
#     print(info)
#
# for info in user_info.keys():
#     print(info)
#
# for info in user_info.values():
#     print(info)
#
# for info in user_info.items():
#     print(info)

# user_info["salary"] = "Rs 20000"
# print(user_info)
#
# user_info.update({"department": "computer science"})
# print(user_info)
#
# user_info.popitem()
# print(user_info)
#
# user_info.pop("Name")
# print(user_info)

# user_info.clear()
# print(user_info)

# print(user_info.get("Name"))

# dicty = user_info.copy()
# print(dicty)


student_info = {
                "id": [234,456,789],
    "Name": ["Rohan", "Rahul", "Arjun"],
    "Major": ["CS", "MechE", "BMS"],
    "Score": [
        {"Rohan": [98, 88, 78]},
        {"Rahul": [88, 68, 77]},
        {"Arjun": [89, 86, 98]},]
}

# count = student_info.get("Name").index("Arjun")
# count = 0
# for i in student_info.get("Name"):
#     if i == "Arjun":
#         break
#     count = count + 1
#
# print(count)
# print(student_info.get("Major")[count])

count = 0
for i in student_info.get("Name"):
    if i == "Arjun":
        break
    count += 1

print(student_info.get("Score")[count])

marks =student_info.get("Score")[count]
# print(sum(marks["Arjun"]))



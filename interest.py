# students = [{"student_name": "s4", "student_id": 24}, {"student_name": "S1", "student_id": 13},
#             {"student_name": "S2", "student_id": 19}, {"student_name": "S3", "student_id": 10}]
#
#
# def sort_dict(students):
#     for i in range(len(students)):
#         for j in range(i+1, len(students)):
#             if students[i]['student_id'] > students[j]['student_id']:
#                 students[i]['student_id'], students[j]['student_id'] = students[j]['student_id'], students[i]['student_id']
#     print(students)
#
# sort_dict(students)




output = [
["ate","eat","tea"],
["nat","tan"],
["stood","todos"],
["bat"],["hen"],
]
c1_dict = {}
input = ["eat", "tea", "tan", "stood", "ate", "nat", "bat", "todos", "hen"]

element_list, main_list = [], []


def check_ana(x, y):
    for data in x:
        if data in y:
            y.replace(data, "")
        else:
            return False
    return True


while input:
    x = input[0]
    main_list.append(x)
    for data in range(1, len(input)):
        ans = check_ana(x, input[data])
        if ans:
            main_list.append(input[data])
    for data in main_list:
        input.remove(data)
    element_list.append(main_list)
    main_list = []
print(element_list)










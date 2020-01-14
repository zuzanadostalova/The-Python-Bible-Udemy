# # 44. lesson - Dictionaries
# # advance data structures
# # if we want to study their student ID
# students = {
#         "Alice":["ID0001", 26, "A"],
#         "Bob":["ID0002", 27, "B"],
#         "Claire":["ID0003", 17, "C"],
#         "Dan":["ID0004", 21, "D"],
#         "Emma":["ID0005", 22, "E"]
#         }

# print(students)
# # Output: {'Alice': ['ID0001', 26, 'A'], 'Bob': ['ID0002', 27, 'B'], 
# # 'Claire': ['ID0003', 17, 'C'], 'Dan': ['ID0004', 21, 'D'], 'Emma': ['ID0005', 22, 'E']}

# print(students["Claire"])
# # Output: ['ID0003', 17, 'C']

# print(students["Claire"][0])
# # Output: ['ID0003']

# print(students["Dan"][1:])
# # Output: [21, 'D']

# # How to make it more clear?
# # Dictionary for each key

students = {
        "Alice":{"id":"ID0001", "age":26, "grade":"A"},
        "Bob":{"id":"ID0002", "age":27, "grade":"B"},
        "Claire":{"id":"ID0003", "age":17, "grade":"C"},
        "Dan":{"id":"ID0004", "age":21, "grade":"D"},
        "Emma":{"id":"ID0005", "age":22, "grade":"E"}
        }

print(students["Dan"]["age"])
# Output: 21

print(students["Emma"]["id"], students["Emma"]["grade"])
# Output: ID0005 E
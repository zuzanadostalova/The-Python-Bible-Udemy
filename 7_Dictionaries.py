# 43. lesson - What are dictionaries?
# symbol of squiggle brackets {}
# NameError: name 'Alice' is not defined...it is not a variable:
# error_students = {Alice:25, Bob:27}

# students = {}
students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":22}
print(students["Dan"])
# Output: 21
students["Fred"] = 25
print(students["Fred"])
# Output: 25...Fred was added to the dictionary

students["Alice"] = 26
print(students["Alice"])
# Alice's age was updated

# How to delete Fred? 
del students["Fred"]
# Going to delete the item with the key of Fred along with any assoc. values





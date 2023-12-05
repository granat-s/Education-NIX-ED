# # Equality operator
# a = 10
# b = 10

# print(a == b)
# print(id(a))
# print(id(b))

# c = a
# print(id(c))

list1 = []
list2 = []
list3 = list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:
    print("False")

# Создать функцию, которая принимает на вход два списка: первый — список,
#  который нужно очистить от определённых значений, второй — список тех
# значений, от которых нужно очистить. Например, list1 = [1, 2, 3, 4, 5],
# list2 = [1, 3, 4], функция должна вернуть [2, 5]

def exclude(list1, list2):
    output_list = []

    for num1 in list1:
        if num1 in list2:
            continue
        else:
            output_list.append(num1)

    return output_list


list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 4]

print(exclude(list1, list2))

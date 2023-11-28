# Дан список из строк. Используя join, соедините строки так, чтобы они были
# разделены через запятую.
# На выходе должна получиться строка в виде "my_string1,my_string2,my_string3"

def string_concatenation(*strings):
    return ",".join(strings)


string1 = "my_string1"
string2 = "my_string2"
string3 = "my_string3"

print(string_concatenation(string1, string2, string3))

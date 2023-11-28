# Дан список из строк. Создайте однострочное решение (при помощи list
# comprehension),
# которое приведёт к верхнему регистру все строки, содержащие слово 'price')

source_list = [
    "afsdfhuishfs",
    "price asdawd ",
    "fisjd ",
    "sdfkops ",
    "price",
    " divjsoi ",
    "ad w wd price",
    "price",
    "divjs disovj",
    "sodv8joe",
    "price",
    "riuvnuisevr",
]
output_list = []

# for line in source_list:
#     if "price" in line:
#         output_list.append(line.upper())
#     else:
#         output_list.append(line)

output_list = [line.upper() if "price" in line else line for line in
               source_list]

print(source_list)
print(output_list)

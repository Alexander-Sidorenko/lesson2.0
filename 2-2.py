count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < count:
    my_list.append(input("Введите следующий элемент списка "))
    i += 1

for el in range(int(len(my_list)/2)):
    my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
    el += 2
print(my_list)

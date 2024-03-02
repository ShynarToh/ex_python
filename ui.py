from loger import input_data, print_data, del_data

def interface():
    print("Привет! Это телефонный справочник \n 1 - запись данных \n 2 - удаление данных")
    comand = int(input())
    while comand !=1 and comand != 2 and comand !=3:
        print ("неправильный ввод")
        comand = int(input("введите число"))
    if comand ==1:
        input_data()
    elif comand == 2:
        print_data()
    elif comand==3:
        del_data()     
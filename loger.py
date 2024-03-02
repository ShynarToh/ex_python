from data_create import name_data, surname_data,  phone_data,adress_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"в каком формате записать данные \n\n"
                    f" вариант 1 \n"
                    f" {name}\n {surname}\n {phone}\n {adress}\n\n"
                    f" вариант 2 \n\n"
                    f" {name};{surname};{phone};{adress}\n"
                    f" Выберите вариантн: "))
    while var !=1 and var != 2:
        print ("неправильный ввод")
        var = int(input("введите число"))
    if var == 1:
        with open('data_1.csv', 'a', encoding ='utf-8') as f:
            f.write(f"{name}\n {surname}\n {phone}\n {adress}\n\n")
    if var == 2:
        with open('data_2.csv', 'a', encoding ='utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {adress}\n\n")

def print_data():
    print("Данные из 1 файла")
    with open('data_1.csv', 'r', encoding ='utf-8') as f:
        data_1 = f.readlines()
        data_1_list = []
        j =0
        for i in range (len(data_1)):
            if data_1[i] =='\n' or i == len(data_1)-1:
                data_1_list.append(''.join(data_1[j:i+1]))
                j=1
        print (''.join(data_1_list))
      
    print("Данные из 2 файла.\n")
    with open('data_2.csv', 'r', encoding ='utf-8') as f:           
        data_2= f.readlines()
        print(*data_2)
def del_data():
    print("Из какого файла удалить данные?: ")
    del_var=int(input("введите номер: "))
    while del_var !=1 and del_var != 2:
        print ("неправильный ввод")
        del_var = int(input("введите число"))
    if del_var == 1:
        with open('data_1.csv', 'r', encoding ='utf-8') as f:
            del_data_1=f.readlines()
            print (del_data_1)

            index_del= int(input("введите номер строки: "))-1
            data_line = []
            for line in del_data_1:
                line = line.split("\n")[0]
                data_line.append(line) 
            del_data_line= data_line[index_del]
            data_line.pop(index_del)
            print(f"удаленная запись: {del_data_line}")
        with open('data_1.csv', 'w', encoding ='utf-8') as f:
            f.write("\n".join(str(x) for x in data_line))
    elif del_var == 2:
        with open('data_2.csv', 'r', encoding ='utf-8') as f:
            del_data_2=f.readlines()
            print (del_data_2)

            index_del= int(input("введите номер строки: "))-1
            data_line = []
            for line in del_data_2:
                line = line.split("\n")[0]
                data_line.append(line) 
            data_line=del_data_2[index_del].split(";")
            del_data_line= data_line[index_del]
            data_line.pop(index_del)
            print(f"удаленная запись: {del_data_line}")
        with open('data_2.csv', 'w', encoding ='utf-8') as f:
            f.write("\n".join(str(x) for x in data_line))    
  
input_data()
print_data()
del_data()

    

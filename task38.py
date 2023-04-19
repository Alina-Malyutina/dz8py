def writing_person():
    lastname = input('Enter lastname: ')
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    phone_number = input('Enter phone_number: ')
    data = open("Phonebook.txt", "a", encoding = "utf=8")
    data.writelines(f'{lastname}\t{name}\t{surname}\t{phone_number}\n')
    data.close()

def search():
    lookfor = input('Enter data of person: ')
    bool1 = False
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if lookfor in line:
                print(line)
                bool_1 = True
            if bool_1 == False:
                print('There is not any records')
                
def printing():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        data_new = data.read()
        print(data_new)  

def load():
    new_phonebook = input('Enter link: ')
    with open(new_phonebook, 'r', encoding='utf-8') as data:
        with open('phonebook.txt', 'a+', encoding='utf-8') as data_1:
            data_1.write("\n")
            for line in data:
                if line not in data_1:
                    data_1.write(line)

def delete():
    text = input('Enter data that need to delete: ')
    with open("phonebook.txt", "r", encoding="utf8" ) as data:
        lines = data.readlines()
        with open("phonebook.txt", "w", encoding="utf8" ) as data_1:
            for line in lines:
                if text not in line:
                    data_1.write(line)

def change():
    text = input('Enter data that need to change: ')
    with open("phonebook.txt", "r", encoding="utf8" ) as data:
        lines = data.readlines()
        with open("phonebook.txt", "w", encoding="utf8" ) as data_1:
            for line in lines:
                if text not in line:
                    data_1.write(line)
                else:
                    ask = int(input('That you want to change? (1 - lastname, 2 - name, 3 - surname, 4 - phone number): '))
                    new_data = input('Enter new data:')
                    line_list = line.split()
                    line_list[int(ask)-1] = new_data
                    data_1.write("\t".join(line_list)+"\n")



ask = int(input('1 - add, 2 - search, 3 - print, 4 - load tp file, 5 - delete, 6 - change: '))
if ask == 1:
    writing_person()
elif ask == 2:
    search()
elif ask == 3:
    printing()
elif ask == 4:
    load()
elif ask == 5:
    delete()
elif ask == 6:
    change()
else:
    print('Something is uncorrect')
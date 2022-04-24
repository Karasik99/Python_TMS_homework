import json
import re
import csv

def task1(byte_code):
    byte_code_utf_8 = byte_code.decode('UTF-8')
    print(byte_code_utf_8)
    byte_code_latin_1 = byte_code_utf_8.encode('Latin1')
    print(byte_code_latin_1)
    byte_code_utf_8 = byte_code_latin_1.decode('iso-8859-1').encode('utf-8').decode('UTF-8')
    print(byte_code_utf_8)


def task2():
    str1 = input('Input 1 string: ')
    str2 = input('Input 2 string: ')
    str3 = input('Input 3 string: ')
    str4 = input('Input 4 string: ')
    with open('print.txt', 'w') as file:
        file.writelines(str1 + '\n')
        file.writelines(str2 + '\n')
        file.close()
    with open('print.txt', 'a') as file:
        file.write(str3 + '\n')
        file.write(str4 + '\n')


def task3():
    """Write in json"""
    id = input('\nInput 6 digits for id: ')
    try:
        x = [int(i) for i in id]
        id_is_correct = (len(id) == 6 and x)
        if not id_is_correct: raise 
    except:
        print('\nIncorrect ID')
    if id_is_correct:
        name = input('\nInput your name: ')
        phone = input('\nInput your phone: ')
        user_data = ('"'+id+'": [{"name": "' + name + '",' +
                                        '"phone": "' + phone + '"}]}')
        try:
            with open('persons.json', 'r') as read_persons:
                read_data = json.load(read_persons)
                read_persons.close()
                if len(read_data) >= 1:
                    result = json.dumps(read_data)
                    result = re.sub(r'}$', ',', result)
                with open('persons.json', 'w', encoding='utf-8') as persons:
                    json.dump(json.loads(result + user_data), persons, 
                              ensure_ascii=False, indent=4)
        except:
            with open('persons.json', 'w', encoding='utf-8') as persons:
                json.dump(json.loads('{'+user_data), persons, ensure_ascii=False, 
                                                                        indent=4)

def task4(file):
    """Json to CSV"""
    if '.json' not in file: 
        file_name = file + '.json'
    else: 
        file_name = file
        file = file[:-4]
    try:
        with open(file_name, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            with open(file + '.csv', 'w', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                # print(type(json_data))
                writer.writerows(json_data.values())
    except FileNotFoundError:
        print('Проверь файл, парень, его нет, ты карты дома забыл')
        
        
if __name__ == '__main__':
    while(True):
        input_user = input('\nPrint "s" for stop the program.\nInput number of task: ')
        if input_user == '1':
            task1(b'r\xc3\xa9sum\xc3\xa9')
        elif input_user == '2':
            task2()
        elif input_user == '3':
            task3()  
        elif input_user == '4':
            task4('persons')
        # elif input_user == '5':
        #     task5()    
        elif input_user == 's':
            break
        else:
            print('\nIncorrect input. Please, try again.')
    
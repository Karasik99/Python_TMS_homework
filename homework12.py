# Написать программу которая будет выводить ингредиенты бургера с помощью декораторов
# Ингредиенты: булка, салат, помидоры (каждый ингредиент добавляется с помощью декоратора)
# Декорируемая(основная) функция принимает в аргументы основной ингредиент (котлета, ветчина и тд) и выводит его



from functools import reduce


def tomatos(func):
    def wrapper():
        res = func()
        print('помидоры')

        return res
    
    return wrapper 




def bread(func):
    def wrapper():
        res = func()
        print('булка')

        return res
    
    return wrapper     


def salt(func):
    def wrapper():
        res = func()
        print('салат')

        return res
    
    return wrapper 


@bread
@tomatos
@salt
def burger():
    return('')







# Написать декоратор который выводиt название декорируемой функции и ее аргументы


def decorator(func):
    def wrapper():
        result1 = ('The name of function is ' + func.__name__)
        return result1
    return wrapper




@decorator
def one():
    i = [x for x in range(1,100) if x % 2 ==0]
    return i






# Map, Filter, Reduce
# 1. Реализовать программу, которая принимает список из дробных чисел и округляет их до целого числа 

def okruglenie():
    c=[6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]

    map_object = map(lambda x: round(x), c)

    print(list(map_object))


# 2.Реализовать программу которая возвращает список из числе больше 80,
#  на основе переданного списка:scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]



def filter1():
   
    scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
    
    filter_object = filter(lambda x: x>=80 , scores)
    
    print(list(filter_object))



# 3. Реализовать программу которая ищет слова палиндромы из списка:
#  values = ["demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP"]
def palindrom():
    pass




# 4. Реализовать программу которая подсчитывает произведение чисел из списка:
#  values= [1, 2, 3, 4]

def reduce_1():
    
    values = [1,2,3,4]

    result = reduce(lambda x, y: x*y, values)

    print(result)
   
   
#    5. Реализовать программу которая возвращает большее число из списка values=[3, 5, 2, 4, 7, 1]

def filter_big():

    values=[3, 5, 2, 4, 7, 1]

    filter_object = filter(lambda x: x>=7 , values)

    print(list(filter_object))




# 6. Подсчитать количество слова капитан в списке 
# sentences = ['капитан джек воробей', 'капитан дальнего плавания', 'ваша лодка готова, капитан']

def kapitan():
    
    sentences = ['капитан джек воробей', 'капитан дальнего плавания', 'ваша лодка готова, капитан']
   
    filter_object =  filter(lambda y:  y == 'капитан' , sentences)

    print(list(filter_object))

'''Этот модуль был создан для решения нескольких задач:
1. Сделать класс
2. Сделать класс наследник
3. Переопределить метод родителя
4. *Перегрузить метод __init__
---------------------------------------------------------------------------
Для решения данных задач я создал несколько классов, 
Взятые мною классы хорошо подходит и сочетаются друг с другом'''

# 1.Создать класс
# В нашем случае, класс будет отображать сущность – автомобиль. 
# Атрибутами класса будут являться двигатель, подвеска, кузов, колеса. 
# Методами класса будет «открыть дверь»,
# а также «закачать порцию бензина из бензобака в двигатель». 
# Первые два метода доступны для выполнения другим классам (в частности, классу «Водитель»). 
# Последний описывает взаимодействия внутри класса и не доступен пользователю.


class Car: 
    car_atr = 'gas_station'

    def __init__(self, name, engine, suspension,body,wheels) -> None:
        self.engine = engine
        self.suspension = suspension
        self.body = body
        self.wheels = wheels
        self.name = name
        self.__repair
    
    def open(self):     
        print(f'open door in {self.name}')

    def refueling(self):     
        print(f'refueling {self.name} in  {self.car_atr}')
    
    def __repair(self):
        print(f'this method repair {self.name},{self.engine},{self.suspension}')


# 2.3.4 Сделать класс наследник
# Для решения этой задачи я взял базовые параметры присущие человеку,
# также в этих примерах я переопределил метод родителя и перезагрузил метод.

class Human:
    super_attr = 'blood'

    def __init__(self, age, height) -> None:
        self.age = age
        self.height = height
        self.__group_of_blood = '2'
    
    def greeting(self):
        print(f'Привет мне {self.age} рост мой  {self.height}')
    
    def read(self): 
        print('Я читаю')


class driver(Human):
    super_attr = 'drive'

    def __init__(self, age, height, driving,data) -> None:
        self.age = age
        self.height = height
        self.__group_of_blood = '2'
        self.drive = driving
        self.data = data
        
    @classmethod
    def fromfilename(cls, filename):
        data = open(filename).readlines()
        return cls(data)

    def greeting(self):
        print(f'Привет мне {self.age} рост мой  {self.height} теперь я умею {self.drive}')
    
    



if __name__ == '__main__':
    pass
    
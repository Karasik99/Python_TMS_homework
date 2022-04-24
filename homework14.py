# 1. Написать программу, которая будет имитировать работу автомобиля, с помощью классов
# Необходимо реализовать классы: 
# Engine (мотор), который будет принимать в себя тип мотора(v6, v8, v10), 
# каждый из этих типов имеет коэффициент разгона: v6-0.2, v8-0.4, v10-0.6, 
# лошадиные силы (любое значение), флаг отображающий присутствие турбины (True, False) 
# добавляющий дополнительный коэффициент разгона равный 0.8.
# Этот класс имеет один метод generate_power, который возвращает мощность
#  вырабатываемой мотором, по формуле: Лошадиные силы * коэффициент 
#  разгона мотора / коэффициент разгона от турбины (если он есть)
# Wheel (колесо), который принимает в себя диаметр (16-21, необходимо 
# сделать проверку на вхождение в этот диапазон) и вес колеса в кг. 
# Этот класс методов не имеет
# Car (машина), который принимает в себя объект мотора, 
# массив из объектов колес, если передано меньше 4 – выкидывать 
# ошибку(почитайте о raise Exception) и тип машины: легковая, джип и грузовая,
#  каждый из типов имеет свой вес в кг (легковая 1200, джип 1500,  грузовая 1800)
# Этот класс имеет следующие методы:
# start_engine, который заводит мотор
# move, который принимает в себя дистанцию на заезд в метрах и возвращает
#  время в секундах за которое эту дистанцию проедет автомобиль. Логика вычисления следующая:
#1. Если двигатель не заведен - выкидывать ошибку (почитайте о raise Exception)
#2. Форму вычисления времени: 
#(Вес автомобиля + вес колес) / мощность мотора (из метода generate_power) * длинна заезда
# 1. Написать программу, которая будет имитировать работу автомобиля, с помощью классов
# Необходимо реализовать классы: 
# Engine (мотор), который будет принимать в себя тип мотора(v6, v8, v10), 
# каждый из этих типов имеет коэффициент разгона: v6-0.2, v8-0.4, v10-0.6, 
# лошадиные силы (любое значение), флаг отображающий присутствие турбины (True, False) 
# добавляющий дополнительный коэффициент разгона равный 0.8.

from functools import reduce

class Engine:
    
    def __init__(self,type_engine,horse_power,turbine,started_engine): 
        self.started_engine = started_engine 
        self.type_engine = type_engine == ('v6') or ('v8') or ('v10')
        #коэффициенты разгона: v6-0.2, v8-0.4, v10-0.6.
        q = 0.2
        w = 0.4
        e = 0.6
        r = 0.8 #дополнительный коэффициент разгона

        if type_engine == 'v6':
            type_engine == q
            print(str(q)+ ' Разгон мотора')
        elif type_engine == 'v8':
            type_engine == w
            print(str(w) + ' Разгон мотора')
        elif type_engine == 'v10':
            type_engine == e
            print(str(e)+ ' Разгон мотора')
            
        self.type_engine == type_engine
        self.horse_power = print(str(horse_power) + ' Лошадиные силы')
        self.turbine = turbine == 'yes' or 'no'

        if turbine == 'yes':            
            print(True)
            print(str(r)+ ' Доп.Разгон')
        elif turbine == 'no':
            print(False)

        self.turbine == r

# Этот класс имеет один метод generate_power, который возвращает мощность
#  вырабатываемой мотором, по формуле: Лошадиные силы * коэффициент 
#  разгона мотора / коэффициент разгона от турбины 
    
    def generate_power(self,horse_power,type_engine,turbine):
        q1 = horse_power
        q2 = type_engine
        q3 = turbine
        reslt = q1*q2/q3
        print(str(reslt)+ ' Формула мощности')


# Wheel (колесо), который принимает в себя диаметр (16-21, необходимо 
# сделать проверку на вхождение в этот диапазон) и вес колеса в кг. 
# Этот класс методов не имеет

class Wheel:

    def __init__(self,diameter,weight_wheel):
        self.diameter = diameter

        if diameter >= 16 and  diameter<=21:
            print(f'diameter {self.diameter} checked successfully')
        else:
            print("don't enter")

        self.diameter = diameter
        self.weight_wheel = weight_wheel
        print(str(weight_wheel) + ' kg' + ' Масса колес')

            
# Car (машина), который принимает в себя класс мотора, 
# массив из объектов колес, если передано меньше 4 – выкидывать 
# ошибку(почитайте о raise Exception) и тип машины: легковая, джип и грузовая,
#  каждый из типов имеет свой вес в кг (легковая 1200, джип 1500,  грузовая 1800)


class Car(Engine, Wheel):

    def __init__(self, type_engine,horse_power,turbine,diameter,weight_wheel,
                                        number_of_wheels,type_of_auto) -> None:

        Engine.__init__(self,horse_power,type_engine,turbine,started_engine=False)
        Wheel.__init__(self,diameter,weight_wheel)
        
        self.number_of_wheels = number_of_wheels
        self.type_of_auto= type_of_auto 
        weight1 = 1200
        weight2 = 1500     # переменные масс
        weight3 = 1800
                                                    #здесь я бы лучше сделал все словорями 
                                                    #но я об этом только потом вспомнил)))) 
                                                    #так было бы и удобнее и проверка сразу же была б.
        if type_of_auto == 'легковая':
            print(weight1)
        elif type_of_auto == 'джип':
            print(weight2)
        elif type_of_auto == 'грузовая':
            print(weight3)
        else:
            print('This type not definded')
       
        self.list_wheels = [diameter,weight_wheel,number_of_wheels]
        result = reduce(lambda x, y: x+y, self.list_wheels)
        self.result = result
        print(str(result) + ' Cумма диаметра веса и кол-ва колес')

        if self.result >= 5:
            print('ok ')
        elif self.result <= 4:
            print("Oops!  That was no valid number.  Try again...")

# Этот класс имеет следующие методы:
# start_engine, который заводит мотор
# move, который принимает в себя дистанцию на заезд в метрах и возвращает
#  время в секундах за которое эту дистанцию проедет автомобиль. Логика вычисления следующая:
# 1. Если двигатель не заведен - выкидывать ошибку (почитайте о raise Exception)
# 2. Форму вычисления времени: 
# (Вес автомобиля + вес колес) / мощность мотора (из метода generate_power) * длинна заезда

    def start_engine(self):
        self.started_engine = True
        print('Мотор заведен')

    def move(self,weight,wheel,reslt,move):
        if not self.started_engine:
            raise NameError('EngineNotWorking')
        return (weight+wheel)/(reslt*move)
          

if __name__ == '__main__':
    honda = Car(1 ,'v8','yes',21,20,4,'грузовая')
    honda.start_engine()
    print(honda.move(2,2,3,4))
    
    
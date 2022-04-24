#  1. Реализовать класс пушки Gun. Он будет иметь два поля: калибр и длину ствола. 
# От калибра зависит урон, и, частично, способность к пробитию брони. От длины ствола – точность стрельбы.
# Помните, что для поражения цели должно произойти две вещи: попадание в цель и пробитие брони? Так вот,
# пушка будет отвечать за первую из них: попадание. Поэтому делаем булевый метод is_on_target, который 
# принимает случайную величину (dice (бросок кубика)) и возвращает результат: попали или нет: 
# ({длинна пушки) *{dice}) > 100;
from email.quoprimime import header_check
from random import randint, random


class Gun:
    
    def __init__(self,caliber,gun_length,) -> None:
        self.caliber = caliber
        self.gun_length = gun_length
        print(caliber)
        print(gun_length)
        # defolt_damage = 15

        # if caliber > 1 and caliber <= 10:
        #     rezult_damage = defolt_damage + 5
        # elif caliber >= 11 and caliber <= 21:
        #     rezult_damage = defolt_damage + 10
        # elif caliber >= 22 and caliber <= 35:
        #     rezult_damage = defolt_damage + 15
        # elif caliber >= 36 and caliber <= 45:
        #     rezult_damage = defolt_damage + 20
        
        # print(rezult_damage)
        # print(gun_length)
        
        # self.rezult_damage = rezult_damage

    def is_on_target(self):
        dice = randint(0,15)
        if self.gun_length*dice >=100:
            print('Попадание')
        elif self.gun_length*dice<= 99:
            print('Промах')


# 2.Реализовать классы снарядов. Конкретные типы снарядов будут наследниками класса прародитель Ammo.
#  Наследники могут просто наследовать методы родителя, но могут и быть переопределены, 
# то есть работать не так, как родительский метод. Но мы точно знаем, что любой снаряд должен 
# иметь ряд методов
# Класс Ammo имеет следующее поля: gun(каждый снаряд делается под конкретную пушку, 
# так что здесь стоит применить агрегацию), type (фугасный, кумулятивный, подкалиберный)
# Класс Ammo имеет базовые методы:
# get_demage, любой снаряд должен наносить урон.  Этот метод просто возвращает калибр пушки, 
# умноженный на три. В общем случае, урон снаряда зависит от калибра. Но этот метод 
# будет переопределяться в дочерних классах (помним, что снаряды, которые хорошо пробивают броню,
#  как правило наносят меньший «заброневой» урон)
# get_penetration, любой снаряд должен пробивать (или по крайней мере пытаться пробить) броню. 
# В общем случае способность пробивать броню также зависит от калибра (ну, и еще от многого
#  – начальной скорости, например, но мы не будем усложнять). Поэтому, метод возвращает калибр пушки. 
# То есть, грубо говоря, снаряд может пробить броню, равную по толщине своему калибру. 
# Этот метод не будет переопределяться в дочерних классах.


class Ammo():

    def __init__(self,gun,type) -> None:
        
        self.gun = gun == 1 or 2 or 3 
        if gun == 1:
            name_puska = 'модель пушки: A20'
        elif gun == 2:
            name_puska = 'модель пушки: A21 '
        elif gun == 3:
            name_puska = 'модель пушки: A24'
        print(name_puska)

        self.type = type  == 1 or 2 or 3       
        if type == 1:
            name_type = 'модель снаряда: фугасный'
        elif type == 2:
            name_type = 'модель снаряд: кумулятивный'
        elif type == 3:
            name_type = 'модель снаряда: подкалиберный'
        print(name_type)



# Класс Ammo имеет базовые методы:
# get_demage, любой снаряд должен наносить урон.  Этот метод просто возвращает калибр пушки, 
# умноженный на три. В общем случае, урон снаряда зависит от калибра. Но этот метод 
# будет переопределяться в дочерних классах (помним, что снаряды, которые хорошо пробивают броню,
#  как правило наносят меньший «заброневой» урон)
# get_penetration, любой снаряд должен пробивать (или по крайней мере пытаться пробить) броню. 
# В общем случае способность пробивать броню также зависит от калибра (ну, и еще от многого
#  – начальной скорости, например, но мы не будем усложнять). Поэтому, метод возвращает калибр пушки. 
# То есть, грубо говоря, снаряд может пробить броню, равную по толщине своему калибру. 
# Этот метод не будет переопределяться в дочерних классах.

    def get_demage(self,caliber):
        self.caliber = caliber
        defolt_uron = caliber * 3
        print(defolt_uron)
        

    def get_penetration(self,caliber):
        print(caliber)



# 3. Реализовать конкретный класс фугасных снарядов HEСartridge (все конкретные 
# классы снарядов наследуются от Ammo), фугасный (дефолтный урон) получаемый из метода get_damage 
# не как не изменяется
#


class HEСartridge(Ammo): #Фугасный снаряд.

    def __init__(self,type_voorysheniya):
    
        spisok2 = {1:'45 mm унитарный патрон УО-243',2:'45 mm унитарный патрон УБР-243',
        3:'45 mm учебный патрон'}
        self.type_voorysheniya = type_voorysheniya == 1 or 2 or 3

        if type_voorysheniya == 1:
            print(spisok2[1])  
        elif type_voorysheniya == 2:
            print(spisok2[2])
        elif type_voorysheniya == 3:
            print(spisok2[3])

#4. Реализовать класс HEATCartridge, кумулятивный (дефолтный урон х 0.6)
# необходимо переопределить метод get_demage – super().get_damage() * 0.6. Урона меньше, 
# но данного типа зарядов будет большая бронебойная способность


class HEATСartridge(Ammo): # Кумулятивный снаряд.

    def __init__(self,type_voorysheniya):
        
        spisok2 = {1:'125 mm кумулятивный патрон 3ВБК16',2:'125 mm кумулятивный патрон DM-12А1',
        3:'125 mm кумулятивный патрон 3ВБК18'}
        self.type_voorysheniya = type_voorysheniya == 1 or 2 or 3

        if type_voorysheniya == 1:
            print(spisok2[1])  
        elif type_voorysheniya == 2:
            print(spisok2[2])
        elif type_voorysheniya == 3:
            print(spisok2[3])

    def get_demage(self,caliber):
        self.caliber = caliber
        defolt_uron = (caliber * 3) * 0.6
        print(defolt_uron)
        
   
#5. Реализовать класс APCartridge, Подкалиберный (дефолтный урон х 0.3).
# необходимо переопределить метод get_demage – super().get_damage() * 0.3

class APCartridge(Ammo): # Подкалиберный снаряд.

    def __init__(self,type_voorysheniya):
    
        spisok2 = {1:'75/55 mm бронебойно-трассирующий снаряд НК',
        2:'75/55 mm бронебойно-трассирующий снаряд Srk'}
        self.type_voorysheniya = type_voorysheniya == 1 or 2 

        if type_voorysheniya == 1:
            print(spisok2[1])  
        elif type_voorysheniya == 2:
            print(spisok2[2])

    def get_demage(self,caliber):
        self.caliber = caliber
        defolt_uron = (caliber * 3) * 0.3
        print(defolt_uron)
        


# Итак, для снарядов мы применили и агрегацию (пушка в базовом классе), и наследование. 
# Создадим теперь броню для танка. Здесь применим только наследование. Любая броня имеет толщину. 
# Поэтому класс прародитель брони будет иметь поле thickness, и строковое поле type, которое будет 
# определятся при создании дочерних классов.
#     1. Реализовать класс прародитель брони Armour, который будет иметь два поля thickness 
# (толщина брони) и type(тип брони). Броня будет в нашей игре определять пробита они или нет. Поэтому,
#  у нее будет лишь один метод - is_penetrated, который будет переопределяться в дочерних классах, 
# в зависимости от типа брони.
# is_penetrated как аргумент принимает объект снаряда, который попал в нее и возвращает bool 
# значение (пробита броня или нет) по условию: {пробивная способность снаряда} > { толщина брони}

class Armour():
    def __init__(self,thickness,type_armour):
        self.thickness = thickness
        self.type = type_armour

    def is_penetrated(defolt_uron):
        if defolt_uron >= 15 and defolt_uron <= 20:
            print(True)


# 2. Реализовать конкретный класс брони HArmour (гомогенная) и переопределить в нем 
# метод is_penetrated , который будет вычислять пробита ли броня в зависимости от типа снаряда
#         a. Фугасный снаряд: {пробивная способность снаряда} > { толщина брони}*1.2
#         b. Кумулятивный: {пробивная способность снаряда} > { толщина брони}*1
#         c. Подкалиберный: {пробивная способность снаряда} > { толщина брони}*0.7



   



class KOff():
    def __init__(self,caliber,gun_length,gun,type,type_voorysheniya,thickness,type_armour) -> None:
        Gun.__init__(self,caliber,gun_length)
        Ammo.__init__(self,gun,type)
        HEСartridge.__init__(self,type_voorysheniya)
        HEATСartridge.__init__(self,type_voorysheniya)
        APCartridge.__init__(self,type_voorysheniya)
        Armour.__init__(self,thickness,type_armour)


        tunk1 = input


if __name__ == '__main__':
    gus = KOff(15,140,1,1,1,1,1)







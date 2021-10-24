print('Имеется 2 ведра, одно 3 литра другое 5 литров и неограниченное количество воды. \nПользователь может:\
 \n1. Набирать воду в любое ведро. \n2. Выливать воду из любого ведра. \n3. Переливать воду из одного ведра в другое.')
print('Команды: \nN5 - налить воду в 5 л ведро, \nN3 - налить воду в 3 л, \nV5 - Вылить воду из 5 л ведра, \nV3 - Вылить воду из 3 л ведра,\
 \nP5 - Перелить воду из 5 л ведра в 3 л, \nP3 - Перелить воду из 3 л ведра в 5 л \nExit - выход из программы')
Vedro_5 = 0
Vedro_3 = 0
i = 0
while Vedro_5 != 4:
    Vedro_5 = Vedro_5
    Vedro_3 = Vedro_3
    com = input('Введите команду: ')
    if com == "Exit":
        break
    if com == "N5":
        Vedro_5 += 5
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    elif com == "V5":
        Vedro_5 -= 5
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    elif com == "N3":
        Vedro_3 += 3
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    elif com == "V3":
        Vedro_3 -= 3
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    if com == "N3" and (Vedro_3 == 2):
        Vedro_3 += 1
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    if com == "V5" and (Vedro_5 == 2):
        Vedro_5 -= 2
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    if com == "P3" and (Vedro_3 == 3):
        Vedro_3 -= 3
        Vedro_5 += 3
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    elif com == "P3" and (Vedro_5 == 0) and (Vedro_3 == 2):
        Vedro_3 -= 2
        Vedro_5 += 2
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    if com == "P5" and (Vedro_5 == 2) and (Vedro_3 == 0):
        Vedro_5 -= 2
        Vedro_3 += 2
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    elif com == "P5" and (Vedro_5 == 5) and (Vedro_3 == 2):
        Vedro_5 -= 1
        Vedro_3 += 1
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    elif com == "P5" and (Vedro_5 == 5) and (Vedro_3 == 0):
        Vedro_5 -= 3
        Vedro_3 += 3
        print("В 5 л ведре:", Vedro_5)
        print("В 3 л ведре:", Vedro_3)
    if com != 'N5' and com != 'N3' and com != 'V5' and com != 'V3' and com != 'P5' and com != 'P3':
        print('Неверная команда.')
    if Vedro_5 < 0:
        Vedro_5 = 0
        print('В вёдрах не может быть отрицательного количества воды. Сейчас в ведре 0 л')
    elif Vedro_5 > 5:
        Vedro_5 = 5
        print('В вёдрах не может быть больше литров чем предусмотрено конструкцией. Сейчас в ведре 5 л')
    elif Vedro_3 < 0:
        Vedro_3 = 0
        print('В вёдрах не может быть отрицательного количества воды. Сейчас в ведре 0 л')
    elif Vedro_3 > 3:
        Vedro_3 = 3
        print('В вёдрах не может быть больше литров чем предусмотрено конструкцией. Сейчас в ведрах 3 л')
    elif (Vedro_5 == 4):
        print('Победа!!! Молодец!!!')

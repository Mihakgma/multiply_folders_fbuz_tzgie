#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os


def create_dirs(spisok_filialov):
    
    path = os.getcwd()  
    print ("Текущая рабочая директория %s" % path)
    for filial in spisok_filialov:
        
        try:
            os.mkdir(path+'/'+filial)
        except OSError:
            print (filial+'-'+"Создать директорию в: %s НЕ УДАЛОСЬ!" % path)
        else:
            print (filial+'-'+"Успешно создана директория в: %s " % path)

spisok_filialov = [
    "Анжеро-Судженский",
    "Белово",
    "Березовский",
    "Гурьевск",
    "Ленинск-Кузнецкий",
    "Мариинск",
    "Междуреченск",
    "Новокузнецк",
    "Осинники",
    "Прокопьевск",
    "Таштагол",
    "Юрга",
    "Промышленновский",
    "Яшкино",
    "ЖД_Новокузнецк"
]

menu_on = True

while menu_on:
    print("ШО ТРЭБА СРОБИТЬ?")
    print("ЧТО НЕОБХОДИМО СДЕЛАТЬ, ХОЗЯЙКА / ХОЗЯИН?")
    print("WHAT SHOULD I DO, MISTRESS / MASTER?")
    print()
    print("""
_____000010001____1001_____100811001______________
_____811001__1111110000__111__18110_______________
_____11_110000000080000011110011111_______________
_____011000001111000008001108111118_______________
_____10001_________1000000000111111_______________
______00_____________0000000000110________________
____100______________18______0000_________________
___0001______000_____11__11___0000________________
__00001______101_____01_100____0000_______________
__00000_____________11_________0000_______________
__1000000__________000_______1000_________________
_____10000001111000000000000001___________________
________80000000010001_10001___________1100000000_
_____________101_10000_8_________1000000000000000_
_____________1001100011001___10100000001111000001_
___________1811000000081100000001110000011111000__
_________1101110011___1081000000011100000111118___
________1100111_______100100100000111000000800____
________1101111________1011011000008110000000_____
_______101011181_______101100100000001110000______
_______11_0111001_____0011101_01000000008_________
_______11100111100___00111001_0018000001__________
_______100101111100110011100010000011_____________
________08_101_1__100111000001081_________________
____________1018000000081_________________________
_____________00100__00111_________________________
__________10111180__08110000_11111111_1___________
__1111111110000000__0000001111111111111111111111__
_____________1_______11___________________________
    """)
    print()
    
    print("\t"+"1 - РАЗМНОЖИТЬ ПУСТЫЕ ПАПКИ С НАЗВАНИЯМИ ФИЛИАЛОВ")
    print()
    print("\t"+"2 - РАЗМНОЖИТЬ ФАЙЛ ЭКСЕЛЬ С НАЗВАНИЯМИ ФИЛИАЛОВ")
    print()
    print("\t"+"X - ЗАКРЫТЬ")
    print()
    
    # ввод значения
    vvod = input()
        
    if vvod.lower() == 'x' or vvod.lower() == 'х':
        print()
        print((("\t")*3)+'ВСЕГО ХОРОШЕГО!')
        input()
        menu_on = False
    elif vvod.isdigit() and int(vvod) == 1:
        print("\t"+"\t"+"Вы выбрали раздел РАЗМНОЖИТЬ ПУСТЫЕ ПАПКИ С НАЗВАНИЯМИ ФИЛИАЛОВ")
        create_dirs(spisok_filialov)
        input()
    
    elif vvod.isdigit() and int(vvod) == 2:
        print("\t"+"\t"+"Вы выбрали раздел РАЗМНОЖИТЬ ФАЙЛ ЭКСЕЛЬ С НАЗВАНИЯМИ ФИЛИАЛОВ")
        print("Приношу свои извенения. На данный момент раздел находится в разработке...")
        print()
        print("""
_______0000000
______0_______00
_000000_0000____00000
0______0____00___0___00
0___0000______0___0____0
0__0____0______0________0_0000000
_0_0_____0_00__0_________0_______00
__00___00_0___0__000_____0_________0
___00____00000____0_0____0_________0
___0_000000000____0____00___0___0__0
___0____0000____00___00____0___0___0
___0_________000____0_0000_0__0___0
____00____000______0_00___0__0___0
______00_____000000__0_0_0_00___0
________00000___00000___00__0000
________0____000__________0___000
_________00000____________00_____0
_________0__0___________00_00_000
_________0_0___________0_00__00
________0__0_________00_0______0
_______0___0000000000_00________0
________000_0000000000__________0
_____________0__________________0
_____________0_______0000______0
______________0_____0____0____0
_______________0___0___000___0
___________00000__0___0___0_0
__________0____000____0____0
__________00___0_______0000
____________000
        """)
        input()
        
    else:
        print("Некорректный ввод")
        print("Пожалуйста, повторите ввод")
    
    

# Табакаев Михаил
# Mihail Tabakaev
# instagram tags: #tabakaev_mv # tmv_stats


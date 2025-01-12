import matplotlib.pyplot as plt
import numpy as np


def draw_gist(finger_dict_qwerty, finger_dict_zubachew, finger_dict_dictor, finger_dict_rusfan,\
        fine_dict_qwerty, fine_dict_zubachew, fine_dict_dictor, fine_dict_rusfan,\
        dig_com_qwertyl, dig_com_qwertyr, dig_com_zubachewl, dig_com_zubachewr, dig_com_dictorl, dig_com_dictorr, dig_com_rusfanl, dig_com_rusfanr,\
        One_hand_click_qwerty, One_hand_click_zubachew):

#############heads of row###################
#touches and fines
    fingers = [
        "Мизинец (левая)", "Безымянный (левая)", "Средний (левая)", 
        "Указательный (левая)", 
        "Указательный (правая)", "Средний (правая)", 
        "Безымянный (правая)", "Мизинец (правая)"]

#digrams for csv
    named_rows = ["Левая рука", "Правая рука"]

#digrams and threegrams for 1grams

###########values of rows###################
#touches     
    fing_qwerty_values = [finger_dict_qwerty[key] for key in ["lpin", "lb", "lmid", "lpoint", "rpoint", "rmid", "rb", "rpin"]]
    fing_zubachew_values = [finger_dict_zubachew[key] for key in ["lpin", "lb", "lmid", "lpoint", "rpoint", "rmid", "rb", "rpin"]]
    fing_dictor_values = [finger_dict_dictor[key] for key in ["lpin", "lb", "lmid", "lpoint", "rpoint", "rmid", "rb", "rpin"]]    
    fing_rusfan_values = [finger_dict_rusfan[key] for key in ["lpin", "lb", "lmid", "lpoint", "rpoint", "rmid", "rb", "rpin"]] 

#fines
    fine_qwerty_values = [fine_dict_qwerty[key] for key in ["lpin", "lb", "lmid", "lpoint", "rpoint", "rmid", "rb", "rpin"]]
    fine_zubachew_values = [fine_dict_zubachew[key] for key in ["lpin", "lb", "lmid", "lpoint", "rpoint", "rmid", "rb", "rpin"]]
    fine_dictor_values = [fine_dict_dictor[key] for key in ["lpin", "lb", "lmid", "lpoint", "rpoint", "rmid", "rb", "rpin"]]
    fine_rusfan_values = [fine_dict_rusfan[key] for key in ["lpin", "lb", "lmid", "lpoint", "rpoint", "rmid", "rb", "rpin"]]

#General digramm from sortchbukw.csv
    gen_dig_qwerty_values = [dig_com_qwertyl, dig_com_qwertyr]
    gen_dig_zubachew_values = [dig_com_zubachewl, dig_com_zubachewr]
    gen_dig_dictor_values = [dig_com_dictorl, dig_com_dictorr]
    gen_dig_rusfan_values = [dig_com_rusfanl, dig_com_rusfanr]

#Word two sym
    One_hand_click_qwerty_values = [value for _, value in One_hand_click_qwerty.items()]
    One_hand_click_zubachew_values = [value for _, value in One_hand_click_zubachew.items()]
    One_hand_click_two_sym = ["Левая рука", "Правая рука", "Левая рука удобные", "Правая рука удобные"]

# Создание фигуры с 2 подграфиками (2x1 сетка)
    fig1, axs1 = plt.subplots(1, 2, figsize=(18, 12))
    fig1.suptitle('Сравнение нагрузок и штрафов на пальцы', fontsize=16)
     
# Построение 2 графиков нагрузки и штрафов
#Fing
    for i, ax in enumerate(axs1.flatten()):
        x = np.arange(len(fingers))
        width = 0.4
    
        ax.barh(x + width / 1.5, fing_qwerty_values, width / 2, label='йцукен', color='#ffb3ba')
        ax.barh(x + width / 4, fing_zubachew_values, width / 2, label='zubachew', color='#c9c9ff')
        ax.barh(x - width / 4, fing_dictor_values, width / 2, label='dictor', color='#cccccc')
        ax.barh(x - width / 1.5, fing_rusfan_values, width / 2, label='русс-фон', color='#ffdddd')
     
        # Настройки графика
        ax.set_xlabel('Количество нажатий', fontsize=10)
        ax.set_title(f'Нагрузка на пальцы', fontsize=12)
        ax.set_yticks(x)
        ax.set_yticklabels(fingers, fontsize=8)
        ax.legend(fontsize=9)
        break

#Fine
    for i, ax in enumerate(axs1.flatten()):
        if i != 1:
            continue
     
        x = np.arange(len(fingers))
        width = 0.4

        ax.barh(x + width / 1.5, fine_qwerty_values, width / 2, label='йцукен', color='#ffb3ba')
        ax.barh(x + width / 4, fine_zubachew_values, width / 2, label='zubachew', color='#c9c9ff')
        ax.barh(x - width / 4, fine_dictor_values, width / 2, label='dictor', color='#cccccc')
        ax.barh(x - width / 1.5, fine_rusfan_values, width / 2, label='русс-фон', color='#ffdddd')

        # Настройки графика
        ax.set_xlabel('Количество нажатий', fontsize=10)
        ax.set_title(f'Штрафы на пальцы', fontsize=12)
        ax.set_yticks(x)
        ax.set_yticklabels(fingers, fontsize=8)
        ax.legend(fontsize=9)
        break

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('result/Two_graphics_touches_fines.png')  # Сохранение графиков
    plt.show()


#Создание фигуры с 2 подграфиками (2x1 сетка)
    fig2, axs2 = plt.subplots(1, 2, figsize=(18, 12))
    fig2.suptitle('Сравнение диграмм и триграмм', fontsize=16)

# Построение 2 графиков ... 

#Набор диграмм для разных расскалдок для файла sortchbukw.csv
    for i, ax in enumerate(axs2.flatten()):
    
        x = np.arange(len(named_rows))
        width = 0.4
    
        # Используем одинаковые данные для всех графиков в качестве примера
        ax.barh(x + width / 1.5, gen_dig_qwerty_values, width / 2, label='йцукен', color='#ffb3ba')
        ax.barh(x + width / 4, gen_dig_zubachew_values, width / 2, label='zubachew', color='#c9c9ff')
        ax.barh(x - width / 4, gen_dig_dictor_values, width / 2, label='dictor', color='#cccccc')
        ax.barh(x - width / 1.5, gen_dig_rusfan_values, width / 2, label='русс-фон', color='#ffdddd')
    
        # Настройки графика
        ax.set_xlabel('Количество нажатий', fontsize=10)
        ax.set_title(f'Набор диграмм для расскладок для файла sortchbukw', fontsize=12)
        ax.set_yticks(x)
        ax.set_yticklabels(named_rows, fontsize=8)
        ax.legend(fontsize=9)
        break

#Word two symbols just and comfortable
    for i, ax in enumerate(axs2.flatten()):
        if i != 1:
            continue

        x = np.arange(len(One_hand_click_two_sym))
        width = 0.4
    
        ax.barh(x + width / 2, One_hand_click_qwerty_values, width, label='йцукен', color='#ffb3ba')
        ax.barh(x - width / 2, One_hand_click_zubachew_values, width, label='zubachew', color='#c9c9ff')
    
        # Настройки графика
        ax.set_xlabel('Количество нажатий', fontsize=10)
        ax.set_title(f'Набор диграмм и триграмм для различных расскладок', fontsize=12)
        ax.set_yticks(x)
        ax.set_yticklabels(One_hand_click_two_sym, fontsize=8)
        ax.legend(fontsize=9)
        break

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('result/Two_graphics_genDig_simComfDigThrig.png')  # Сохранение графиков
    plt.show()


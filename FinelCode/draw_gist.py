""" Функция draw_gist принимает различные данные, связанные с анализом клавиатуры,
и подготавливает их для дальнейшего использования в функциях построения графиков.
Она преобразует данные из словарей в списки, что облегчает их использование при создании гистограмм."""
import matplotlib.pyplot as plt
import numpy as np


def draw_gist(finger_dict_qwerty, finger_dict_zubachew, finger_dict_dictor, finger_dict_rusfan,\
        fine_dict_qwerty, fine_dict_zubachew, fine_dict_dictor, fine_dict_rusfan,\
        dig_com_qwertyl, dig_com_qwertyr, dig_com_zubachewl, dig_com_zubachewr, dig_com_dictorl, dig_com_dictorr, dig_com_rusfanl, dig_com_rusfanr,\
        one_hand2_qwerty, one_hand2_zubachew, one_hand3_qwerty, one_hand3_zubachew):


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
#"qwerty2w_1Lhand": 0, "qwerty2w_1Rhand": 0, "qwerty2w_1LhandC": 0,"qwerty2w_1RhandC": 0
    Hands_digramm_threegramm = ["Левая рука диграмм", "Левая рука удобных диграмм", "Правая рука диграмм", "Правая рука удобных диграмм", "Левая рука триграмм", "Левая рука удобных триграмм", "Правая рука триграмм", "Правая рука удобных триграмм"]


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

#General and comdortable digramm and threegramm
    hand_qwerty_values = [one_hand2_qwerty["qwerty2w_1Lhand"], one_hand2_qwerty["qwerty2w_1LhandC"], one_hand2_qwerty["qwerty2w_1Rhand"], one_hand2_qwerty["qwerty2w_1RhandC"], one_hand3_qwerty["qwerty3w_1Lhand"], one_hand3_qwerty["qwerty3w_1LhandC"], one_hand3_qwerty["qwerty3w_1Rhand"], one_hand3_qwerty["qwerty3w_1RhandC"]]
    hand_zubachew_values = [one_hand2_zubachew["zubachew2w_1Lhand"], one_hand2_zubachew["zubachew2w_1LhandC"], one_hand2_zubachew["zubachew2w_1Rhand"], one_hand2_zubachew["zubachew2w_1RhandC"], one_hand3_zubachew["zubachew3w_1Lhand"], one_hand3_zubachew["zubachew3w_1LhandC"], one_hand3_zubachew["zubachew3w_1Rhand"], one_hand3_zubachew["zubachew3w_1RhandC"]]

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

        x = np.arange(len(Hands_digramm_threegramm))
        width = 0.4
    
        ax.barh(x + width / 2, hand_qwerty_values, width, label='йцукен', color='#ffb3ba')
        ax.barh(x - width / 2, hand_zubachew_values, width, label='zubachew', color='#c9c9ff')
    
        # Настройки графика
        ax.set_xlabel('Количество нажатий', fontsize=10)
        ax.set_title(f'Набор диграмм и триграмм для различных расскладок', fontsize=12)
        ax.set_yticks(x)
        ax.set_yticklabels(Hands_digramm_threegramm, fontsize=8)
        ax.legend(fontsize=9)
        break

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('result/Two_graphics_genDig_simComfDigThrig.png')  # Сохранение графиков
    plt.show()


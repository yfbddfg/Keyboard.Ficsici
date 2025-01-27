""" определяет несколько групп переменных, которые используются для подсчета
различных параметров, связанных с набором текста на клавиатуре.
1. Словари для подсчета нажатий пальцами
2. Словари для подсчета штрафов (fine) пальцев
3. Числовые значения для подсчета комфортных комбинаций двух символов
4. Словари для подсчета нажатий одной рукой (двухсимвольных и трехсимвольных комбинаций)"""
#Touches for fingers
finger_dict_qwerty = {"lpin": 0, "lb": 0, "lmid": 0, "lpoint": 0, "rpoint": 0, "rmid": 0, "rb": 0, "rpin": 0}
    
finger_dict_zubachew = {"lpin": 0, "lb": 0, "lmid": 0, "lpoint": 0, "rpoint": 0, "rmid": 0, "rb": 0, "rpin": 0}

finger_dict_dictor = {"lpin": 193774, "lb": 247191, "lmid": 304345, "lpoint": 746797, "rpoint": 616720, "rmid": 328810, "rb": 293453, "rpin": 286008}

finger_dict_rusfan = {"lpin": 445217, "lb": 337842, "lmid": 318340, "lpoint": 428458, "rpoint": 431212, "rmid": 356409, "rb": 499560, "rpin": 194889}


#Fine for fingers
fine_dict_qwerty = {"lpin": 0, "lb": 0, "lmid": 0, "lpoint": 0, "rpoint": 0, "rmid": 0, "rb": 0, "rpin": 0}

fine_dict_zubachew = {"lpin": 0, "lb": 0, "lmid": 0, "lpoint": 0, "rpoint": 0, "rmid": 0, "rb": 0, "rpin": 0}

fine_dict_dictor = {"lpin": 37355, "lb": 70118, "lmid": 91100, "lpoint": 530423, "rpoint": 554541, "rmid": 171236, "rb": 146445, "rpin": 237562}

fine_dict_rusfan = {"lpin": 179797, "lb": 189524, "lmid": 243470, "lpoint": 635825, "rpoint": 712212, "rmid": 269356, "rb": 372619, "rpin": 399899}


#Dig comfortable form sortchbukw.csv 
dig_com_qwertyl = 0
dig_com_qwertyr = 0
#
dig_com_zubachewl = 0
dig_com_zubachewr = 0
#
dig_com_dictorl = 36
dig_com_dictorr = 113
#
dig_com_rusfanl = 74
dig_com_rusfanr = 74


#One hand click
One_hand2_qwerty = {"qwerty2w_1Lhand": 0, "qwerty2w_1LhandC": 0, "qwerty2w_1Rhand": 0, "qwerty2w_1RhandC": 0}
One_hand2_zubachew = {"zubachew2w_1Lhand": 0, "zubachew2w_1LhandC": 0, "zubachew2w_1Rhand": 0, "zubachew2w_1RhandC": 0}
One_hand3_qwerty = {"qwerty3w_1Lhand": 0, "qwerty3w_1LhandC": 0, "qwerty3w_1Rhand": 0, "qwerty3w_1RhandC": 0}
One_hand3_zubachew = {"zubachew3w_1Lhand": 0, "zubachew3w_1LhandC": 0, "zubachew3w_1Rhand": 0, "zubachew3w_1RhandC": 0}


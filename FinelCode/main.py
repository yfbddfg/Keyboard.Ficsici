""" программа выполняет комплексный анализ текстовых данных с точки зрения эргономики клавиатуры.
Она читает данные из разных файлов, вызывает функции для подсчета различных метрик, связанных с
использованием пальцев, штрафов за использование определенных пальцев, комбинаций символов и т.д.,
и наконец, выводит результаты в виде текста и гистограмм."""
import data as d
import check_file as c_f 
import check_filecsv as c_f_csv
import write_count_fing as w_c_fing
import write_count_fine as w_c_fine
import write_count_dig_com as w_c_dc
import check_1hand_click2_qwerty as c2q
import check_1hand_click2_zubachew as c2z
import check_1h3_qwerty as c3q
import check_1h3_zubachew as c3z
import draw_gist as dg


if __name__ == "__main__":

############################The counting
    strs1 = c_f.check_file("books/voina-i-mir.txt")
    d.finger_dict_qwerty, d.finger_dict_zubachew = w_c_fing.write_count_fing(strs1, \
                            d.finger_dict_qwerty, d.finger_dict_zubachew)
#####################
    strs3 = strs1
    d.fine_dict_qwerty, d.fine_dict_zubachew = w_c_fine.write_count_fine(strs3, d.fine_dict_qwerty, d.fine_dict_zubachew)
#####################
    strs4 = c_f_csv.check_filecsv("books/sortchbukw.csv") 
    d.dig_com_qwertyl, d.dig_com_qwertyr, d.dig_com_zubachewl, d.dig_com_zubachewr  = w_c_dc.write_count_dig_com(strs4)
#####################
    strs5 = c_f.check_file("books/final_test.txt")
    d.One_hand2_qwerty["qwerty2w_1Lhand"], d.One_hand2_qwerty["qwerty2w_1Rhand"] = c2q.check_h2_qwerty(strs5)
    
    d.One_hand2_qwerty["qwerty2w_1LhandC"], d.One_hand2_qwerty["qwerty2w_1RhandC"] = c2q.check_h2_qwerty_com(strs5)

    d.One_hand2_zubachew["zubachew2w_1Lhand"], d.One_hand2_zubachew["zubachew2w_1Rhand"] = c2z.check_1hand_click2_zubachew(strs5)

    d.One_hand2_zubachew["zubachew2w_1LhandC"], d.One_hand2_zubachew["zubachew2w_1RhandC"] = c2z.check_1hand_click2_zubachew_comfortable(strs5)

    d.One_hand3_qwerty["qwerty3w_1Lhand"], d.One_hand3_qwerty["qwerty3w_1Rhand"] = c3q.check_h3_qwerty(strs5)
    
    d.One_hand3_qwerty["qwerty3w_1LhandC"], d.One_hand3_qwerty["qwerty3w_1RhandC"] = c3q.check_h3_qwerty_com(strs5)

    d.One_hand3_zubachew["zubachew3w_1Lhand"], d.One_hand3_zubachew["zubachew3w_1Rhand"] = c3z.check_h3_zubachew(strs5)
                                                                                                                                                
    d.One_hand3_zubachew["zubachew3w_1LhandC"], d.One_hand3_zubachew["zubachew3w_1RhandC"] = c3z.check_h3_zubachew_com(strs5)

#For touches fingers
    print("Touches")
    print("ЙЦУКЕН:", d.finger_dict_qwerty)
    print("Zubachew:", d.finger_dict_zubachew)
    print("Dictor:", d.finger_dict_dictor)
    print("Русский-фонетический:", d.finger_dict_rusfan)

#For fine fingers
    print("\nFines")
    print("ЙЦУКЕН:", d.fine_dict_qwerty)
    print("Zubachew:", d.fine_dict_zubachew)
    print("Dictor:", d.fine_dict_dictor)
    print("Русский-фонетический:", d.fine_dict_rusfan)

#For digramm
    print("\nDigrams comfortable in sortchbukw:")
    print("Digrams ЙЦУКЕН left hand:", d.dig_com_qwertyl)
    print("Digrams ЙЦУКЕН right hand:", d.dig_com_qwertyr)
    print("Digrams Zubachew left hand:", d.dig_com_zubachewl)
    print("Digrams Zubachew right hand:", d.dig_com_zubachewr)

#For click Digramm
    print("\ndigrams")
    print("ЙЦУКЕН:", d.One_hand2_qwerty)
    print("Zubachew:", d.One_hand2_zubachew)

#For click Threegramm
    print("\nThreegrams")
    print("ЙЦУКЕН:", d.One_hand3_qwerty)
    print("Zubachew:", d.One_hand3_zubachew)

    dg.draw_gist(d.finger_dict_qwerty, d.finger_dict_zubachew, d.finger_dict_dictor, d.finger_dict_rusfan,\
        d.fine_dict_qwerty, d.fine_dict_zubachew, d.fine_dict_dictor, d.fine_dict_rusfan,\
        d.dig_com_qwertyl, d.dig_com_qwertyr, d.dig_com_zubachewl, d.dig_com_zubachewr, d.dig_com_dictorl, d.dig_com_dictorr, d.dig_com_rusfanl, d.dig_com_rusfanr,\
        d.One_hand2_qwerty, d.One_hand2_zubachew, d.One_hand3_qwerty, d.One_hand3_zubachew)


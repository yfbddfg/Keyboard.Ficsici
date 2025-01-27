"""Функция предназначена для анализа текста и подсчета "штрафов"
за нажатие клавиш разными пальцами на двух разных раскладках клавиатуры:
    QWERTY и Zubachew."""
import check_fine as c_fine


def write_count_fine(strs, fine_dict_qwerty, fine_dict_zubachew):

    for ch in strs:
        presseddict1 = c_fine.check_fine_zubachew(ch)
        presseddict2 = c_fine.check_fine_qwerty(ch)

        for fingerkey in presseddict1:
            fine_dict_zubachew[fingerkey] += presseddict1[fingerkey]

        for fingerkey in presseddict2:
            fine_dict_qwerty[fingerkey] += presseddict2[fingerkey]
    return fine_dict_qwerty, fine_dict_zubachew


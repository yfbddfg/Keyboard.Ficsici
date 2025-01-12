import check_finger as c_fing


def write_count_fing(strs, finger_dict_qwerty, finger_dict_zubachew):

    for ch in strs:
        presseddict1 = c_fing.check_finger_zubachew(ch)
        presseddict2 = c_fing.check_finger_qwerty(ch)

        for fingerkey in presseddict1:
            finger_dict_zubachew[fingerkey] += presseddict1[fingerkey]

        for fingerkey in presseddict2:
            finger_dict_qwerty[fingerkey] += presseddict2[fingerkey]
    return finger_dict_qwerty, finger_dict_zubachew


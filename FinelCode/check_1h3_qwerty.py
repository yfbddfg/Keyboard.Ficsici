"""функции анализируют текстовую строку для подсчета сочетаний символов,
    которые набираются левой и правой рукой на QWERTY-клавиатуре."""
def check_h3_qwerty(strs):
    """считает любые комбинации трех символов, набранных одной рукой"""

    letterL = ['й','ф','я','1','!','ц','ы','ч','2','"','у','в','с','3','№','к','а','м','е','п','и','4','5',';','%',"'"]
    letterR = ['-','+','_','=','\\','|','.',',','з','ж','х','э','0',')','щ','д','ю','9','(','ш','л','б','8','*','н','р','т','г','о','ь','7','6','?',':','"']

    Two_1RightHand = 0
    Two_1LeftHand = 0

    for i in range(len(strs) - 2):
        symLowP = strs[i].lower()
        symLow = strs[i+1].lower()
        symLowN = strs[i+2].lower()
        if (symLowP in letterL) and (symLow in letterL) and (symLowN in letterL):
            Two_1LeftHand += 1
        if (symLowP in letterR) and (symLow in letterR) and (symLowN in letterR):
            Two_1RightHand += 1

    return Two_1LeftHand, Two_1RightHand

def check_h3_qwerty_com(strs):
"""учитывает более сложные "комфортные" комбинации"""

    letterL = ["йфя1!", 'цыч2"', "увс3№", "камепи45;%"]
    letterR = ["-+_=\\|.,зжхэ0)", "щдю9(", "шлб8*", "нртгоь76?:"]

    Two_1RightHandComf = 0
    Two_1LeftHandComf = 0

    for i in range(len(strs) - 2):
        symLowP = strs[i].lower()
        symLow = strs[i+1].lower()
        symLowN = strs[i+2].lower()
        if symLowP in letterL[0]:
            if symLow in letterL[1]:
                if (symLowN in letterL[2]) or (symLowN in letterL[3]):
                    Two_1LeftHandComf += 1
        if symLowP in letterL[1]:
            if symLow in letterL[2]:
                if symLowN in letterL[3]:
                    Two_1LeftHandComf += 1

        if symLowP in letterR[0]:
            if symLow in letterR[1]:
                if (symLowN in letterR[2]) or (symLowN in letterR[3]):
                    Two_1RightHandComf += 1
        if symLowP in letterR[1]:
            if symLow in letterR[2]:
                if symLowN in letterR[3]:
                    Two_1RightHandComf += 1
    
    return Two_1LeftHandComf, Two_1RightHandComf
"""Обе функции возвращают количество найденных сочетаний для левой и правой руки."""

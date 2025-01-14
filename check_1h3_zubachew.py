def check_h3_zubachew(strs):

    letterL = ['ф','г','ш','ё','1','!','ы','и','ь','ъ','2','"','а','е','ю','3','№','я','ъ','о','у','ь','э','4',';','5','%','.',',']
    letterR = ['щ', 'ц', 'ж', 'х', 'з', 'ч', '+', '=', '-', '_', '0', ')', '\\', '/', 'п', 'н', 'к', '9', '(', 'р', 'с', 'в', '8', '*', 'м', 'т', 'д', 'й', 'л', 'б', '7', '?', '6', ':']

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

def check_h3_zubachew_com(strs):

    letterL = ["фгшё1!", 'ыиьъ2"', "аею3№", "яъоуьэ4;5%.,"]
    letterR = ["щцжхзч+=-_0)\\/", "пнк9(", "рсв8*", "мтдйлб7?6:"]

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


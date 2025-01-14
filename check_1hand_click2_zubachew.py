def check_1hand_click2_zubachew(strs):

    letterL = ['ф','г','ш','ё','1','!','ы','и','ь','ъ','2','"','а','е','ю','3','№','я','ъ','о','у','ь','э','4',';','5','%','.',',']
    letterR = ['щ', 'ц', 'ж', 'х', 'з', 'ч', '+', '=', '-', '_', '0', ')', '\\', '/', 'п', 'н', 'к', '9', '(', 'р', 'с', 'в', '8', '*', 'м', 'т', 'д', 'й', 'л', 'б', '7', '?', '6', ':']
    Two_1RightHand = 0
    Two_1LeftHand = 0

    for i in range(len(strs) - 1):
        symLow = strs[i].lower()
        symLowN = strs[i+1].lower()
        if (symLow in letterL) and (symLowN in letterL):
            Two_1LeftHand += 1
        if (symLow in letterR) and (symLowN in letterR):
            Two_1RightHand += 1

    return Two_1LeftHand, Two_1RightHand

def check_1hand_click2_zubachew_comfortable(strs):

    letterL = ["фгшё1!", 'ыиьъ2"', "аею3№", "яъоуьэ4;5%.,"]
    letterR = ["щцжхзч+=-_0)\\/", "пнк9(", "рсв8*", "мтдйлб7?6:"]
    TwoWordL = []
    TwoWordR = []

    for i in range(len(letterL) - 1):
        sym1 = letterL[i]
        for sym11 in sym1:
            for j in range(i+1, len(letterL)):
                symp = letterL[j]
                for symp1 in symp:
                    word = sym11 + symp1
                    TwoWordL.append(word)

    for i in range(len(letterR) - 1):
        sym1 = letterR[i]
        for sym11 in sym1:
            for j in range(i+1, len(letterR)):
                symp = letterR[j]
                for symp1 in symp:
                    word = sym11 + symp1
                    TwoWordR.append(word)

    Two_1RightHandComf = 0
    Two_1LeftHandComf = 0

    for i in range(len(strs) - 1):
        symLow = strs[i].lower()
        symLowN = strs[i+1].lower()
        symTwo = symLow + symLowN
        if symTwo in TwoWordL:
            Two_1LeftHandComf += 1
        if symTwo in TwoWordR:
            Two_1RightHandComf += 1
    
    return Two_1LeftHandComf, Two_1RightHandComf


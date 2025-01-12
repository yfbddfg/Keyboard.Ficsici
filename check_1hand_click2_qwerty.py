def check_1hand_click2_qwerty(strs):

    RusAlphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

    letterL = ["йфя", "цыч", "увс", "камепи"]
    letterR = ["нртгоь", "шлб", "щдю", "зжхэ"]
    TwoWordL = []
    TwoWordR = []

    for sym1 in letterL:
        for sym11 in sym1:
            for symp in letterL:
                if sym1 == symp:
                    continue
                for symp1 in symp:
                    word = sym11 + symp1
                    TwoWordL.append(word)

    for sym1 in letterR:
        for sym11 in sym1:
            for symp in letterR:
                if sym1 == symp:
                    continue
                for symp1 in symp:
                    word = sym11 + symp1
                    TwoWordR.append(word)

    lenstrs = len(strs)
    strs1HandClick2 = ""
    Two_1RightHand = 0
    Two_1LeftHand = 0

    for i in range(lenstrs - 1):
        symLow = strs[i].lower()
        symLowN = strs[i+1].lower()
        if (symLow not in RusAlphabet) or (symLowN not in RusAlphabet):
            continue
        symTwo = symLow + symLowN
        if symTwo in TwoWordL:
            strs1HandClick2 += symTwo
            Two_1LeftHand += 1
        if symTwo in TwoWordR:
            strs1HandClick2 += symTwo
            Two_1RightHand += 1
        i += 1

    return Two_1LeftHand, Two_1RightHand, strs1HandClick2

def check_1hand_click2_qwerty_comfortable(strsHandClick2):

    letterLc = ["фы", "фв", "фа", "ыв", "ыа", "ва"]
    letterRc = ["жд", "жл", "жо", "дл", "до", "ло"]

    Two_1RightHandComf = 0
    Two_1LeftHandComf = 0

    lenstrsh = len(strsHandClick2)
    
    for i in range(lenstrsh - 1):
        word2com = strsHandClick2[i] + strsHandClick2[i+1]
        if word2com in letterLc:
            Two_1RightHandComf += 1
        if word2com in letterRc:
            Two_1LeftHandComf += 1

    return Two_1LeftHandComf, Two_1RightHandComf


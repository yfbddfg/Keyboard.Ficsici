def check_h2_qwerty(strs):

    letterL = ['й','ф','я','1','!','ц','ы','ч','2','"','у','в','с','3','№','к','а','м','е','п','и','4','5',';','%',"'"]
    letterR = ['-','+','_','=','\\','|','.',',','з','ж','х','э','0',')','щ','д','ю','9','(','ш','л','б','8','*','н','р','т','г','о','ь','7','6','?',':','"']

    lenstrs = len(strs)
    Two_1RightHand = 0
    Two_1LeftHand = 0

    for i in range(lenstrs - 1):
        symLow = strs[i].lower()
        symLowN = strs[i+1].lower()
        if (symLow in letterL) and (symLowN in letterL):
            Two_1LeftHand += 1
        if (symLow in letterR) and (symLowN in letterR):
            Two_1RightHand += 1

    return Two_1LeftHand, Two_1RightHand

def check_h2_qwerty_com(strs):

    letterL = ["йфя1!", 'цыч2"', "увс3№", "камепи45;%"]
    letterR = ["-+_=\\|.,зжхэ0)", "щдю9(", "шлб8*", "нртгоь76?:"]
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

    lenstrs = len(strs)
    Two_1RightHandComf = 0
    Two_1LeftHandComf = 0

    for i in range(lenstrs - 1):
        symLow = strs[i].lower()
        symLowN = strs[i+1].lower()
        symTwo = symLow + symLowN
        if symTwo in TwoWordL:
            Two_1LeftHandComf += 1
        if symTwo in TwoWordR:
            Two_1RightHandComf += 1
    
    return Two_1LeftHandComf, Two_1RightHandComf


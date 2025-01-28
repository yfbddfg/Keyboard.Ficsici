""" 
анализирует строку на предмет пар символов и подсчитывает,
сколько из этих пар образованы из определенных зон (левых и правых)
на двух разных раскладках клавиатуры.
"""
def write_count_dig_com(strs4):

    TwoWordL = []
    TwoWordR = []
    count_qwertyl = 0
    count_qwertyr = 0
    count_zubachewl = 0
    count_zubachewr = 0

#########################
    letterL = ["йфя", "цыч", "увс", "камепи"]
    letterR = ["зжхэ", "щдю", "шлб", "нртгоь"]

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

    for dig in strs4:
        if dig in TwoWordL:
            count_qwertyl += 1
        if dig in TwoWordR:
            count_qwertyr += 1

################################
    letterL = ["фгш", "ыиьъ", "аею", "яъоуьэ"]
    letterR = ["щцжхзч", "пнк", "рсв", "мтдйлб"]

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

    for dig in strs4:
        if dig in TwoWordL:
            count_zubachewl += 1
        if dig in TwoWordR:
            count_zubachewr += 1

    return count_qwertyl, count_qwertyr, count_zubachewl, count_zubachewr


""" функции описывают раскладку клавиатуры Зубачева и Йцукен,
где символы назначены на определенную комбинацию пальцев (включая использование мизинцев).
Функции возвращают словари, которые содержат одно или несколько ключей""" 
def check_fine_zubachew(letter):

#lpin
    if letter in ["ф","ш"]:
        return {"lpin": 1}

    if letter in ["1"]:
        return {"lpin": 2}

    if letter in ["ё"]:
        return {"lpin": 3}

#lpin and lb
    if letter in ["Ф","Ш"]:
        return {"lpin": 1, "lb": 3}

    if letter in ["!"]:
        return {"lpin": 2, "lb": 3}

    if letter in ["Ё"]:
        return {"lpin": 3, "lb": 3}

#lb
    if letter in ["ы","ь"]:
        return {"lb": 1}

    if letter in ["2"]:
        return {"lb": 2}

#lb and lpin
    if letter in ["Ы","ъ"]:
        return {"lb":1 ,"lpin": 2}

    if letter in ['"']:
        return {"lb":2 ,"lpin": 2}

#lmid
    if letter in ["а","ю"]:
        return {"lmid": 1}

    if letter in ["3"]:
        return {"lmid": 2}

#lmid and lpin
    if letter in ["А","Ю"]:
        return {"lmid":1 ,"lpin": 2}

    if letter in ['№']:
        return {"lmid":2 ,"lpin": 2}

#lpoint    
    if letter in ["я","у","."]:
        return {"lpoint": 1}

    if letter in ["4",",","э"]:
        return {"lpoint": 2}

    if letter in ["5"]:
        return {"lpoint": 3}

#lpoint and lpin
    if letter in ["Ь","Я","У"]:
        return {"lpoint": 1, "lpin": 2}

    if letter in [";","Ъ","Э"]:
        return {"lpoint": 2, "lpin": 2}

    if letter in ["%"]:
        return {"lpoint": 3, "lpin": 2}

#rpoint
    if letter in ["м","л","д"]:
        return {"rpoint": 1}

    if letter in ["7","й","б"]:
        return {"rpoint": 2}

    if letter in ["6"]:
        return {"rpoint": 3}

#rpoint and lpin
    if letter in ["М","Л","Д"]:
        return {"rpoint": 1, "lpin": 2}

    if letter in ["?","Й","Б"]:
        return {"rpoint": 2, "lpin": 2}

    if letter in [":"]:
        return {"rpoint": 3, "lpin": 2}

#rmid
    if letter in ["р","в"]:
        return {"rmid": 1}

    if letter in ["8"]:
        return {"rmid": 2}

#rmid and lpin
    if letter in ["Р","В"]:
        return {"rmid":1 ,"lpin": 2}

    if letter in ['*']:
        return {"rmid":2 ,"lpin": 2}

#rb
    if letter in ["п","к"]:
        return {"rb": 1}

    if letter in ["9"]:
        return {"rb": 1}

#rb and lpin
    if letter in ["П","К"]:
        return {"rb":1 ,"lpin": 2}

    if letter in ['(']:
        return {"rb":2 ,"lpin": 2}

#rpin
    if letter in ["х","ж","ч"]:
        return {"rpin": 1}

    if letter in ["0","ц","\n"]:
        return {"rpin": 2}

    if letter in ["-","щ"]:
        return {"rpin": 3}

    if letter in ["=","\\"]:
        return {"rpin": 4}

#rpin and lpin
    if letter in ["Х","Ж","Ч"]:
        return {"rpin": 1, "lpin": 2}

    if letter in [")","Ц"]:
        return {"rpin": 2, "lpin": 2}

    if letter in ["_","Щ"]:
        return {"rpin": 3, "lpin": 2}

    if letter in ["+","/"]:
        return {"rpin": 4, "lpin": 2}
    
    return {"rpin": 0}

def check_fine_qwerty(letter):

#lpin
    if letter in ["й","я"]:
        return {"lpin": 1}

    if letter in ["1"]:
        return {"lpin": 2}

    if letter in ["ё"]:
        return {"lpin": 3}

#lpin and lb
    if letter in ["Й","Я"]:
        return {"lpin": 1, "lb": 3}

    if letter in ["!"]:
        return {"lpin": 2, "lb": 3}

    if letter in ["Ё"]:
        return {"lpin": 3, "lb": 3}

#lb
    if letter in ["ц","ч"]:
        return {"lb": 1}

    if letter in ["2"]:
        return {"lb": 2}

#lb and lpin
    if letter in ["Ц","Ч"]:
        return {"lb":1 ,"lpin": 2}

    if letter in ['"']:
        return {"lb":2 ,"lpin": 2}

#lmid
    if letter in ["у","с"]:
        return {"lmid": 1}

    if letter in ["3"]:
        return {"lmid": 2}

#lmid and lpin
    if letter in ["У","С"]:
        return {"lmid":1 ,"lpin": 2}

    if letter in ['№']:
        return {"lmid":2 ,"lpin": 2}

#lpoint    
    if letter in ["к","м","п"]:
        return {"lpoint": 1}

    if letter in ["4","е","и"]:
        return {"lpoint": 2}

    if letter in ["5"]:
        return {"lpoint": 2}

#lpoint and lpin
    if letter in ["К","М","П"]:
        return {"lpoint": 1, "lpin": 2}

    if letter in [";","Е","И"]:
        return {"lpoint": 1, "lpin": 2}

    if letter in ["%"]:
        return {"lpoint": 1, "lpin": 2}

#rpoint
    if letter in ["р","г","ь"]:
        return {"rpoint": 1}

    if letter in ["7","н","т"]:
        return {"rpoint": 2}

    if letter in ["6"]:
        return {"rpoint": 3}

#rpoint and lpin
    if letter in ["Р","Г","Ь"]:
        return {"rpoint": 1, "lpin": 2}

    if letter in ["?","Н","Т"]:
        return {"rpoint": 2, "lpin": 2}

    if letter in [":"]:
        return {"rpoint": 3, "lpin": 2}

#rmid
    if letter in ["ш","б"]:
        return {"rmid": 1}

    if letter in ["8"]:
        return {"rmid": 2}

#rmid and lpin
    if letter in ["Ш","Б"]:
        return {"rmid":1 ,"lpin": 2}

    if letter in ['*']:
        return {"rmid":2 ,"lpin": 2}

#rb
    if letter in ["щ","ю"]:
        return {"rb": 1}

    if letter in ["9"]:
        return {"rb": 2}

#rb and lpin
    if letter in ["Щ","Ю"]:
        return {"rb":1 ,"lpin": 2}

    if letter in ['(']:
        return {"rb":2 ,"lpin": 2}

#rpin
    if letter in ["з",".","э"]:
        return {"rpin": 1}

    if letter in ["\n","0","х"]:
        return {"rpin": 2}

    if letter in ["-","ъ"]:
        return {"rpin": 3}

    if letter in ["=","\\"]:
        return {"rpin": 4}

#rpin and lpin
    if letter in ["З",",","Э"]:
        return {"rpin": 1, "lpin": 2}

    if letter in [")","Х"]:
        return {"rpin": 2, "lpin": 2}

    if letter in ["_","Ъ"]:
        return {"rpin": 3, "lpin": 2}

    if letter in ["+","/"]:
        return {"rpin": 4, "lpin": 2}

    return {"rpin": 0}


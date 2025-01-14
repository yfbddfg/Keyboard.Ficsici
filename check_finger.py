def check_finger_zubachew(letter):
    if letter in ["ё","1","ф","г","ш"]:
        return {"lpin": 1}

    if letter in ["Ё","!","Ф","Г","Ш"]:
        return {"lpin": 1, "lb": 1}

    if letter in ["2","ы","и","ь"]:
        return {"lb": 1}

    if letter in ['"',"Ы","И","ъ"]:
        return {"lb":1 ,"lpin": 1}

    if letter in ["3","а","е","ю"]:
        return {"lmid": 1}

    if letter in ['№',"А","Е","Ю"]:
        return {"lmid":1 ,"lpin": 1}
    
    if letter in ["4","5","я",",","о","у",".","э"]:
        return {"lpoint": 1}

    if letter in [";","%","Ъ","Ь","Я","О","У","Э"]:
        return {"lpoint": 1, "lpin": 1}

    if letter in ["6","7","й","м","л","т","б","д"]:
        return {"rpoint": 1}

    if letter in [":","?","Й","М","Л","Т","Б","Д"]:
        return {"rpoint": 1, "lpin": 1}

    if letter in ["8","р","с","в"]:
        return {"rmid": 1}

    if letter in ['*',"Р","С","В"]:
        return {"rmid":1 ,"lpin": 1}

    if letter in ["9","п","н","к"]:
        return {"rb": 1}

    if letter in ['(',"П","Н","К"]:
        return {"rb":1 ,"lpin": 1}

    if letter in ["0","-","=","х","ц","щ","\\","з","ж","ч"]:
        return {"rpin": 1}

    if letter in [")","_","+","Х","Ц","Щ","/","З","Ж","Ч"]:
        return {"rpin": 1, "lpin": 1}
    
    if letter == "\n":
        return {"rpin":1}

    if letter == " ":
        return {"rpin":0}
    
    print("unfound symbol")
    return exit

def check_finger_qwerty(letter):
    if letter in ["ё","1","й","ф","я"]:
        return {"lpin": 1}

    if letter in ["Ё","!","Й","Ф","Я"]:
        return {"lpin": 1, "lb": 1}

    if letter in ["2","ц","ы","ч"]:
        return {"lb": 1}

    if letter in ['"',"Ц","Ы","Ч"]:
        return {"lb":1 ,"lpin": 1}

    if letter in ["3","у","в","с"]:
        return {"lmid": 1}

    if letter in ['№',"У","В","С"]:
        return {"lmid":1 ,"lpin": 1}
    
    if letter in ["4","5","к","а","м","е","п","и"]:
        return {"lpoint": 1}

    if letter in [";","%","К","А","М","Е","П","И"]:
        return {"lpoint": 1, "lpin": 1}

    if letter in ["6","7","н","р","т","г","о","ь"]:
        return {"rpoint": 1}

    if letter in [":","?","Н","Р","Т","Г","О","Ь"]:
        return {"rpoint": 1, "lpin": 1}

    if letter in ["8","ш","л","б"]:
        return {"rmid": 1}

    if letter in ['*',"Ш","Л","Б"]:
        return {"rmid":1 ,"lpin": 1}

    if letter in ["9","щ","д","ю"]:
        return {"rb": 1}

    if letter in ['(',"Щ","Д","Ю"]:
        return {"rb":1 ,"lpin": 1}

    if letter in ["0","-","=","з","ж",".","\\","х","э","ъ"]:
        return {"rpin": 1}

    if letter in [")","_","+","З","Ж",",","/","Х","Э","Ъ"]:
        return {"rpin": 1, "lpin": 1}
    
    if letter == "\n":
        return {"rpin":1}

    if letter == " ":
        return {"rpin":0} 

    print("unfound symbol")
    return exit


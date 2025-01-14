def check_filecsv(filecsv):
    list_dig = []
    with open(filecsv, "r") as fcsv:
        for line in fcsv: 
            if not line: break
            _, nado, _, _ = line.split(" , ")
            list_dig.append(nado)
    fcsv.close()
    return list_dig


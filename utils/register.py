def createDict():
    exists = {}
    file = open("data/data.csv", 'r')
    update = file.read()
    udpatedFur = a.split("\n")
    for k in updatedFur:
        line = k.split(",")
        try:
            exists[line[0]] = line[1]
        except:
            return exists
    return exists

def add(user,passw):
    f = open("data/data.csv","a")
    f.write(str(user) +','+ str(passw) + "\n")
    f.close()

   

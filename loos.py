from random import randint
from time import sleep

andja = ["Kadri","Markus","Kati","Raul","Joosep","Sander","Inge"]
saaja = ["Kadri","Markus","Kati","Raul","Joosep","Sander","Inge"]
kontroll = ["Kadri","Markus","Kati","Raul","Joosep","Sander","Inge"]
fail = open("Jõululoos.txt","w")
for x in kontroll:
    i  = 0
    a_pikkus = len(andja)
    s_pikkus = len(saaja)
    l1 = andja[randint(0,a_pikkus - 1)]
    l2 = saaja[randint(0,s_pikkus - 1)]
    while l1 == l2:
        l1 = andja[randint(0,a_pikkus - 1)]
        l2 = saaja[randint(0,s_pikkus - 1)]
    print(l1 + " --> " + l2)
    fail.write(l1 + " --> " + l2 + "\n")
    saaja.remove(l2)
    andja.remove(l1)
fail.close()

import sys
#hahaha zmena z poicitace na github push
def prumer(cislo):
    soucet=0
    for i in cislo:
        soucet+=i
    return(soucet/len(cislo))

print(prumer(sys.argv[1:]))

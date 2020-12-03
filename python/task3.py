# Detta är ett program för att lösa uppg3 till AoC2020

# Skapat av Mikael Sahleström
# 2020-12-01

# ---------------------------- Programfunktioner ----------------------------#
def laddaRådata():
    """
    Laddar in rådata till uppgiften
    input: void
    output: Array
    """
    rådata = open("data3.txt", "r")
    backe = []
    for rad in rådata:
        rad = rad.rstrip("\n")
        # print(rad)
        backe.append(rad)
    rådata.close()
    return backe

def trädräknare(right, down, backe):
    antalTräd = 0
    posX = 0
    for i, rad in enumerate(backe[::down]):
        posX = i*right%len(rad)
        if rad[posX] == '#':
            antalTräd += 1
    return antalTräd
   

def main():
    """
    Huvudprogram för uppgiften
    Input: void
    Output: void
    """
    backe = laddaRådata()
    antalTrädUppg1 = trädräknare(3,1,backe)
    print("Antal träd i uppgift 1:",antalTrädUppg1)

    antalTrädUppg2 = trädräknare(1,1,backe) * trädräknare(3,1,backe) * trädräknare(5,1,backe) * trädräknare(7,1,backe) * trädräknare(1,2,backe)
    print("Antal träd i uppgift 2:",antalTrädUppg2)

# Kör programmet
main()
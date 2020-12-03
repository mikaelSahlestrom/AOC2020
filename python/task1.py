# Detta är ett program för att lösa uppg1 till AoC2020

# Skapat av Mikael Sahleström
# 2020-12-01

# ---------------------------- Programfunktioner ----------------------------#
def laddaRådata():
    """
    Laddar in rådata till uppgiften
    input: void
    output: Array
    """
    rådata = open("data1.txt", "r")
    utgifter = []
    for rad in rådata:
        rad = int(rad)
        utgifter.append(rad)
    rådata.close()
    return utgifter

def uppgift1(utgifter): 
    """
    Lösning för del 1 i uppgift 1
    """
    for i,utgift in enumerate(utgifter):
        for j,andraUtgiften in enumerate(utgifter):
            if(utgift + andraUtgiften == 2020):
                # print(utgift, andraUtgiften, i, j)
                print(utgift * andraUtgiften)

def uppgift2(utgifter): 
    """
    Lösning för del 1 i uppgift 1
    """
    for i,utgift in enumerate(utgifter):
        for j,andraUtgiften in enumerate(utgifter):
            for k,trefjeUtgiften in enumerate(utgifter):
                if(utgift + andraUtgiften + trefjeUtgiften == 2020):
                    print(utgift, andraUtgiften, trefjeUtgiften, i, j, k)
                    print(utgift * andraUtgiften * trefjeUtgiften)

def main():
    """
    Huvudprogram för uppgiften
    Input: void
    Output: void
    """
    utgifter = laddaRådata()
    # uppgift1(utgifter)
    uppgift2(utgifter)


# Kör programmet
main()
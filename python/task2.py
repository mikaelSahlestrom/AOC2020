# Detta är ett program för att lösa uppg2 till AoC2020

# Skapat av Mikael Sahleström
# 2020-12-01

# ---------------------------- Programfunktioner ----------------------------#
def laddaRådata():
    """
    Laddar in rådata till uppgiften
    input: void
    output: Array
    """
    rådata = open("data2.txt", "r")
    utgifter = []
    for rad in rådata:
        rad = rad.rstrip("\n").rsplit(":")
        utgifter.append(rad)
    rådata.close()
    return utgifter

def kontrolleraLösenordUppgift1(min, max, kontrollBokstav, lösenord):
    antalGodkändaBokstäver = 0
    for bokstav in lösenord:
        if bokstav == kontrollBokstav:
            antalGodkändaBokstäver += 1

    if antalGodkändaBokstäver >= min and antalGodkändaBokstäver <= max:
        return 1
    else: 
        return 0

def kontrolleraLösenordUppgift2(första, andra, kontrollBokstav, lösenord):
    antalGodkändaBokstäver = 0
    if lösenord[första] == kontrollBokstav:
        antalGodkändaBokstäver += 1

    if lösenord[andra] == kontrollBokstav:
        antalGodkändaBokstäver += 1

    if antalGodkändaBokstäver == 1:
        return 1
    else: 
        return 0

def rådataParser(lösenordsKontrollInformation):
    lösenordsKontrollInformation = lösenordsKontrollInformation.rsplit(" ")
    kontrollBokstav = lösenordsKontrollInformation[1]
    minMaxLösenordslängd = lösenordsKontrollInformation[0].rsplit("-")
    min = int(minMaxLösenordslängd[0])
    max = int(minMaxLösenordslängd[1])
    return min,max, kontrollBokstav

def main():
    """
    Huvudprogram för uppgiften
    Input: void
    Output: void
    """
    databas = laddaRådata()
    antalGodkändaLösenordUppgift1 = 0
    antalGodkändaLösenordUppgift2 = 0
    for rad in databas:
        (min, max, kontrollBokstav) = rådataParser(rad[0])
        antalGodkändaLösenordUppgift1 += kontrolleraLösenordUppgift1(min, max, kontrollBokstav, rad[1])
        antalGodkändaLösenordUppgift2 += kontrolleraLösenordUppgift2(min, max, kontrollBokstav, rad[1])

    print("Antal godkända lösenord enl. uppg1: ",antalGodkändaLösenordUppgift1)
    print("Antal godkända lösenord enl. uppg2: ",antalGodkändaLösenordUppgift2)

# Kör programmet
main()
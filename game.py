import random

def setupGameBoard(kolommen, rijen):
    "maakt een tabel aan met daarin een enkele bom"

    # Maak een leeg board
    gameboard = []
    rij = []
    for x in range (0, rijen):
        for y in range (0, kolommen):
            rij.append('.')
        gameboard.append(rij)
        rij=[]


    # Plaats de Bom
    x = random.randrange(0, kolommen)
    y = random.randrange(0, rijen)
    gameboard[y][x]='B'

    return gameboard

def vraagGebruikerOmEenPositie(maxX, maxY):
    x = int(input("Geef een positie x: "))
    while not (1 <= x <= maxX):
        x = int(input("Geef een positie x: "))

    y = int(input("Geef een positie y: "))
    while not (1 <= y <= maxY):
        y = int(input("Geef een positie y: "))

    return (x-1), (y-1)  # correctie van -1 omdat de gebruiker in 
    # tegenstelling tot de computer wel bij 1 begint met tellen.

def bepaalOfErEenBomLigt(gameboard, x, y):
    erLigtEenBom = gameboard[y][x] == 'B'
    gameboard[y][x]='x'
    if erLigtEenBom:
        gameboard[y][x]='@'
    return erLigtEenBom

def toonGameBoard(gameboard, beurt):
    aantalRijen = len(gameboard)
    for rij in range(aantalRijen):
        aantalKolommen = len(gameboard[rij])
        for kol in range(aantalKolommen):
            if gameboard[rij][kol]=='B':
                print('.', sep="", end="")
            else:
                print(gameboard[rij][kol], sep="", end="")
        print()
    print("Dit was beurt "+str(beurt)+".")


# ---- Hoofdprogramma ----
aantalKolommen = 9
aantalRijen = 5

gameboard = setupGameBoard(aantalKolommen, aantalRijen)

gameOver = False
beurt = 0
toonGameBoard(gameboard, beurt)

while not gameOver:
    beurt += 1
    x, y = vraagGebruikerOmEenPositie(aantalKolommen, aantalRijen)
    gameOver = bepaalOfErEenBomLigt(gameboard, x, y)
    toonGameBoard(gameboard, beurt)
    
print("----  Game Over  ----")

class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = ""
        self.suviai = {"i_virsu": 0,"i_apacia": 0, "kairen": 0, "desinen": 0}

    def sauti(self):
        if self.kryptis == "i_virsu":
            self.suviai["i_virsu"] += 1
        elif self.kryptis == "i_apacia":
            self.suviai["i_apacia"] += 1
        elif self.kryptis == "kairen":
            self.suviai["kairen"] += 1
        elif self.kryptis == "desinen":
            self.suviai["desinen"] += 1


    def judeti(self, judejimo_kryptis):
        if judejimo_kryptis == 'i_virsu':
            self.y += 1
            self.kryptis = "i_virsu"
        elif judejimo_kryptis == "i_apacia":
            self.y -= 1
            self.kryptis = "i_apacia"
        elif judejimo_kryptis == "kairen":
            self.x -= 1
            self.kryptis = "kairen"
        elif judejimo_kryptis == "desinen":
            self.x += 1
            self.kryptis = "desinen"

    def informacija(self):
        print(f"Tanko_Koordinates: x{self.x} : y{self.y}")
        print(f"Suviai: {self.suviai}")
        print(f"Atliko_suviu: {sum(self.suviai.values())}")
        print(f"Vazevimo_Kryptis: {self.kryptis}")

print("Phyton_Battle_Tank")
tankas = Tankas()

while True:
    print("_________________________________")
    print("Valdymo instrukcija")
    pasirinkimai = input(" w - i_virsu, s - i_apacia \n a - kairen , d - desinen \n x - sauti \n i - informacija \n q - iseiti \n Tavo_ejimas:")

    print(tankas.x, tankas.y)

    match pasirinkimai:
        case "w":
            tankas.judeti("i_virsu")
        case "s":
            tankas.judeti("i_apacia")
        case "a":
            tankas.judeti("kairen")
        case "d":
            tankas.judeti("desinen")
        case "x":
            tankas.sauti()
        case "i":
            tankas.informacija()
        case "q":
            print("Zaidimo_pabaiga")
            break










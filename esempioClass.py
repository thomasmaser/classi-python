class Persona:
    specie = "Homo Sapiens" #Attributo di classe
    def __init__(self, nome, età):
        self.nome = nome #attributo di istanza
        self.età = età
    def eiacula(self):
        print("mi sono eiaculato")

persona1 = Persona("Mario", 30)

# print(persona1.specie)
# print(persona1.nome)
# print(persona1.età)


#ereditarietà classe
class Studente(Persona):
    def __init__(self, nome, età, quantità):
        self.nome = nome #attributo di istanza
        self.età = età
        self.quantità = int(quantità)
        
      
    def eiacula(self):
        print("mi sono eiaculato, sono uno studente")
    


boyy = Studente("pierino", 15, 27)

print("mi chiamo ", boyy.nome, "ho", boyy.età)
boyy.eiacula()
print(boyy.quantità)


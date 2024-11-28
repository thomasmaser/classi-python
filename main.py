from ClasseAuto import Auto


punto = Auto("fiat", "punto", "bianco")

print(punto.marca)
print(punto.modello)
print(punto.colore)
punto.clacson()

while punto.velocità < 150:
    variazione = input("accelerare o frenare?")
    if variazione == "accelerare":
        incremento = int(input("di quanto vuoi accelerare?"))
        punto.velocità += incremento
        print("la velocità ora è di", punto.velocità, "km/h")
    else:
        print("che succede??? i freni non funzionano????") 
        # decremento = int(input())
        # punto.velocità -= decremento
        punto.velocità += 20
        print("la velocità ora è di", punto.velocità, "km/h")
        print("cazzo stiamo per morire")
punto.clacson()
print("ti sei schiantato: sei morto")
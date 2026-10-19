materiau = input("Quel materiau ou objet souhaitez-vous customiser ?")

poids = float(input("Quel est le poids de l'objet (en kg) ?"))

if poids > 0:
    co2_evite = poids * 15.0
    print(f"En customisant {materiau} de {poids} kg, vous évitez l'émission de {co2_evite} kg de CO2.")


else:
    print("Erreur : le poids doit être supérieur à 0 kg.")
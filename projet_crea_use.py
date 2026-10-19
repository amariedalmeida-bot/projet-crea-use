materiau = input("Quel materiau ou objet souhaitez-vous customiser ?")

poids = float(input("Quel est le poids de l'objet (en kg) ?"))

co2_evite = poids * 15.0

print(f"En customisant {materiau} de {poids} kg, vous évitez l'émission de {co2_evite} kg de CO2.")
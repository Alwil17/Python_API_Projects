from controllers.auth import Auth
from controllers.etablissement_controller import get_all_etablissements
from controllers.med_et_controller import get_medecin_in_etablissement

Auth()
print(Auth.connected_user)
print("\n---------- Prenez facilement un rendez-vous médical ----------")
axe = input("Saisissez l'axe cible: ")
lieu = input("Saisissez le lieu de la consultation: ")

etablissements = get_all_etablissements()
suggested_ets = []
final_ets = []
for etablissement in etablissements:
    for acte in etablissement["actes"]:
        if axe in acte["nom"]:
            suggested_ets.append(etablissement)

if len(suggested_ets) >= 0:
    for suggested_et in suggested_ets:
        if lieu in suggested_et["adresse"]:
            final_ets.append(suggested_et)

if len(final_ets) >= 0:
    founded_meds = []
    for et in final_ets:
        founded = get_medecin_in_etablissement(et["id"])
        for i in founded:
            founded_meds.append(i)
    print("Medecins disponibles")
    for i in founded_meds:
        idx = founded_meds.index(i)
        print(f"{idx+1} - {i['medecin']['utilisateur']['nom']}")

else:
    print("Aucun etablissement trouvé dans cette zone")

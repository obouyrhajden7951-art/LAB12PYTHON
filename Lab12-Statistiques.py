# Task 1.1 - Initialisation de l'environnement
import numpy as np

# Task 1.2 - Definir le mini-jeu de donnees
noms = np.array(["Alice", "Bob", "Chloe", "David"])
notes = np.array([
    [14.5, 16.0, 13.0],  # Alice
    [11.0, 10.5, 12.5],  # Bob
    [17.0, 18.5, 16.5],  # Chloe
    [9.0, 11.0, 10.0]    # David
])

print("Etudiants :", noms)
print("Notes :\n", notes)
print("Shape notes :", notes.shape)  # (4, 3)

# Etape 2 - Statistiques globales
moyenne_globale = np.mean(notes)
min_global = np.min(notes)
max_global = np.max(notes)
somme_globale = np.sum(notes)
ecart_type_global = np.std(notes)

print(f"Moyenne generale : {moyenne_globale:.2f}")
print(f"Minimum global : {min_global}")
print(f"Maximum global : {max_global}")
print(f"Somme globale : {somme_globale}")
print(f"Ecart-type global : {ecart_type_global:.2f}")

# Etape 3 - Statistiques par axe
# Axe 0 (par epreuve)
moyennes_epreuves = np.mean(notes, axis=0)
mins_epreuves = np.min(notes, axis=0)
maxs_epreuves = np.max(notes, axis=0)
std_epreuves = np.std(notes, axis=0)

print("Moyennes par epreuve :", moyennes_epreuves)
print("Min par epreuve :", mins_epreuves)
print("Max par epreuve :", maxs_epreuves)
print("Ecart-type par epreuve :", std_epreuves)

# Axe 1 (par etudiant)
moyennes_etudiants = np.mean(notes, axis=1)
mins_etudiants = np.min(notes, axis=1)
maxs_etudiants = np.max(notes, axis=1)
std_etudiants = np.std(notes, axis=1)

print("Moyenne personnelle :", moyennes_etudiants)
print("Note min. personnelle :", mins_etudiants)
print("Note max. personnelle :", maxs_etudiants)
print("Dispersion personnelle :", std_etudiants)

# Etape 4 - Identification de performances
idx_top_etudiant = np.argmax(moyennes_etudiants)
meilleur_etudiant = noms[idx_top_etudiant]
meilleure_moyenne = moyennes_etudiants[idx_top_etudiant]
print(f"Top etudiant : {meilleur_etudiant} ({meilleure_moyenne:.2f})")

idx_epreuve_difficile = np.argmin(moyennes_epreuves)
epreuves = np.array(["E1", "E2", "E3"])
epreuve_difficile = epreuves[idx_epreuve_difficile]
print(f"Epreuve la plus difficile : {epreuve_difficile} (moy. {moyennes_epreuves[idx_epreuve_difficile]:.2f})")

# Etape 5 - Selection conditionnelle
seuil_moyenne = 12
masque_moyenne = moyennes_etudiants >= seuil_moyenne
etudiants_admis = noms[masque_moyenne]
notes_admis = notes[masque_moyenne]
print(f"Etudiants avec moyenne >= {seuil_moyenne} :", etudiants_admis)
print("Leurs notes :\n", notes_admis)

masque_e2 = notes[:, 1] >= 15
print("Etudiants avec >=15 en E2 :", noms[masque_e2])

# Etape 6 - Enrichissement & tableau final
moyennes_colonne = moyennes_etudiants.reshape(-1, 1)
notes_enrichies = np.hstack([notes, moyennes_colonne])
epreuves_ext = np.append(epreuves, "Moyenne")
ligne_moyennes = np.append(moyennes_epreuves, [np.mean(moyennes_etudiants)])
tableau_final = np.vstack([notes_enrichies, ligne_moyennes])
noms_ext = np.append(noms, "Moyennes globales")

# Ajouter ecart-type par etudiant
ecarts_colonne = std_etudiants.reshape(-1, 1)
notes_info = np.hstack([notes_enrichies, ecarts_colonne])
epreuves_finales = np.append(epreuves_ext, "Ecart-type")

# Etape 7 - Synthese visuelle / Rapport
print("\n=== Tableau final formaté ===")
for nom, ligne in zip(noms_ext, tableau_final):
    valeurs = " | ".join(f"{val:.2f}" for val in ligne)
    print(f"{nom:>20s} : {valeurs}")

print("\n=== Resume des performances ===")
print(f"Top etudiant : {meilleur_etudiant} avec une moyenne de {meilleure_moyenne:.2f}")
print(f"Epreuve la plus difficile : {epreuve_difficile} (moyenne {moyennes_epreuves[idx_epreuve_difficile]:.2f})")
print(f"Etudiants avec moyenne >= {seuil_moyenne} :", ", ".join(etudiants_admis))

print("Analyse :")
print("- Clara / Top etudiant : tres reguliere et performante sur toutes les epreuves.")
print("- David / a ameliorer : toutes les notes sont en dessous de la moyenne globale.")
print("- Alice et Bob : moyennes correctes, peuvent progresser sur certaines epreuves.")


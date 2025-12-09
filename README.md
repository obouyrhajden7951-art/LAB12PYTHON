# LAB12PYTHON

<img width="706" height="238" alt="image" src="https://github.com/user-attachments/assets/28e857b2-95c2-4687-b70f-54c04c6a793b" />

      # Quiz rapide & réflexion

Quelle est la shape de notes.mean(axis=0) ?
    → (3,), une moyenne par colonne/épreuve.
Comment récupérer les étudiants dont la moyenne dépasse celle de l’ensemble ?
    → noms[moyennes_etudiants > moyenne_globale]
Comment ajouter une nouvelle épreuve fictive avec np.hstack ?
    → Générer une colonne (n,1) et utiliser np.hstack([notes, nouvelle_epreuve])
Comment sélectionner les étudiants ayant une note < 10 dans au moins une épreuve ?
    → masque = (notes < 10).any(axis=1); noms[masque]

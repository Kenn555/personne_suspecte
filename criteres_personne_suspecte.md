# Critères d'une personne suspecte

- Taille de la boîte englobante (bounding box) supérieure à un seuil (ex : area > 50000)
- Présence détectée par le modèle YOLO (classe 0 = personne)
- Autres critères à définir selon le contexte (comportement, vêtements, objets, etc.)

# Exemple de critère utilisé dans main.py
- Si la surface de la boîte englobante dépasse 50000 pixels, la personne est considérée comme suspecte.

# À compléter selon les besoins du projet

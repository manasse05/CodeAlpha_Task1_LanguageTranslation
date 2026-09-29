# CodeAlpha - Language Translation Tool

Projet réalisé dans le cadre du stage virtuel **Artificial Intelligence** chez CodeAlpha (Tâche 1 : Language Translation Tool).

## Objectif

Créer une application avec une interface graphique où l'utilisateur écrit un texte, choisit la langue de départ et la langue d'arrivée, puis obtient la traduction affichée à l'écran.

## Fonctionnalités

- Saisie d'un texte à traduire
- Choix de la langue source et de la langue cible (8 langues)
- Bouton pour inverser les deux langues
- Affichage clair de la traduction
- Bouton pour copier la traduction dans le presse-papiers
- Messages d'erreur clairs (texte vide, problème de connexion)

## Langues disponibles

Français, Anglais, Espagnol, Allemand, Italien, Portugais, Arabe, Chinois.

## Outils utilisés

- Python 3
- Tkinter (interface graphique, inclus avec Python)
- deep-translator (bibliothèque qui envoie le texte au service Google Translate et récupère la traduction)

## Comment ça marche

1. L'utilisateur écrit son texte et choisit les langues.
2. Au clic sur **Traduire**, le texte est envoyé au service de traduction.
3. La réponse est récupérée et affichée dans la zone "Traduction".
4. Le bouton **Copier la traduction** place le résultat dans le presse-papiers.

## Aperçu

![Capture de l'application](capture.png)

## Structure du projet

```
CodeAlpha_TranslationTool/
├── app.py
├── requirements.txt
├── .gitignore
├── capture.png
└── README.md
```

## Installation et lancement

1. Créer et activer un environnement virtuel :
```
python -m venv venv
venv\Scripts\activate
```
2. Installer la bibliothèque :
```
pip install -r requirements.txt
```
3. Lancer l'application :
```
python app.py
```

Une connexion internet est nécessaire pour que la traduction fonctionne.

## Limites et améliorations possibles

- Nombre de langues limité à 8 (facile à étendre dans le dictionnaire `LANGUES`)
- Ajout possible d'une fonction de lecture à voix haute (text-to-speech)
- Détection automatique de la langue du texte

## Auteur

Doou - Stagiaire Artificial Intelligence chez CodeAlpha
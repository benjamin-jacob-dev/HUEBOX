# HUEBOX - Palette Extractor Premium

<p>
  <img src="HUEBOX-Logo.png" alt="HUEBOX" width="90">
</p>

HUEBOX est un outil de création de palettes de couleurs à partir d’images. Simple, rapide et élégant, il vous permet d’extraire automatiquement les couleurs dominantes d’une photo et de les visualiser directement dans le terminal avec des carrés de couleur et leurs codes HEX.

## Caractéristiques

- 🎨 Extraction automatique de 5 couleurs dominantes (configurable)  
- 🖼️ Support des formats PNG, JPG, JPEG et BMP  
- 🟦 Affichage des couleurs avec carrés ANSI dans le terminal  
- ⏱️ Animation de chargement stylée pour une expérience utilisateur premium  
- ⚡ 100 % local, aucune donnée envoyée sur le cloud  
- 🧩 Open Source et modifiable selon vos besoins  

## Prérequis

- Python 3.7 ou supérieur  
- pip (gestionnaire de paquets Python)  

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/benjamin-jacob-dev/HUEBOX.git
cd HUEBOX
```
Installez les dépendances :
```bash
pip install -r requirements.txt
```
Utilisation
Lancer l'application
```bash
python HUEBOX.py
```
## Étapes

- Affichage du logo et animation de démarrage
- Saisie du chemin de l'image (formats supportés : PNG, JPG, JPEG, BMP)
- Analyse automatique et extraction des couleurs dominantes
- Affichage des couleurs sous forme de carrés et codes HEX dans le terminal

## Exemple de sortie

<p>
  <img src="HUEBOX-screenshot.png" alt="HUEBOX-screenshot" width="500">
</p>


🎨 Palette dominante détectée :

  ▇  #FF5733
  ▇  #33FFBD
  ▇  #335BFF
  ▇  #F1FF33
  ▇  #FF33E3


- Interface terminal épurée et premium
- Animations discrètes pour renforcer l’expérience utilisateur

## Structure du projet

HUEBOX/
├── README.md           # Documentation du projet
├── requirements.txt    # Dépendances Python
├── HUEBOX.py           # Code source principal
├── HUEBOX-Logo.png          # Logo

Dépendances
Pillow : Manipulation d’images
numpy : Calcul et traitement des couleurs
scikit-learn : Clustering KMeans pour extraction de couleurs

## Bonnes pratiques

Images :
Préférez des images de bonne résolution
Évitez les images très petites ou très compressées

Palette :
Ajustez le nombre de couleurs si nécessaire dans le code
Vérifiez la cohérence avec votre branding ou projet graphique
Sécurité et gestion :

- Les images restent locales, aucun risque d’envoi externe
- Supprimez les fichiers temporaires si nécessaire

## Limitations

- Extraction limitée à 5 couleurs par défaut (modifiable)
- Fonctionne uniquement avec des images locales
- Les couleurs peuvent légèrement varier selon la compression de l’image

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :
- Forkez le projet
- Créez une branche pour votre fonctionnalité
- Committez vos changements
- Poussez vers la branche
- Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT.

## 👥 Auteurs

- Benjamin Jaccob - *Développeur initial* <br><br>
[![Atelier Digital VisiCraft](https://img.shields.io/badge/Atelier%20Digital-VisiCraft-orange?style=for-the-badge&logo=github&logoColor=white)](https://visicraft.fr)

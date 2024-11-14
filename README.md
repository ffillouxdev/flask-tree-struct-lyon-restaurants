# Flask Tree Struct: Lyon Restaurants

## Description
Ce projet est une application web développée avec Flask qui permet d'explorer les meilleurs restaurants de Lyon à travers une structure en arbre organisée. L'application utilise des structures de données pour organiser les informations sur les restaurants, les arrondissements et les types de restaurants.

## Technologies Utilisées
- **Flask** : Framework web léger en Python utilisé pour créer l'application web.
- **SQLite** : Base de données relationnelle utilisée pour stocker les informations sur les restaurants.
- **HTML/CSS** : Utilisés pour structurer et styliser les pages web.
- **JavaScript** : Utilisé pour les interactions dynamiques sur la page.
- **Leaflet** : Bibliothèque JavaScript pour les cartes interactives.
- **Tailwind CSS** : Framework CSS utilitaire pour styliser rapidement les composants.

## Structure du Projet
- `app.py` : Fichier principal de l'application Flask.
- `data_structures/` : Contient les implémentations des structures de données utilisées pour organiser les informations.
  - `pileTree.py` : Implémentation d'une pile pour parcourir les arbres.
  - `recursiveTree.py` : Implémentation d'un parcours récursif des arbres.
  - `tree.py` : Contient la classe `Arbre` pour gérer les arbres.
- `db/` : Contient les opérations de base de données et les modèles.
  - `db_operations.py` : Fonctions pour interagir avec la base de données.
  - `models.py` : Définitions des modèles de base de données.
- `static/` : Contient les fichiers statiques (CSS, images, JavaScript).
  - `css/style.css` : Fichier de styles principal.
- `templates/` : Contient les templates HTML pour les pages web.

## Couleurs Utilisées
Les couleurs utilisées dans le projet sont définies dans le fichier `static/css/style.css` :
- **Couleur de fond primaire** : #333333
- **Couleur de fond secondaire** : #444
- **Couleur de fond au survol** : #555
- **Couleur de texte primaire** : white
- **Couleur de texte secondaire** : #bbbbbb
- **Couleur de texte au survol** : #ffffff
- **Couleur de fond des modales** : rgba(0, 0, 0, 0.5)
- **Couleur de fond du contenu des modales** : white
- **Couleur de fond du footer** : #333
- **Couleur de bordure du footer** : #555

## Structures de Données
Le projet utilise plusieurs structures de données pour organiser les informations :
- **Noeud** : Représente un noeud dans un arbre.
- **Pile** : Implémentation d'une pile pour gérer les noeuds.
- **PileTree** : Utilise une pile pour parcourir les arbres.
- **recursiveTree** : Utilise des méthodes récursives pour parcourir les arbres.

## Pourquoi Flask ?
Flask a été choisi pour ce projet en raison de sa simplicité et de sa flexibilité. Il permet de créer rapidement des applications web tout en offrant la possibilité de s'étendre avec des extensions. De plus, Flask est bien adapté pour des projets de petite à moyenne taille, ce qui correspond aux besoins de ce projet. Je voulais surtout démontrer son utilité pour un projet de groupe en Python.

## Installation
1. Clonez le dépôt :
   ```sh
   git clone https://github.com/ffillouxdev/flask-tree-struct-lyon-restaurants.git

2. Créer l'environnement virtuel :
   ```sh
   python -m venv venv 
   .\venv\Scripts\activate

3. Installez les dépendances :
   ```sh
   pip install -r requirements.txt

4. Exécutez l'application :
   ```sh
    python app.py

5. Ouvrez votre navigateur et accédez à l'URL suivante :
    ```
    http://localhost:8080/

## Auteur
- **FFillouxDev** : apprenti Développeur 

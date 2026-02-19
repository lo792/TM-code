## Environnement virtuel
Un environnement virtuel permet d'isoler l'environnement d'exécution Python propre au projet.
Ainsi, seules les librairies nécessaires au projet seront chargées.

#### Création d'un environnement virtuel
```perl
python -m venv ./.venv
```
L'exécution de cette commande crée l'environnement virtuel .venv

Pour *utiliser* l'environnement virtuel *.venv* il faut **l'activer**:
```perl
.\.venv\Scripts\activate
```

## Utilisation de git pour gérer le code source

Les commandes qui suivent supposent que le programme git est installé.
Pour initialiser un répertoire *git*:
```perl
git init

Afin de ne pas polluer le répertoire *git*, les fichiers provenant de l'extérieur et géré par d'autres, les fichier précompilés, etc. ne sont pas gérés avec git.
Pour cela, un fichier *.gitignore* est créé et indique les répertoire, fichiers, extensions que nous ne voulons pas gérer avec git.

# Exercice 1 - Tests statiques

## Pré-requis
* Avoir un compte Github
* Avoir git, docker et docker-compose installé

## Objectifs

* Cet exercice a pour objectifs :
    * de préparer une image d'analyse de code statique
    * de savoir lancer une anayse de code statique


## Préparation de l'image

* Créer un dépôt sur votre compte github en forkant celui-ci : https://github.com/vanessakovalsky/python-api-handle-it 
* Ajouter dans les dépendances de Python l'utilitaire pylint
* Construire l'image et la taguer avec le nom que vous souhaitez

## Lancement du linter

* Lancer un conteneur à partir de l'image créé
* Ouvrir un bash sur le conteneur 
* Lancer pylint sur l'application : 
```
cd /app
pylint *.py
```
* Vous obtiendrez alors un retour vous indiquant si des erreurs sont présentes dans votre code

## Bonus - Ajout d'autres outils

* d'autres outils permettant de faire de l'analyse qualité sur une application python existent, par exemple vous pouvez voir une liste avec une description ici : https://realpython.com/python-code-quality/ 
* Si vous avez terminé le reste, vous pouvez installer un ou plusieurs autres outils dans votre images et les lancer pour voir le résultat

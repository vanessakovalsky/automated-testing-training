# Exercice 6 - Générer des rapports de tests

## Objectifs
Cet exercice a pour objectifs :
* de générer un rapport de tests unitaire depuis unitest
* de générer un rapport de tests depuis Selenium
* d'apprendre à lire ces rapports

## Préèrequis
* Avoir un environnement Python avec : 
    * une application
    * des tests unitaires unittest
    * des tests selenium

## Générer un rapport de test pour les tests unitaires

* Ajouter au requirements.txt le package suivant
```
html-testRunner
```
* Installer ce paquet avec pip
* Dans le fichier de test ajouter au debut la ligne
```
import HtmlTestRunner
```
* Puis remplacer la section
```
if __name__ == '__main__':
	unittest.main()
```
* Par :
```
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
```
* Lancer vos tests :
```
python test.py
```
* Un rapport au format HTML devrait être généré dans le dossier reports 
* Ouvrer le avec un navigateur web

## Générer un rapport de test pour Selenium
* Pour selenium, si vous utiliser aussi unittest, vous pouvez suivre la même procédure que pour les tests unitaires
* Si vous avez utilisez pytest, il faut installer le module pytest-html et ajouter l'option --html=report.html lors du lancement de pytest pour l'execution de vos tests selenium

## Lire et exploiter ces rapports

* Ouvrir les deux rapports dans un navigateur
* A quoi correspondent le nombre de test ? De testcases ?
* Pouvez vous accéder au détail de chaque test ?
* A quoi va servir ce type de rapport ?
* Quelles métriques pouvons nous exploiter pour suivre l'évolution de l'exécution des tests sur le projet ?

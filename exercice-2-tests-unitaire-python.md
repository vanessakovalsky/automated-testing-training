# Exercice 2 - Ecrire ses premiers tests unitaire

## Pré-requis

* Avoir suivi l'exercice 1

## Installation de pyTest

* Ajouter dans les dépendances de Python le module `pytest`
* Construire l'image avec cette nouvelle dépendance
* Lancer un conteneur à partir de cette nouvelles images
* Se connecter dans le conteneur en bash et vérifier que la commande pytest fonctionne

## Ecriture des tests

* Dans le dossier app/tests un fichier test.py existe déjà
* Importer pytest
* Ecrire un premier test qui va vérifier que la fonction add de la class application, renvoie bien comme valeur 'Application ajoutée' 
* Pour vous aider la documentation pour l'écriture des tests est ici : https://docs.pytest.org/en/7.2.x/how-to/assert.html 

## Exécution des tests

* Construire de nouveau l'image (pour que les tests que vous avez ajouter soit pris en compte)
* Lancer un conteneur a partir de cette nouvelle image
* Se connecter au conteneur en bash
* Lancer le fichier test.py avec la commande pytest chemin/vers/le/fichier/test.py
* Vous devriez obtenir un résultat ressemblant à celui-ci (avec des noms et des résultats différents):
```
pytest test.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-7.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test.py F                                                    [100%]

================================= FAILURES =================================
______________________________ test_function _______________________________

    def test_function():
>       assert f() == 4
E       assert 3 == 4
E        +  where 3 = f()

test.py:6: AssertionError
========================= short test summary info ==========================
FAILED test.py::test_function - assert 3 == 4
============================ 1 failed in 0.12s =============================
```

## Bonus - Ecrire les tests de l'ensemble de l'application

* Pour chaque fonction, concevoir et écrire le tests unitaire qui permet de tester deux éléments :
    * si les données passés sont bonnes, le resultat est OK (conforme à ce qui est attendu)
    * si les données passés ne correspondent pas à l'attendu, vérifier qu'on a bien une erreur en retour
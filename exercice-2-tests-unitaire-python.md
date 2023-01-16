# Exercice 2 - Ecrire ses premiers tests unitaire

## Pré-requis

* Avoir suivi l'exercice 1

## Ecriture des tests

* Dans le dossier app/ créer un fichier test.py
* Importer unittest
* Ecrire un premier test qui va vérifier que la fonction add de la class application, renvoie bien comme valeur 'Application ajoutée' 
* Pour cela : 
    * Importer le module unittest
    * Importer la classe Application depuis le module application
    * créer une classe TestApplication
    * Créer une méthode : test_add_application 
    * Dans cette méthode : appeler votre fonction add de la classe application
    * Puis toujours dans la méthode vérifier que le résultat renvoyé par votre fonction correspond à 'Application ajoutée'
    * Ensuite au même niveau que la place initialiser le lancement des tests avec : 
    ```
    if __name__ == '__main__':
	unittest.main()
    ```
* Pour vous aider la documentation pour l'écriture des tests est ici : https://docs.pytest.org/en/7.2.x/how-to/assert.html 

## Exécution des tests

* Construire de nouveau l'image (pour que les tests que vous avez ajouter soit pris en compte)
* Lancer un conteneur a partir de cette nouvelle image
* Se connecter au conteneur en bash
* Lancer le fichier test.py avec la commande python chemin/vers/le/fichier/test.py
* Vous devriez obtenir un résultat ressemblant à celui-ci (avec des noms et des résultats différents):
```
/app/test.py:24: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(contenu_liste,'Liste des applications')
.E
======================================================================
ERROR: test_ajout_machine (__main__.TestMachines.test_ajout_machine)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/app/test.py", line 29, in test_ajout_machine
    ajout_machine = Machine.add((),('mes donnees à écrire',"fichier=machines.json"))
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/machine.py", line 17, in add
    with open(self.fichier, 'w') as f:
              ^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'fichier'

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (errors=1)
```

## Bonus - Ecrire les tests de l'ensemble de l'application

* Pour chaque fonction, concevoir et écrire le tests unitaire qui permet de tester deux éléments :
    * si les données passés sont bonnes, le resultat est OK (conforme à ce qui est attendu)
    * si les données passés ne correspondent pas à l'attendu, vérifier qu'on a bien une erreur en retour

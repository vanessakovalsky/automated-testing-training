# Exercice 4 - Tester une IHM avec selenium

## Objectifs

Cet exercice a pour objectif
* d'être capable d'installer selenium et ses dépendances
* de savoir ecrire un tests d'IHM avec Selenium en Python
* de pouvoir exécuter les tests écrit avec Selenium

## Pré-requis
* Avoir docker installé
* Avoir des connaissances de base en Python (qui sera utilisé dans cet exemple)

## Installation et configuration d'un projet de test

* Créer un projet vierge dans votre environnement de développement
* Pour fonctionner Selenium a besoin d'accéder à un navigateur, pour cela nous utilisons une image docker (adapter le chemin du volume pour le faire correspondre à votre projet): 
```
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.7.2-20221219
```

* Dans votre projet, créer un fichier requirements.txt avec le contenu suivant
```
selenium
```
* Installer les dépendances
```
pip install -r requirements.txt
```
* Dans votre projet, créer un fichier testSelenium.py avec le contenu suivant qui permet de configurer le projet et d'exécuter les tests dans votre conteneur:
```
import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        """Explicitly create a browser instance."""
        print("Test Execution Started")
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        self.browser = webdriver.Remote(
            desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )
        self.addCleanup(self.browser.quit)

if __name__ == '__main__':
    unittest.main(verbosity=2)
```
* Ici nous avons :
    * Créer une classe de test avec unittest
    * Définit avec la fonction set up l'appel au navigateur présent dans le conteneur avec ces différentes options
* Pour lancer les tests
```
python testSelenium.py
```
* Ici il ne se passe pas grand chose, aucun test n'a été écrit encore

## Premiers tests

* Nous allons commencer par ajouter un test qui va simplement ouvrir la page de recherche de Google :
```
    def test_page_title(self):
        """Assert that title of page says 'Google'."""
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
```
* Ce test se décompose comme suit :
    * la fonction get sur le browser permet de demander à Selenium d'ouvrir un navigateur et de se rendre sur l'url demandé
    * Puis assertIn est une fonction de vérification de unittest qui permet de vérifier que le titre de la page du navigateur correpond bien à Google
* Pour aller plus loin, nous faisons un deuxième test qui va faire une recherche sur le terme Red Hat:
```
    def test_search_page_title(self):
        """Assert that Google search returns data for 'Red Hat'."""
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
        element = self.browser.find_element_by_id('lst-ib')
        assert element is not None
        element.send_keys('Red Hat' + Keys.RETURN)
        assert self.browser.title.startswith('Red Hat')
```
* Cette fois ci nous utilisons les fonction qui permette de rechercher un élément dans le HTML par son identifiant, puis la fonction qui permet d'ecrire du texte (send_keys) 
* Lancer ces différents tests
* Rajouter un autre test pour aller chercher le site officiel de redhat (redhat.com) sur la page et l'ouvrir.
* Pour vous aider la documentation de Selenium Python est ici : https://selenium-python.readthedocs.io/ 


## Pour aller plus loin - Tester un site de ecommerce

* Ce site : https://www.saucedemo.com/ est un site de ecommerce faux qui permet de faire des tests
* A l'aide de python selenium, écriver les scénarios de tests pour les cas suivant :
    * se connecter
    * Afficher la liste de produit
    * Afficher le détail d'un produit
    * Ajouter un produit au panier
    * Voir son panier
    * Valider son panier
* Des exemples avec pytests sont disponible ici : https://github.com/PaulVaroutsos/SauceDemo-Automation/tree/master/tests 
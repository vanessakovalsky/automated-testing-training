# Exercice 5 - Automatiser ses tests avec Robot Framework

## Objectifs

Cet exercice a pour objectifs
* d'ecrire des scénarios de tests automatisés avec Robot Framework
* d'exectuer ces scénarios de tests

## Pré-requis

* avoir docker installé
* avoir un environnement de développement python
* avoir des tests Selenium écrit en Python
* Avoir un driver installé pour son navigateur :
    * Pour chrom : https://chromedriver.chromium.org/downloads 
    * Pour firefox : https://www.selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/firefox.html 

## Installation de robot Framework

* dans un environnement python, ajouter à votre fichier requirements.txt la ligne suivante
```
robotframework
```
* Installer cette dépendance
```
pip install -r requirements.txt
```
* Robot Framework peut maintenant être utilisé pour écrire vos scénarios de tests

## Scenario de test IHM avec la bibliothèque Selenium

* Pour executer des scénarios de tests RobotFramework s'appuie sur des librairies
* Pour commencer nous allons utiliser la bibliothèque SeleniumLibrary, qui doit être rajouter dans le requirements.txt
```
robotframework-selenium2library 
webdrivermanager
```
* Puis nous lançons l'installation
```
pip install -r requirements.txt
```
* Ensuite nous créons un fichier searchgoogle.robot avec le contenu suivant :
```
*** Settings ***
Library  Selenium2Library
Suite Setup     Open Browser    ${URL}   ${BROWSER}
Suite Teardown  Close All Browsers


*** Variables ***
${URL}              https://www.google.com
${BROWSER}          Chrome
${search_form}      css=form[name=f]
${search_query}     css=input[name=q]
${search_term}      Red Hat

*** Test Cases ***
Google Search
    Wait Until Element Is Visible  ${search_form}
    Wait Until Element Is Visible  ${search_query}
    Input Text      ${search_query}   ${EMPTY}
    Input Text      ${search_query}   ${search_term}
    Submit Form
```

* Pour lancer le test
```
robot searchgoogle.robot
```
* Vous obtenez alors un navigateur qui se lance, ouvre google et fais votre recherche, ainsi qu'un résultat dans votre terminal
* La documentation pour la rédaction des tests est ici : https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html 


## Pour aller plus loin - Tester des API avec Robot Framework

* Voir ici : https://testersdock.com/api-testing-robot-framework/ 
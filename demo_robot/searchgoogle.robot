*** Settings ***
Library  Selenium2Library
Suite Teardown  Close All Browsers

*** Variables ***
${URL}              http://www.google.com
${BROWSER}          Firefox
${search_form}      css=form[name=f]
${search_query}     css=input[name=q]
${search_term}      Red Hat

*** Test Cases ***
Launch Browser
    Open Browser   ${URL}  ${BROWSER} 
Google Search
    Wait Until Element Is Visible  ${search_form}
    Wait Until Element Is Visible  ${search_query}
    Input Text      ${search_query}   ${EMPTY}
    Input Text      ${search_query}   ${search_term}
    Submit Form
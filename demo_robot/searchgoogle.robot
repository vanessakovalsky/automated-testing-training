*** Settings ***
Library  SeleniumLibrary
Suite Teardown  Close All Browsers

*** Variables ***
${URL}              http://www.google.com
${BROWSER}          Chrome
${search_query}     css=input[name=q]
${search_term}      Red Hat
${CHROMEDRIVER_PATH}        /snap/bin/chromium.chromedriver
${ACCEPT_COOKIES_BUTTON}   xpath://*[contains(text(), 'Tout accepter')]
${search_button}                                    css=input.lsb

*** Test Cases ***
Launch Browser
    ${chrome_options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Open Browser    ${URL}    ${BROWSER}    options=${chrome_options}      executable_path=${CHROMEDRIVER_PATH}

Google Search
    Page Should Contain Button  id:L2AGLb
    Click Element  id:L2AGLb
    Wait Until Element Is Visible  ${search_query}
    Input Text  ${search_query}  ${EMPTY}
    Input Text  ${search_query}  ${search_term}

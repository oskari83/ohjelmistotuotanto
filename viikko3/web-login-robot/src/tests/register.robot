*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset and Go Register Page 

*** Test Cases ***
Register With Valid Username And Password
    Set Username  completelyNew
    Set Password  jukka123
    Set Password Confirmation  jukka123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ju
    Set Password  jukka123
    Set Password Confirmation  jukka123
    Submit Register Credentials
    Register Should Fail With Message  Username too short (minimum 3 characters)

Register With Valid Username And Too Short Password
    Set Username  MaijaMeikalainen
    Set Password  juk
    Set Password Confirmation  juk
    Submit Register Credentials
    Register Should Fail With Message  Password too short (minimum 8 characters and has to include numbers)

Register With Nonmatching Password And Password Confirmation
    Set Username  hattivatti
    Set Password  jukka12345
    Set Password Confirmation  jukkka44444
    Submit Register Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Register Test Account
    Go To Login Page
    Login Page Should Be Open
    Set Username  Tester
    Set Password  jukka123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Register Test Account 2
    Go To Login Page
    Login Page Should Be Open
    Set Username  Te
    Set Password  jukka123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Register Succeed Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${passwordconfirmation}
    Input Password  password_confirmation  ${passwordconfirmation}

Reset And Go Register Page
    Reset Application
    Go To Register Page

Register Test Account
    Set Username  Tester
    Set Password  jukka123
    Set Password Confirmation  jukka123
    Submit Register Credentials
    Register Should Succeed

Register Test Account 2
    Set Username  Te
    Set Password  jukka123
    Set Password Confirmation  jukka123
    Submit Register Credentials
    Register Should Fail With Message  Username too short (minimum 3 characters)

Submit Credentials
    Click Button  Login

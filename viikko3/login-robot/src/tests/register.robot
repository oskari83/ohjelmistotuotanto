*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jukka  jukka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  jukka123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ok  jukka123
    Output Should Contain  Username too short (minimum 3 characters)

Register With Valid Username And Too Short Password
    Input Credentials  sami  viisi
    Output Should Contain  Password too short (minimum 8 characters and has to include numbers)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  sami  viisitoista
    Output Should Contain  Password too short (minimum 8 characters and has to include numbers)

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
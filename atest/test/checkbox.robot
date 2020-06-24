*** Settings ***
Library		Browser
Test Setup	Run Keywords 	Open Browser	chrome	AND	Go To	http://localhost:7272/checkbox_and_radio.html
Test Teardown	Close Browser

*** Test Cases ***
Checkbox Should Be Checked
    Checkbox Should Be	css=[name=can_send_email]	checked	

Checkbox Should Not Be Checked
    Checkbox Should Be	css=[name=can_send_sms]		unchecked

Check Checkbox
    Checkbox Should Be	css=[name=can_send_sms]		unchecked
    Check Checkbox	css=[name=can_send_sms]
    Checkbox Should Be	css=[name=can_send_sms]		checked

Uncheck Checkbox
    Checkbox Should Be	css=[name=can_send_email]	checked
    Uncheck Checkbox	css=[name=can_send_email]
    Checkbox Should Be	css=[name=can_send_email]	unchecked

*** Settings ***
Documentation   Ubuntu apt-get install negative test cases
Library         AptGetInstall


*** Test Cases ***
2001_apt_get_install_unexisting_package
    ${stdout}  ${stderr}    apt get install     unexiting_package_name
    should contain          ${stderr}           Unable to locate package unexiting_package_name

2002_apt_get_install_unsupported_local_package
    ${stdout}  ${stderr}                        apt get install     -y ./TestData/text.txt
    should contain          ${stderr}           Unsupported file ./TestData/text.txt given on commandline

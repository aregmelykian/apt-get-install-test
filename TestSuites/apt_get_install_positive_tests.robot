*** Settings ***
Documentation   Ubuntu apt-get install positive test cases
Library         AptGetInstall


*** Test Cases ***
1001_apt_get_install_with_out_package_param
    ${stdout}  ${stderr}                        apt get install
    should contain          ${stdout}           0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded
    should be equal         ${stderr}           ${empty}

1002_apt_get_install_package_from_repo
    ${stdout}  ${stderr}                        apt get install     nano
    should contain          ${stdout}           0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded
    should be equal         ${stderr}           ${empty}

    ${stdout}  ${stderr}                        run command         which nano
    should be equal         ${stdout}           /bin/nano
    should be equal         ${stderr}           ${empty}

1003_apt_get_install_package_from_local_deb
    ${stdout}  ${stderr}                        apt get install     -y ./TestData/rolldice_1.14-2_amd64.deb
    should contain          ${stdout}           0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded
    should be equal         ${stderr}           ${empty}

import pytest
from AptGetInstall import AptGetInstall


@pytest.fixture(scope='module')
def bash():
    return AptGetInstall()


@pytest.mark.usefixtures('bash')
class TestAptGetInstallPositive:

    @staticmethod
    def success_string(upgraded=0, installed=1):
        return '{} upgraded, {} newly installed'.format(upgraded, installed)

    def test_apt_get_install_with_out_package_param(self, bash):
        stdout, _ = bash.apt_get_install()
        assert self.success_string(installed=0) in stdout

    def test_apt_get_install_package_from_repo(self, bash):
        stdout, _ = bash.apt_get_install('nano')
        assert self.success_string() in stdout

        stdout, _ = bash.run_command('which nano')
        assert stdout == '/bin/nano'

    def test_apt_get_install_package_from_local_deb(self, bash):
        stdout, _ = bash.apt_get_install('-y ./TestData/rolldice_1.14-2_amd64.deb')
        assert self.success_string() in stdout


@pytest.mark.usefixtures('bash')
class TestAptGetInstallNegative:

    def test_apt_get_install_unexisting_package(self, bash):
        _, stderr = bash.apt_get_install('unexiting_package_name')
        assert 'Unable to locate package unexiting_package_name' in stderr

    def test_apt_get_install_unsupported_local_package(self, bash):
        _, stderr = bash.apt_get_install('-y ./TestData/text.txt')
        assert 'Unsupported file ./TestData/text.txt given on commandline' in stderr

    def test_apt_get_install_from_repo_no_permission(self, bash):
        _, stderr = bash.apt_get_install('gedit', sudo=False)
        assert 'Permission denied' in stderr

    def test_apt_get_install_package_from_local_deb_no_permission(self, bash):
        _, stderr = bash.apt_get_install('-y ./TestData/rolldice_1.14-2_amd64.deb', sudo=False)
        assert 'Permission denied' in stderr

from Bash import Bash


class AptGetInstall(Bash):

    def apt_get_install(self, package='', sudo=True):
        """
        :param package: package name to be installed
        :param sudo: run as sudo or not
        :return: list [stdout, stderr]
        """
        command = 'apt-get install ' + package
        return self.run_command(command, sudo)

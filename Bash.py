from subprocess import PIPE, Popen


class Bash:

    @staticmethod
    def run_command(command, sudo=True):
        """
        :param command: string with a command to run
        :param sudo: run as sudo or not
        :return: list [stdout, stderr]
        """
        if sudo:
            command = 'echo docker | sudo -S ' + command
        process = Popen(args=command, stdout=PIPE, stderr=PIPE, shell=True)
        r = [x.decode('utf-8').strip() for x in process.communicate()]
        return r

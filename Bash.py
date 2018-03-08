from subprocess import PIPE, Popen


class Bash:

    # should not be static due to robot framework restrictions
    def run_command(self, command, sudo=False):
        """
        :param command: string with a command to run
        :return: list [stdout, stderr]
        """
        if sudo:
            command = 'sudo ' + command
        process = Popen(args=command, stdout=PIPE, stderr=PIPE, shell=True)
        r = [x.decode('utf-8').strip() for x in process.communicate()]
        return r

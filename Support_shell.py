from subprocess import call as shell_exec
import cmd, readline
from Text_exit import Console
from Config_manager import ConfigMan
Show = Console()


class Shell(cmd.Cmd):
    intro = """ + Tool for quick access and diagnose of clients."""
    prompt = 'Support>'
    debug = 'False'
    clients_dict = ''
    hosts = ''
    cfg = ''

    def __init__(self, home, hosts, clients_dict, ssh_bin="ssh", debug=True):
        super(Shell, self).__init__()
        self.hosts = hosts
        self.clients_dict = clients_dict
        self.ssh_bin = ssh_bin
        self.debug = debug
        self.cfg = ConfigMan(home)

    def do_connect(self, cli_input):
        """Connect to a server. Expects server name or hostname."""

        if not cli_input:
            print(Show.error("Connect expects server name or hostname."))
            return

        elif cli_input not in self.clients_dict:
            print(Show.error("Server " + cli_input + " not found!"))
            return

        else:
            # Only gets here if cli_input not empty and if it is a valid server
            print("Connecting to " + Show.info(cli_input) +
                  " + At ip " + Show.warning(self.clients_dict[cli_input]))

            if self.debug:
                print(Show.debug("Running in debug mode: " +
                                 self.clients_dict[cli_input]))
                shell_exec(self.ssh_bin + " " + "localhost", shell=True)

            else:
                shell_exec(self.ssh_bin + " " +
                           self.clients_dict[cli_input], shell=True)

    def complete_connect(self, text, cli_input, start_index, end_index):
        if text:
            return [host for host in self.hosts
                    if host.startswith(text)]

        else:
            return self.hosts

    @staticmethod
    def help_connect():
        print("Connect to a server. Expects server name or hostname.\n" +
              Show.info("Usage: connect <SERVER|HOSTNAME>"))
        return

    def do_config (self, cli_input):
        """Handle configuration of the app"""
        cli_input_array = cli_input.split()
        print( cli_input_array)

         # handle display of configs
        if cli_input in self.cfg.get_opt():
            # Ensure that option passed is supported and display the current value
            print( cli_input + " = " + self.cfg.get_opt(cli_input))


        # handle set configs
        elif len(cli_input_array) >= 2 \
                and cli_input_array[0] == "set" :
            # Check if the argument set was provided
            if cli_input_array[1] in self.cfg.get_opt() \
                    and len(cli_input_array) > 2:

                if self.cfg.set_opt( cli_input_array[1], cli_input_array[2]):
                    print(Show.info("Option " + cli_input_array[1] + " set."))

                else:
                    print(Show.error("Error setting option " +
                                     cli_input_array[1] + "."))


            elif len(cli_input_array) <= 2:
                # Print message if a value was not passed
                print(Show.error("Config option " + cli_input_array[1] +
                      " expects a value."))

            elif cli_input_array[1] not in self.cfg.get_opt() and (cli_input_array[2]) > 0:
                # Check if the option passed
                print(Show.error("Config option " + cli_input_array[1] +
                      "not found.") + Show.info(" Use one of the following:"))
                print ("\t+ " .join(self.cfg.get_opt().keys()))


        else:
            print(Show.error("You need to pass a config option."))
            # Print a list of supported options
            print("\t".join(self.cfg.get_opt()),end=' ',)
            print()

    @staticmethod
    def do_EOF():
        print("")
        return True

    @staticmethod
    def emptyline():
        pass

    @staticmethod
    def postloop(self):
        print ()


""" End of Support_shell class """

from colorama import Fore,Back


class Console():

    def info(self, text):
        return Fore.LIGHTGREEN_EX + text + Fore.RESET

    def error(self, text):
        return Fore.LIGHTRED_EX + text + Fore.RESET

    def warning(self, text):
        return Fore.LIGHTYELLOW_EX + text + Fore.RESET

    def debug(self, text):
        return Fore.LIGHTBLACK_EX + text + Fore.RESET

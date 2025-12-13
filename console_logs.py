from colorama import Fore

class Logs:
  SETTINGS_FILE = "settings.json"

  @staticmethod
  def success(msg):
    print(f"[ {Fore.GREEN}LOADED{Fore.WHITE} ]: {msg}")

  @staticmethod
  def error(msg):
    print(f"[ {Fore.RED}ERROR{Fore.WHITE} ]: {msg}")

  @staticmethod
  def warning(msg):
    print(f"[ {Fore.YELLOW}WARN{Fore.WHITE} ]: {msg}")

  @staticmethod
  def ignore(msg):
    print(f"[{Fore.CYAN} IGNORED {Fore.WHITE}]: {msg}")
import colorama
a =dir(colorama)
print(a)


from colorama import *
print(Fore.RED + Back.YELLOW + Style.BRIGHT + "Hello, colorful world!" + Style.RESET_ALL)
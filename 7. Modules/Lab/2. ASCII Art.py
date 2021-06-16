from pyfiglet import figlet_format


def print_art_msg(msg):
    ascii_art = figlet_format(msg)
    print(ascii_art)


print_art_msg(input())

import subprocess

def terminal_talker(text):
    cow_speak = 'cowsay '  + text
    print(cow_speak)
    translated = subprocess.check_output(cow_speak)
    print(translated)
    return translated
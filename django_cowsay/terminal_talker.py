import subprocess

def terminal_talker(text):
    cow_speak = 'cowsay '  + text
    translated = subprocess.check_output(cow_speak, shell=True).decode()
    print(translated)
    return translated
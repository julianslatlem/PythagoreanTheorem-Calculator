import os

os.system("")

def colored(r,g,b,text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def error(message,code):
    print(colored(255,0,0,f'ERROR: {message} CODE: {code}'))
    
def warning(message):
    print(colored(255,255,0,f'WARNING: {message}'))
    
def info(message):
    print(colored(175,175,175,f'INFO: {message}'))
    
def misc(message):
    input(colored(175,175,175,f"{message}"))
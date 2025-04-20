import time

def consoleprint(message, color=None):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "black": "\033[98m",
        "reset": "\033[0m"
    }
    if color:
        print(colors[color] + message + colors["reset"])
    else:
        print(message)

def log(message, color="yellow"):
    output = f"[{time.strftime('%H:%M:%S')}] {message}"
    consoleprint(output, color=color)

    with open("log.txt", "a") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}] {message}\n")

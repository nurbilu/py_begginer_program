import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_color_to_text(text, color):
    return f"{color}{text}{Style.RESET_ALL}"

def colorize_text():
    clear_terminal()
    print("Select a color:")
    print("1 - Red")
    print("2 - Green")
    print("3 - Blue")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        color = Fore.RED
    elif choice == '2':
        color = Fore.GREEN
    elif choice == '3':
        color = Fore.BLUE
    else:
        print("Invalid choice. Defaulting to white.")
        color = Fore.WHITE

    text = input("Enter the text you want to colorize: ")
    colored_text = add_color_to_text(text, color)
    
    print(f"Colored text: {colored_text}")
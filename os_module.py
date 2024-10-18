import os
from colorama import Fore, Style

def list_directory_contents():
    try:
        list_directory = os.listdir(path)
        print("-" * 50)
        print("The following directory contains the following\n")
        print(f"--- {Fore.GREEN}{path}{Style.RESET_ALL} ---")
        print("-" * 50)
        for item in list_directory:
            print(f"{Fore.CYAN}{item}{Style.RESET_ALL}")
            print("-" * 50)
    except FileNotFoundError:
        print("-" * 50)
        print(f"Error: The directory\n--- {Fore.RED}{path}{Style.RESET_ALL} ---\n was not found.")
        print("-" * 50)
    except PermissionError:
        print("-" * 50)
        print(f"Error: You do not have permission to access\n--- {Fore.RED}{path}{Style.RESET_ALL} ---")
        print("-" * 50)
    except ValueError:
        print("-" * 50)
        print(f"Error: Try again.")
        print("-" * 50)

    
print("-" * 50)
path = input("Enter Full Directory Path Below\n")

if isinstance(path, str):
    list_directory_contents()

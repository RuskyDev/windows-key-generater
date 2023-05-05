import random
import os
import win32api
from colorama import Fore, Style, init
init()
os.system("cls")
os.system("@echo off")
os.system("@title Windows Key Generater [PRO]")


def generate_key():
    groups = []
    for i in range(5):
        group = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=5))
        groups.append(group)
    key = '-'.join(groups)
    return key

def is_valid_key(key):
    try:
        result = win32api.IsProductKeyValid(key)
    except:
        return False
    return result == 1

num_keys = int(input("How many Windows 10 Pro keys would you like to generate? "))
keys = [generate_key() for _ in range(num_keys)]

valid_keys = []
valid_count = 0
invalid_count = 0

for key in keys:
    if is_valid_key(key):
        valid_keys.append(key)
        valid_count += 1
    else:
        invalid_count += 1

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
valid_filename = os.path.join(desktop_path, 'valid_windows_10_keys.txt')

with open(valid_filename, 'w') as f:
    for key in valid_keys:
        f.write(key + '\n')

print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}+{Fore.WHITE}] {Fore.GREEN}{valid_count}{Fore.WHITE} Windows 10 Pro keys are valid and have been saved to {Fore.GREEN}{valid_filename}.{Fore.WHITE}")
print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}+{Fore.WHITE}] {Fore.RED}{invalid_count}{Fore.WHITE} Windows 10 Pro keys are invalid.")

os.system("pause>nul")
generate_key()
from art import text2art
from colorama import Fore

# pseudocode

# ask the user to input name
name = input(Fore.LIGHTYELLOW_EX + "Please enter your name: ")
# ask the user to input age
# validate age
while True:
    age = int(input(Fore.LIGHTYELLOW_EX + "Please enter your age: "))
    if age <= 0 or age > 100:
        print("Invalid Input! Please enter a valid age: ")
    else:
        break
# ask the user to input dream job
dream_job = input(Fore.LIGHTYELLOW_EX + "Please enter your dream job: ")
# add art to name
art_name = text2art(name, font='block', chr_ignore=True)
# add art to age
art_age = text2art(str(age), font='block', chr_ignore=True)
# add art to dream job
art_dream_job = text2art(dream_job, font='block', chr_ignore=True)
# print name in a fancy way
print(Fore.LIGHTMAGENTA_EX + text2art("Name: ", font='block', chr_ignore=True))
print(Fore.LIGHTCYAN_EX + text2art(name, font='block', chr_ignore=True))
# print age in a fancy way
print(Fore.LIGHTMAGENTA_EX + text2art("Age: ", font='block'))
print(Fore.LIGHTCYAN_EX + text2art(str(age), font='block', chr_ignore=True))
# print dream job in a fancy way
print(Fore.LIGHTMAGENTA_EX + text2art("Dream Job: ", font='block'))
print(Fore.LIGHTCYAN_EX + text2art(dream_job, font='block', chr_ignore=True))
# add printing animation
# add printing animation function

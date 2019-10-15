import random

human_choice = input("Rock, paper or scissors?")

stupidinput = False

if (human_choice) == ("Rock"):
    print("You picked rock.")
if (human_choice) == ("Paper"):
    print("You picked Paper.")
if  (human_choice) == ("Scissors"):
    print("You picked Scissors.")
if (human_choice) != (("Rock") or ("Paper") or ("Scissors")):
    print("You didn't select a proper input. You lose.")
    stupidinput = True

computer_choice = random.randint(1,3)

if (computer_choice == 1) & (stupidinput == False):
    print("The computer picked Rock.")
if (computer_choice == 2) & (stupidinput == False):
    print("The computer picked paper.")
if (computer_choice == 3 & stupidinput == False):
    print("The computer picked scissors.")
import random
l=("rock","paper","scissor")
comp=random.choice(l)
user=input("enter your choice:")
if comp==user:
    print("it is a tie game")
elif comp=="rock" and user=="scissor":
    print("computre has bet u with rock.")
elif comp=="scissor" and user=="paper":
    print("computer has cut u with scissor")
elif comp=="paper" and user=="rock":
    print("computer is caughtu with paper")
else:
    print("you won upon computr")

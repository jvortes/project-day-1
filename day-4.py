import random
# random_integer = random.randint(1,2)
# if random_integer == 1:
#     print("Heads")
# else:
#     print("Tails")

# list
# fruits = [item1, item2]
# allows for grouping items by categories

# state1 = "Delaware"
# state2 = "Texas"

# states_of_america = ["Delaware","Pennsylvania","New Jersey"]

# #prints the first item within the list. First item begins with index 0 or [0]
# print(states_of_america[0])

# #prints the first item at the end of the list
# print(states_of_america[-1])

# #adds item on the the end of the list
# states_of_america.append("JuliusLand")
# print(states_of_america)

# Import the random module here

# Split string method
# names_string = input("\nGive me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above

#Write your code below this line
# num_items = len(names)
# rand_names = random.randint(0, num_items - 1)
# person_to_pay = names[rand_names]
# print(f"Person who will pay the meal today is {person_to_pay}")


cpu_choices = ["Rock", "Paper", "Scissors"]
num_choices = len(cpu_choices)
rand_choices = random.randint(0, num_choices - 1)

choice = print("\nEnter Rock: 0 \nPaper: 1 \nScissors:2\n")

if rand_choices == choice:
    print("Tie Game!")
elif rand_choices == 0 and choice == 2:
    print("You lose!")
elif choice == 2 and rand_choices == 2:
    print("You win!")
elif rand_choices > choice:
    print("you lose")
elif choice > rand_choices:
    print("You win!")
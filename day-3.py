print('''
      
           /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
      
      ''')

print("Welcome, brave adventurers, to the shrimmering shores of treasure island")
print("A world shrouded in mystery and brimmering with untold riches..")
print("\nWhile this isle beckons those with a thirst for adventure know that it is also filled with chilling dangers...")

direction = (input("\nWould you like to go left (L) into reptilian forest, or right (R) to take a boat across the lake..?: ")).upper()

if direction == "L":
    print("You pick up a bag which holds a sword, and torch; thus, begins your journey..")

    print("\nYour path forks into 3 directions, each, blocked by thick otherworldly vines.. Nothing a mighty sword cannot handle.")
    path = (input("Choose your path; left (L), center (C), or right (R)? R: ")).upper()
        
    if path == "C": 
        print("\n""HACK/SLASH!""")
        print("As you hack away at the vines, pythons creep through; you are bitten but use your torch kills off the snakes.")

        print("\n with little time left, you notice a cabin in the distance, and a cave to your right. Which will you choose..?")
        choice = (input("cabin or cave: ")).lower
        if choice == "cabin":
            print("\nyou are greeted by an elderly woman at the cabin. She provides antidote for the venom.")
            print("The kind woman also provides a hot meal. As you eat, your stomache aches in agony. You feel yourself slipping away as the elderly woman continues to smile.. You have been poisoned.")
            print("\nAnother soul forever trapped within treasure island... GAME OVER\n")
        else:
            print("within the cave with little time to spare, a bag lies on the ground with antivenom and a key.")
            print("As you venture through the cave you across a door; the key unlocks it.")
            print("The room is filled with treasures of gold.\nCongratz, you have defeated treasure island and live to tell it tale...\n")

    
    elif direction == "L" or "R":
        print("\n""HACK/SLASH!""")
        print("As you hack away at the vines, you walk the path and become surrounded by blood thirsty crocodiles and are torn to pieces..")
        print("Another soul forever trapped within treasure island... GAME OVER\n")


else:
    print("\nAs your journey begins across the lake, the sound of sizzling reaches your ear, and a chemical smell, faint, becomes more distinct.. ")
    print("You look overboard and see acid melting the boat slowly. In agony, you meet your untimely death..")
    print("\nAnother soul forever trapped within treasure island... GAME OVER\n")


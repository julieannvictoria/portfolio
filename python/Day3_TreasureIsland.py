print('''          ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\\_`"-._
             .'     / /                    \ \\     '.
             |=====/o/======================\o\\=====|
             |____/_/________..____..________\_\\____|
             /   _/ \_     <_o#\__/#o_>     _/ \\_   \\
             \\_________\\####/_________/
              |===\!/========================\\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \\() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \\__     '-.\\uuu/.-'    __/ \\__ |
              |==== .'.'^'.'.====|
          jgs |  _\\o/   __  {.' __  '.} _   _\\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
      ''')
choice = input('''
      Welcome to Treasure Island. \n
      Your mission is to find the treasure.\n
      You\'re at a corss road. Where do you want to go? \n
      Type "left" or right"\n
      ''')

if choice == 'left':
    choice = input(''' You\'ve come to the lake.
                    There is an island in the middle of the lake.\n
                    Type "wait" to wait for a boat.
                    Type "swim" to swim across.\n
                    ''')
    if choice == 'wait':
      choice = input('''You arrive at the island unharmed.
                    There is a house with 3 doors.\n
                    One red, one yellow and one blue. Which colour do you choose?\n
                    ''')
      if choice == 'yellow':
        print('You Win!')
      elif choice == 'blue':
        print('Eaten by beasts. Game Over')
      else:
        print('Game Over')
    else:
      print('Attacked by trout. Game Over')
else:
    print('Fall into a hole. Game Over.')
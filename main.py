player_name =""
player_age = 0
player_energy = 5
player_inventory = []
player_location = "Beach"
game_running = True

def collect_items(item):
        if item not in player_inventory:
            player_inventory.append(item)
            print(f"You collected a {item}!")
        else:
            print(f"You already have the {item}.")

def show_menu():
        print("1. Explore locations.\n2. Check inventory.\n3. Check player status.\n4. Quit the game.")

def show_inventory():
    if not player_inventory:
        print("Your inventory is empty.")
    else:
        for item in player_inventory:
            print(item)

def show_status():
        print(f"Player name: {player_name}\n player age: {player_age}\n energy: {player_energy}\n location: {player_location}")

def explore_island():
        global player_location, player_energy, game_running

        print("1. Beach\n2. Jungle\n3. Cave\n4. Old Bridge\n5. Lighthouse")
        try:
            player_choice = int(input("Choose a location: "))
        except ValueError:
            print("Please enter a valid number!")
            return
        
        locations = {
            1: "Beach",
            2: "Jungle",
            3: "Cave",
            4: "Old Bridge",
            5: "Lighthouse"
        }
        
        if player_choice not in locations:
            print("Invalid choice. Try again!")
            return
        
        new_location = locations[player_choice]

        if new_location == player_location:
            print(f"You are already at the {player_location}.")
            return
        
        if player_energy <= 0:
            print("Not enough energy!")
            return
        
        if new_location == "Cave" and "lantern" not in player_inventory:
            print("It's too dark! You need a lantern.")
            return
        elif new_location == "Old Bridge" and "rope" not in player_inventory:
            print("The bridge is broken! You need a rope.")
            return
        elif new_location == "Lighthouse":
            if "rope" not in player_inventory or "lantern" not in player_inventory:
                print("You need both a rope and a lantern to enter!")
                return
            
            player_energy -= 1
            
            print("Congratulations! You found the Lost Lighthouse. You won!")
            player_location = new_location
            game_running = False
            return

            
        player_energy -= 1
        player_location = new_location

        if new_location == "Beach":
            collect_items("lantern")
        elif new_location == "Jungle":
            collect_items("rope")

        print(f"You travelled to the {player_location}!")
        print(f"Remaining energy: {player_energy}")        

def main():
    global player_name, player_age
    global player_energy, player_inventory
    global player_location, game_running

    print("Welcome to Mystery Island!")


    player_name = input("Enter your name: ")
    player_age = int(input("Enter your age: "))


    print(f"Welcome, {player_name}! you are {player_age} years old, have {player_energy} energy and are currently at the {player_location}.")


    while True:
        #reset player state for a new game
        player_energy = 5
        player_inventory = []
        player_location = "Beach"
        game_running = True
        collect_items("lantern")

        # main game loop
        while game_running:
            show_menu()

            try:
                player_choice = int(input("Choose an option: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if player_choice == 1:
                explore_island()
            elif player_choice == 2:
                show_inventory()
            elif player_choice == 3:
                show_status()
            elif player_choice == 4:
                game_running = False
            else:
                print("Invalid choice. Try again.")

        # Ask whether the player wants another game
        while True:
            replay = input("Would you like to play again? (yes/no): ").strip().lower()

            if replay == "yes":
                break
            elif replay == "no":
                print("Thanks for playing!")
                return
            else:
                print("Plesase enter yes or no.")

if __name__ == "__main__":
    main()
import random
playing = True

rounds=int(input("How many rounds would you like to play? "))
player_score=0
computer_score=0
for i in range(rounds):
    
    choices =["rock","paper","scissor"]
    user_choice = input("Please enter (Rock Paper Scissor) or quit:  \n").lower()
    
    if(user_choice == 'quit'):
        playing = False
    
   # print(user_choice)
    computer_choice=random.choice(choices)
    if(computer_choice == user_choice):
        print(f"Computer chooses: {computer_choice} \n")
        print("It's a tie")
    elif(computer_choice == 'rock' and user_choice == 'paper'):
        player_score += 1
        print(f"Computer chooses: {computer_choice} \n")
        print(" paper beats rock!")
    elif(computer_choice == 'rock' and user_choice == 'scissor'):
        computer_score += 1
        print(f"Computer chooses: {computer_choice} \n")
        print(" ohhh no!!rock beats scissors")
    elif(computer_choice == 'paper' and user_choice == 'scissor'):
            player_score += 1
            print(f"Computer chooses: {computer_choice} \n")
            print(" scissors cuts paper!")
    elif(computer_choice == 'paper' and user_choice == 'rock'):
            computer_score += 1
            print(f"Computer chooses: {computer_choice} \n")
            print(" ohhh no!!paper covers rock")
    elif(computer_choice == 'scissor' and user_choice == 'rock'):
                player_score += 1
                print(f"Computer chooses: {computer_choice} \n")
                print(" scissors cuts paper!")
    elif(computer_choice == 'scissor' and user_choice == 'paper'):
                computer_score += 1
                print(f"Computer chooses: {computer_choice} \n")
                print(" ohhh no!!scissor covers paper")
                
print("\n=== FINAL RESULTS ===")
print(f"Your Score: {player_score} | Computer Score: {computer_score}")

if player_score > computer_score:
    print("Congratulations! You won the game!!! 🎉")
elif player_score < computer_score:
    print("The computer won the game! Better luck next time. 🤖")
else:
    print("The overall game is a tie! 👔")
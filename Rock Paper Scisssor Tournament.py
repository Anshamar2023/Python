import random

print("Just press enter to start Rock Paper Scissors Ai\n")
input("Welcome to Rock, Paper, Scissors Tournament\n")

def Description():
    Description = """
    Description:
    Rock Paper Scissors Tournament is a game where two players play against each other.
    One player is Bot means computer
    Second player is the user means You 
    We will conduct 10 Rounds of Rock, Paper, Scissors Game 
    """
    print(Description)
def Rock_Paper_scissor():
  user_score = 0
  computer_score = 0

  user_choice = input("\nChoose Rock : 1, Paper : 2 or Scissors : 3 (Enter the assigned number to choose any choice)\n")

  choice = ['Rock', 'Paper', 'Scissor']
  computer_choice = random.choice(choice)
  print(computer_choice)
  
  tie = "Tie!"
  compute_won = "Computer won!"
  user_won = "You won!"
  #Tie conditions
  if user_choice == '1' and computer_choice == 'Rock':
    print(tie)
    computer_score = computer_score 
    user_score = user_score
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score))

  elif user_choice == '2' and computer_choice == 'Paper':
    print(tie)
    computer_score = computer_score
    user_score = user_score
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score))
    
  elif user_choice == '3' and computer_choice == 'Scissor':
    print(tie)
    computer_score = computer_score
    user_score = user_score
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score))

  #User win conditions
  elif user_choice == '1' and computer_choice == 'Scissor':
    print(user_won)
    user_score = user_score + 1
    computer_score = computer_score
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score))
  
  elif user_choice == '2' and computer_choice == 'Rock':
    print(user_won)
    user_score += 1
    computer_score = computer_score
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score))

  elif user_choice == '3' and computer_choice == 'Paper':
    print(user_won)
    user_score = user_score + 1
    computer_score = computer_score
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score))

  #Computer win conditions
  elif user_choice == '1' and computer_choice == 'Paper':
    print(compute_won)
    user_score = 0
    computer_score += 1
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score))

  elif user_choice == '2' and computer_choice == 'Scissor':
    print(compute_won)
    user_score = 0
    computer_score += 1
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score))
    
  elif user_choice == '3' and computer_choice == 'Rock':
    print(compute_won)
    user_score = 0
    computer_score += 1
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score))

  else:
    print("Invalid Input")

  user_score_1 = 0
  computer_score = 0

  user_choice = input("\nChoose Rock : 1, Paper : 2 or Scissors : 3 (Enter the assigned number to choose any choice)\n")

  choice = ['Rock', 'Paper', 'Scissor']
  computer_choice = random.choice(choice)
  print(computer_choice)
  
  tie = "Tie!"
  compute_won = "Computer won!"
  user_won = "You won!"
  #Tie conditions
  if user_choice == '1' and computer_choice == 'Rock':
    print(tie)
    computer_score = computer_score 
    user_score_1 = user_score_1
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score_1))

  elif user_choice == '2' and computer_choice == 'Paper':
    print(tie)
    computer_score = computer_score
    user_score_1 = user_score_1
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score_1))
    
  elif user_choice == '3' and computer_choice == 'Scissor':
    print(tie)
    computer_score = computer_score
    user_score_1 = user_score_1
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score_1))

  #User win conditions
  elif user_choice == '1' and computer_choice == 'Scissor':
    print(user_won)
    user_score_1 = user_score_1 + 1
    computer_score = computer_score
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score_1))
  
  elif user_choice == '2' and computer_choice == 'Rock':
    print(user_won)
    user_score_1 += 1
    computer_score = computer_score
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score_1))

  elif user_choice == '3' and computer_choice == 'Paper':
    print(user_won)
    user_score_1 = user_score_1 + 1
    computer_score = computer_score
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score_1))

  #Computer win conditions
  elif user_choice == '1' and computer_choice == 'Paper':
    print(compute_won)
    user_score_1 = 0
    computer_score += 1
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score_1))

  elif user_choice == '2' and computer_choice == 'Scissor':
    print(compute_won)
    user_score_1 = 0
    computer_score += 1
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score_1))
    
  elif user_choice == '3' and computer_choice == 'Rock':
    print(compute_won)
    user_score_1 = 0
    computer_score += 1
    print("Computer score: " + str(computer_score))
    print("User score: " + str(user_score_1))

  else:
    print("Invalid Input")

 

Description()
Rock_Paper_scissor()
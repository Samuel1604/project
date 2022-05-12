import random

def play():
  user = input("what's your choice? 'r' rock, 'p' paper, 's' scissors \n")
  computer = random.choice(['r','p','s'])
  
  if  user == computer:
    return "it's a tie"
  if is_win(user,computer):
    return "You won"
  
  return "You lost"
    
  
  
def is_win(player, opponet):
  if (player == 'r' and opponet == 's') or (player == 'p' and opponet == 'r') or (player == 's' and opponet == 'p'):
    return True
  
print(play())
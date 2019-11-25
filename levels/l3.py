from random import randint

def sticks_game_l3():
  '''
  Level 3 Game Rules
  Allow the user to input a username for themself and the computer.
  Ensure that the user is able to enter how many sticks to remove (1, 2, or 3)
  The user should ONLY be able to remove 1, 2, or 3 sticks.
  Ensure that player turns are kept track of.
  When the game is down to a small number of sticks, ensure that the user’s moves are legal. (with one stick left, the user should not be able to remove three sticks)
  The game should end when the number of sticks reduces to zero.
  Ensure that the correct winner is announced at the end of the game.
  '''

  sticks_left = 15
  p1 = input("Enter a name please: ")
  p2 = input("Enter a name for the computer: ")
  
  whos_turn = input('Who goes first: 1(%s) or 2(%s)' % (p1, p2))
  if int(whos_turn) == 1:
    p1_turn = True
  else:
    p1_turn = False  

  while sticks_left > 0:
    turn_name = p1 if p1_turn else p2
    if turn_name == p1: #Players Turn
      print()
      remove = input('%s would you like to remove 1, 2, or 3 sticks? --> ' % turn_name)
      remove = '1' if len(remove) == 0 else remove
      remove = int(remove)
      remove = 1 if remove <= 0 else remove
      remove = 3 if remove > 3 else remove
      print()
    else: # CPU's turn
      # Pick a random number of sticks between 1 and 3.
      # When sticks are within three of 1 make the optimal move
      # otherwise take the final stick and lose.
      if sticks_left > 1 and sticks_left <= 4:
        remove = sticks_left - 1
      elif sticks_left == 1:
        remove = 1
      elif sticks_left > 4:
        remove = randint(1,3)
    sticks_left -= remove if sticks_left > remove else sticks_left
    print("%s removes %s sticks - %s sticks left" % (turn_name, str(remove), str(sticks_left)))
    p1_turn = not p1_turn

  winner = p1 if p1_turn else p2
  print("Congratulations %s, you won!" % winner)

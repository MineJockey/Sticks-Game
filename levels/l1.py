def sticks_game_l1():
  '''
  Level 1 Game Rules
  Ensure that the user is able to enter how many sticks to 
    remove (1, 2, or 3)
  The user should ONLY be able to remove 1, 2, or 3 sticks.
  When the game is down to a small number of sticks, ensure that 
    the user’s moves are legal.  (with one stick left, the user 
    should not be able to remove three sticks)
  The game should end when the number of sticks reduces to zero.
  Some sort of message is appropriate here.
  '''
  sticks_left = 15

  while sticks_left > 0:
    remove = int(input('Remove 1, 2, or 3 sticks? -->'))
    remove = 1 if remove <= 0 else remove
    remove = 3 if remove > 3 else remove
    sticks_left -= remove if sticks_left > remove else sticks_left
    print(sticks_left)

  print("Congratulations you lost to yourself!")

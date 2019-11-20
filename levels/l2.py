def sticks_game_l2():
  # Level 2 Game Rules
  # Allow each user to input a username.
  # Ensure that the user is able to enter how many sticks to 
  #   remove (1, 2, or 3)
  # The user should ONLY be able to remove 1, 2, or 3 sticks.
  # Ensure that player turns are kept track of.
  # When the game is down to a small number of sticks, ensure that 
  #   the user’s moves are legal.  (with one stick left, the user 
  #   should not be able to remove three sticks)
  # The game should end when the number of sticks reduces to zero.
  # Ensure that the correct winner is announced at the end of the game.

  sticks_left = 15
  p1 = input("Player 1, enter a name please: ")
  p2 = input("Player 2, enter a name please: ")
  p1_turn = True

  while sticks_left > 0:
    turn_name = p1 if p1_turn else p2
    remove = int(input('%s would you like to remove 1, 2, or 3 sticks? -->' % turn_name))
    remove = 1 if remove < 0 else remove
    remove = 3 if remove > 3 else remove
    sticks_left -= remove if sticks_left > remove else sticks_left
    print(sticks_left)
    p1_turn = not p1_turn

  winner = p1 if p1_turn else p2
  print("Congratulations %s, you won!" % winner)

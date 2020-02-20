####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'S & Y'
strategy_name = 'Collude then follow'
strategy_description = '''Collude first round, then follow.'''
    
def move(my_history, their_history, my_score, their_score):
  '''This strategy will start by colluding, then follow the other player.'''
  return 'c'#It will return c first.
  if their_history[-1] == 'b':#It will return b if they returned b in the last round.
    return 'b'
  elif their_history[-1] == 'c':#It will return c if they returned c in the last round.
    return 'c' 
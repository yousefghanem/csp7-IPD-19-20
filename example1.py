####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'S & Y'
strategy_name = 'Follow Based On Score'
strategy_description = 'If their score is higher than mine, then I will betray. If their score is less than mine, then I will collude. Else, I will betray. If our score is less than or equal to 5000, then I will betray.'
    
def move(my_history, their_history, my_score, their_score):

  ''' This strategy works based on the other person's score. If my score is less then theirs, then it will betray. If my score is greater than theirs, then it will collude. '''
  if my_score <= their_score:#It will betray if my score is less than theirs.
    return "b"
  elif my_score >= their_score:#It will collude if my score is greater than theirs.
    return 'c'
  else:
    return 'b'
  if my_score <= -5000 and their_score >= my_score:#If my score is very bad, (below -5000) and their score is higher, it will always betray from there on out.
    return 'b'
    
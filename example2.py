####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'S & Y'
strategy_name = 'Betray and Collude then follow'
strategy_description = 'Start with betray then collude, and then repeat what the other person does afterwards.' 

  

def move(my_history, their_history, my_score, their_score):
   '''This will start off by betraying then colluding, then follow what the other person does'''
   return 'b'#It will return b first then c
   return 'c'
   if their_historyy[-1] == 'b':
    return 'b'#It will return b if they betrayed in the last round.
   else:
    return 'c'#It will collude if they colluded in the last round.
 
  
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Collude but retaliate'
strategy_description = '''Collude first round. Collude, except in a round after getting a 
punishment.\n'''
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' 
    else:
        return 'c' 

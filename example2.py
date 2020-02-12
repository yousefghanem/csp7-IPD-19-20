####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E2'
strategy_name = 'Collude first 50 rounds unless betrayed. Betray 51st round forward.'
strategy_description = '''Betray if ever betrayed. If I haven't been betrayed yet, I'll betray 
starting with the 50th round.\n'''
    
def move(my_history, their_history, my_score, their_score):
   
    if 'b' in their_history or len(their_history)>50: 
        return 'b'        
    else:
        return 'c'         
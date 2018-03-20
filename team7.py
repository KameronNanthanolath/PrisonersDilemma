####
# Each team's file must define four tokens:
# team_name: a string
# strategy_name: a string
# strategy_description: a string
# move: A function that returns 'c' or 'b'
####


team_name = 'Sloth Bear' # Only 10 chars displayed.
strategy_name = 'History Check'
strategy_description = 'If they betray twice, start betraying. Otherwise, alternate inbetween betray and collude.'


''' Arguments accepted: my_history, their_history are strings.
my_score, their_score are ints.
Make my move.
Returns 'c' or 'b'. 
'''

# my_history: a string with one letter (c or b) per round that has been played with this opponent.
# their_history: a string of the same length as history, possibly empty. 
# The first round between these two players is my_history[0] and their_history[0].
# The most recent round is my_history[-1] and their_history[-1].
# Analyze my_history and their_history and/or my_score and their_score.
# Decide whether to return 'c' or 'b'.

def history_check(my_history, their_history, my_score, their_score):


r = 0 #Random variable to use to check for betrayals in their history
for i in their_history: #For every round in their history...
    if i == 'b': #...That's a betray...
        r = r + 1 #...Add 1 to the variable 'r'. Unsure how to actually check for the existence of 2 betrayals in a string, so it check for any betrays and adds one to 'r' to count the number of betrays.
if r >= 2: #If 'r,' the number of betrays is 2 or greater, we want the code to only betray.
    return 'b'
else:
    if len(my_history) == 0: #First round, we want to collude, to test the waters. Checks the length of the history to see if what round it's on. On round 1, where the length of my history is 0, we begin with a collude.
        return 'c' 
    if my_history[-1] == 'b': #Now we want to alternate by checking or past choice. If our past choice was a betray, we would want to collude, and vice-versa. This is performed by checking the last round's move. With a [-1], it's the latest index because 0 is the first index.
        return 'c'
    if my_history[-1] == 'c': #Collusion if previously a betray
        return 'b'


def test_move(my_history, their_history, my_score, their_score, result):

'''calls move(my_history, their_history, my_score, their_score)

from this module. Prints error if return value != result.

Returns True or False, dpending on whether result was as expected.

'''

real_result = history_check(my_history, their_history, my_score, their_score)
if real_result == result:
    return True
else:

print("move(" +
", ".join(["'"+my_history+"'", "'"+their_history+"'",
str(my_score), str(their_score)])+
") returned " + "'" + real_result + "'" +
" and should have returned '" + result + "'")
return False



if __name__ == '__main__':

# Test 1: Alternate

if test_move(my_history='cbcbc',
their_history='bb', 
my_score=0,
their_score=0,
result='c'):

print 'Test passed'
#Checks if by the end of the sequence we end with c when starting with c. Program is set up to end with a collude if no intervention by the "if" code in the history_check function.

# Test 2: Betrayal after being betrayed twice

test_move(my_history='cbcbb',
their_history='bcbcc', 

#Checks to see if we would betray on the fifth round due to being betrayed twice. Fifth round would normally be a collusion 
#Compare histories. My_history would alternate until betrayed twice, which is measured in the fifth round since fourth is a betray either way.

my_score=0, 
their_score=0,
result='b')

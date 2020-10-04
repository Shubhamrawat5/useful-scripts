import keyboard as key
import time
from pycricbuzz import Cricbuzz
import json
import requests

time.sleep(2)

#key.write('Heyyy')

def send_score(data):
    print(data)
    key.write(data)
    key.press_and_release('shift+enter')


def make_goodLookingScore(lscore):
    team_name = lscore['batting']['team']
    score=lscore['batting']['score'][0]
    total_runs=score['runs']
    overs=score['overs']
    wickets=score['wickets']

    score_str=team_name+": "+total_runs+'/'+wickets+' ('+overs+')'


    batting=lscore['batting']['batsman']
    first_batsman=batting[0]
    second_batsman=batting[1]
    
    fbatsman_str=first_batsman['name']+': '+first_batsman['runs']+' ('+first_batsman['balls']+')'
    sbatsman_str=second_batsman['name']+': '+second_batsman['runs']+' ('+second_batsman['balls']+')'
    
    key.write(score_str)
    key.press_and_release('shift+enter')
    #time.sleep(1)
    key.write(fbatsman_str)
    key.press_and_release('shift+enter')
    #time.sleep(1)
    key.write(sbatsman_str)
    key.press_and_release('enter')
    
    #send_score(score_str+fbatsman_str+sbatsman_str)


def live_score(mid):
    c = Cricbuzz()
    lscore = c.livescore(mid)
    #print(lscore['batting']['score'][0]['overs'])
    #print(json.dumps(lscore, indent=4, sort_keys=True))
    make_goodLookingScore(lscore)


c = Cricbuzz()
matches = c.matches()
#print(type(matches))
print (json.dumps(matches,indent=4)) //by this match id will be recieved

id = "30384" #match id

#print(c.livescore(id))
#live_score(id)

i=0
while i<20:
    live_score(id)
    i = i+1
    time.sleep(100)

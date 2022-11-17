#import pandas as pd

def userdict(Users):

    #creds = {'credentials'}
    
    #creds['credentials'] 
    #creds['credentials']=
    creds = {'usernames':{}}
    
    #creds['usernames']['gaabbot'] = {'username':'gaabbot', 'email':'gerald.abbot@gmail.com'}
    #creds['usernames']['mpabbot'] = {'username':'mpabbot', 'email':'matthew.p.abbot@gmail.com'}

    for x in range(len(Users)):
        creds['usernames'][Users['username'][x]] =  {'username': Users['username'][x], 'email': Users['email'][x], 'name': Users['name'][x], 'password': Users['pwd'][x]}
        


#    for x in range(len(Users)):
#        creds['credentials'][0]['usernames'] =  { Users['username'][x] : { 
#             'username': Users['username'][x], 
#             'email': Users['email'][x], 
#             'name': Users['name'][x], 
#             'password': Users['pwd']}}



    return(creds)


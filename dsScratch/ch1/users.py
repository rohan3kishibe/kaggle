users=[
    {
    "id":0,"name":"Hero"},{
    "id":1,"name":"Dunn"
    },{
    "id":2,"name":"Sue"
    },{
    "id":3,"name":"Chi"
    },{
    "id":4,"name":"Clive"
    },
    {
    "id":5,"name":"Devin"
    },
    {
    "id":6,"name":"Klein"
    },
]

#now wants to map them to the friendship pairs 
friendsip_pairs=[(0,1),(0,2),(3,4)]

#using a dict 

friendshisp = {user["id"]: [] for user in users}

#and now looping over the friendhsip pairs to populate it 
for i,j in friendsip_pairs:
    friendshisp[i].append(j)#adding j as a friend of user i
    friendshisp[j].append(i)# adding i as a friend of user j 

#to get the total number of conenctions by summing up the length of all the friends lists 

def numberOfFriends(user):
    user_id = user["id"]
    friend_ids = friendshisp[user_id]
    return len(friend_ids)

##total connections 

total_connections = sum(numberOfFriends(user) for user in users)
print(total_connections)

#now dividing by the number of users 
num_users= len(users) 
avgCOnnections = total_connections/ num_users 

#it is also easy to find the most connected people:- they are people who have the largetst 
#number of freinds 

#creating a list:- (usr_id,numberofFreinds)

num_friends_by_id = [(user["id"] , numberOfFriends(user)) for user in users]

#sort the list by num_freinds ,largest to smallest
num_friends_by_id.sort(
    key=lambda id_and_friends:id_and_frineds[1],
    reverse=True)

from collections import Counter

def friends_of_friends(user):
    '''
    returns the friends or friends
    '''
    user_id = user["id"]
    return Counter(
        foaf_id,
        for friend_id in friendship[user_id]
        for foaf_id in friendship[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendship[user_id]
    )

print(friends_of_friends[users[3]])


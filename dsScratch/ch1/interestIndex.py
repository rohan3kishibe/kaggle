from collections import defaultdict

# keys are interest ,values are lists of user_ids with that interest
user_id_by_interest = defaultdict(list)


for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)


# similarly for intereset
interest_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)

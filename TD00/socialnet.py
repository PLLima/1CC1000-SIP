def common_friends(friendships):
    

    common_friends = {}

    for person1, person1_friends in friendships.items():
        for person2, person2_friends in friendships.items():
            if person1 != person2:

                key = (person1, person2) if person1 < person2\
                    else (person2, person1)

                if key in common_friends:
                    continue

                common = list(set(person1_friends) &
                              set(person2_friends))

                common_friends[key] = common

    return common_friends


social_network = {'a': ['b', 'c', 'd'], 'b': [
    'a', 'd'], 'c': ['a', 'd'], 'd': ['a', 'b', 'c']}

print(common_friends(social_network))

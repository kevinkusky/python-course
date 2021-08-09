# Custom Sorting

users = [
    {'id': 55, 'displayName':'Johnny Quest', 'email': 'lessthanjake@yahoo.com'},
    {'id': 200, 'displayName':'Morgan S', 'email': 'mo4g4n@aol.com'},
    {'id': 22, 'displayName':'Yogi Bear', 'email': 'mrbear@ygmail.com'},
]

print('Users list: %s' %users)


def mySorter(user):
    return user['displayName']

users.sort(key = mySorter)

print('Sorted Users List: %s' %users)

# key and reverse - named parameters
# sorted() is non distructive - assign to new variable
reverseUseres = sorted(users, key = mySorter, reverse = True)
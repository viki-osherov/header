# 4-10
locations = ['Rome', 'Israel', 'Paris', 'Russian', 'New York']
print(locations[0:3])

locations = ['Rome', 'Israel', 'Paris', 'Russian', 'New York']
print(locations[1:3])

locations = ['Rome', 'Israel', 'Paris', 'Russian', 'New York']
print(locations[2:3])

# 4-12
# 1

my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods[1:2])

print("\nMy friend's favorite foods are:")
print(friend_foods[2:2])

# 2

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods[0:2])

print("\nMy friend's favorite foods are:")
print(friend_foods[1:2])

# 4-13, (a)
Foods = (cucumbers, tomatoes, onion, salt)
print(Foods[0])
print(Foods[1])
print(Foods[2])

# (b)
Foods = (cucumbers, tomatoes, onion, salt)
Foods[3] = sugar

# (c)
Foods = (cucumbers, tomatoes, onion, salt)
print("Original Foods:")
for Basic in Foods:
    print(Basic)

Foods = (eggs, flour, yeast, sugar)
print("\nModified Foods:")
for Basic in Foods:
    print(Basic)

# 2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.
#        Test Data :
#        color_list_1 = set(["White", "Black", "Red"])
#        color_list_2 = set(["Red", "Green"])
#        Expected Output :
#        {'Black', 'White'}


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(f"list 1: {color_list_1}")
print(f"list 2: {color_list_2}")
print(f"List difference: {color_list_1.difference(color_list_2)}")

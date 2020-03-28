"""
Problem:
Modify your program from Exercise 6-2 so each person can have more than one 
favorite number. Then print each person’s name along with their favorite numbers.
"""
fav_num = {
    'amit': [23, 46, 12, 54],
    'vishal': [47, 58, 67, 65],
    'purvesh': [74, 1, 58],
    'jayesh': [28, 45, 97, 32],
    'sahil': [11],
}
for people, fav_num in fav_num.items():
    print(people.title() +"'s favorite number is")
    for number in fav_num:
        print("\t", str(number))

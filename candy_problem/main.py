'''
DIRECTIONS
==========

1. In `get_friends_favorite_candy_count()`, return a dictionary of candy names and the
amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

2. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

3. In `get_friends_who_like_specified_candy()`, return 
a tuple of friends who like the candy specified in the candy_name parameter.

4. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

5. Starting with nominal cases, write tests for each of the functions below then 
write tests to handle edge cases.
'''

#1
from hashlib import new


def get_friends_most_favored_candy(favorites):
    candy_dict = {}

    for friend in favorites:
        for candy in friend[1]:
            # print(candy)
            if candy.lower() not in candy_dict:
                candy_dict[candy] = 1
            elif candy in candy_dict:
                candy_dict[candy] += 1

    return candy_dict

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
#2
def create_new_candy_data_structure(favorites):

    new_candy = {}

    for friend in favorites:
        for candy in friend[1]:

            if candy in new_candy:
                new_candy[candy].append(friend[0])
            else:
                new_candy[candy]= [friend[0]]
                
    print(new_candy)    
    return new_candy

create_new_candy_data_structure(friend_favorites)



#3
def get_friends_who_like_specific_candy(data, candy_name):

    if candy_name in data:

        friends_who_like_candy = tuple(data[candy_name])
    else:
        return None
    
    return friends_who_like_candy


#4
def create_candy_set(data):

    set_of_candies = set()

    for candy in data:
        set_of_candies.add(candy)

    print(set_of_candies)
    return set_of_candies

#5 write tests

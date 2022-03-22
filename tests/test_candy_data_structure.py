import pytest
from candy_problem.main import * 


def test_get_friends_most_favorite_candy():
    data = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

    candy_dict = get_friends_most_favored_candy(data)

    assert candy_dict["chocolate bar"] == 1
    assert candy_dict["laffy taffy"] == 3

def test_get_friends_most_favorite_candy_capitalized():
    data = [
    ["Lollipop", "bubble gum", "laffy taffy" ],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

    candy_dict = get_friends_most_favored_candy(data)

    assert candy_dict["chocolate bar"] == 1
    

def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict
    

def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8
    assert new_candy_data == {'lollipop': ['Sally', 'Bob'], 'bubble gum': ['Sally'], 'laffy taffy': ['Sally', 'Arlene', 'Carlie'], 'milky way': ['Bob', 'Arlene'], 'licorice': ['Bob'], 'chocolate bar': ['Arlene'], 'nerds': ['Carlie'], 'sour patch kids': ['Carlie']}

def test_get_friends_who_like_lollipop():
    #arrange


    data = {'lollipop': ['Sally', 'Bob'], 'bubble gum': ['Sally'], 'laffy taffy': ['Sally', 'Arlene', 'Carlie'], 'milky way': ['Bob', 'Arlene'], 'licorice': ['Bob'], 'chocolate bar': ['Arlene'], 'nerds': ['Carlie'], 'sour patch kids': ['Carlie']}

    candy_name = "lollipop"


    #act
    friends_who_like_specific_candy = get_friends_who_like_specific_candy(data, candy_name)

    #assert
    assert friends_who_like_specific_candy == ("Sally", "Bob")

def test_get_friends_who_like_laffy_taffy():
    #arrange


    data = {'lollipop': ['Sally', 'Bob'], 'bubble gum': ['Sally'], 'laffy taffy': ['Sally', 'Arlene', 'Carlie'], 'milky way': ['Bob', 'Arlene'], 'licorice': ['Bob'], 'chocolate bar': ['Arlene'], 'nerds': ['Carlie'], 'sour patch kids': ['Carlie']}

    candy_name = "laffy taffy"


    #act
    friends_who_like_specific_candy = get_friends_who_like_specific_candy(data, candy_name)

    #assert
    assert friends_who_like_specific_candy == ("Sally", "Arlene", "Carlie")
    assert len(friends_who_like_specific_candy) == 3

def test_get_friends_who_like_candy_not_in_data():
    #arrange


    data = {'lollipop': ['Sally', 'Bob'], 'bubble gum': ['Sally'], 'laffy taffy': ['Sally', 'Arlene', 'Carlie'], 'milky way': ['Bob', 'Arlene'], 'licorice': ['Bob'], 'chocolate bar': ['Arlene'], 'nerds': ['Carlie'], 'sour patch kids': ['Carlie']}

    candy_name = "black thunder"


    #act
    friends_who_like_specific_candy = get_friends_who_like_specific_candy(data, candy_name)

    #assert
    friends_who_like_specific_candy is None

def test_create_candy_set():
    #arrange

    data = {'lollipop': ['Sally', 'Bob'], 'bubble gum': ['Sally'], 'laffy taffy': ['Sally', 'Arlene', 'Carlie'], 'milky way': ['Bob', 'Arlene'], 'licorice': ['Bob'], 'chocolate bar': ['Arlene'], 'nerds': ['Carlie'], 'sour patch kids': ['Carlie']}

    #act
    set_of_candies = create_candy_set(data)

    #assert
    assert len(set_of_candies) == 8

def test_create_candy_set_no_data():
    data = {}

    set_of_candies = create_candy_set(data)

    assert set_of_candies == set()
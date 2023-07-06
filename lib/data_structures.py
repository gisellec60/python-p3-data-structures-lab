spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_list=list()
    for food in spicy_foods:
        food_list.append(food["name"] )
    return food_list

def get_spiciest_foods(spicy_foods):
    food_list=list()
    for food in spicy_foods:
        if food["heat_level"] > 5:
            food_list.append(food)
    return food_list


def print_spicy_foods(spicy_foods):
    emoji="🌶"
    for food in spicy_foods:
        count_emoji=food['heat_level'] * emoji
        print (f"{food['name']} ({food['cuisine']}) | Heat Level: {count_emoji}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    emoji="🌶"
    for food in spicy_foods:
        if food["heat_level"] > 5:
            count_emoji=food['heat_level'] * emoji
            print (f"{food['name']} ({food['cuisine']}) | Heat Level: {count_emoji}")

def get_average_heat_level(spicy_foods):
    avg=0
    for food in spicy_foods:
        avg += food["heat_level"] 
    return int(avg / len(spicy_foods))     

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods.append(spicy_food)

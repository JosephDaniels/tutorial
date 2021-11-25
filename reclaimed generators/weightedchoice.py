import random

def get_weight_table(monster_dictionary):
    weighted_monsters = []
    sum_of_weights = 0
    bottom = 0.0
    for definition in monster_dictionary:
        sum_of_weights += int(monster_dictionary[definition])
    for monster in monster_dictionary:
        lower = bottom
        upper = float(monster_dictionary[monster])/sum_of_weights + bottom
        bottom = upper
        weighted_monsters.append( [monster, lower, upper] )
    return weighted_monsters

def is_between(lower, upper, x):
    return x>=lower and x<upper

def weighted_choice(weighted_monsters):
    value = random.random()
    for line in weighted_monsters:
        name = line[0]
        lower = line[1]
        upper = line[2]
        if is_between(lower, upper, value):
            return name

def generation(dictionary):
    weight_list = get_weight_table(dictionary)
    a = weighted_choice(weight_list)
    return a

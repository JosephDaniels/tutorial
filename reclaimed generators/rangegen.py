# this program generates height, weight, and body fat randomly based on a random race
import random

height_range_by_race = {
    "human" : {
        "male" : (160,167,182),
        "female" : (152,162,172)
    },
    "elf" : {
        "male" : (152,157,167),
        "female" : (152,157,167)
    },
     "dwarf" : {
        "male" : (109,121,134),
        "female" : (101,111,129)
    },
     "half elf" : {
        "male" : (157,162,167),
        "female" : (152,160,165)
    },
     "gnome" : {
        "male" : (81,83,93),
        "female" : (78,81,83)
    },
     "halfling" : {
        "male" : (73,76,81),
        "female" : (71,73,76)
    },
    "half orc" : {
        "male" : (172,185,213),
        "female" : (172,175,193)
    }
}

weight_range_by_race = {
    "human" : {
        "male" : (150,180,220),
        "female" : (80,120,180)
    },
    "elf" : {
        "male" : (75,85,90),
        "female" : (70,80,85)
    },
     "dwarf" : {
        "male" : (115,130,145),
        "female" : (90,100,115)
    },
     "half elf" : {
        "male" : (90,100,110),
        "female" : (80,85,90)
    },
     "gnome" : {
        "male" : (35,40,45),
        "female" : (30,35,40)
    },
     "halfling" : {
        "male" : (28,30,35),
        "female" : (20,25,30)
    },
    "half orc" : {
        "male" : (200,220,300),
        "female" : (190,220,240)
    }
}

bodyfat_range_by_race = {
    "human" : {
        "male" : (5,18,25),
        "female" : (8,24,32)
    },
    "elf" : {
        "male" : (3,16,22),
        "female" : (5,16,24)
    },
     "dwarf" : {
        "male" : (6,20,26),
        "female" : (10,26,32)
    },
     "half elf" : {
        "male" : (3,6,20),
        "female" : (8,12,22)
    },
     "gnome" : {
        "male" : (3,6,12),
        "female" : (4,7,15)
    },
     "halfling" : {
        "male" : (5,18,25),
        "female" : (8,20,35)
    },
    "half orc" : {
        "male" : (3,5,8),
        "female" : (8,12,16)
    }
}

def gen_from_range(lower,mid,upper):
    """this will generate a value from within the lower to upper clustering
       towards mid"""
    flip = random.random ()
    if flip > 0.5: # calculate using the upper range
        new_value = mid + random.random() * (upper-mid)
    else:
        new_value = lower + random.random() * (mid-lower)
    return new_value

def ft_from_cm(cm):
    """returns the feet, inch tuple for a given cm measurement"""
    total_inches = int(cm/2.54+0.5)
    feet = total_inches/12
    inches = total_inches%12
    return feet, inches
    
def cm_from_ft(ft,inch):
    """ returns cm from feet and inches"""
    total_inches = (ft*12+inch)
    cm = int(total_inches*2.54)
    return cm
    
race = random.choice(["human", "elf", "dwarf", "half elf", "half orc", "gnome", "halfling",])
gender = random.choice(["male", "female"])

print "You are a %s %s" % (gender, race)

lower, mid, upper = height_range_by_race[race][gender]
for i in range(1):
    print "your height is %i ft and %i inches"% ft_from_cm(gen_from_range(lower, mid, upper))

lower, mid, upper = weight_range_by_race[race][gender]
for i in range(1):
    print "your weight is %i lbs"% gen_from_range(lower, mid, upper)

lower, mid, upper = bodyfat_range_by_race[race][gender]
for i in range(1):
    print "your body fat percentage is %i percent"% gen_from_range(lower,mid,upper)
        

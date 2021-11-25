# an example of DRY (Don't Repeat Yourself)
#
#  say you need to initialize a data structure like this:
#

##weapons = {
##    "knife": {
##        "desc": "a pointy thingy",
##        "price": 1200,
##        "mass": -1
##        },
##    "anvil": {
##        "desc": "ACME roadrunner killer",
##        "price": 100,
##        "mass": 1000
##        }
##    }

# you notice as we add to the list of weapons we end up repeating outselves
# a lot. This is the naive way to do it, and is done in a similar way in XML
# and JSON, two popular data exchange languages. It's actually quite valid
# to do it this way with XML and JSON since the were designed to easily
# exchange data between systems but be human readable. It's been proven that
# some redunancy make thing easier for people to understand. However, it you
# are asking someone to enter in that data in the above dictionary, you can
# see where it might become tedious and error prone(even if the above format
# is highly useful for us in our program. There is a principle in programming
# called DRY or "Don't Repeat Yourself". What you want to do is mimimize the
# amount you repeat things so you minimize mistakes due to mistyping or
# having the same information in too many different places. So here's a
# different way to initialize the above data structure:

fields = ["desc", "price", "mass"]
data = [
    ("knife",       "a pointy thingy",          1200,       -1),
    ("anvil",       "ACME roadrunner killer",   100,        1000),
    ]


# initialize weapons
weapons = {}
for row in data:
    values = {}
    name = row[0]
    values.update(zip(fields, row[1:]))
    weapons[name]  = values    

import pprint
pprint.pprint(weapons,width=10)



    

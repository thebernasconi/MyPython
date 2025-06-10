# a first look at loops
# fistly a /for/ loop
# i'm making it say what ingredients are in the list

ingredient_collection = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
for ingredient in ingredient_collection:
    print("Now I'll use some " + ingredient)

# now a /while/ loop
# a countdown from 10 to 0

count = 10
while count >= 0:
	print(count)
	count -= 1
      
# now a /while/ loop in a situation where we are using lists

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# I'll make it say the topics

# first I need a variable to use anchor/comparison with the list length
index = 0

# now I'll create a variable to compare with /index/ and I'll assign it the value of len

length = len(python_topics)

# now for the loop

while index < length:
      print("I'm learning about " + python_topics[index])
      index += 1
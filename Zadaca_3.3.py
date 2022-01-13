import random

jobs = ["The tester", "The cajka", "The fireman", "The surgeon", "The programmer"]
adverbs = ["somewhat", "slightly", "extremely"]
adjectives = ["happy", "crazy", "anxious", "insane", "sexy"]
hairColors = ["blond", "purple", "pink", "red"]

print(str(random.choice(jobs)) + " is " + str(random.choice(adverbs)) + " " + str(random.choice(adjectives)) +
      " and has " + str(random.choice(hairColors)) + " hair.")

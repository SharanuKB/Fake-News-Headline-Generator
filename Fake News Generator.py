import random

subjects = [
    "A local politician",
    "A famous actor",
    "A tech CEO",
    "A college student",
    "A scientist",
    "A social media influencer",
    "A delivery driver",
    "A school principal",
]

actions = [
    "accidentally discovered",
    "secretly built",
    "publicly announced",
    "mysteriously lost",
    "unexpectedly won",
    "was caught using",
    "revealed plans for",
    "launched",
]

places = [
    "in Chennai",
    "at a local college",
    "inside a shopping mall",
    "at the airport",
    "in a government office",
    "on social media",
    "in a small village",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"Breaking News: {subject} {action} {place}"
    print("\n"+ headline)

    user = input("Do you want to generate another headline? (yes/no): ").lower()
    if user == "no":
        break


print("\nThank you for watching, have a fun day!")
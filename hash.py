"""
In this example your supposed to be running an election
your supposed to prevent people from voting mutliple times
"""

voted = {}

def vote(name):
    if voted.get(name):
        return "Kick them out"
    else:
        voted[name] = "Voted"
        return "Let them vote"
    
print(vote("Majd"))
print(voted)
print(vote("Majd"))
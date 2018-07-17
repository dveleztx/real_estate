lookup = {}
lookup = dict()
lookup = {"age": 33, "loc": "Texas"}
lookup = dict(age=42, loc="Texas")


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name


gandalf = Wizard("Gandalf", 50)
print(gandalf.__dict__)

print()
print(lookup)
print(lookup["loc"])

lookup["cat"] = "fun code demos"

if "cat" in lookup:
    print(lookup["cat"])

# Suppose these came from a data source, e.g. database, web service, etc
# And we want to randomly access them
import collections

User = collections.namedtuple("User", "id, name, email")
users = [
    User(1, "user1", "user1@domain.com"),
    User(2, "user2", "user2@domain.com"),
    User(3, "user3", "user3@domain.com"),
    User(4, "user4", "user4@domain.com"),
]

lookup = dict()
for u in users:
    lookup[u.email] = u

print(lookup["user4@domain.com"])

for v in users:
    lookup[v.id] = v

print(lookup[3])

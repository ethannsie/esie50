"""
Ethan Sie
Elmo's Cheez-it
SoftDev
05_bitsream
2024-09-17
time spent: 0.5
"""

f = open("krewes.txt", "r")
people = f.read().replace("\n", "").split('@@@')
for count, person in enumerate(people):
    people[count] = person.split('$$$')
    people[count] = {"period":people[count][0], "devo":people[count][1], "ducky":people[count][2]}

print(people)

# Lets say you want to know all of the people/duckys in period 4
p4Peeps = []
p4Duckys = []
for person in people:
    if person.get("period") == '4':
        p4Peeps.append(person.get("devo"))
        p4Duckys.append(person.get("ducky"))
print(p4Peeps)
print(p4Duckys)


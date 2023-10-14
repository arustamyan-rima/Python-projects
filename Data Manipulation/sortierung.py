# 1. Sortiere nach Einwohner
lst = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
]

print('sorted Einwohner:', sorted(lst, key = lambda e:e[0]))

# 2. Sortiere nach Bundesstaaten (Alabama, California...)
states = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
]

print('sorted states:', sorted(states, key = lambda x: x[1]))

# 3. Sortiere absteigend
lst = [500, 1000, 400, 40000, 999, 2, 0.5, 17]

print(sorted(lst, reverse = True))

# 4. Sortiere nach Vornamen
people = [
    {"first": "Arthur", "last": "Dent", "id": "23s"},
    {
        "first": "Zaphod",
        "last": "Beeblebrox",
        "id": "42ai",
    },
    {"first": "Ford", "last": "Perfect", "id": "233"},
]

print('sorted Vornamen: ', sorted(people, key = lambda x: x['first']))

# 5. Sortiere nach Punkten (aufsteigend)
player = {"peter": 100, "klaus": 34, "wizz": 222, "angela": 23, "sabine": 400}
print(sorted(player.items(), key = lambda x: x[1]))

# 6 Gegebene eine Liste mit Personen und deren Verkäufen.
# Der Verkaufserlös errechnet sich durch die letzten beiden Positionen,
# z.b. 46 x 18.67 für John Miller. Sortiere nach Verkaufserlös
umsaetze = [
    ("John", "Miller", 46, 18.67),
    ("Randy", "Steiner", 48, 27.99),
    ("Tina", "Baker", 53, 27.23),
    ("Andrea", "Baker", 40, 31.75),
    ("Eve", "Turner", 44, 18.99),
    ("Henry", "James", 50, 23.56),
]

print("Sortiert nach Verkaufserlös:")
for i in sorted(umsaetze, key=lambda x: x[2] * x[3]):
    print(i)

# 7. Sortiere aufsteigend nach höchstem Wert der Liste.
stox = [
    ["a", [22, 25, 14, 23]],
    ["b", [122, 25, 14, 233]],
    ["c", [422, 25, 14, 33]],
    ["d", [22, 1025, 14, 33]],
    ["e", [2, 5, 4, 3]],
]

print('sorted stox: ', sorted(stox, key = lambda x: max(x[1])))
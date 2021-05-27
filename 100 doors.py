def toglesingledoor(i): # i tells us which door to togle
    if doors[i] == "Is open":
        doors[i] = "Is closed"
    elif doors[i] == "Is closed":
        doors[i] = "Is open"

doors = {}
print("Initial state")
for i in range(1, 101): #sozdayem biblioteku dverei
    doors[i] = "Is closed"

for p in range(1, 101): #eto prohodi
    #print("Prokhod #" + str(p))
    for d in range(1, 101): # visit k kazhdoi dveri
        visit = isinstance(d/p, int)
        if d%p == 0:
            toglesingledoor(d)
    print(doors)

Opened = ["Doors which are opened: "]
Closed = ["Doors which are closed: "]
for e in range(1, 101):
    if doors[e] == "Is open":
        Opened.append(str(e)+", ")
    elif doors[e] == "Is closed":
        Closed.append(str(e)+", ")

print(Opened)
print(Closed)
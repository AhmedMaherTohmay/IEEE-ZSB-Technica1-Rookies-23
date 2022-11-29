n = input("\n").split(" ")
stations = input("\n").split(" ")

cities = []
for i in range(int(n[0])):
    cities.append([i, 0])
    
for i in range(int(n[1])):
    cities[int(stations[i])][1] = 1

distance = []
dist1 = 0
dist2 = 0

for i in range(len(cities)):
    for j in range(i, len(cities)):
        if cities[j][1] == 1:
            dist1 = abs(j - i)
            break
        
    for k in reversed(range(i)):
        if cities[k][1] == 1:
            dist2 = abs(k - i)
            break
    distance.append(min(dist1, dist2))
    
print(max(distance))        
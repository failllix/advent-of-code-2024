from collections import Counter

f = open("./day-1.txt", "r")
x = f.read()

list_entries= x.split("\n")[:-1]

a = [int(list_entry.split("   ")[0]) for list_entry in list_entries]
b = [int(list_entry.split("   ")[1]) for list_entry in list_entries]

a.sort()
b.sort()

distances = [abs(a[i] - b[i]) for i in range(len(a))]

print(sum(distances))

# --- 2nd star solution

frequency = Counter(b)

print(sum([x * frequency[x] for x in a]))

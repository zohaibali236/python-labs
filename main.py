a = {i for i in range(10)}
print(a)
b = {i for i in range(10,20)}
print(b)

if(a.intersection(b) != set()):
    if(a > b): print("b is subset")
    elif(a < b): print("b is superset")
    else: print("improper subset")
else: print("Not subset")

d = {
    "k1":"v1",
    "k2":"v2",
    "k3":"v3"
}
print()
for i in d:
    print(d[i])

print()

for i in d.keys():
    print()
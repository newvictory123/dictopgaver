iq ={"oliver" : 80, "ditte" : 200, "gustav" : 2,}

iq["oliver"]-=20

iq.pop("oliver",None)
print(iq)

print(iq.values())
print(iq.keys())

for key, value in iq.items():
    print(key, "-", value)


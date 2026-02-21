s= {"Alice": 85,"Bob": 90,"Charlie": 75}
find = 90
for key, value in s.items():
    if value == find:
        print("Key found:", key)
        break
else:
    print("Value not found")
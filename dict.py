dict = {"a": 10, "b": 20, "c": 30}
print("Keys:", dict.keys())
print("Values:", dict.values())
print("Items:", dict.items())
dict.pop("b")
print("After pop:", dict)
del dict["c"]
print("After delete:", dict)
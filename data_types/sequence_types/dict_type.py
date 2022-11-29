fruits_colors = {
    "green_apple": "green",
    "banana": "yellow",
    "peach": "orange",
}

print(fruits_colors["green_apple"])
print(fruits_colors.get(0, "NOT FOUND"))

fruits_colors["orange"] = "ohra"
print(fruits_colors)

print(fruits_colors.setdefault("orange", "pink"))
print(fruits_colors)

fruits_colors["banana"] = "green"
print(fruits_colors)

# fruits_colors.update(banana="yellow")
# fruits_colors.update({"banana": "yellow"})
# print(fruits_colors)

print(len(fruits_colors))

# Iterate by using iteration on keys and Key look up
for key in fruits_colors:
    print(key, fruits_colors[key])

# print(fruits_colors.keys())
# print(fruits_colors.values())
# print(fruits_colors.items())
#
# for key in fruits_colors.keys():
#     print(key)
#
# for value in fruits_colors.values():
#     print(value)
#
# for key, value in fruits_colors.items():
#     print(key, value)

orange = fruits_colors.pop("orange", "NO SUCH FRUIT")
print(orange)
print(fruits_colors)

popped_item = fruits_colors.popitem()

del fruits_colors["green_apple"]
del fruits_colors["bumba"]  # What here?
del fruits_colors

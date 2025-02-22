items = ["apple","banana","orange","apple","mango"]

uniqueItem = set()

for item in items:
    if items in uniqueItem:
        print("Duplicate:",item)
        break;
    uniqueItem.add(item)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

def list_manipulate(list):
    list.pop(1)
    list.append("fig")
    print(list)

if __name__ == "__main__":
    list_manipulate(fruits)
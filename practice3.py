GIVEN = "pynative"

def logic():
    for i in range(0, len(GIVEN)-1, 2):
        print(GIVEN[i])

def logic2():
    sliced = GIVEN[::2]
    for char in sliced:
        print(char)

if __name__ == "__main__":
    logic2()
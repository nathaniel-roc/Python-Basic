running = True


def FToC(x):
    return x * 1.8 + 32


while running:
    try:
        x = int(input('Give me a number:   '))
        print(FToC(x))
        running = False
    except:
        print("The input is not an integer...")
        print("try again:   ")

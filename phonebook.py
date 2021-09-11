x = int(input())

dictt = {}

for i in range(x):
    text = input().split()
    dictt[text[0]] = text[1]

while True:
        inpt = input()
        if inpt in dictt:
            print(inpt+"="+dictt[inpt])
            break
        else:
            print("Not found")
            break
            
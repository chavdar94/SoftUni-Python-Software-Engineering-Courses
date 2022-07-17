script = input()
new_massage = []
for i in script:
    new_massage.append(i)

while True:
    command = input().split("|")
    if command[0] == "Decode":
        print(f"The decrypted message is: {''.join(new_massage)}")
        break

    if command[0] == "Move":
        item = new_massage[0:int(command[1])]
        for i in item:
            new_massage.append(i)
        del new_massage[0:int(command[1])]

    elif command[0] == "Insert":
        new_massage.insert(int(command[1]), str(command[2]))

    elif command[0] == "ChangeAll":
        for i in range(len(new_massage)):
            if new_massage[i] == command[1]:
                new_massage[i] = command[2]
if __name__ == '__main__':
    N = int(input())   # Read number of commands
    lst = []           # Initialize an empty list

    for _ in range(N):
        command = input().split()      # Read the command and split into parts
        cmd = command[0]               # First word is the command name

        if cmd == "insert":
            i = int(command[1])
            e = int(command[2])
            lst.insert(i, e)
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            e = int(command[1])
            lst.remove(e)
        elif cmd == "append":
            e = int(command[1])
            lst.append(e)
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()

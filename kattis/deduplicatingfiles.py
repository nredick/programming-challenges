import itertools


def hash_func(file):
    xor = 0
    for c in file:
        xor ^= ord(c)
    # return the xor
    return xor


def main():
    while True:
        n = int(input())
        if n == 0:  # eof
            break

        files = {}  # key = hash; value = [n, {}] where n is the # of times something hashed to the slot
        for i in range(0, n):  # loop through files in a group
            line = input()  # get a file aka line of input
            hashed_line = hash_func(line)  # hash the file
            if hashed_line not in files:  # if hash not in dict:files, add at the index of the hash
                files[hashed_line] = [0, {}]  # second index is dict to keep track of lines
            files[hashed_line][0] += 1  # keep track of the number of items at the hash index of the dict

            # counting real duplicates vs collisions
            if line not in files[hashed_line][1]:  # [0, {}]
                files[hashed_line][1][line] = 1  # line is dict key in sub dict
            else:
                files[hashed_line][1][line] += 1  # key already exists, increment it

        collision = 0
        unique = 0
        for _, value in files.items():
            if value[0] > 1:  # only enter filled hash slots
                combos = itertools.combinations([v[1] for v in value[1].items()], 2)
                for pair in combos:
                    collision += pair[0]*pair[1]
                unique += len(value[1])
            else:
                unique += 1
        print(unique, collision)


if __name__ == "__main__":
    main()

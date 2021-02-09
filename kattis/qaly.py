#!/usr/bin/env python3


def main():
    qaly = 0
    for i in range(int(input())):
        temp = [float(el) for el in input().split(' ')]
        qaly += temp[0] * temp[1]
    print(qaly)


if __name__ == "__main__":
    main()

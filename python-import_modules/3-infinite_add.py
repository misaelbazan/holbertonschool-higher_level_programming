#!/usr/bin/python3
import sys


def main():
    sum = 0
    for each_num in sys.argv[1:]:
        sum = int(each_num) + sum

    print(sum)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
import hidden_4


def main():

    for c in dir(hidden_4):
        if c[0] != "_":
            print(c)


if __name__ == "__main__":
    main()

def read_and_print(filename):
    with open(filename, "r") as fp:
        data = fp.readlines()
        for i in data:
            print(i)


def read_and_count(filename):
    with open(filename, "r") as fp:
        data = fp.readlines()
        counter = 0
        for i in data:
            if not i.startswith("T"):
                counter += 1
        print(counter)


def count_words(filename):
    with open(filename, "r") as fp:
        data = fp.readlines()
        counter = 0
        for i in data:
            counter += len(i.split())
        print(counter)


def count_the(filename):
    with open(filename, "r") as fp:
        data = fp.read()
        print(data.count("the"))


def display_words(filename):
    with open(filename, "r") as fp:
        data = fp.readlines()
        for i in data:
            for j in i.split():
                if len(j) <= 4:
                    print(j)


def count_words(filename):
    with open(filename, "r") as fp:
        data = fp.readlines()
        counter = 0
        for i in data:
            counter += i.count("this") + i.count("these")
        print(counter)


def count_ewords(filename):
    with open(filename, "r") as fp:
        counter = 0
        for i in fp.read().split():
            if i.endswith("e"):
                counter += 1
        print(counter)


def count_upper(filename):
    with open(filename, "r") as fp:
        counter = 0
        for i in fp.read().split():
            for j in i:
                if j.isupper():
                    counter += 1
        print(counter)


def hash_display(filename):
    with open(filename, "r") as fp:
        content = ""
        for i in fp.read().split():
            for j in i:
                content += j + "#"
        print(content)


import os.path


filepath = "./file.txt"
read_and_print(os.path.abspath(filepath))
read_and_count(os.path.abspath(filepath))
count_words(os.path.abspath(filepath))
count_the(os.path.abspath(filepath))
display_words(os.path.abspath(filepath))
count_ewords(os.path.abspath(filepath))
count_upper(os.path.abspath(filepath))
hash_display(os.path.abspath(filepath))

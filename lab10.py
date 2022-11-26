def stats(filename):
    fopen = open(filename, "rt")

    lines = fopen.readlines()

    fopen.seek(0)

    words = fopen.read()

    print("no of lines:", len(lines))
    print("no of words", len(words.split()))
    print("no of characters", len(list(words)))
    fopen.close()

stats("text.txt")

def distribution(filename):
    fopen = open(filename, "rt")

    read = fopen.read()
    read = read.split()

    temp = list()
    for i in read:
        if(i not in temp):
            if(read.count(i) > 1): print(read.count(i), "students got", i)
            else: print(read.count(i), "student got", i)
            temp.append(i)
    del(temp)

distribution("grades.txt")

def duplicates(filename):
    fopen = open(filename, "rt")

    words = fopen.read()
    fopen.close()
    words = words.split()

    for i in words:
        if(words.count(i) > 1):
            return True
        else: return False

print("File text.txt contains duplicate text:", duplicates("text.txt"))


def abc(self):
    fopen = open(self, "rt")
    read = fopen.read()
    print(read)
    fopen.close()

    read = read.split()

    for i, j in zip(read, range(len(read))):
        if(len(i) == 4):
            read[j] = "xxxx"
    read = " ".join(read)
    print(read)

    fopen = open("abc.txt", "x+")
    fopen.write(read)
    print(fopen.read())
    fopen.close()

abc("text.txt")
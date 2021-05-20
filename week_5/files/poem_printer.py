# f = open("invictus.txt")
# for line in f:
#     print(line)
# f.close()

# f = open("invictus.txt")
# for line in f:
#     # we could alternately use .strip() or .strip("\n") here
#     line = line.rstrip()
# print(line)
# f.close()

with open("invictus.txt") as f:
    for line in f:
        line = line.rstrip()
        print(line)

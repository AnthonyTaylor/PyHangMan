def num(lives):
    for i in range((((lives + 1)* 7)-7), ((lives + 1)* 7), 1):
        print (i)


# expected output:
# 43 - 49
num(6)


# expected output:
# 36 - 42
num(5)


# expected output:
# 29 - 35
num(4)


# expected output:
# 22 - 28
num(3)


# expected output:
# 15 - 21
num(2)


# expected output:
# 8 - 14
num(1)

# expected output:
# 1 - 7
num(0)
def print_stars(num):
    for i in range(1, num+1):
        for x in range(0,i):
            print("*",end='')
        print()


print_stars(5)
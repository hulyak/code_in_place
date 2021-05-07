
def main():
    x = 3
    # x = change(x)
    x = plus_five(x)
    print(x)


def plus_five(x):
    x += 5
    return x


if __name__ == '__main__':
    main()

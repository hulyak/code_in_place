
def main():
    mid = average(5.0, 10.2)
    print(mid)


def average(a, b):
    """
    returns the average of the two inputs. 
    assumes that both inputs are numbers.
    """
    total = a + b
    return total / 2


if __name__ == '__main__':
    main()

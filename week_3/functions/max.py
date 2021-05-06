def main():
    larger = max(1, 10)
    print(larger)


def max(num_1, num_2):
    """
    returns the larger of the two values
    """
    if num_2 > num_1:
        return num_2
    return num_1


if __name__ == '__main__':
    main()

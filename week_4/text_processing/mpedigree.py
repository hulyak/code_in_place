import random

N_LABELS = 5000


def main():
    for i in range(N_LABELS):
        rand_part = pad(random.randint(0, 99999), 5)
        unique_part = pad(i, 4)
        id = rand_part + unique_part
        print(id)


def pad(num, length):
    """
    >>> pad(42, 4)
    '0042'
    >>> pad(100, 3)
    '100'
    """
    num_string = str(num)
    while len(num_string) < length:
        # insert a 0 at the start of the string, increasing its length by one
        num_string = "0" + num_string
    return num_string


if __name__ == "__main__":
    main()

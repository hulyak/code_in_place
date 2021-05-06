def main():
    meters = float(input('enter meters: '))
    result = meters_to_cm(meters)
    print(result)


def meters_to_cm(meters):
    """
    Takes in meters as incoming information.
    Returns the corresponding number of cms
    """
    return 100 * meters


if __name__ == '__main__':

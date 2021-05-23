def main():
    print('hello world')
    ages = {
        'Mehran': 51,
        'Gary': 70,
        'Chris': 33,
        'Brahm': 24,
        'Adele': 33,
        'Freya': 0.3,
        'Lionel': 33,
        'Rihanna': 33,
        'Stephen': 33,
        'Skrillex': 33
    }
    reversed_dict = reverse(ages)

    # standard code to print out a dictionary
    print('Reversed:')
    # for each key
    for key in reversed_dict:
        # print out the key, and its corresponding value.
        print(key, '->', reversed_dict[key])


def reverse(original):
    """
    should create and return a new dictionary where
    the values of the original are now keys!
    """
    reversed_dict = {}
    for old_key in original:
        old_value = original[old_key]

        # actually we need to make a list for every value
        if old_value not in reversed_dict:
            # if it is the first time you have seen old_value...
            reversed_dict[old_value] = [old_key]
        else:
            # otherwise, lets find the list that already exists...
            reversed_dict[old_value].append(old_key)
    return reversed_dict


if __name__ == '__main__':
    main()

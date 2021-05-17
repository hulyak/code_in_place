"""
File: count_characters.py
-------------------------
This program counts the number of each character in the string TEXT.
It uses a dictionary to store the results, where each key is a
character and the corresponding value is the number of times that
character appeared in the string.
"""

TEXT = 'Happy day! I love the Code in Place community!'


def get_counts_dict(str):
    """
    Returns a dictionary with where each key is a character and the corresponding
    value is the number of times that character appeared in the string str passed in.
    """
    counts = {}                             # create empty dictionary

    for ch in str:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] += 1

    return counts


def print_counts(dict):
    """
    This function prints out the key and its associated value for each
    key/value pair in the dictionary passed in.
    """
    print('Counts from dictionary')
    for key in dict:
        print(str(key) + ' = ' + str(dict[key]))


def main():
    """
    Display the number of times each character appears in the constant TEXT.
    """
    count_dict = get_counts_dict(TEXT)
    print('count_dict = ', count_dict)
    print_counts(count_dict)


# Python boilerplate.
if __name__ == '__main__':
    main()

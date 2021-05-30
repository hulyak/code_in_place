from urllib.request import urlopen
import sys

# https://sixty-north.com/c/t.txt


def fetch_words(url):
    """ 
    Fetch a list of words from a URL 
    Args: 
        url: the URL of a UTF-8 text document
    Returns: 
        A list of strings containing the words from the document
    """
    story = urlopen(url)

    story_words = []

    for line in story:
        # decode bytes literals to unicode string
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_words(words)
# print(__name__) # __main__


if __name__ == '__main__':
    main(sys.argv[1])  # 0th arg is the module filename


# python3 words.py  https://sixty-north.com/c/t.txt

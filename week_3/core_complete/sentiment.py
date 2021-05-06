#!/usr/local/bin/python

import nltk.sentiment
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()


def main():
    while True:
        user_text = input('? ')
        score = get_sentiment(user_text)
        reaction = get_reaction(score)
        print(reaction)
        print(score)
        print('')


def get_reaction(score):
    """
    Parameter score: a float between -1 and 1.
    Return: an emoji as a string!
    """
    if score > 0.5:
        return "happier"
    if score > 0:
        return "happy"
    if score == 0:
        return "normal"
    if score < -0.5:
        return "sad"
    if score < 0:
        return "scared"


def get_sentiment(user_text):
    """
    Parameter user_text: any text(string)
    return: a sentiment score between -1 and +1 (float)
    """
    # 1. pass the text into the analyzer.polarity_scores function,part of nltk package
    scores = analyzer.polarity_scores(user_text)
    # 2. extract the sentiment score. Scores is a dictionary
    sentiment_score = scores['compound']
    return sentiment_score


if __name__ == '__main__':
    main()

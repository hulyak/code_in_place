from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []

for line in story:
  # byte literals prefixed with lowercase 'b', HTTP data is provided as bytes
  # use bytes.decode() to get strings
    line_words = line.decode('utf-8').split()
    for word in line_words:
        story_words.append(word)

story.close()
print(story_words)

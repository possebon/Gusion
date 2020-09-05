from scholarly import scholarly


# Retrieve the author's data, fill-in, and print
#earch_query = scholarly.search_author('Steven A Cholewiak')
#author = next(search_query).fill()

# Print the titles of the author's publications
#print([pub.bib['title'] for pub in author.publications])

# Take a closer look at the first publication
#pub = author.publications[0].fill()
#print(pub)

# Which papers cited that publication?
#print([citation.bib['title'] for citation in pub.citedby])
from nltk.corpus import stopwords
from collections import Counter
import string
STOPWORDS = set(stopwords.words("english"))
strings = ["aaabb kasjsahsaf", "afjfabjasfbhfasg asdasd"]
def get_most_common_words(data):
    common_words = Counter()
    for row in data:
        for word in row.split(" "):
            if len(word) > 3 and not word in STOPWORDS:
                punctuation = str.maketrans(dict.fromkeys(string.punctuation))
                word = word.translate(punctuation)
                common_words[word] += 1
    return common_words

print(get_most_common_words(strings))


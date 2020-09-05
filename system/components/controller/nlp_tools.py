# Python Standard Libraries
import re
import string
from collections import Counter
# External Libraries
import nltk
from nltk.corpus import stopwords
import pyLDAvis
import pyLDAvis.sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
# Components
#
# STOPWORDS
STOPWORDS = set(stopwords.words("english"))
# Topic modelling
def topic_modelling(data):
    abstracts = []
    for abstract in data:
        # Remove punctuation
        abstract = re.sub('[,\.!?]', '', abstract)
        # Remove numbers
        abstract = re.sub('[0-9]', '', abstract)
        # Convert the abstracts to lowercase
        abstract = abstract.lower()
        abstracts.append(abstract)
    # Splitting abstracts
    snnipets = []
    for abstract in abstracts:
        if abstract != "abstract not available":
            length = len(abstract)
            index = 0
            last_i = 0
            n=256
            while index < length:
                i = abstract.rfind(". ", index, index + n)
                if i == -1 or i == index:
                    i = index + n
                text = abstract[index : i + 2]
                index = i + 2
                snnipets.append(text)
    # Creating LDA
    #number_topics = 5
    tf_vectorizer  = CountVectorizer(stop_words='english')
    tfidf_vectorizer = TfidfVectorizer(**tf_vectorizer.get_params())
    dtm_tfidf = tfidf_vectorizer.fit_transform(snnipets)
    lda_tfidf = LDA( random_state=0)
    lda_tfidf.fit(dtm_tfidf)
    # Visualizing LDA
    data = pyLDAvis.sklearn.prepare(lda_tfidf, dtm_tfidf, tfidf_vectorizer, mds='mmds')
    html = pyLDAvis.prepared_data_to_html(data, template_type="simple")
    return html
# Common words
def common_words(data):
    common_words = Counter()
    for row in data:
        if row != "Abstract not available":
            for word in row.split(" "):
                if len(word) > 3 and not word in STOPWORDS:
                    punctuation = str.maketrans(dict.fromkeys(string.punctuation))
                    word = word.translate(punctuation)
                    word = word.lower()
                    common_words[word] += 1              
    counts = []
    words = []
    for word, count in common_words.most_common(30):
        counts.append(count)
        words.append(word)
    return words, counts
# Common bigrams
def common_bigrams(data):
    common_bigrams = Counter()
    for row in data:
        last_word = ""
        rows = row.split(" ")
        for word in rows:
            punctuation = str.maketrans(dict.fromkeys(string.punctuation))
            word = word.translate(punctuation)
            if len(word) > 3 and not word in STOPWORDS:
                if len(last_word) > 3 and not word in STOPWORDS:
                    common_bigrams[f"{last_word} {word}"] += 1
            last_word = word
    counts = []
    bigrams = []
    for bigram, count in common_bigrams.most_common(30):
        counts.append(count)
        bigrams.append(bigram)
    return bigrams, counts
# Common speech tagging
def common_speech_tagging(data):
    common_speech_tagging = Counter()
    for row in data:
        for word in row.split(" "):
            word = re.sub('[^A-Za-z0-9]+', '', word)
            if len(word) > 1:
                punctuation = str.maketrans(dict.fromkeys(string.punctuation))
                word = word.translate(punctuation)
                tagged = nltk.pos_tag([word])
                tag = tagged[0][1]
                common_speech_tagging[tag] += 1
                
    counts = []
    tags = []
    for tag, count in common_speech_tagging.most_common():
        counts.append(count)
        tags.append(tag)
    return tags, counts

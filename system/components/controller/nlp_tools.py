# Python Standard Libraries
import re
# External Libraries
import pyLDAvis
import pyLDAvis.sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
# Components
#
# Topic modelling
def topic_modelling(data):
    abstracts = []
    for abstract in data:
        # Remove punctuation
        abstract = re.sub('[,\.!?]', '', abstract)
        # Remove numbers
        abstract = re.sub('[0-9]', '', abstract)
        # Convert the titles to lowercase
        abstract = abstract.lower()
        abstracts.append(abstract)
    # Splitting abstracts
    snnipets = []
    for abstract in abstracts:
        print(abstract)
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
    number_topics = 5
    tf_vectorizer  = CountVectorizer(stop_words='english')
    tfidf_vectorizer = TfidfVectorizer(**tf_vectorizer.get_params())
    dtm_tfidf = tfidf_vectorizer.fit_transform(snnipets)
    lda_tfidf = LDA(n_components=number_topics, random_state=0)
    lda_tfidf.fit(dtm_tfidf)
    # Visualizing LDA
    data = pyLDAvis.sklearn.prepare(lda_tfidf, dtm_tfidf, tfidf_vectorizer, mds='mmds')
    html = pyLDAvis.prepared_data_to_html(data, template_type="simple")
    return html
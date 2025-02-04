import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


nltk.download('punkt')
nltk.download('stopwords')


def outputsumm(input_text, no_of_sentences=5):  # Default to 5 sentences if not provided
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(input_text)
    f = dict()
    for i in words:
        i = i.lower()
        if i in stopWords:
            continue
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    sentences = sent_tokenize(input_text)
    fsent = dict()
    for j in sentences:
        for x, y in f.items():
            if x in j.lower():
                if j in fsent:
                    fsent[j] += y
                else:
                    fsent[j] = y
    count = 0
    for k in fsent:
        count += fsent[k]
    average = int(count / len(fsent))
    output_text = ''
    for p in sentences:
        if (p in fsent) and (fsent[p] > (1.2 * average)):
            output_text += " " + p
    # Limit summary to no_of_sentences
    summarized_sentences = sent_tokenize(output_text)[:no_of_sentences]
    summarized_text = ' '.join(summarized_sentences)
    return summarized_text
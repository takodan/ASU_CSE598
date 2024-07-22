from flask import Flask, request
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

@app.route('/')
@app.route('/top10tfidf')
def calculate_top_tfidf():

    # get the texts/docs from args
    input = request.args.get('input', '')
    # path = 'output.txt'
    # f = open(path, 'a', encoding='utf-8')
    # f.write(input)
    # f.close()

    try:
        # print("***INPUT:", input)
        docs = input.lower().split(",")
        words = input.lower().split()


        # find top 10 words
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        top_10 = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]

        print("***TOP_10:", top_10)
        top_10_words_only = []
        for ele in top_10:
            top_10_words_only = top_10_words_only + [ele[0]]
        print(top_10_words_only)

        # calculate tf-idf
        tfidf = TfidfVectorizer(vocabulary=top_10_words_only)
        tfidf_result = tfidf.fit_transform(docs)
        words_names = tfidf.get_feature_names_out()

        results = []
        for doc_idx, doc in enumerate(docs):
            results = results + [f"<br>Document {doc_idx + 1}:"]
            for word_idx in tfidf_result[doc_idx].nonzero()[1]:
                results = results + [f"{words_names[word_idx]}: {tfidf_result[doc_idx, word_idx]:.4f}"]

        print(results)
        return " | ".join(results)


    except ValueError:
        return "Please input strings separate by comma"


if __name__ == '__main__':
    app.run('localhost', 4447)
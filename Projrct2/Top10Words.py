from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
@app.route('/topTen')
def Url():
    input = request.args.get('input', '')

    try:
        print("***INPUT:", input)
        # input = input + " python"*5 # for testing

        words = input.lower().split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        top_10 = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]

        print("***TOP_10:", top_10)
        
        return top_10

    except ValueError:
        return "Please input string"



if __name__ == '__main__':
    app.run('localhost', 4447)
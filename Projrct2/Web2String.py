from flask import Flask, request
import requests
from bs4 import BeautifulSoup as bs
import re

app = Flask(__name__)

# @app.route('/')
@app.route('/url')
def Url():
    input = request.args.get('input', '')

    try:
        print("***INPUT:", input)

        url = input
        response = requests.get(url)
        print("***RESPONSE:", response)
        soup = bs(response.text, "html.parser")
        body = soup.find("body").text.strip()
        print("***BODY:", body)
        result_without_punctuation = re.sub(r'(\b\w{2,})([,.!?])\s*', r'\1 ', body)
        print("***RESULT:", result_without_punctuation)

        return result_without_punctuation

    except ValueError:
        return "Please input url"



if __name__ == '__main__':
    app.run('localhost', 4449)
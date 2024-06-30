from flask import Flask, request
import requests
from bs4 import BeautifulSoup as bs
import re

app = Flask(__name__)

@app.route('/')
@app.route('/content')
def GetWebContent():

    # get the url from args
    input = request.args.get('input', '')

    try:
        # print("***INPUT:", input)
        url = input
        response = requests.get(url)
        # print("***RESPONSE:", response)

        # using bs to get the text without tags
        soup = bs(response.content, "html.parser")
        txt = soup.text.strip()
        # body = soup.find("body").text.strip()
        # print("***TEXT:", txt)

        # strip the text for later usage
        lines = txt.splitlines()
        non_blank_lines = [line for line in lines if line.strip()]
        stripped_lines = [line.strip() for line in non_blank_lines]
        stripped_string = '\n'.join(stripped_lines)
        stripped_string = stripped_string.replace(" |", "")
        stripped_string = stripped_string.replace(",", "")
        result_without_punctuation = re.sub(r'(\(*)(\b\w{2,})(\)*)([,.!?)])\s*', r'\2 ', stripped_string)
        # print("***RESULT:", result_without_punctuation.strip())

        return result_without_punctuation

    except ValueError:
        return "wrong url"



if __name__ == '__main__':
    app.run('localhost', 4449)
from flask import Flask, request
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

# @app.route('/')
@app.route('/url')
def Url():
    input = request.args.get('input', '')

    try:
        print("INPUT:", input)
        url = input
        response = requests.get(url)
        print("RESPONSE:", response)
        soup = bs(response.text, "html.parser")
        body = soup.find("body").text.strip()
        print(body)
        # bodyInList = body.split(", ")
        # print(bodyInList)
        return "String get: \n"+body
    except ValueError:
        return "Please input url"



if __name__ == '__main__':
    app.run('localhost', 4449)
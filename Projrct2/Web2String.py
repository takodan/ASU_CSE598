from flask import Flask, request
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/')
@app.route('/url')
def absolute():
    input = request.args.get('input', '')

    try:
        print("*****", input)
        url = input
        response = requests.get(url)
        print("*****", response)
        soup = bs(response.text, "html.parser")
        body = soup.find("body").text.strip()
        print(body)
        # bodyInList = body.split(", ")
        # print(bodyInList)
        return "String get"
    except ValueError:
        return "Please input url"

    

if __name__ == '__main__':
    app.run('localhost', 4449)
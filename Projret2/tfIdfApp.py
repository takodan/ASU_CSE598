from flask import Flask, request, render_template, redirect, url_for, flash
import urllib3
from bs4 import BeautifulSoup as bs
from urllib.parse import urlencode
import requests
import urllib.parse

app = Flask(__name__)
app.secret_key = 'this is my key'

@app.route('/')
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/answer', methods = ['POST'])
def answer():

    # get urls
    first_url = ""
    first_url = dict(request.form.items())["Url"]
    print(first_url)

    if not first_url:
        flash("Url is required!")
        return redirect(url_for('form'))


    http = urllib3.PoolManager(retries=False)
    other_two_urls = get_first_two_links(first_url)
    print(other_two_urls)

    urls = [first_url] + other_two_urls
    print("***URLS:", urls)

    # call Web2String to get texts
    url_texts = []
    for url in urls:
        try:
            response = http.request("GET", "http://localhost:4449/content?input="+url)
            url_texts = url_texts + [response.data.decode("utf-8")]
            response.close()
        except urllib3.exceptions.NewConnectionError:
            url_texts = url_texts + ["Invalid link"]
    
    # filter the texts
    not_filtered_texts = []
    for url_text in url_texts:
        if not url_text == "Invalid link":
            not_filtered_texts = not_filtered_texts + [url_text]
    
    filtered_texts = []
    # texts_string = ' '.join(not_filtered_texts)
    # path = 'output0.txt'
    # f = open(path, 'a', encoding='utf-8')
    # f.write(astring)
    # f.close()


    if not not_filtered_texts:
        filtered_texts = ["no text to be filtered"]
    else:
        for not_filtered_text in not_filtered_texts:
            not_filtered_text = urllib.parse.quote(not_filtered_text)
            # path = 'output0.txt'
            # f = open(path, 'a', encoding='utf-8')
            # f.write(not_filtered_text)
            # f.close()
            response = requests.get("http://localhost:4448//filter?input=" + not_filtered_text)
            # response = http.request("GET", "http://localhost:4448//filter?input=" + not_filtered_text)
            filtered_texts = filtered_texts + [response.content.decode("utf-8")]
            response.close()
        
        print(filtered_texts)

    # get top 10 words and their tf-idf
    try:
        filtered_string = ",".join(filtered_texts)
        # path = 'output0.txt'
        # f = open(path, 'a', encoding='utf-8')
        # f.write(filtered_string)
        # f.close()
        filtered_string = urllib.parse.quote(filtered_string)
        response = http.request("GET", "http://localhost:4447/top10tfidf?input="+ filtered_string)
        answer = response.data.decode("utf-8")
        response.close()
    except urllib3.exceptions.NewConnectionError:
        url_texts = url_texts + ["Something went wrong"]


    
    return \
        "The text form first page:<br>"+url_texts[0]+"<br><br>"\
        "The text form second page:<br>"+url_texts[1]+"<br><br>"\
        "The text form third page:<br>"+url_texts[2]+"<br><br>"\
        "The filtered texts:<br>"+filtered_texts[0]+"<br><br>"+filtered_texts[1]+"<br><br>"+filtered_texts[2]+"<br><br>"\
        "The answer is :<br>"+answer+"<br><br>"\
        '''
        <br>
        <form action="/form" method = "GET">
            <p><input type = "submit" value = "Try again" /></p>
        </form>
        '''

def get_first_two_links(url):

    # to get other 2 urls
    http = urllib3.PoolManager(retries=False)
    response = http.request("GET", url)
    soup = bs(response.data, 'html.parser')

    links = soup.find_all('a', href=True)[:2]
    return [link['href'] for link in links]


if __name__ == '__main__':
    app.run('localhost', 5000)
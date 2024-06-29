import requests
from bs4 import BeautifulSoup as bs
import string
import re

def Web2String(input):
  print("INPUT:", input)

  url = input
  response = requests.get(url)
  print("RESPONSE:", response)
  soup = bs(response.text, "html.parser")
  body = soup.find("body").text.strip()
  print(body)
  punctuation = set(string.punctuation)
  no_punctuation_text = ''.join(ch for ch in text if ch not in punctuation)
  return no_punctuation_text

if __name__ == '__main__':
  text = "This is an example sentence with punctuation!@#$%^&*()?"
  cleaned_text = remove_punctuation(text)
  print(cleaned_text)
  return "String get: \n"+body
# url = "http://localhost:5000/"
# response = requests.get(url)
# soup = bs(response.text, "html.parser")
# body = soup.find("body").text.strip()
# print(body)
# data = body.split()
# print(data)

# txt = "one one was a race horse, two two was one too."

# x = txt.replace("o", "t")
# print(x)

stopWords = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
    "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself',
    'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her',
    'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',
    'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
    "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be',
    'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
    'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as',
    'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against',
    'between', 'into', 'through', 'during', 'before', 'after', 'above',
    'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
    'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
    'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own',
    'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just',
    'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're',
    've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn',
    "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
    "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't",
    'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn',
    "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
    ]

text1 = "This Web page tests a Python service which takes a number and return its absolute value.\
\
Url  E.g. http://localhost:4449/\
Input  E.g. 1, 2, -3, -4.5"


def remove_stopwords(text):
  stop_words = stopWords
  filtered_words = [word for word in text.split() if word.lower() not in stop_words]
  return ' '.join(filtered_words)

if __name__ == '__main__':
  text = text1
  cleaned_text = remove_stopwords(text)
  print(cleaned_text)

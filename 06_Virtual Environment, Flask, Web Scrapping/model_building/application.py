from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)   # __main__

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)

status = response.status_code

content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.body)

@app.route('/')
def index():
    return "Hello from Index of My Flask App"

@app.route('/status')
def india():
    return "Hello"

@app.route('/profile')
def profile():
    name = "Himanshu Ramchandani"
    return render_template('index.html', n = name)

if __name__ == '__main__':
    app.run(port=5000)


#   https://github.com/hemansnation
#  scheme   DNS          / routes
#    Domain Name System 

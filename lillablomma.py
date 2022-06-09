
from ctypes import Structure
from flask import Flask, render_template
from numpy import unicode_
import requests
from bs4 import BeautifulSoup as bs
from sympy import true




def grab():
    try:
        list = []
        #create a  new txt file to store the data
        f = open("data.txt", mode='w+t',encoding="utf-8")
        request = requests.get('https://lbkc.se/smorgasbutik/veckans-meny/')
        #convert to a soup object
        soup = bs(request.content, features="lxml")
        list.append('__________________________________'+'LILLA BOMMEN' + '__________________________________')
        for day in soup.find_all('div', class_='food-menu folded'):
            list.append(day.h2.text + ' ')
            for meal in day.find_all('div', class_='row mb-4'):
                list.append(meal.get_text())
            list.append('_________________')

        request = requests.get('https://restauranglappstiftet.gastrogate.com/lunchmeny/')
        #convert to a soup object
        soup = bs(request.content, features="lxml")
        list.append('__________________________________'+'RESTAURANG LÄPPSTIFTET' + '__________________________________')

        for thing in soup.find('table', class_='table lunch_menu animation'):
            for text in thing.stripped_strings:
                list.append(text)
            if thing.name == 'tbody':
                list.append('_________________')
    finally:
    #return file to browser
    
        return list
    #myString = ' '.join(map(str,list))
    #pageList = f"<html><head><title>Lunchmeny</title></head><body><h1>Lunchmeny</h1><p>{myString}</p></body></html>"
    #myString = ' '.join(map(str,list))
    #return myString

# with open('index.html','w', encoding="utf-8") as f:
#     f.write(pageList)
    


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",content=grab())
    

if __name__ == "__main__":
	app.run(debug=true)

app.run(debug = True)
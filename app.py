from flask import Flask, redirect, render_template, request,jsonify,session,url_for
import os
import json
import urllib
import requests
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'harrish07')

def plotp(key):
    url = 'https://parseapi.back4app.com/classes/Indiacities_india_cities_database?limit=30&order=-population&keys=ascii_name,population'
    headers = {
        'X-Parse-Application-Id': 'bBB1GF1hGSKHO3IYwP1oNU07HxISLxdfQxieDHyt', # This is your app's application id
        'X-Parse-REST-API-Key': 'ZLiGteuGocYrU7iSlDtNcpxHyKN3cDwpUjjpiUUk' # This is your app's REST API key
    }
    data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
    dat = json.dumps(data, indent=2)
    dat = json.loads(dat)
    dat2 = dat['results']
    plotd = {}
    for i in dat2:
        try:
            plotd[i['ascii_name']] = i['population']
        except:
            plotd[i['ascii_name']] = 0


    print(plotd)

    plotd1 = {}
    plotd2 = {}
    plotd3 = {}
    ind = 0
    for i in plotd:
        if ind == 30:
            break
        if ind < 10:
            plotd1[i] = plotd[i]
        elif ind < 20:
            plotd2[i] = plotd[i]
        else:
            plotd3[i] = plotd[i]
        ind += 1 
        


    

    courses = list(plotd1.keys())
    values = list(plotd1.values())
    
    fig = plt.figure(figsize = (15, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon',
            width = 0.4)
    
    plt.xlabel("Cities")
    plt.ylabel("Population")
    plt.title("Population census")
    plt.savefig('static/images/population1.jpg')

    courses = list(plotd2.keys())
    values = list(plotd2.values())
    
    fig = plt.figure(figsize = (15, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon',
            width = 0.4)
    
    plt.xlabel("Cities")
    plt.ylabel("Population")
    plt.title("Population census")
    plt.savefig('static/images/population2.jpg')

    courses = list(plotd3.keys())
    values = list(plotd3.values())
    
    fig = plt.figure(figsize = (15, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon',
            width = 0.4)
    
    plt.xlabel("Cities")
    plt.ylabel("Population")
    plt.title("Population census")
    plt.savefig('static/images/population3.jpg')



def plote(key):
    url = 'https://parseapi.back4app.com/classes/Indiacities_india_cities_database?limit=30&order=-elevation&keys=ascii_name,elevation'
    headers = {
        'X-Parse-Application-Id': 'bBB1GF1hGSKHO3IYwP1oNU07HxISLxdfQxieDHyt', # This is your app's application id
        'X-Parse-REST-API-Key': 'ZLiGteuGocYrU7iSlDtNcpxHyKN3cDwpUjjpiUUk' # This is your app's REST API key
    }
    data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
    dat = json.dumps(data, indent=2)
    dat = json.loads(dat)
    dat2 = dat['results']
    plotd = {}
    for i in dat2:
        try:
            plotd[i['ascii_name']] = i['elevation']
        except:
            plotd[i['ascii_name']] = 0

    print(plotd)


    plotd1 = {}
    plotd2 = {}
    plotd3 = {}
    ind = 0
    for i in plotd:
        if ind == 30:
            break
        if ind < 10:
            plotd1[i] = plotd[i]
        elif ind < 20:
            plotd2[i] = plotd[i]
        else:
            plotd3[i] = plotd[i]
        ind += 1 
        


    

    courses = list(plotd1.keys())
    values = list(plotd1.values())
    
    fig = plt.figure(figsize = (15, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon',
            width = 0.4)
    
    plt.xlabel("Cities")
    plt.ylabel("Elevation")
    plt.title("Elevation census")
    plt.savefig('static/images/elevation1.jpg')

    courses = list(plotd2.keys())
    values = list(plotd2.values())
    
    fig = plt.figure(figsize = (15, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon',
            width = 0.4)
    
    plt.xlabel("Cities")
    plt.ylabel("Elevation")
    plt.title("Elevation census")
    plt.savefig('static/images/elevation2.jpg')

    courses = list(plotd3.keys())
    values = list(plotd3.values())
    
    fig = plt.figure(figsize = (15, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon',
            width = 0.4)
    
    plt.xlabel("Cities")
    plt.ylabel("Elevation")
    plt.title("Elevation census")
    plt.savefig('static/images/elevation3.jpg')


@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/loads', methods = ['POST'])
def load():

    session['key'] = 0
    plotp(0)
    plote(0)

    return jsonify({'data' : 1})


if __name__ == "__main__":
    app.run(debug = True)
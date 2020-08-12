
import flask
from flask import Flask, redirect, url_for, request, render_template, make_response, jsonify
from class_user import *
from heatmap import *

app = Flask(__name__)

"""
NOTE: @app.route('/test'), ('/login'), and ('/success) are all for TESTING
They will not go into the final product
TODO:
- Create requirements.txt
- Create basic working pages with HTML/CSS from Bootsnip
- Create login page (Still needs frontend)
- Heatmap Page (Still needs frontend)
- Contact Tracing Page (Still needs frontend)
- Warning notification Page 
"""



"""This is the home page, it checks to see if you have already logged in or not before redirecting you"""
@app.route('/home')
def home_page():
    print('Cookies:', request.cookies.keys())
    if ('Name' in request.cookies.keys()) and ('User ID' in request.cookies.keys()) and ('Password' in request.cookies.keys()):
        return render_template('home_page.html')
    else:
        return render_template('index.html')

"""This is the login page. We do this with the assumption the user has already made an account
It also sets cookies for the user when they log in again, so they don't have to keep doing it"""
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        name, user_id, password = request.form.values()
        #print("DEBUG LOGIN:", name, user_id, password)
        resp = flask.make_response(render_template('home_page.html'))
        resp.set_cookie('Name', name)
        resp.set_cookie('User ID', user_id)
        resp.set_cookie('Password', password)
        return resp

"""This is the heatmap"""
@app.route('/heatmap')
def heatmap():
    #generate_heatmap()
    return render_template('heatmap.html')

"""This is the list of those the user has been in contact with"""
@app.route('/contact_tracr')
def contact_tracer():
    john = Tracr_User(55555, 'ImAFake')
    john.name = 'John Doe'
    shalin = Tracr_User(12345, 'No')
    dan = Tracr_User(54321, 'Yes')
    youssef = Tracr_User(11221, 'Maybe')

    users = [john, shalin, dan, youssef]
    interact([john, shalin], 'August 9')
    interact([john, dan], 'August 10')
    interact([john, youssef], 'August 11')
    #print('DEBUG contact tracer fxn:', request.cookies)

    return render_template('contact_tracr.html', user_id = int(request.cookies['User ID']), users = users)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)


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

john = Tracr_User(55555, 'ImAFake')
john.name = 'John Doe'
shalin = Tracr_User(12345, 'No')
dan = Tracr_User(54321, 'Yes')
youssef = Tracr_User(11221, 'Maybe')

#users = [john, shalin, dan, youssef]
interact([john, shalin], 'August 11')
interact([john, dan], 'August 10')
interact([john, youssef], 'August 9')
interact([john, Tracr_User(84720, 'Maybe')], 'August 9')
interact([john, Tracr_User(37564, 'Maybe')], 'August 8')
interact([john, Tracr_User(20472, 'Maybe')], 'August 8')
interact([john, Tracr_User(20291, 'Maybe')], 'August 8')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe', True)], 'August 8')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 6')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 5')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 5')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 5')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 4')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 4')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 3')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 3')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 2')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'August 1')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'July 30')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'July 30')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'July 29')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'July 29')
interact([john, Tracr_User(random.randint(10000, 99999), 'Maybe')], 'July 28')

logged_in = False

"""This is the home page, it checks to see if you have already logged in or not before redirecting you"""
@app.route('/home')
def home_page():

    if logged_in:
        return render_template('home_page.html')
    else:

        return render_template('index.html', logged_in=True)

"""This is the login page. We do this with the assumption the user has already made an account
It also sets cookies for the user when they log in again, so they don't have to keep doing it"""
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        name, user_id, password = request.form.values()
        print("DEBUG LOGIN:", name, user_id, password)

        if int(user_id) in john.login_info.keys() and john.login_info[int(user_id)] == password:
            global logged_in
            logged_in = True
            resp = flask.make_response(render_template('home_page.html'))
            resp.set_cookie('Name', name)
            resp.set_cookie('User ID', user_id)
            resp.set_cookie('Password', password)
            return resp
        else:
            return render_template('index.html', logged_in=False)

"""This is the heatmap"""
@app.route('/heatmap')
def heatmap():
    generate_heatmap()
    return render_template('heatmap.html')

"""This is the list of those the user has been in contact with"""
@app.route('/contact_tracr')
def contact_tracer():

    print('DEBUG contact tracer fxn:', john.interactions)

    return render_template('contact_tracr.html', user_id = int(request.cookies['User ID']), interactions = john.interactions)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)

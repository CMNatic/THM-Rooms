from flask import Flask, redirect, render_template, make_response, request
from datetime import datetime

import uuid
import pickle
import base64

import sys

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html')

@app.route("/myprofile", methods=['GET'])
def myprofile():
    cookie = request.cookies.get('userType')
    exchangedCookie = request.cookies.get('exchangeStatus')
    if cookie is None:
        return "Uh oh! You need to create an account first!"

    if 'admin' in cookie:
        resp = make_response(redirect("/admin"))
        return resp

    if 'user' in cookie:
        username = request.cookies.get('username')
        accesslevel = request.cookies.get('userType')
        registration = request.cookies.get('registrationTimestamp')
        return render_template('myprofile.html', username=username, accesslevel=accesslevel, registration=registration)

    if exchangedCookie:
        exchanged = 'Yes!'
        exchangeCookie = pickle.loads(base64.b64decode(exchangedCookie))

        return render_template('myprofile.html', exchanged=exchanged)

    else:
        return "Your cookie is not set to a valid account type. Try again!"


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        encodedflag = "FLAG_REDACTED"

        dateTime = datetime.now()

        timestamp = str(dateTime)

        userType = "user"
        token = str(uuid.uuid4().hex)
        session = {"sessionId": token, "encodedflag": encodedflag}
        pickle_cmnatic = pickle.dumps(session)
        encodedSessionCookie = base64.b64encode(pickle_cmnatic)

        resp = make_response(redirect("/login"))
        resp.set_cookie("userType", userType)
        resp.set_cookie("sessionId", encodedSessionCookie)
        resp.set_cookie("username", username)
        resp.set_cookie("password", password)
        resp.set_cookie("registrationTimestamp", timestamp)
        print(resp, file=sys.stderr)
        print(resp, file=sys.stdout)
        return resp

    else:
        return render_template('register.html')


#    # return render_template('register.html')


@app.route("/login", methods=['GET'])
def login():
    cookie = request.cookies.get('userType')
    if cookie is None:
        return "Uh oh! You need to create an account first!"

    # cookie = pickle.loads(base64.b64decode(cookie))

    else:
        resp = make_response(redirect("/myprofile"))
        return resp

    print(cookie, file=sys.stderr)
    print(cookie, file=sys.stdout)

@app.route("/admin")
def admin():
    adminflag = "FLAG_REDACTED"
    username = request.cookies.get('username')

    pickle_admin = pickle.dumps(adminflag)
    adminFlagE = base64.b64encode(pickle_admin)

    resp = make_response(redirect("/admin"))
    resp.set_cookie("adminflag", adminflag)

    return render_template('admin.html', username=username, adminflag=adminflag)


@app.route("/exchange", methods=['GET', 'POST'])
def exchange():
#    exchangedStatus = "Yes!"
#    exchangedata = 'vulnerable!'
    payload = "default"
    cookie = { "replaceme":payload}


#    pickle_exchangedata = pickle.dumps(exchangedata)

#    encodeddata = base64.b64encode(pickle_exchangedata)

    pickle_payload = pickle.dumps(cookie)
    encodedPayloadCookie = base64.b64encode(pickle_payload)
    resp = make_response(redirect("/myprofile"))
    resp.set_cookie("encodedPayload", encodedPayloadCookie)


#    resp.set_cookie("exchangeStatus", exchangedStatus)
#    resp.set_cookie("exchangeData", encodeddata)
    return resp

#    return render_template('myprofile.html', exchangedStatus=exchangedStatus)

@app.route("/quiz", methods=['GET', 'POST'])
def quiz():

    return render_template('quiz.html')

@app.route("/feedback", methods=['GET', 'POST'])
def feedback():

    cookie = request.cookies.get("encodedPayload")
    cookie = pickle.loads(base64.b64decode(cookie))

    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")

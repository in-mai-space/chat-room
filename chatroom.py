from flask import Flask, redirect, url_for, request, render_template, session
from flask_socketio import emit, SocketIO

app = Flask(__name__) 
app.secret_key = 'SECRET_KEY' 
socketio = SocketIO(app) 

# constant definition
username = [] 
password = []
message = [] 
login_error = "You have not sign up for an account or your username is wrong"
password_failure = "Wrong password, please try again"
username_error = "Username already exists, please choose another one"

@app.route('/success/<name>') 
def success(name):
    if 'logged_in' in session:
        return f'Welcome {name}, view your <a href="/feed">feed</a>. <br> You are logged in! <a href="/logout">Logout</a> '
    else:
        return 'Please Login! <a href="/login">Login</a>' 

# render templates when users login
@app.route("/login", methods = ['POST', 'GET'])
def login(): 
    global username, password
    if request.method == 'POST':
        user = request.form['name'] if 'name' in request.form else ""
        passw = request.form['pass'] if 'pass' in request.form else ""
        for i in range(len(username)): 
            if username[i] == user: 
                if password[i] == passw: 
                    session['logged_in'] = True
                    session['user'] = user
                    return redirect(url_for('success', name = user))
    return render_template('login.html', username = username, password = password, password_failure = password_failure, login_error  = login_error) 
            
# render templates when users sign up         
@app.route("/signup", methods = ['POST', 'GET'])
def signup(): 
    global username, password, username_error
    if request.method == 'POST':
        new_username = request.form['name']
        if new_username in username:  # Check if the username already exists
            return render_template('signup.html', username = username, username_error=username_error)
        else:
            username.append(new_username)
            password.append(request.form['pass']) 
            return redirect(url_for('login'))
    return render_template('signup.html') 

# if user is logged in, redirect them to log out, else log in         
@app.route('/')
def index():
    if 'logged_in' in session:
       return 'You are logged in! <a href="/logout">Logout</a> '
    else:
       return 'Please Login! <a href="/login">Login</a> ' 

# event handler that responds to the 'message' event and updates the message list and emits an 'update' event to the connected clients
@socketio.on('send_message')
def handle_message(data):
    message.insert(0, data)
    socketio.emit('receive_message', {'message': data})

# if user is logged out, pop session
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

# render feed template for users where they can post message
# updates the message list when a POST request is made, and emits a new message to the Socket.IO server
@app.route('/feed', methods = ['POST', 'GET']) 
def view_feed(): 
    global message
    if request.method == 'POST':
        session['logged_in'] = True
        user_message = request.form['message'] 
        if 0 < len(user_message) and 'logged_in' in session:
            new_message = session['user'] + ": " + user_message
            message.insert(0, new_message)
            socketio.emit('receive_message', {'message': new_message})
    return render_template('feed.html', message = message, name = session['user']) 

if __name__ == '__main__':
    socketio.run(app, debug=True, port=8123, host="0.0.0.0")

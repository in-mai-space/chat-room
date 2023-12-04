# chat-room: Technical Challenge for Code4Community

<h2>Overview</h2>
<p>This is a chat room that allows users to sign up, log in, log out, post under a username and chat with other users from different devices.</p>
<ul>
<li>Languages: Python, Javascript, HTML</li>
<li>Framework: Flask, Bootstrap</li>
<li>Other Tools: Socket.IO library, jQuery library, Jinjja2 web template</li>
</ul>
<p>I used Python since it is a beginner friendly language that I am more familiar with, and Flask framework which is helpful and simple to build small web apps. While, Bootstrap allows me to modify the front-end design from libraries without building CSS from scartch. Jinjja2 web template is a way to incorporate Python code into HTML file.</p>
<p>Another technology that I used is Socket.IO. I encountered the problem of needing to refresh the page to see newest messages form other users. Thus, since socket.io supports real time and bi-directional communication between servers and users, all users can view messages from other users without the need to refresh.</p>
<br>

<h2>Components and Interactions</h2>
<p>My web app is comprised of two main parts:</p>
<ul>
    <li>HTML templates (feed.html, login.html, signup.html): These files store the front-end interface that users interact with and Javascript code that connects with the server.</li>
    <li>Back-end file (chatroom.py): This file stores functions that operate the front-end interface for users, such as redirecting users to signup, login, see and post in their feed and logout.</li>
</ul>
<p>session['logged_in'] is used to store a key-value pair in the session. When a user successfully logs in, session['logged_in'] is set to True. When the user logs out (session.pop('logged_in', None)), this key is removed from the session, signifying that the user is no longer logged in.</p>
<p>When a user is in session, they will be redirect to login.html page. If users have not signed up, they can choose to signup for a new account. When users are logged in, they have an option to either log out or view their feed, which will redirect them to feed.html page.</p>
<p>To sign up, users are redirected to signup.html. As users enter the info, POST method is used to pull the data users enter to the chatroom.py to protect their data since it will not display private information on the link. It will append the username and password to two lists. To log in, users are redirected to login.html, where their information is also pulled using POST method and will be compared to data in existing lists. If the password and username matches, users log in successfully and will have option to view their feed or log out.</p>
<p>There are a few errors users might encounter, such as signing up with a username that already exists, or logging in with wrong username or password. An error message will appear to tell users what the error if the conditions above are not met.</p>
<p>In chatroom.py, view_feed() handles HTTP requests to display and update a feed. It updates the message list by receiving what the users enter when a POST request is made, and emits a new message to the Socket.IO server. handle_message() is a Socket.IO event handler that responds to the 'message' event. When this event is triggered by view_feed(), it updates the message list and emits an 'update' event to the connected clients. From client-side (Javascript code in feed.html), when user connects, it will wait for message sent by the server, then div is created to display received messages and add on to the webpage. These three components keep working in a cycle to ensure communication between users and the server. </p>
<p>The second function in Javascript in feed.html adds a listener to the form user is entering message in to count the length. If the length of the string that users enter exceeds the maxchar, it prevents further input by returning false. If the length is greater than 0 but does not exceed the limit, it shows the remaining characters.</p>

<br>

<h2>Requirements</h2>
<b><p>Requirement 1: Users should be able to type a message and post it to the message board.</p></b>
<ul>
    <li>Users cannot post non-empty message since there is a conditional in chatroom.py that new messages can only be posted if its length is larger than 0.</li>
    <li>There is also a text displayed how many characters users have left. When the text in the box reaches limit of 128 characters, users cannot type more, since there is a Javascript function in feed.html that enforces the limit. Users will not be able to type a string that has length longer than 128 characters.</li>
</ul>
<b><p>Requirement 2: Users should be able to see messages on the message board from most to least recent as the latest message will be append to the beginner of list of messages.</p></b>
<ul>
    <li>I created a list of messages, as a user posts a new string, it is appended in the beginning for the list in chatroom.py, and all the messages in the list will be displayed on the feed using for loop in feed.html</li>
    <li>When user waits for communication from the server, the latest message from other users will also be prepend to the container of all text messages from Javascript function from feed.html</li>
</ul>
<b><p>Requirement 3: Users on different computers should be able to post to the same board and view each other’s messages.</p></b>
<ul>
    <li>Since users can sign up under a username, and all their messages are stored in a list, all past messages stored in list will be shown. SocketIO also allows users to see other users' messages the instant they send it without refreshing.</li>
</ul>
<br>

<h2>Additional Feature</h2>
<p>Users can signup, login, logout and post under a username.</p>
<br>

<h2>Installation and Running the Program</h2>
<h3>Installation Guide</h5>
<ol>
    <li>Install an IDE (e.g. VSCode)</li>
    <li>Install Python https://www.python.org/downloads/</li>
    <li>can either install using the commands below in terminal for Mac, or create (python -m venv venv) and activate a new environment (venv\Scripts\activate) in terminal of IDE, then run the commands in the IDE terminal</li>
    <ul>
        <li>Install Flask command: pip install -U Flask</li>
        <li>Install Socket.io command: pip install flask-socketio</li>
        <li>Install jinja2 command: pip install -U Jinja2</li>
    </ul>
</ol>

<h3>How to Run the Program</h5>
<ol>
    <li>Download or clone the project from the repository</li>
    <li>Run chatroom.py in IDE (e.g. VSCode)</li>
    <li>Access app through the link: http://10.110.197.207:8123</li>
</ol>


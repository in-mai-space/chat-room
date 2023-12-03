# chat-room: Technical Challenge for Code4Community

<h2>Overview</h2>
<p>This is a chat room that allows users to sign up, log in, log out, post under a username and chat with other users from different devices.</p>
<ul>
<li>Languages: Python, Javascript, HTML</li>
<li>Framework: Flask, Bootstrap</li>
<li>Other Tools: Socket.IO library, Jinjja2 web template</li>
</ul>
<p>I used Python since it is a beginner friendly language that I am more familiar with, and Flask framework which is helpful and simple to build small web apps. While, Bootstrap allows me to modify the front-end design from libraries without building CSS from scartch. Jinjja2 web template is a way to incorporate Python code into HTML file.</p>
<p>Another technology that I used is Socket.IO. I encountered that problem of needing to refresh the page to see newest messages form other users. Thus, since socket.io supports real time and bi-directional communication between servers and users, all users can view messages from other users without the need to refresh.</p>
<br>

<h2>Components and Interactions</h2>
<p>My web app is comprised of two main parts:</p>
<ul>
    <li>HTML templates (feed.html, login.html, sign.html): These files store the front-end interface that users interact with and Javascript code that connects with the server.</li>
    <li>Back-end file (chatroom.py): This file stores functions that operate the front-end interface for users, such as redirecting users to signup, login, see and post in their feed and logout.</li>
</ul>
<br>

<h2>Requirements</h2>
<p>Requirement 1: Users should be able to type a message and post it to the message board.</p>
<ul>
    <li>Users cannot post non-empty message since there is a conditional in chatroom.py that new messages can only be posted if its length is larger than 0.</li>
    <li>There is also a text displayed how many characters users have left. When the text in the box reaches limit of 128 characters, users cannot type more, since there is a Javascript function in feed.html that enforces the limit. Users will not be able to type a string that has length longer than 128 characters.</li>
</ul>
<p>Requirement 2: Users should be able to see messages on the message board from most to least recent as the latest message will be append to the beginner of list of messages.</p>
<ul>
    <li>I created a list of messages, as a user posts a new string, it is appended in the beginning for the list in chatroom.py, and all the messages in the list will be displayed on the feed using for loop in feed.html</li>
    <li>When user waits for communication from the server, the latest message from other users will also be prepend to the container of all text messages from Javascript function from feed.html</li>
</ul>
<p>Requirement 3: Users on different computers should be able to post to the same board and view each other’s messages.</p>
<ul>
    <li>Since users can sign up under a username, and all their messages are stored in a list, all past messages stored in list will be shown. SocketIO also allows users to see other users' messages the instant they send it without refreshing.</li>
</ul>
<br>

<h2>Additional Feature</h2>
<p>Users can signup, login, logout and post under a username.</p>
<br>

<h2>Installation and Running the Program</h2>
- IDE: VSCode
- install Flask
- install jinjja2
- must have Python support
- can run on either on of these two links
    http://127.0.0.1:8123
    http://10.110.197.207:8123


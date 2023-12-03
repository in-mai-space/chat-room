# chat-room: Technical Challenge for Code4Community

**A high level overview**
<p>This is a chat room that allows users to sign up, log in, log out, post under a username and chat with other users from different devices.</p>
<ul>
<li>Languages: Python, Javascript, HTML</li>
<li>Framework: Flask, Bootstrap</li>
<li>Other Tools: Socket.IO library, Jinjja2 web template</li>
</ul>
<p>I used Python since it is a beginner friendly language that I am more familiar with, and Flask framework which is helpful and simple to build small web apps. While, Bootstrap allows me to modify the front-end design from libraries without building CSS from scartch. Jinjja2 web template is a way to incorporate Python code into HTML file, which is useful to make changes to front-end.</p>
<p>Another technology that I used is Socket.IO. I encountered that problem of needing to refresh the page to see newest messages form other users. Thus, since socket.io supports real time and bi-directional communication between servers and users, all users can view messages from other users without the need to refresh.</p>

**An explanation of the components and their interactions**
Main 3 components:
- static files (CSS)
- templates (HTML + Javascript)
- chatroom.py (back-end of the app) 
- MORE WORK ON THIS

**Why you fulfill the requirements**
- Users should be able to type a message and post it to the message board. If the message non-empty, users would not be able to send the message to the board.
- There is also text displayed how characters users have left, and when it reaches the limit of 128 characters users cannot type more.
- Users should be able to see messages on the message board from most to least recent as the latest message will be append to the beginner of list of messages.
- Users on different computers should be able to post to the same board and view each other’s messages without the need to refresh the page.
- potentially add media to each of these points 

**Additional Features**
- Allow users to sign up, log in, log out, and post under a username.

**How to Install and Run the Project**
Choose something reasonable; if we can’t run it, we can’t grade it.
- IDE: VSCode
- install Flask
- install jinjja2
- must have Python support
- can run on either on of these two links
    http://127.0.0.1:8123
    http://10.110.197.207:8123


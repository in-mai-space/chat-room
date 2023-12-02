# chat-room

**A high level overview**
This is a chat room that allows users to sign up, log in, log out, post under a username and chat with other users from different devices.
- Languages: Python, Javascript, HTML
- Framework: Flask, Bootstrap
- Other Tools: Socket.IO library, Jinjja2 web template
- why Python and Flask?: Python is a simple coding language, and Flask is a micro-web framework, which is simple to use when the program is small 
- why Socket.IO: encounter problems of refreshing pages to receive the message, thus, through socket.io, there is a real time and bi-directional communication between server and client. This allows users to view new messages in real time from other users without the need for refreshing.

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
- must have Python support
- can run on either on of these two links
    http://127.0.0.1:8123
    http://10.110.197.207:8123


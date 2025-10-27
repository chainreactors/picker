---
title: Extending Burp Suite for fun and profit – The Montoya way – Part 3
url: https://security.humanativaspa.it/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-3/
source: hn security
date: 2023-07-20
fetch_date: 2025-10-04T11:54:54.464116
---

# Extending Burp Suite for fun and profit – The Montoya way – Part 3

[![logo](https://hnsecurity.it/wp-content/uploads/2025/09/HN_Security_v2.svg)](https://hnsecurity.it/)

* [Home](https://hnsecurity.it)
* [Company](https://hnsecurity.it/company/)
* [Services](https://hnsecurity.it/services/)
  + [Red Teaming](https://hnsecurity.it/services/red-teaming/)
  + [DORA TLPT](https://hnsecurity.it/services/threat-led-penetration-test-dora/)
  + [AI Red Teaming](https://hnsecurity.it/services/ai-red-teaming/)
  + [Network Assessment](https://hnsecurity.it/services/network-assessment/)
  + [Web Assessment](https://hnsecurity.it/services/web-application-assessment/)
  + [Mobile Assessment](https://hnsecurity.it/services/mobile-application-assessment/)
  + [Mainframe Assessment](https://hnsecurity.it/services/mainframe-assessment/)
  + [Cloud Assessment](https://hnsecurity.it/services/cloud-assessment/)
  + [OT Assessment](https://hnsecurity.it/services/ot-assessment/)
  + [IoT Assessment](https://hnsecurity.it/services/iot-assessment/)
  + [Hardware Assessment](https://hnsecurity.it/services/hardware-assessment/)
  + [Security by Design](https://hnsecurity.it/services/security-by-design/)
* [Blog](https://hnsecurity.it/blog/)
* [Careers](https://hnsecurity.it/careers/)
* [Contacts](https://hnsecurity.it/contacts/)
* [![Italian](https://hnsecurity.it/wp-content/plugins/sitepress-multilingual-cms/res/flags/it.svg)](https://hnsecurity.it/it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-3/ "Switch to ")

Get in touch

info@hnsecurity.it

![](https://hnsecurity.it/wp-content/uploads/2025/09/BURP-uai-836x836.jpg)

# Extending Burp Suite for fun and profit – The Montoya way – Part 3

July 19, 2023|[![Federico Dotta](https://hnsecurity.it/wp-content/uploads/2025/09/Dotta-sm-150x150.jpg)](https://hnsecurity.it/blog/author/federico-dotta/)By [Federico Dotta](https://hnsecurity.it/blog/author/federico-dotta/)

[Articles](https://hnsecurity.it/blog/category/articles/ "View all posts in Articles"), [Tools](https://hnsecurity.it/blog/category/tools/ "View all posts in Tools")

1. [Setting up the environment + Hello World](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-1/)
2. [Inspecting and tampering HTTP requests and responses](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-2/)
3. **-> Inspecting and tampering WebSocket messages**
4. [Creating new tabs for processing HTTP requests and responses](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-4/)
5. [Adding new functionalities to the context menu (accessible by right-clicking)](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-5/)
6. [Adding new checks to Burp Suite Active and Passive Scanner](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-6/)
7. [Using the Collaborator in Burp Suite plugins](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-7/)
8. [BChecks – A quick way to extend Burp Suite Active and Passive Scanner](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-8/)
9. … and much more!

Hi there!

In the [last article of the series](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-2/) we learned how to develop the most commonly used type of Burp extensions during a penetration test, namely **HttpHandler** plugins (or **HttpListener** in the old APIs). These plugins allow us to inspect or modify all HTTP requests exiting from every tool in [Burp Suite](https://portswigger.net/burp) and all incoming responses. Today we will see how to do a similar thing when our target application uses **WebSockets**.

WebSocket is a **stateful** **full-duplex** protocol supported by modern browsers, usually employed in applications that need real-time updates. Until a few years ago, Burp Suite only partially supported WebSockets (I used [OWASP Zap](https://www.zaproxy.org/) for WebSocket testing instead, as it supported them better). Then Burp Suite improved its support over this technology and now WebSockets are well integrated in the Proxy and Repeater tools.

Speaking of extensions, WebSocket support was introduced only with the **Montoya API**, which is another reason to choose them over the previous APIs, even though they don’t currently support Python and Ruby. Over the years, I’ve come across many applications that used WebSockets and for which I needed an extension (which was often already available publicly for the HTTP counterpart), and the lack of support for this technology was a sore point. Now, as we will see, we can finally inspect and modify WebSocket requests in a similar way to what we did for HTTP requests.

As always, we start from a test scenario that uses WebSocket. For the purpose, I made a few small changes in [one of the examples of the Flask-SocketIO project](https://github.com/miguelgrinberg/Flask-SocketIO/tree/main/example) (an integration of SocketIO for Flask). The *app.py* example of that project runs a simple chat server using SocketIO and it is perfect for our purposes, because it can use WebSocket for communications.

![](https://hnsecurity.it/wp-content/uploads/2023/06/e1-1.png)

The modified test application is available in [my GitHub repository](https://github.com/federicodotta/Burp-Suite-Extender-Montoya-Course), along with the extension code we are going to create. The following changes have been made to the SocketIO example, in order to fit our needs:

* The SocketIO applications (including our test one) can use many different async modes; some of them uses WebSockets while others use HTTP requests. I set a mode (named *eventlet*) that uses WebSocket, adding also the required modules to the Python requirements.
* The test application continuously sends back and forth ping requests and responses. I commented that code in order to limit the number of WebSocket messages and simplify our scenario.
* A hash has been added to the “Echo” functionality of our chat, that prints the messages we send at the bottom of the page. Now the JavaScript code calculates a SHA-256 hash of the message and attaches the hash to the message. The backend checks if the hash if correct. If not, it returns an error message instead of the message sent by the user.

This is the edited code of the backend that checks for the hash of the message:

```
[...]
@socketio.event
def my_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1

    # Edited by fd for test case

    if 'hash' in message:
        calculated_hash = sha256(message['data'].encode('utf-8')).hexdigest()
        if(message['hash'] == calculated_hash):
            emit('my_response',
                 {'data': message['data'], 'count': session['receive_count']})
        else:
            emit('my_response',
                 {'data': 'INVALID SIGNATURE', 'count': session['receive_count']})

    else:

        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
            {'data': message['data'], 'count': session['receive_count']})
[...]
```

The test application can be executed as follows:

1. (optional) Create a Python virtual environment and activate it
   1. `python -m venv venv`
   2. `source venv/bin/activate`
2. Install requirements
   1. `pip install -r requirements.txt`
3. Run the application
   1. `python app.py`
4. The application can be reached at http://localhost:5000/

We can try to send a message using the “Echo” functionality from the web GUI:

![](https://hnsecurity.it/wp-content/uploads/2023/06/e2-2.png)

By inspecting the WebSocket traffic in Burp Suite we can see that our browser sent a message containing the “test” string and its SHA256 hash (the hash is computed only on the value of the *data* field) and received a message with the same string (unlike HTTP protocol, Websockets don’t have requests and correspond...
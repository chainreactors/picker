---
title: Extending Burp Suite for fun and profit – The Montoya way – Part 2
url: https://security.humanativaspa.it/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-2/
source: hn security
date: 2023-07-06
fetch_date: 2025-10-04T11:53:48.131370
---

# Extending Burp Suite for fun and profit – The Montoya way – Part 2

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
* [![Italian](https://hnsecurity.it/wp-content/plugins/sitepress-multilingual-cms/res/flags/it.svg)](https://hnsecurity.it/it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-2/ "Switch to ")

Get in touch

info@hnsecurity.it

![](https://hnsecurity.it/wp-content/uploads/2025/09/BURP-uai-836x836.jpg)

# Extending Burp Suite for fun and profit – The Montoya way – Part 2

July 5, 2023|[![Federico Dotta](https://hnsecurity.it/wp-content/uploads/2025/09/Dotta-sm-150x150.jpg)](https://hnsecurity.it/blog/author/federico-dotta/)By [Federico Dotta](https://hnsecurity.it/blog/author/federico-dotta/)

[Articles](https://hnsecurity.it/blog/category/articles/ "View all posts in Articles"), [Tools](https://hnsecurity.it/blog/category/tools/ "View all posts in Tools")

1. [Setting up the environment + Hello World](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-1/)
2. **-> Inspecting and tampering HTTP requests and responses**
3. [Inspecting and tampering WebSocket messages](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-3/)
4. [Creating new tabs for processing HTTP requests and responses](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-4/)
5. [Adding new functionalities to the context menu (accessible by right-clicking)](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-5/)
6. [Adding new checks to Burp Suite Active and Passive Scanner](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-6/)
7. [Using the Collaborator in Burp Suite plugins](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-7/)
8. [BChecks – A quick way to extend Burp Suite Active and Passive Scanner](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-8/)
9. … and much more!

Hi there!

Today we will cover how to develop the type of extension most commonly used during a penetration test, namely **HttpHandler** plugins (or **HttpListener** in the old APIs). These plugins allow us to inspect or modify all HTTP requests exiting from every tool in Burp Suite and all incoming responses. It is possible to inspect and modify the traffic of specific tools in Burp Suite through other types of plugins as well, but these HttpHandler plugins provide access to all outgoing and incoming traffic.

With the new Montoya API, we can also inspect and modify **WebSocket** traffic, one of the features I have been eagerly awaiting for a long time (or better, **the** feature I have been waiting for the most). Before Montoya API we could write great plugin to handle encryption, signature, encodings, etc. in HTTP requests and responses and we had to keep our fingers crossed that the application didn’t use WebSockets. Otherwise, we could use Burp Suite only in standard scenarios and we had to switch to much more inconvenient tools in more complex ones.

Let’s consider the following example scenario: we have an application that adds a SHA256 hash of the body in an HTTP Header (usually things are a little more complex with for example a HMAC-SHA but let’s keep things simple). If we intercept a request and modify a parameter in the body without regenerating the hash, the request will be rejected by the backend. In the **Proxy** and **Repeater**, we can consider manually regenerating the SHA256 for each request we send, but this could significantly slow down the testing process and be quite annoying…

![](https://hnsecurity.it/wp-content/uploads/2023/06/monkey-laptop-2.gif)

Additionally, if we were to use the **Intruder** or the **Scanner**, every request generated by Burp would be rejected by the backend as it would have an incorrect hash. The best way to handle this type of situation is to create an HttpHandler plugin that transparently regenerates the signatures of all the requests that require it.

Let’s see how we can do that. First, let’s code a simple demo backend with Python and Flask.

```
import flask
from flask import request
from hashlib import sha256

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    hash = request.headers.get('Hash')
    body = request.get_data()
    calculated_hash = sha256(body).hexdigest()
    if(hash.strip() == calculated_hash):
        data = request.form.get('data')
        return data
    else:
        return("Invalid signature!")

app.run(host="127.0.0.1", port=5000, debug=True)
```

The code simply extracts the hash contained in the “Hash” header, calculates the hash of the body and then compares the two values. If they are equal, the backend returns the values sent in the “data” body parameter, otherwise it returns an error. Very simple.

The following request has the **correct SHA256 hash**:

```
POST / HTTP/1.1
Host: localhost
Content-Length: 19
Hash: 0bae7db0e4ee21521569abf0b881349c7d1da125a49435f8ea0a733b1ef4be78
Content-Type: application/x-www-form-urlencoded

data=Attack+vector!
```

```
HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.11.3
Date: Mon, 12 Jun 2023 16:05:29 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 14
Connection: close

Attack vector!
```

The following one has an **invalid hash**:

```
POST / HTTP/1.1
Host: localhost
Content-Length: 21
Hash: 0bae7db0e4ee21521569abf0b881349c7d1da125a49435f8ea0a733b1ef4be78
Content-Type: application/x-www-form-urlencoded

data=Attack+vector+2!
```

```
HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.11.3
Date: Mon, 12 Jun 2023 16:10:17 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 18
Connection: close

Invalid signature!
```

Let’s run our IDE and create the skeleton for an empty plugin (refer to [part 1](https://hnsecurity.it/blog/extending-burp-suite-for-fun-and-profit-the-montoya-way-part-1/) for the tutorial on how to setup the IDE and create the skeleton).

```
package org.fd.montoyatutorial;

import burp.api.montoya.BurpExtension;
import burp.api.montoya.MontoyaApi;
import burp.api.montoya.logging.Logging;

public class HttpHandlerExample implements BurpExtension {

    MontoyaApi api;
    Logging logging;

    @Override
    public void initialize(MontoyaApi api) {

        // Save a reference to the MontoyaApi object
        this.api = api;

        // api.logging() returns an object that we can use to print messages to stdout and stderr
        this.logging = api.logging();

        // Set the name of the extension
        api.extension().setName("Montoya API tutorial - HttpHandlerExample");

        // Print a message to the stdout
        this.logging.logToOutput("*** Montoya API tutorial - HttpHandlerExample loaded ***");

    }
}...
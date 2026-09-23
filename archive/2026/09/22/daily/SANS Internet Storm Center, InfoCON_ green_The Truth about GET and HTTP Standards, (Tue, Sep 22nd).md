---
title: The Truth about GET and HTTP Standards, (Tue, Sep 22nd)
url: https://isc.sans.edu/diary/rss/33358
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-22
fetch_date: 2026-09-23T06:55:14.198973
---

# The Truth about GET and HTTP Standards, (Tue, Sep 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/33352)
* [next](/diary/33360)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [The Truth about GET and HTTP Standards](/forums/diary/The%2BTruth%2Babout%2BGET%2Band%2BHTTP%2BStandards/33358/)

**Published**: 2026-09-22. **Last Updated**: 2026-09-22 19:06:15 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/The%2BTruth%2Babout%2BGET%2Band%2BHTTP%2BStandards/33358/#comments)

On Friday, Xavier talked about the newly introduced [HTTP Query](https://isc.sans.edu/diary/HTTP%20QUERY%20Method%3A%20The%20Grey%20Zone%20Between%20GET%20And%20POST./33352) method. This new method was introduced to allow "GET" requests that include a body. The main reason for this was that GET requests typically do not contain a body. But what if they do?

The HTTP RFCs had "issues" defining this properly. RFC2616, which originally defined HTTP 1.1, stated in section 4.3:

> A message-body MUST NOT be included in a request if the specification of the request method (section [5.1.1](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html#sec5.1.1)) does not allow sending an entity-body in requests.

And the GET specification never discussed message bodies.

This was somewhat reworded in the newer version, RFC 7231, section 4.3.2:

> ??????A payload within a GET request message has no defined semantics; sending a payload body on a GET request might cause some existing implementations to reject the request.

I did a quick check of a couple of common web servers I had handy, to see what would happen:

### Apache

For this test, I ran Apache 2.4.68 on a Mac. It happily accepted a body with a GET request:

> ```
>
> % nc -c localhost 8080
> GET /cgi-bin/test-cgi HTTP/1.1
> Host: localhost
> Content-Length: 6
>
> TEST
> HTTP/1.1 200 OK
> Date: Tue, 22 Sep 2026 14:39:17 GMT
> Server: Apache/2.4.68 (Unix)
> Transfer-Encoding: chunked
> Content-Type: text/plain; charset=iso-8859-1
>
> 18a
> CGI/1.0 test script report:
> [some details omited]
> CONTENT_LENGTH = 6
> BODY = TEST
> ```

The data was collected using a slightly modified version of the standard "test-cgi" script. The body was received just fine, and a 200 status was returned.

### NGINX

> `% nc -c 10.128.1.11 80
> GET /cgi-bin/test-cgi HTTP/1.1
> Host: localhost
> Content-Length: 6`
>
> `TESTHTTP/1.1 301 Moved Permanently
> Server: nginx`

The request still did not trigger an error. But the body was ignored. The server started sending the response as soon as it received the headers. The body was ignored.

### Python

A simple Python web server (python -m http.server 8000) appears to behave just like NGINX. The body is ignored, but a response is sent back, and the status code is 200.

### Node

Node also ignores the Content-Length header and processes the request without error.

### lighthttpd

lighttpd/1.4.74 will return a 400 error and refuse to process the request.

### Java/Tomcat

Tomcat ignores the Content-Length header but returns a 200 response.

Do you have any web servers to test to see how they respond to a GET request with a body?

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/The%2BTruth%2Babout%2BGET%2Band%2BHTTP%2BStandards/33358/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33352)
* [next](/diary/33360)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)
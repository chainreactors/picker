---
title: Week 5— Learning Basic Concepts of Cybersecurity
url: https://infosecwriteups.com/week-5-learning-basic-concepts-of-cybersecurity-ae310b92ab71?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-22
fetch_date: 2025-10-06T23:26:40.246184
---

# Week 5— Learning Basic Concepts of Cybersecurity

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fae310b92ab71&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweek-5-learning-basic-concepts-of-cybersecurity-ae310b92ab71&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweek-5-learning-basic-concepts-of-cybersecurity-ae310b92ab71&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ae310b92ab71---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ae310b92ab71---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Week 5 — *HTTP’s Epic Evolution: From 0.9 to 3.0 and Beyond*

[![Aang](https://miro.medium.com/v2/resize:fill:64:64/1*8OFSxi24TNgHQCLpC-bCGQ.jpeg)](https://iamaangx028.medium.com/?source=post_page---byline--ae310b92ab71---------------------------------------)

[Aang](https://iamaangx028.medium.com/?source=post_page---byline--ae310b92ab71---------------------------------------)

11 min read

·

Jul 20, 2025

--

Listen

Share

## Intro

Hi there! If you’re wondering who I am, I go by **@iamaangx028** on the internet — you can call me Aang :)

I am a student who is trying to get into the cybersecurity field. As a part of that journey, I would like to share my progress with all of you through weekly blogs.

***Just a small note for continuity…***

*So, up to now we have learnt basic Network concepts and Browser concepts. Now that I think, we are good to start with the Web concepts. We will go slowly, one concept at a time. So, if you haven’t read my previous* [*blogs*](https://iamaangx028.medium.com/)*, I highly recommend that you cover those. However, it's still okay if you have the required basics. Let us go!!*

Press enter or click to view image in full size

![]()

Let us start the week — 5

### Welcome to the World Wide Web

Let us try to learn the basic concepts of the World Wide Web. The phase will take more time than the network part, the web browsers part. But we will be trying to cover as many concepts as possible. So, let us start by knowing how HTTP evolved.

## HTTP Evolution — HTTP/0.9/1.0/1.1/2.0/3.0

The way people use the web has changed rapidly, so has the Engineering behind it! We learned that Sir Tim-Bernerlee has laid the foundation for the Hypertext Transfer Protocol and the Hypertext Markup Language.

### HTTP/0.9

In **1991, HTTP/0.9** was the first version of HTTP. And it only had the GET method along with the Path for the requested resource. Except that there was nothing to look at. No Headers, no status codes, No Content-Type, nothing!! There was no formal Request For Comments (RFC). It looked as follows:

```
REQUEST:GET /mypage.html RESPONSE:<html> .... </html>
```

Usually, if a user wants to access a resource, then a successful TCP 3-way Handshake would happen and then followed by a GET request, and if the server is in the mood to send the response, it will send. Then TCP Teardown would happen. A TCP Teardown is just a way the client and server end the TCP session. So, TCP was established and closed every time for each new request. Which is not efficient.

### HTTP/1.0

**In 1996, HTTP/1.0** was released, which laid the foundation for the change of the web. HTTP/1.0 supported new HTTP methods like **POST, HEAD,** and **Status codes, Headers like Content-Type, and Content Negotiation** between the browser and the server. HTTP/1.0 has significant changes when compared to HTTP/0.9. Then, engineers figured out ways to send other Media types like Image, Video, along with Text. With the use of Content-Type headers in the request and response, both server and client become capable of understanding the MIME type of the file they are dealing with. And interoperability problems were common at that time. And even RFC (Request For Comments) and other documentation were developed and maintained to help other developers understand the Web. Still, it was following a strict Request-Response model, which means, a second request it sent only when the response for the first request arrived. And, even in HTTP/1.0, the TCP session by default tears down immediately after the data transfer of the requested resource. But some say the Connection: Keep-alive header was supported in HTTP/1.0, but not used by default. HTTP/1.0 can support Secure HTTP with the SSL/TLS handshake. So, typically in HTTP/1.0, each request has to go through a TCP 3-way handshake and a TLS handshake. Which is not feasible given how much costlier and valuable the bandwidth was at that time. And I think one of the reasons for not keeping the connection alive indefinitely is not sufficient memory in the computers at that time.

A major change to HTTP occurred at the end of the year **1994**. The Netscape company developed an encrypted transmission layer over the basic TCP/IP stack to prevent the MITM attacks. Netscape introduced SSL 1.0 but never released its documentation to the public. Then, later versions of SSL, like SSL 2.0, were published. SSL was first adopted by e-commerce websites. But later, due to the fact that more powerful websites were being developed and sensitive information like PII was needed by websites to provide more and more services, SSL/TLS became a mandatory requirement for all websites.

### HTTP/1.1

**HTTP/1.1** was released in **1997,** only a few months after HTTP/1.0. This version of HTTP was the most widely used. Most of the legacy applications and servers support HTTP/1.1. HTTP/1.1 solves some of the major problems in HTTP/1.0. It solves the immediate TCP teardown after the data transfer is done for the requested resource. In HTTP/1.1, we do not need to perform the 3-way handshake & TLS handshake again and again for every resource requested. The `Connection: Keep-Alive` is made default in HTTP/1.1. Due to which we can request multiple resources over a single TCP & TLS session. The `session or Connection` will be alive until a `close` request is sent or until the time allocated for the session expires (Whichever is first). HTTP/1.1 also supports Pipelining, which we cannot see in the initial versions of HTTP. This pipelining enables clients (like browsers) to send multiple requests even before receiving the response for the first request. This way, the client need not wait for the first request’s response. So, these major improvements enable the browsers to load pages faster than before. But, like Peter’s uncle said, with great power comes great responsibility. The pipelining implementations have some limitations; the responses you get should be in ...
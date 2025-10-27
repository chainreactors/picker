---
title: Collaborator Everywhere v2
url: https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-10
fetch_date: 2025-10-02T19:55:35.481507
---

# Collaborator Everywhere v2

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Collaborator Everywhere v2](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/ "Collaborator Everywhere v2")

[September 9, 2025](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/ "Collaborator Everywhere v2")
 /
[Andreas Brombach](https://blog.compass-security.com/author/abrombach/ "Posts by Andreas Brombach")
 /
[0 Comments](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/#respond)

# Overview

Collaborator Everywhere is a well-known extension for Burp Suite Professional to probe and detect out-of-band pingbacks in [web applications](https://www.compass-security.com/en/services/penetration-tests#c89).

We developed an upgrade to the existing extension with several new exciting features. Payloads can now be edited, interactions are displayed in a separate tab and stored with the project file. This makes it easier to detect and analyze any out-of-band communication that typically occurs with SSRF or Host header vulnerabilities.

You can find the extension in the [BApp Store](https://portswigger.net/bappstore/2495f6fb364d48c3b6c984e226c02968) or on our [GitHub repository](https://github.com/CompassSecurity/CollaboRaider).[1](#0730dbfd-a245-4674-9024-1716b0bc6877)

# Background

The Collaborator service in Burp Suite Professional is a handy tool for identifying various misconfigurations and vulnerabilities that do not elicit a direct response but instead trigger a request to another system. This is also referred to as *out-of-band* communication. Using a dedicated external server that listens to incoming connections on multiple protocols, such requests can be collected in a Burp instance for further inspection.

[![](https://blog.compass-security.com/wp-content/uploads/2025/07/2025-07-24-11_11_47-development_kali-VMware-Workstation-1.png)](https://blog.compass-security.com/wp-content/uploads/2025/07/2025-07-24-11_11_47-development_kali-VMware-Workstation-1.png)

Source: <https://portswigger.net/burp/documentation/collaborator>

Burp Collaborator generates special URLs and regularly polls the Collaborator server for any incoming requests to those URLs. If the Collaborator server receives a request while Burp Suite is not running, the request is stored until the next poll. This asynchronous pattern is particularly useful for dealing with payloads with delayed execution, such as blind XSS or blind SQL injection.

## Original extension

The extension Collaborator Everywhere was initially developed by James Kettle as part of a research project to identify backend vulnerabilities. Acting as a passive scanner, it automatically inserts new Collaborator URLs into various HTTP headers for every in-scope request. As unique payloads are created for each header and URL parameter, any received interaction can be immediately correlated with the originating request and header.

To illustrate what it does, here is a quick example. Given the following request:

```
GET / HTTP/1.1
Host: 0a190072032d8a6d80141783008800f9.web-security-academy.net
[CUT BY COMPASS]
```

It is then modified with several additional headers:

```
GET / HTTP/1.1
Host: 0a190072032d8a6d80141783008800f9.web-security-academy.net
[CUT BY COMPASS]
Contact: [email protected]
From: [email protected]
Referer: https://6u1tcw8rgyl8z7nwwqth1xzxbohj58.oastify.com
X-Original-URL: https://twtgejaeilnv1upjydv43k1kdbj77w.oastify.com/
X-Wap-Profile: https://uljh3kzf7mcwqveknek5slql2c89wy.oastify.com/wap.xml
Profile: https://f9p2r5n0v70heg25bz8qg6e6qxwvkk.oastify.com/wap.xml
X-Arbitrary: https://rmhe4h0c8jdtrsfhobl2tiri3998xx.oastify.com/
X-HTTP-DestinationURL: https://659tnwjrryw8a7yw7q4hcxaxmosogd.oastify.com/
X-Forwarded-Proto: https://7ksu2xys6zb9p8dxmrjirypy1p7qvf.oastify.com/
X-Forwarded-Host: 7iqu0xws4z99n8bxkrhipynyzp5rtg.oastify.com
X-Forwarded-For: spoofed.u1whjkffnmsw6vuk3e058l6licofc4.oastify.com
True-Client-IP: spoofed.dev0w3sy055fje73gxdol4j4vv1zpo.oastify.com
Client-IP: spoofed.lj881bx65danomcbl5iwqcoc0368ux.oastify.com
X-Client-IP: spoofed.m2p9kcg7oeto7nvc461x9d7dj4pvfj4.oastify.com
X-Real-IP: spoofed.1lno3rzm7tc3q2ernlkcssqs2j8azyo.oastify.com
X-Originating-IP: spoofed.7v3udx9shzm908oxxrui2y0ycpiga4z.oastify.com
CF-Connecting_IP: spoofed.4w1reuapiwn615puyovf3v1vdmjdc11.oastify.com
Forwarded: for=spoofed.w2zjkmghooty7xvm4g179n7njep5jt8.oastify.com;by=spoofed.w2zjkmghooty7xvm4g179n7njep5jt8.oastify.com;host=spoofed.w2zjkmghooty7xvm4g179n7njep5jt8.oastify.com
```

### Limitations

#### No payload customization

Without a convenient way to configure the payloads, the extension does not always work as intended. For instance, a WAF might block certain headers that look like a Host header injection attack. Alternatively, the application might display error messages due to unexpected header values.

There are two possible ways to remediate this. One option is to completely disable the extension, which will not bring any benefit. Alternatively, one could clone the extension’s source code from GitHub, edit the payload and rebuild it. However, if it is not immediately clear which payload is causing trouble, determining this through the process of elimination can be quite tedious.

Additionally, there are many more possibilities than simply modifying different Host headers. Consider an application that collects the *User-Agent* or *Referer* headers in order to track their visitors. If these headers are then processed and displayed for instance on an internal dashboard, this could be an opportunity to test for blind XSS vulnerabilities.

Finally, remember the infamous Shellshock or Log4j vulnerabilities? These could be exploited by adding malicious payloads to different headers, which are then stored and evaluated by the application. For the latter, there even exists a [fork of the original extension](https://github.com/portswigger/log4shell-everywhere) designed specifically for injecting Log4j payloads into all requests. Having configurable payloads that could be modified or turned on and off individually would already be a huge improvement.

#### Poor Issue Visibility

With multiple extensions enabled, the “Issues” tab in Burp Suite fills up quickly, making it increasingly difficult to sift through the growing list of discovered problems. There might be a notification that a Collaborator pingback has been triggered by a specific header, but this information can easily drown in a flood of other issues. Having a dedicated overview of all received interactions would help not only to spot a vulnerability faster, but also to analyze it more thoroughly: are the requests always coming from the same servers? Are there different headers that cause these interactions? Is just one endpoint affected or several?

# New Features

## Issue Details

As in the original extension, issues are raised for received interactions. The issue details now contain additional info, such as the hostname and the correct local timestamp, including the time difference to the corresponding request.

[![](https://blog.compass-security.com/wp-content/uploads/2025/07/2025-07-25-14_48_35-development_kali-VMware-Workstation.png)](https://blog.compass-security.com/wp-content/uploads/2025/07/2025-07-25-14_48_35-development_kali-VMware-Workstation.png)

Scanner Issues created by the extension.

In the Proxy view, requests for which a Collaborator pingback has been received are now highlighted and marked ...
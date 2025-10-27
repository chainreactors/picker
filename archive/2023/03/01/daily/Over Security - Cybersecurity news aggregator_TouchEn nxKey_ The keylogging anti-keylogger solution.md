---
title: TouchEn nxKey: The keylogging anti-keylogger solution
url: https://palant.info/2023/01/09/touchen-nxkey-the-keylogging-anti-keylogger-solution/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:21:57.315936
---

# TouchEn nxKey: The keylogging anti-keylogger solution

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# TouchEn nxKey: The keylogging anti-keylogger solution

2023-01-09
 [Korea](/categories/korea/)/[Security](/categories/security/)/[Add-Ons](/categories/add-ons/)
 26 mins
 [26 comments](/2023/01/09/touchen-nxkey-the-keylogging-anti-keylogger-solution/#comments)

**Update** (2023-01-16): This article is now available [in Korean](https://github.com/alanleedev/KoreaSecurityApps/blob/main/01_touchen_nxkey.md).

I wrote about [South Koreaâs mandatory so-called security applications](/2023/01/02/south-koreas-online-security-dead-end/) a week ago. My journey here started with TouchEn nxKey by RaonSecure which got my attention because the corresponding browser extension has more than 10 million users â the highest number Chrome Web Store will display. The real number of users is likely considerably higher, the software being installed on pretty much any computer in South Korea.

Thatâs not because people like it so much: they outright hate it, resulting in an average rating of 1,3 out of 5 stars and lots of calls to abolish it. Yet using it is required if you want to do things like online banking in South Korea.

The banks pushing for the software to be installed claim that it improves security. People [call it âmalwareâ and a âkeylogger.â](https://www.reddit.com/r/korea/comments/9qwucv/comment/e8ch6yn/) I spent some time analyzing the inner workings of the product and determined the latter to be far closer to the truth. The application indeed contains key logging functionality by design, and it fails to sufficiently restrict access to it. In addition, various bugs range from simple denial of service to facilitating remote code execution. Altogether I reported seven security vulnerabilities in the product.

#### Contents

* [The backdrop](#the-backdrop)
* [What does TouchEn nxKey actually do?](#what-does-touchen-nxkey-actually-do)
* [How do websites communicate with TouchEn nxKey?](#how-do-websites-communicate-with-touchen-nxkey)
* [Abusing TouchEn extension to attack banking websites](#abusing-touchen-extension-to-attack-banking-websites)
  + [Side-note: Browser extensions similar to TouchEn](#side-note-browser-extensions-similar-to-touchen)
* [Using keylogging functionality from a website](#using-keylogging-functionality-from-a-website)
* [Attacking the application itself](#attacking-the-application-itself)
* [Abusing the helper application](#abusing-the-helper-application)
* [Accessing the driverâs keylogging functionality directly](#accessing-the-driver-s-keylogging-functionality-directly)
  + [Side-note: Driver crashes](#side-note-driver-crashes)
* [Will it be fixed?](#will-it-be-fixed)
  + [Side-note: The information leak](#side-note-the-information-leak)
* [Can the nxKey concept even work?](#can-the-nxkey-concept-even-work)

## The backdrop

After I gave an [overview of South Koreaâs situation](/2023/01/02/south-koreas-online-security-dead-end/), people started discussing my article on various Korean websites. [One comment in particular](https://www.clien.net/service/board/news/17827726?c=true#140131396) provided crucial information that I was missing: two news stories from 2005 on the Korea Exchange Bank hacking incident [[1]](https://news.kbs.co.kr/news/view.do?ncd=735696) [[2]](https://news.kbs.co.kr/news/view.do?ncd=735697). These are light on technical details but let me try to explain how I understand this.

This was apparently a big deal in Korea in 2005. A cybercrime gang managed to steal 50 million Won (around $50,000 at the time) from peopleâs banking accounts by means of a [Remote Access Trojan](https://www.malwarebytes.com/blog/threats/remote-access-trojan-rat). This way they not only got the userâs login credentials but also information from their security card. From what I can tell, this security card was similar to indexed TANs, a second factor authentication method banished in the European Union in 2012 for the exact reason of being easily compromised by banking trojans.

How did the usersâ computers get infected with this malicious application? From the description this sounds like a [drive-by download](https://en.wikipedia.org/wiki/Drive-by_download) when visiting a malicious website with the browser, a browser vulnerability was likely exploited. Itâs also possible however that the user was tricked into installing the application. The browser in question isnât named, but it is certain to be Internet Explorer as South Korea didnât use anything else at this point.

Now the news stress the point that the user didnât lose or give away their online banking credentials, theyâve done nothing wrong. The integrity of online banking in general is being questioned, and the bank is criticized for not implementing sufficient security precautions.

In 2005 there have been plenty of stories like this one in other countries as well. While I cannot claim that the issue has been completely eliminated, today it is far less common. On the one hand, web browsers got way more secure. On the other hand, banks have improved their second factor. At least in Europe you usually need a second device to confirm a transaction. And you see the transaction details when confirming, so you wonât accidentally confirm a transfer to a malicious actor.

South Korea chose a different route, the public outrage demanded quick results. The second news story identifies the culprit: a security application could have stopped the attack, but its use wasnât mandatory. And the bank complies. It promises to deliver an âanti-hackingâ application and to make its use mandatory for all users.

So itâs likely not a coincidence that I can find the first mentions of TouchEn Key around 2006/2007. The application claims to protect your sensitive data when you enter data into a web page. Eventually, TouchEn nxKey was developed to support non-Microsoft browsers, and thatâs the one I looked into.

## What does TouchEn nxKey actually do?

All the public sources on TouchEn nxKey tell that it is somehow meant to combat keyloggers by encrypting keyboard input. Thatâs all the technical information I could find. So I had to figure it out on my own.

Websites relying TouchEn nxKey run the nxKey SDK which consists of two parts: a bunch of JavaScript code running on the website and some server-side code. Here is how it works:

1. You enter a password field on a website that uses the nxKey SDK.
2. JavaScript code of the nxKey SDK detects it and notifies your local nxKey application.
3. nxKey application activates its device driver in the Windows kernel.
4. Device driver now intercepts all keyboard input. Instead of having it processed by the system, keyboard input is sent to the nxKey application.
5. The nxKey application encrypts the keyboard input and sends it to the JavaScript code of the nxKey SDK.
6. The JavaScript code puts the encrypted data into a hidden form field. The actual password field receives only dummy text.
7. You finish entering your login credentials and click âLogin.â
8. The encrypted keyboard input is sent to the server along with other data.
9. The server-side part of the nxKey SDK decrypts it and retrieves the plain text password from it. Regular login procedure takes over.

So the theory is: a keylogger attempting to record data entered into this website will only see encrypted data. It can see the public key used by the website, but it wonât have the corresponding private key. So no way to decrypt, the password is safe.

Yes, itâs a really nice theory.

## How do websites communicate with TouchEn nxKey?

How does a website even know that a particular application is installed on the computer? And how does it communicate with it?

It appears that there is an ongoing paradigm shift here. Originally, TouchEn nxKey required its browser extension to be installed. That browser extension forwarded ...
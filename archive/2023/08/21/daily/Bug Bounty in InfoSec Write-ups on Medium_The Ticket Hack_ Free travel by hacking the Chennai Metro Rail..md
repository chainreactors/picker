---
title: The Ticket Hack: Free travel by hacking the Chennai Metro Rail.
url: https://infosecwriteups.com/the-ticket-hack-free-travel-by-hacking-the-chennai-metro-rail-6ddaf5457ecf?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-08-21
fetch_date: 2025-10-04T11:59:05.967648
---

# The Ticket Hack: Free travel by hacking the Chennai Metro Rail.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6ddaf5457ecf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-ticket-hack-free-travel-by-hacking-the-chennai-metro-rail-6ddaf5457ecf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-ticket-hack-free-travel-by-hacking-the-chennai-metro-rail-6ddaf5457ecf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6ddaf5457ecf---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6ddaf5457ecf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# The Ticket Hack: Free travel by hacking the Chennai Metro Rail.

[![Manav Bankatwala](https://miro.medium.com/v2/resize:fill:64:64/1*lKKgns5f3pH7FpGgLfe27A@2x.jpeg)](https://medium.com/%40manavbankatwala29?source=post_page---byline--6ddaf5457ecf---------------------------------------)

[Manav Bankatwala](https://medium.com/%40manavbankatwala29?source=post_page---byline--6ddaf5457ecf---------------------------------------)

7 min read

·

Aug 20, 2023

--

11

Listen

Share

Hello Amazing readers, This writeup is all about how, during my internship in Chennai, I stumbled upon a critical vulnerability in the Chennai Metro Rail ticket booking system. By taking a closer look at the system’s inner workings, I was able to exploit a flaw and book tickets at a significant discount/almost for free. This article highlights the importance of ethical hacking and responsible disclosure, ultimately resulting in the rectification of the vulnerability.

### **I know I was going to post about an IDOR as referred in my previous writeup, but this looked more interesting to share.**

You can read my previous writeup here :

[## Forging a Path to Account Takeover: Copy Password Reset Link Vulnerability worth $$$$.

### Don’t stop on errors

infosecwriteups.com](/forging-a-path-to-account-takeover-copy-password-reset-link-vulnerability-worth-4ad1f9ae03be?source=post_page-----6ddaf5457ecf---------------------------------------)

## Initial Phase:

This all started when I have to move to Chennai to complete my Internship where I have to travel from my stay to the office through Metro. This was the first time I was travelling by any metro and I was little bit excited how they manage the ticket booking and verification of all these travelers. So what I observed during my travel was that the Chennai Metro Rail uses QR code based ticket to scan so that it opens the gate to platforms. I manually had the ticket from the ticket counters there and saw the QR code on the ticket and other details. All the security researchers here will understand the urge to look into this and think that what will the QR code data will have? What if I can view or manipulate the data? Yes all these questions crossed my mind too. So I though to have a look at the ticket by scanning the QR code using a QR code scanner app.

## Discovery Phase:

To get a better idea, I collected 3–4 tickets and scanned the QR Code of all the tickets. While analyzing the data from these tickets I have observed that there was some encrypted token, Ticket number and Date-time of the booked ticket. All the details like origin station and destination station was I guess present in this encrypted token value. As this tickets were generated from the ticket counters. I was clueless how this tokens were generated and what was the actual mechanism behind it. I kept this aside for some days and suddenly I got to know from my friend that we can book the tickets from their online portal too. I was like, now let this begin again. I immediately visited the website to book tickets online and see how the ticket was getting generated. This is how it looked like :

![]()

So this website was very very simple and user friendly. We just have to enter the **origin station and destination station.** The fare will be calculated automatically and upon paying through online methods, we get the QR code ticket. We can even see our booked ticket history.

## Analyzing Phase :

So I turned my Burp Suite proxy on and was observing the traffic to which I found that all the traffic to the server and from the server is encrypted. We cannot see what actually the data is going to the server and coming from the server. You can see the request here :

Press enter or click to view image in full size

![]()

Like this every request was encrypted and we cannot see what’s actually going on. I thought that there’s no point to see anything here as it will not make any sense. So just looking at other requests there I found a request which was an API endpoint used to get the fare details from the server in encrypted format. So when we select origin station and destination station it will send a request to the server to get the fare details of that route. As it was also encrypted, we cannot edit or do anything with the fare details too.

## The Flow:

I just observed that what was the actual flow even the requests are encrypted. So the flow was like :

1. We have to enter the source and destination.
2. Encrypted request sent to server to get the fare details.
3. Encrypted response received from server about the fare.
4. Heading to payment page and book the ticket.

This was the flow of whole ticket booking process happening in backend. The fare request looked like this :

Press enter or click to view image in full size

![]()

## The Hack:

The very first thing I thought to try is to get a fare amount response for a journey of less distance. Keeping a note of it. Then while requesting the fare for a journey with more distance replace the response with previous one. So instead of showing any errors, it redirected me to the payment page where I was able to pay successful and the ticket was generated. I was like Is this really happening? I just bought a ticket with 80–90% discounted rate? I can now travel through metro for almost free? I booked another ticket with the same method and again it was successful.

Let me tell you the complete flow with details now :

**Example : Thousand Lights to Ag-DMS : Ticket Fare : Rs.8**

**Example : Thousand Lights to Ashok Nagar : Ticket Fare : Rs.32**

1. I kept a note of the encrypted fare response for the first one i.e. less distance and lower fare amount.
2. I replaced the new response i.e. more distance and higher fare amount with the previous encrypted response.
3. Made the payment and got a ticket from Thousand Lights to Ashok Nagar for Rs.8 instead of Rs.32

Press enter or click to view image in full s...
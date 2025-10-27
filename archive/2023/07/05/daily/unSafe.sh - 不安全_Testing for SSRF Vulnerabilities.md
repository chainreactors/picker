---
title: Testing for SSRF Vulnerabilities
url: https://buaq.net/go-171187.html
source: unSafe.sh - 不安全
date: 2023-07-05
fetch_date: 2025-10-04T11:52:27.415405
---

# Testing for SSRF Vulnerabilities

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Testing for SSRF Vulnerabilities

Server Side Request forgeryHey Guys welcome to my blog so today we going to discuss about SSRF vulne
*2023-7-4 18:12:2
Author: [infosecwriteups.com(查看原文)](/jump-171187.htm)
阅读量:28
收藏*

---

## Server Side Request forgery

[![Vignesh](https://miro.medium.com/v2/resize:fill:88:88/1*_mX7FdsItcAllcM0GMI_tg.jpeg)](https://evilox.medium.com/?source=post_page-----309ec90b976f--------------------------------)[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:48:48/1*A6LVtmXcJ3QJy_sdCyFx1Q.png)](https://infosecwriteups.com/?source=post_page-----309ec90b976f--------------------------------)

Hey Guys welcome to my blog so today we going to discuss about SSRF vulnerability which is critical/high severity in bug bounty and I going to explain some testing methodologies to find the SSRF quickly and finally end up with a basic SSRF portswigger lab

> Instead of being a noob stumbling over useless bugs, become a true hacker who navigates the complexities of the digital world with finesse and purpose
>
> — unkown or me 😂

## What is SSRF?

SSRF is nothing but Server-Side request forgery which allows the attacker to make the forged request to the vulnerable server to make the unintended request to the internal server and gain access to the internal server

Using this SSRF vulnerability the attacker is able to make the connection to the internal server via the public server ( trusted server )

Because usually, the internal server of the website won’t accept the direct request from the attacker or any user but it will accept when we make the request from the public-facing server (this server is accessed by everyone) from the internal server

## How do you say there is internal server?

Let’s take any website like Instagram, Facebook, or youtube here is a sign/login feature in which you enter the username and password right Now How this website validates your username and password is correct because there is an internal database that only been accessed by that website

So here attacker making the request using that public website to access that remote internal database if it is accessible this is called SSRF

The above scenario is not a confirmation of the internal server it is just an example

## Types of SSRF

There are two types of the SSRF

1. Regular SSRF
2. Blind SSRF

## Regular SSRF

In a regular SSRF vulnerability, an attacker can send requests to internal resources from the targeted server and receive the responses directly. This means that the attacker can see the content of the response, which helps them determine if the SSRF vulnerability exists and potentially extract sensitive information.

## Blind SSRF

In a blind SSRF vulnerability, the attacker is also able to send requests to internal resources, but they do not receive the responses directly. This could be due to various reasons, such as the server not returning the response to the attacker or the response being blocked by security measures. Despite not receiving the responses directly, blind SSRF can still be considered a vulnerability because it allows the attacker to interact with internal resources and potentially exploit other vulnerabilities or perform malicious actions indirectly.

## **Testing for SSRF**

The best way to find the SSRF is by looking at the Source code of that website but still fine if don’t get access to that

## Spot feature prone to SSRF

Like visiting and fetching the external resource like webhook, file upload, thumbnails, proxy services, and image processing

1. Less observable places are embedded in the file like pdf or XML this often able to trigger the SSRF

**Note: Most of the testers missing this place**

2. Input that gets inserted into the HTML tag

3. Find the functionality that one action from the application need to trigger another action

4. Check the hidden API in the body of the message (Post request)

## Potential SSRF Place

1. PDF or XML or Documents ( This very most hidden feature )
2. Webhook, file upload, and proxy services

## Next, confirm that vulnerability with internal IPs

First If you have the burpsuite pro or ngrok check with if any interaction reviving in the poll or log

Common IP: localhost 127.0.0.1 and 10.0.0.1

IP list: <https://en.wikipedia.org/wiki/Reserved_IP_addresses>

## Check the response

4. If you get a response like leaking sensitive information or banner information it is regular SSRF

5. If you won’t get response means go to blind SSRF

## Out-of-Band Techniques

To detect Blind SSRF there are some out-band techniques detect we need to get the interaction of that server

First setup the server to get the interaction or log

In that interaction sometimes it leaks the banner information in your log

1. Burpsuite Pro Collaborator
2. Hosting the website on online services like Godaddy
3. Netcat
4. Ngrok
5. **If don’t have the burp collaborator don’t worry use this interactsh** [**https://github.com/projectdiscovery/interactsh**](https://github.com/projectdiscovery/interactsh)

This one amazing tool when compare with collaborator

My personal opinion is to Check with this all four methods because in prevention they block the burp and netcat sometimes

## Basic portswigger SSRF Lab

Let’s Next move for basic portswigger SSRF lab to demonstrate this vulnerability

This lab has a stock check feature that fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`.

First, go to the stock check functionality using this we can count the stock of that product ( While testing you need to understand the functionality )

Next, click that check stock and capture that request in burp

Next, send it to the repeater and open the brup collaborator if you have or

Use this tool: <https://github.com/projectdiscovery/interactsh>

Click the copy to the clipboard to get the link

Change that StockApi link to the server link ( collaborator link ) and send that request

Now click the poll now you will get the interactions so this safe way to detect the SSRF but this does not confirm the message we need proof by accessing the internal resource

**Note: Most people submit the report if they get interaction from that application this is not valid you need proof that vulnerability is exist by accessing the internal resources**

> Instead of being a noob stumbling over useless bugs, become a true hacker who navigates the complexities of the digital world with finesse and purpose

Next, replace the link with accessing the internal page

> <http://localhost/admin>

If you get this response it is valid regular SSRF and to solve this lab delete the Carlos user

> <http://localhost/admin>/delete?username=carlos

Booooommm!!!! Now the Lab get Solved

## Prevention

1. Allowlist
2. Blacklist

**Allowlist**

Implementing an allowlist approach for SSRF prevention involves explicitly specifying the trusted and allowed target resources or endpoints that the server can communicate with. This means that only requests to the pre-approved resources are allowed, and any requests to other resources will be blocked or denied.

For example, you can define a set of safe and trusted URLs or IP addresses that the server is permitted to access. Any request originating from the server to these approved URLs or IP addresses will be allowed, while requests to unlisted or unapproved resources will be rejected.

**Blacklist**

In addition to an allowlist, a blacklist approach can be used to block known vulnerable or malicious URLs, IP addresses, or domains that are commonly associ...
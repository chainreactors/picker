---
title: How to Hack Applications’ Logic
url: https://buaq.net/go-138830.html
source: unSafe.sh - 不安全
date: 2022-12-07
fetch_date: 2025-10-04T00:38:38.671855
---

# How to Hack Applications’ Logic

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

How to Hack Applications’ Logic

Hi everyone, I decided to write a guide about finding logical bugs on applications like the web, mob
*2022-12-6 19:45:29
Author: [infosecwriteups.com(查看原文)](/jump-138830.htm)
阅读量:16
收藏*

---

Hi everyone, I decided to write a guide about finding logical bugs on applications like the web, mobile, and desktop. Actually, this write-up will not only be about breaking logic, if you understand well, it will guide you to think like a hacker, and with that, you may also find a lot of different kind of vulnerabilities.

**Who Am I?**

First of all, who am I? I will not talk about my past, however, right now, I’m working for a company that is about financial things and I’m doing internal, and external penetration tests, mostly for applications. I can say that in 3 months I have found almost 30 critical logical vulnerabilities in different companies. So, I will try to show you how I found all of them. How I found that vulnerabilities cost millions for companies.

**Why Logical Vulnerabilities are Important?**

In my opinion, finding vulnerabilities is about style, and I think a pentester who is looking only at his company should leave from there in 2–3 years. Why? Because almost every hacker has their own style to check vulnerabilities. And after 2 years, that eyes found all vulnerabilities of his style and you should look further with another. The second reason is we are in 2022 and I think working for 10 years in the same company is outmoded. The most important reason is, always different applications, systems, and persons will teach you different things and you have to exit from your comfort zone. Of course, you can work with yourself to improve yourself but always real zones will push you to learn further.

There is a style that is looking for applications' logic and how to break them.

The reason why logical vulnerabilities are valuable and you should look for them is that there is no automated tool to check logical bugs because machine learning didn’t learn to learn yet. So that’s why you have to learn what application does and why you shouldn’t be an automized robot. ;)

**From Which Window am I looking?**

So as I talked about, I hate to do hacking randomly. What I mean, I hate trying XSS, SQL payloads, or something like that without any understanding of the application. I know you heard that enumeration is the key. But it is not only for certification exams or boxes. In the real life, if you want to know what you are hacking, you should learn what the application does.

I’m not using any roadmap to enumerate applications or network systems. However, I can suggest the below link for peoples which are new in this area. Before you have your own style, you need to follow people's way to learn.

*In the future, I will publish my notes on gitbook, So do not forget to check here if I edited.*

**How do Developers Think When Building Applications?**

There is a funny store that I experienced and I want to tell you that. With that, I think you will understand the main difference between hackers and developers.

Last year, I have found a critical IDOR in an online shopping application and I contacted one of the developers who build it in order to fix that together. The funny thing at the meeting was that.

> ~Developer thinking via pseudo-code~
>
> if the customer id is 1234,
>
> GET 1234's information,
>
> if the customer id is 5678,
>
> GET 5678’s information.

It is not looking like a buggy, right? At least not for the developer. Because he thinks there is a problem when we get via 1234 id and the application sends 5678 information.

But the developer didn’t think about one thing. We are getting 5678’s information using 1234’s session. And the problem starts there...

**Where do Logical Bugs Start and How to Find Them?**

As far as I talked, all about why you should learn application logic. Now we will come to breaking them. If you understand the logic of the application, you should think about how can we break its logic to use it for what we want.

Let’s say there is a login panel and the panel has some forgot password link.

You should create accounts to test it. Don’t forget, first we should understand them, and then we should break them!

We looked the login was clear however when we check the forgot password part we have seen that when we click the forgot password, it says please enter your dog’s name or whatever the unique thing they want.

You should examine the response and request in order to understand how they control the variables and if we can manipulate them.

If you understand it is JSON or it is SQLite, and you shouldn’t find anything, you should research hacking and bypass techniques on google and on payload all the things.(<https://github.com/swisskyrepo/PayloadsAllTheThings>)

However, most research should be about the understanding application. Hacking is %90 understanding it and %10 exploiting it. Google is our best friend, never forget to research with it.

Let’s turn back to our example, we examine the request and response and there is a control parameter that checks the dog’s name. We should understand what response is ok and what is not. If the application sends something not unique or the hacker can find it, there is a logical account takeover vulnerability. Because even if developers check request inputs, developers usually forget hackers can manipulate the response. If the hacker can find the thing for the key in response, he can manipulate the response. Don’t be shocked about developers, these ears hear that too much. :D Their thinking style really different than ours. Maybe from everybody :D

**Second Example:**

This is not really a logical bug, however, I put this in order to show you how you should think while hacking.

I was pentesting one of the websites and I have seen there is an upload file funciton. First of all, I tried to upload a shell just like everyone. But then I saw there is an error about parsing. And errors are our second best friend after google. They are the enemy of developers and the enemy’s enemy is our friend. :) They give us info about applications and this is the gold for hacking. So before that, I did my enumeration and I know it is a ASP.net app and we are uploading xslx file, then it parses it to show us in the other part of the application.

When I look there the parse error says that we couldn’t find the required part to parse. I started to research via google, how asp.net parses xslx files.

Then I saw that, when we unzip the xlsx file, there is a file in XML format and it includes the titles of xslx. (xslx part of excel app) And the asp.net code, looking in it.

Then secondly, I think how can I harm with that, what can I put in it?

As it was an XML file, I thought I can try XXE injection, however if you are new, you should look for google, how can I attack via XML. When you learn it, you will think like me in the next pentest you find it. And after then I create my payload in it and rebuild the xlsx, I was able to run my codes in application.

Here is an example of the attack:

<https://www.4armed.com/blog/exploiting-xxe-with-excel/>

[**LET'S CREATE A ROADMAP!**](https://github.com/swisskyrepo/PayloadsAllTheThings)

1- Understand the application goal, and what it wants to do for humans.

2- Enumerate all the parts of the application, and learn how much bigger.

3- Understand the application feature, what kind of features it has and what kind of vulnerabilities can arise. You will be better at this in time.

4- What way do developers think while building that function we are examining and how can we use it for...
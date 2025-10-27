---
title: Zero to Hero: DOM XSS
url: https://infosecwriteups.com/zero-to-hero-dom-xss-d291d62432d8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-15
fetch_date: 2025-10-04T09:35:34.399122
---

# Zero to Hero: DOM XSS

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd291d62432d8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fzero-to-hero-dom-xss-d291d62432d8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fzero-to-hero-dom-xss-d291d62432d8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d291d62432d8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d291d62432d8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **Zero to Hero: DOM XSS**

[![Prameya Singh Soni](https://miro.medium.com/v2/resize:fill:64:64/1*3EvWOomAhgXboVtN2c-AYA.png)](https://blackburn0027.medium.com/?source=post_page---byline--d291d62432d8---------------------------------------)

[Prameya Singh Soni](https://blackburn0027.medium.com/?source=post_page---byline--d291d62432d8---------------------------------------)

7 min read

·

Mar 9, 2023

--

2

Listen

Share

Press enter or click to view image in full size

![]()

This is the first blog of my series “Zero to Hero”. I am a beginner bug bounty hunter and have reported many bugs to different organizations. I have a lot of things to share with the infosec community, and hence I thought while I keep hunting I would share my learning through this series of blogs. While writing, I will be focusing more on real-world hunting techniques that I encounter while hunting.

### **What is XSS and DOM XSS?**

Cross-site scripting or XSS, allows an attacker to compromise the interactions between the victim and the vulnerable server, allowing him to inject malicious executable javascript code, targeting the victim directly. By performing this attack, a malicious actor steals the cookies of the victim and can perform actions on the victim’s behalf.

In DOM XSS, the vulnerable website takes unsafe data (javascript code) from an attacker-controlled source and then passes it to a javascript sink which executes the code, resulting in an XSS attack.

### **Types of DOM XSS**

Just like the old school XSS, DOM-based XSS is also of two types, depending upon how the vulnerable server responds to the malicious request,

* If the server, reflects the malicious string in the immediate response to an HTTP request and passes it to a sink, it results in **Reflected DOM XSS**.
* If the server, stores the malicious string and reflects it into a later HTTP response further passing into a sink, it results in **Stored DOM XSS**.

Both types of DOM XSS are equally dangerous and must be addressed immediately.

### **Source? Sink? What the …?**

**DOM:** The Document Object Model or DOM is a programming interface for web documents which represents the document as nodes and objects so that programming languages can interact with it and modify the content of the web page according to the code. In the case of javascript as well, it manipulates the nodes and objects of the DOM. If manipulated in an unsafe way, it can result in XSS.

**Source:** The javascript property which accepts user data in an unsafe way is considered as the source. The most common example of a source is “location.search” which is used with almost every GET parameter.

**Sink:** The potential javascript function which can execute our script passed into a source is considered as the sink. For example, the eval() function.

Before we hunt in the wild, let us discuss the technique of finding and exploiting DoM XSS in some practice labs.

### Lab-1: [Reflected DOM XSS by port swigger](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected)

To solve the lab we have to call an alert() function. To exploit we just need two things,

A source where we enter our malicious javascript code and,

A sink that will execute our malicious js code. It is important to understand that without a sink a source is useless and vice versa.

Now, to find the source and sinks, the best and easiest way is to use the DOM invader. When you suspect that a parameter can be a source leading to a potential sink, just spray it with your canary and load it in the burp browser. Before that, make sure that you turn on the DOM invader extension.

Press enter or click to view image in full size

![]()

Now, change the value of the parameter to your canary and load the URL.

Press enter or click to view image in full size

![]()

From this, two things are pretty much clear,

1. The parameter “search” is a potential source,
2. It is passing the user-controlled data into eval() which is a potential sink.

Now to exploit it, we first have to locate the part of the javascript code where our malicious input is getting injected. You can either search every JS file in your browser’s debugger or Just perform a stack trace in the burp browser to know the exact location.

Press enter or click to view image in full size

![]()

After locating, you can add a breakpoint by pressing “Ctrl + B” and by reloading you can check that the value is getting passed into our sink i.e. eval().

Press enter or click to view image in full size

![]()

Now to craft our payload, just follow the basics of XSS exploitation. For example, I will now inject blackburn” to find out that “ is getting escaped by the use of a backslash \.

Press enter or click to view image in full size

![]()

To solve this, we will also add a backslash before our quotation mark since the backslash is not escaped.

Press enter or click to view image in full size

![]()

Now the complete exploit will be,

> search=blackburn\”-alert(1)} //

An arithmetic operator (-) is used to separate the expressions before the alert() is called. And then JSON format is completed by adding a } and // are used to comment out the rest of the code.

Press enter or click to view image in full size

![]()

### Lab-2: [Stored DOM XSS by port swigger](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-stored)

To solve the lab we have to call an alert() function. Again, To exploit we just need two things i.e. Source and a potential sink. From the name of the lab, we know that this is going to be a case of stored XSS, So we will only be testing our canary on the parameters storing our data for later responses (comments, username, etc).

There is functionality to leave comments on any post on the web page. Let’s spray all of those parameters with our canary in DOM invader.

Press enter or click to view image in full size

![]()

From this, we can confirm that the Name and website fields are working as a potential source an...
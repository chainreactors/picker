---
title: South Korea’s online security dead end
url: https://palant.info/2023/01/02/south-koreas-online-security-dead-end/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:21:56.072947
---

# South Korea’s online security dead end

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More 脗禄

[ ]

# South Korea芒聙聶s online security dead end

2023-01-02
 [Korea](/categories/korea/)/[Security](/categories/security/)/[Privacy](/categories/privacy/)
 9 mins
 [41 comments](/2023/01/02/south-koreas-online-security-dead-end/#comments)

**Edit** (2023-01-04): A Korean translation of this article is now available [here](https://www.woojinkim.org/wiki/spaces/me/pages/733085820/South%2BKorea%2Bs%2Bonline%2Bsecurity%2Bdead%2Bend), thanks to Woojin Kim. **Edit** (2023-01-07): Scheduled one more disclosure for February.

Last September I started investigating a South Korean application with unusually high user numbers. It took me a while to even figure out what it really did, there being close to zero documentation. I eventually realized that the application is riddled with security issues and, despite being advertised as a security application, makes the issue it is supposed to address far, far worse.

That芒聙聶s how my journey to the South Korea芒聙聶s very special security application landscape started. Since then I investigated several other applications and realized that the first one wasn芒聙聶t an outlier. All of them caused severe security and privacy issues. Yet they were also installed on almost every computer in South Korea, being a prerequisite for using online banking or government websites in the country.

![Message on www.citibank.co.kr stating: [IP Logger] program needs to be installed to ensure safe use of the service. Do you want to move to the installation page?](/2023/01/02/south-koreas-online-security-dead-end/message.png)

Before I start publishing articles on the individual applications芒聙聶 shortcomings I wanted to post a summary of how (in my limited understanding) this situation came about and what exactly went wrong. From what I can tell, South Korea is in a really bad spot security-wise right now, and it needs to find a way out ASAP.

#### Contents

* [Historical overview](#historical-overview)
* [Current situation](#current-situation)
* [Software quality](#software-quality)
* [Security through obscurity](#security-through-obscurity)
* [Explanation attempts](#explanation-attempts)
* [Getting out of the dead end](#getting-out-of-the-dead-end)
* [Schedule of future disclosures](#schedule-of-future-disclosures)

## Historical overview

I芒聙聶ve heard about South Korea being very 芒聙聹special芒聙聺 every now and then. I cannot claim to fully understand the topic, but there is a whole [Wikipedia article on it](https://en.wikipedia.org/wiki/Web_compatibility_issues_in_South_Korea). Apparently, the root issue were the US export restrictions on strong cryptography in the 90ies. This prompted South Korea to develop their own cryptographic solutions.

It seems that this started a fundamental distrust in security technologies coming out of the United States. So even when the export restrictions were lifted, South Korea continued adding their own security layers on top of SSL. All users had to install special applications just to use online banking.

Originally, these applications used Microsoft芒聙聶s proprietary ActiveX technology. This only worked in Internet Explorer and severely hindered adoption of other browsers in South Korea.

Wikipedia lists several public movements aimed at improving this situation. Despite the pressure from these, it took until well after 2010 that things actually started changing.

Technologically, the solutions appear to have gone through several iterations. The first one were apparently [NPAPI plugins](https://en.wikipedia.org/wiki/NPAPI), the closest thing to ActiveX in non-Microsoft browsers. I芒聙聶ve also seen solutions based on browser extensions which are considerably simpler than NPAPI plugins.

Currently, the vendors appear to have realized that privileged access to the browser isn芒聙聶t required. Instead, they merely need a communication channel from the websites to their application. So now all these applications run a local web server that websites communicate with.

## Current situation

Nowadays, a typical Korean banking website will require five security applications to be installed before you are allowed to log in. One more application is suggested to manage this application zoo. And since different websites require different sets of applications, a typical computer in South Korea probably runs a dozen different applications from half a dozen different vendors. Just to be able to use the web.

![Screenshot of a page titled 芒聙聹Install Security Program.芒聙聺 Below it the text 芒聙聹To access and use services on Busan Bank website, please install the security programs. If your installation is completed, please click Home Page to move to the main page. Click [Download Integrated Installation Program] to start automatica installation. In case of an error message, please click 'Save' and run the downloaded the application.芒聙聺 Below that text the page suggests downloading 芒聙聹Integrated installation (Veraport)芒聙聺 and five individual applications.](/2023/01/02/south-koreas-online-security-dead-end/applications.png)

Each of these applications comes with a website SDK that the website needs to install, consisting of half a dozen JavaScript files. So your typical Korean banking website takes quite a while to load and initialize.

Interestingly, most of these applications don芒聙聶t even provide centralized download servers. The distribution and updates have been completely offloaded to websites using these security applications.

And that is working exactly as well as you芒聙聶d expect. Even looking at mere usability, I芒聙聶ve noticed an application that a few years ago went through a technology change: from using a browser extension to using a local web server for communication. Some banks still distribute and expect the outdated application version, others work with the new one. For users it is impossible to tell why they have the application installed, yet their bank claims that they don芒聙聶t. And they complain en masse.

Obviously, websites distributing applications also makes them a target. And properly securing so many download servers is unrealistic. So a few years ago the North Korean Lazarus group made the news by [compromising some of these servers in order to distribute malware](https://threatpost.com/hacked-software-south-korea-supply-chain-attack/161257/).

## Software quality

I took a thorough look at the implementation of several security applications widely used in South Korea. While I芒聙聶ll go into the specific issues in future blog posts, some tendencies appear universal across the entire landscape.

One would think, being responsible for the security of an entire nation would make vendors of such software be extra vigilant. That芒聙聶s not what I saw however. In fact, security-wise these applications are often decades behind state of the art.

This starts with a simple fact: some of these applications are written in the [C programming language](https://en.wikipedia.org/wiki/C_%28programming_language%29), not even C++. It being a low-level programming language, these days it is typically used in code that has to work close to hardware such as device drivers. Here however it is used in large applications interacting with websites in complicated ways.

The manual approach to memory management in C is a typical source of exploitable memory safety issues like [buffer overflows](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow). Avoiding them in C requires utmost care. While such bugs weren芒聙聶t the focus of my investigation, I couldn芒聙聶t fail noticing that the developers of these applications didn芒聙聶t demonstrate much experience avoiding memory safety issues.

Modern compilers provide a number of security mechanisms to help alleviate such issues. But these applications don芒聙聶t use modern compilers, relying on Visual Studio versions released around 15 years ago instead.

And even the basic ...
---
title: Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000
url: https://buaq.net/go-141756.html
source: unSafe.sh - 不安全
date: 2022-12-29
fetch_date: 2025-10-04T02:39:22.380651
---

# Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000

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

Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000

Hello people, Here I am sharing another four digit write-up which is one of my very old finding. If
*2022-12-28 21:1:29
Author: [infosecwriteups.com(查看原文)](/jump-141756.htm)
阅读量:25
收藏*

---

Hello people, Here I am sharing another four digit write-up which is one of my very old finding. If you haven’t read my previous writeup about how I was able to bypass a strong rate limit mechanism on all the endpoints then here is the link to it:

Lots of people were confused with the title when I initially posted about this bug. So here is the complete writeup and methodology that I used. At the time I discovered this bug I had just started my bug bounty journey after reading many E-books and write-ups.

I decided to choose a target randomly to which I got to know that only mentioned domains and subdomains were in scope. All the other subdomains were considered as Out of Scope. They also mentioned in their policy that **\*.target.com** is out of scope but target.com was in scope. This is because the company was actually providing some kind of services to their clients which allows them to make their customize subdomains like **client1.target.com,client2.target.com.** Due to this they restricted to test on any of the subdomains. So what to do when this type of target crosses our brain? The first thought came into my mind was that maybe I should try to find any critical vulnerability on their subdomains as not so many researchers have checked due to their policy.

The first thing I did was to find subdomains but not with our normal method. Instead I used subdomain enumeration wordlist which contained words like app,development,dev,service,app-dev etc.

Very limited subdomains were extracted using this method and out of them, one subdomain was like **services.target.com.** On visiting this subdomain it showed a DNS error but still I don’t know how this got detected in subdomain enumeration phase. Next thing I tried to use google dork i.e. **site:\*.services.target.com** where I found some results from domains like **public.services.target.com** etc.

You must have observed that the subdomain contains word “services” which may indicate that there are some more services running on this subdomain. Next thing I extracted subdomains for the domain “services.target.com”. Interestingly I found a subdomain “**sserver.services.target.com**”.

This page contains a normal login page and upon observing UI, I guessed that it was used to manage source codes and other things by directly giving access to the github account.

So maybe this login portal was meant for employees and only employees are given credentials to access further. Now I was just wondering what to do next, Search for JS files, use github dorks for credentials leak etc. but nothing interesting came as this domain was not mentioned anywhere.

I observed the URL which was “/sign-in?returnTo=%2F”. And tried to change the “sign-in” to other URLs like “register”, ”get-started” and simply **“sign-up”** showed me a signup page asking for email, username and password.

Still I was in doubt that after clicking on register, it may show error that sign-up is not possible just like JIRA. But guess what? It allowed me to signup using my email and I was successful in signing into account.

Now next task was to see what access we have and what sensitive information we can see. And I was not able to believe my eyes, They were using this server portal to manage all of their github codes. Even the private repositories. Any new users were given direct access to all the codes shared on this portal.

Normally it was a private repository if directly accessed through github

Now when I tried to access the same repo from the portal, then it was easily accessible and I was able to see all the credentials as well as any secret files.

Secrets file containing some secret tokens

All of their private repository were accessible and all of their secret API keys, and admin account credentials were visible. It was a complete organization takeover. As they were providing services to many clients, all of their client data was also accessible through these exposed credentials.

I immediately created a report and the team triaged and fixed this report within 40mins making the portal inaccessible from public view. Also they rotated any credentials exposed. They rewarded me with their highest payout for critical i.e. 2000$

**TIP: Even if something is not in scope, give it a try. Don’t try aggressive testing but still look for any critical vulnerabilities.**

**Look even for subdomains of subdomain if you feel any suspicious subdomains running.**

**Look for any endpoints that may contain words like “services”, “internal” etc. and look for any open services available.**

That’s it guys, I hope you liked it and do share if you found it helpful.

<https://www.linkedin.com/in/manavbankatwala/>

<https://www.instagram.com/manav.bug/>

<https://twitter.com/manavbankatwala>

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/unauthorized-sign-up-on-subdomain-of-subdomain-leading-to-organization-takeover-worth-2000-a7199952d80b?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
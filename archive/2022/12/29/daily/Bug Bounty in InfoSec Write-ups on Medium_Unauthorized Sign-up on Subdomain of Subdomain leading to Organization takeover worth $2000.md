---
title: Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000
url: https://infosecwriteups.com/unauthorized-sign-up-on-subdomain-of-subdomain-leading-to-organization-takeover-worth-2000-a7199952d80b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-29
fetch_date: 2025-10-04T02:39:55.195007
---

# Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa7199952d80b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthorized-sign-up-on-subdomain-of-subdomain-leading-to-organization-takeover-worth-2000-a7199952d80b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthorized-sign-up-on-subdomain-of-subdomain-leading-to-organization-takeover-worth-2000-a7199952d80b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a7199952d80b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a7199952d80b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Unauthorized Sign-up on Subdomain of Subdomain leading to Organization takeover worth $2000

[![Manav Bankatwala](https://miro.medium.com/v2/resize:fill:64:64/1*lKKgns5f3pH7FpGgLfe27A@2x.jpeg)](https://medium.com/%40manavbankatwala29?source=post_page---byline--a7199952d80b---------------------------------------)

[Manav Bankatwala](https://medium.com/%40manavbankatwala29?source=post_page---byline--a7199952d80b---------------------------------------)

5 min read

·

Dec 28, 2022

--

2

Listen

Share

Hello people, Here I am sharing another four digit write-up which is one of my very old finding. If you haven’t read my previous writeup about how I was able to bypass a strong rate limit mechanism on all the endpoints then here is the link to it:

[## Unique Rate limit bypass worth 1800$

### Proving the organization statement wrong with OOS Rate limit bypass.

medium.com](https://medium.com/%40manavbankatwala29/unique-rate-limit-bypass-worth-1800-6e2947c7d972?source=post_page-----a7199952d80b---------------------------------------)

## **Starting with the initial phase.**

Lots of people were confused with the title when I initially posted about this bug. So here is the complete writeup and methodology that I used. At the time I discovered this bug I had just started my bug bounty journey after reading many E-books and write-ups.

I decided to choose a target randomly to which I got to know that only mentioned domains and subdomains were in scope. All the other subdomains were considered as Out of Scope. They also mentioned in their policy that **\*.target.com** is out of scope but target.com was in scope. This is because the company was actually providing some kind of services to their clients which allows them to make their customize subdomains like **client1.target.com,client2.target.com.** Due to this they restricted to test on any of the subdomains. So what to do when this type of target crosses our brain? The first thought came into my mind was that maybe I should try to find any critical vulnerability on their subdomains as not so many researchers have checked due to their policy.

The first thing I did was to find subdomains but not with our normal method. Instead I used subdomain enumeration wordlist which contained words like app,development,dev,service,app-dev etc.

Very limited subdomains were extracted using this method and out of them, one subdomain was like **services.target.com.** On visiting this subdomain it showed a DNS error but still I don’t know how this got detected in subdomain enumeration phase. Next thing I tried to use google dork i.e. **site:\*.services.target.com** where I found some results from domains like **public.services.target.com** etc.

You must have observed that the subdomain contains word “services” which may indicate that there are some more services running on this subdomain. Next thing I extracted subdomains for the domain “services.target.com”. Interestingly I found a subdomain “**sserver.services.target.com**”.

## **What content was present on this subdomain?**

This page contains a normal login page and upon observing UI, I guessed that it was used to manage source codes and other things by directly giving access to the github account.

Press enter or click to view image in full size

![]()

So maybe this login portal was meant for employees and only employees are given credentials to access further. Now I was just wondering what to do next, Search for JS files, use github dorks for credentials leak etc. but nothing interesting came as this domain was not mentioned anywhere.

## Here comes the interesting part!

I observed the URL which was “/sign-in?returnTo=%2F”. And tried to change the “sign-in” to other URLs like “register”, ”get-started” and simply **“sign-up”** showed me a signup page asking for email, username and password.

Press enter or click to view image in full size

![]()

Still I was in doubt that after clicking on register, it may show error that sign-up is not possible just like JIRA. But guess what? It allowed me to signup using my email and I was successful in signing into account.

Now next task was to see what access we have and what sensitive information we can see. And I was not able to believe my eyes, They were using this server portal to manage all of their github codes. Even the private repositories. Any new users were given direct access to all the codes shared on this portal.

Press enter or click to view image in full size

![]()

Normally it was a private repository if directly accessed through github

Now when I tried to access the same repo from the portal, then it was easily accessible and I was able to see all the credentials as well as any secret files.

![]()

Press enter or click to view image in full size

![]()

Secrets file containing some secret tokens

All of their private repository were accessible and all of their secret API keys, and admin account credentials were visible. It was a complete organization takeover. As they were providing services to many clients, all of their client data was also accessible through these exposed credentials.

I immediately created a report and the team triaged and fixed this report within 40mins making the portal inaccessible from public view. Also they rotated any credentials exposed. They rewarded me with their highest payout for critical i.e. 2000$

**TIP: Even if something is not in scope, give it a try. Don’t try aggressive testing but still look for any critical vulnerabilities.**

**Look even for subdomains of subdomain if you feel any suspicious subdomains running.**

**Look for any endpoints that may contain words like “services”, “internal” etc. and look for any open services available.**

That’s it guys, I hope you liked it and do share if you found it helpful.

## Follow me to get latest updates:

<https://www.linkedin.com/in/manavbanka...
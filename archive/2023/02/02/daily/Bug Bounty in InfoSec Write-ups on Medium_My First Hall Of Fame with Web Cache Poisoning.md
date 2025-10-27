---
title: My First Hall Of Fame with Web Cache Poisoning
url: https://infosecwriteups.com/my-first-hall-of-fame-with-web-cache-poisoning-c11749017cd8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-02
fetch_date: 2025-10-04T05:28:51.974537
---

# My First Hall Of Fame with Web Cache Poisoning

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc11749017cd8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-hall-of-fame-with-web-cache-poisoning-c11749017cd8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-hall-of-fame-with-web-cache-poisoning-c11749017cd8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c11749017cd8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c11749017cd8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# My First Hall Of Fame with Web Cache Poisoning

## Web Cache Poisoning — An Introduction | Karthikeyan Nagaraj

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--c11749017cd8---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--c11749017cd8---------------------------------------)

4 min read

·

Jan 31, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

## What is Caching?

* Caching is a process that temporarily stores frequently accessed web pages on a server to reduce the time it takes to access them.
* This allows web servers to respond to user requests faster, improving the overall user experience.

## What is Web Cache Poisoning?

* Web cache poisoning is a form of attack that takes advantage of the way web servers store and serve cached web content.
* However, web cache poisoning attacks exploit this process by injecting malicious content into the cache, which is then served to all users who access the website.
* This malicious activity is performed to alter the content that is stored in a cache, with the aim of tricking users into viewing malicious content or spreading malware.
* Web caching systems, including proxy servers and content delivery networks, store website data to speed up access times and reduce the load on web servers.

## How to Find and Attack Web Cache Poisoning?

* Web cache poisoning attacks can be difficult to detect because they often go unnoticed. The first sign of a cache poisoning attack is usually the appearance of malicious content on a website, which can be anything from pop-up ads, malicious links, or injected code.
* The attack is carried out by exploiting a vulnerability in the web server, such as an outdated software version or misconfigured security settings.
* One common method of web cache poisoning is called cross-site scripting (XSS). In an XSS attack, the attacker injects malicious code into a website, which is then executed by the browser of every user who visits the site.
* The malicious code can then be used to steal sensitive information, redirect users to malicious websites, or install malware on their systems.
* Another method of web cache poisoning is called cache injection, which involves manipulating the webserver to cache malicious content.
* This type of attack is typically carried out by exploiting vulnerabilities in the web server software, such as a missing patch or outdated software version. The attacker then injects malicious content into the cache, which is then served to all users who access the website.

## Impact of Web Cache Poisoning:

* Web cache poisoning can have serious consequences for both websites and users. For websites, it can result in the loss of credibility, as users may distrust the site and refuse to return.
* Additionally, it can result in the loss of business, as users may avoid purchasing products or services from the site.
* For users, the impact of web cache poisoning can be even more severe. They can be exposed to malicious code, which can steal sensitive information, such as passwords, credit card numbers, and personal information.
* Additionally, they can be infected with malware, which can compromise their systems, steal data, and cause other damage.

## Prevention of Web Cache Poisoning:

* Preventing web cache poisoning requires a multi-layered approach, which includes regular software updates, security patches, and proper security configuration.
* Websites should also implement security measures such as SSL encryption, to ensure that the cache is not tampered with during transit.
* Another important step in preventing web cache poisoning is to use a web application firewall (WAF), which acts as a barrier between the web server and the internet.
* A WAF can detect and block malicious traffic, helping to prevent cache poisoning attacks. Additionally, websites should implement access controls, such as authentication and authorization, to prevent unauthorized access to the cache.

## Conclusion

* Web cache poisoning is a serious threat that can have serious consequences for both websites and users.
* By exploiting vulnerabilities in the web server, attackers can inject malicious content into the cache, which can be used to steal sensitive information, compromise systems, and cause other damage

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

[![]()](http://buymeacoffee.com/cyberw1ng)

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

[## Cyberw1ng

### Learn Cyber Security and Create Awareness ~ cyberwing Stay tuned with me, Subscribe, and Like the Videos… Ask Doubts…

www.youtube.com](https://www.youtube.com/channel/UCBg0UIT0319Xc-cw4QK8bqA?sub_confirmation=1&source=post_page-----c11749017cd8---------------------------------------)

Github for Resources:

[## Cyberw1ng — Overview

### Security Researcher and Bug Hunter. Cyberw1ng has 8 repositories available. Follow their code on GitHub.

github.com](https://github.com/cyberw1ng?source=post_page-----c11749017cd8---------------------------------------)

Telegram Channel for Free Ethical Hacking Dumps

[## Ethical Hacking Dumps — CEH, OSCP, Comptia

### Materials and Books for Ethical Hacking Exams like CEH v12, OSCP, Comptia Pentest+, Comptia Security+, Comptia Network+…

t.me](https://t.me/ethicalhackingessentials?source=post_page-----c11749017cd8---------------------------------------)

Thank you for Reading!

Happy Ethical Hacking ~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----c11749017cd8---------------------------------------)

[Hall Of Fame](https://medium.com/tag/hall-of-fame?source=post_page-----c11749017cd8------------...
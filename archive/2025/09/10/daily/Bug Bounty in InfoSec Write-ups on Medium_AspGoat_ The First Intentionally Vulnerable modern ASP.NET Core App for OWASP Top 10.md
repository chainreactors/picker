---
title: AspGoat: The First Intentionally Vulnerable modern ASP.NET Core App for OWASP Top 10
url: https://infosecwriteups.com/aspgoat-the-first-intentionally-vulnerable-modern-asp-net-core-app-for-owasp-top-10-d6037f7ac3f1?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-10
fetch_date: 2025-10-02T19:54:14.500131
---

# AspGoat: The First Intentionally Vulnerable modern ASP.NET Core App for OWASP Top 10

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd6037f7ac3f1&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faspgoat-the-first-intentionally-vulnerable-modern-asp-net-core-app-for-owasp-top-10-d6037f7ac3f1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faspgoat-the-first-intentionally-vulnerable-modern-asp-net-core-app-for-owasp-top-10-d6037f7ac3f1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d6037f7ac3f1---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d6037f7ac3f1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# AspGoat: The First Intentionally Vulnerable modern ASP.NET Core App for OWASP Top 10

[![Soham](https://miro.medium.com/v2/resize:fill:64:64/1*Rkot45JMEwqrO7Ki_RXMjQ.jpeg)](https://medium.com/%40sohamdas334?source=post_page---byline--d6037f7ac3f1---------------------------------------)

[Soham](https://medium.com/%40sohamdas334?source=post_page---byline--d6037f7ac3f1---------------------------------------)

2 min read

·

Sep 8, 2025

--

2

Listen

Share

Most intentionally vulnerable applications we know and use for training like **DVWA**, **Juice Shop**, and **WebGoat** are written in **PHP** , **Node.JS** and **Java**. While they are fantastic for learning security concepts, there has always been a gap for those working with **modern ASP.NET Core applications**.

Press enter or click to view image in full size

![]()

AspGoat — GitHub 🐐

That’s exactly why I created [**AspGoat**](https://github.com/Soham7-dev/AspGoat) 🐐, an intentionally vulnerable web application built with **ASP.NET Core MVC + SQLite + EF Core**, designed to help **developers**, **security researchers**, and **bug bounty hunters** sharpen their skills.

The latest release (v1.0.1) includes:

1. Polished Labs for OWASP Top 10 (and more) vulnerabilities.
2. Hands-on challenges covering **XSS, SQL Injection, CSRF, SSRF, IDOR, Insecure Deserialization, Prototype Pollution**, and more.
3. **Secure Coding** Challenges in order to understand the **Whitebox** aspect of **Penetration Testing**.
4. A fully supported **official Docker image**, so you can spin it up in seconds:

```
docker pull sohamburger/aspgoat:latest
docker run --rm -p 8000:8000 sohamburger/aspgoat:latest
```

Whether you’re a:

1. **Developer** who wants to understand how security vulnerabilities arise into modern **ASP.NET Core** Web Applications.
2. **Security researcher or bug bounty hunter** looking to sharpen your **Penetration Testing** skills.
3. **Student** preparing for AppSec interviews and AppSec certifications.

[AspGoat](https://github.com/Soham7-dev/AspGoat) is for you…

Explore the Project here 👉 : <https://github.com/Soham7-dev/AspGoat>

Issues, Contributions and Suggestions are always welcomed.

[Application Security](https://medium.com/tag/application-security?source=post_page-----d6037f7ac3f1---------------------------------------)

[Dotnet](https://medium.com/tag/dotnet?source=post_page-----d6037f7ac3f1---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----d6037f7ac3f1---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----d6037f7ac3f1---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----d6037f7ac3f1---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d6037f7ac3f1---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d6037f7ac3f1---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d6037f7ac3f1---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d6037f7ac3f1---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--d6037f7ac3f1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Soham](https://miro.medium.com/v2/resize:fill:96:96/1*Rkot45JMEwqrO7Ki_RXMjQ.jpeg)](https://medium.com/%40sohamdas334?source=post_page---post_author_info--d6037f7ac3f1---------------------------------------)

[![Soham](https://miro.medium.com/v2/resize:fill:128:128/1*Rkot45JMEwqrO7Ki_RXMjQ.jpeg)](https://medium.com/%40sohamdas334?source=post_page---post_author_info--d6037f7ac3f1---------------------------------------)

[## Written by Soham](https://medium.com/%40sohamdas334?source=post_page---post_author_info--d6037f7ac3f1---------------------------------------)

[5 followers](https://medium.com/%40sohamdas334/followers?source=post_page---post_author_info--d6037f7ac3f1---------------------------------------)

·[4 following](https://medium.com/%40sohamdas334/following?source=post_page---post_author_info--d6037f7ac3f1---------------------------------------)

OWASP Project Leader | Security Researcher

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d6037f7ac3f1---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d6037f7ac3f1---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d6037f7ac3f1---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d6037f7ac3f1---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d6037f7ac3f1---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d6037f7ac3f1---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d6037f7ac3f1---------------------------------------)

...
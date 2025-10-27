---
title: Unauthorized access to the admin panel via leaked credentials on the WayBackMachine
url: https://infosecwriteups.com/unauthorized-access-to-the-admin-panel-via-leaked-credentials-on-the-waybackmachine-55c3307141c6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-05-02
fetch_date: 2025-10-04T11:39:27.147195
---

# Unauthorized access to the admin panel via leaked credentials on the WayBackMachine

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F55c3307141c6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthorized-access-to-the-admin-panel-via-leaked-credentials-on-the-waybackmachine-55c3307141c6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthorized-access-to-the-admin-panel-via-leaked-credentials-on-the-waybackmachine-55c3307141c6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-55c3307141c6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-55c3307141c6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Unauthorized access to the admin panel via leaked credentials on the WayBackMachine

[![M7arm4n](https://miro.medium.com/v2/resize:fill:64:64/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---byline--55c3307141c6---------------------------------------)

[M7arm4n](https://m7arm4n.medium.com/?source=post_page---byline--55c3307141c6---------------------------------------)

2 min read

·

May 1, 2023

--

3

Listen

Share

Hello my friends, Today I want to talk about one of my admin panel bypass methods which leads me to easily bypass the admin panel.

In my pervasive write-up, I noticed the power of the Wayback Machine and how it helped me to discover the hidden endpoints and exploit an XSS on a famous bank, Here is the write-up:

[## Let’s Hacking Citizens Bank

### Hi Guys, Here is another write-up about how I hacked the Citizens Bank and how chrome extensions helped me in this way…

infosecwriteups.com](/lets-hacking-citizens-bank-9520e9c05cf9?source=post_page-----55c3307141c6---------------------------------------)

So, Today I want to show you how to think out of the box and use this.

Let’s talk about the recon part, The program specified that the target.com domain was in scope, and after subdomains enumeration, I started fuzzing the directories of one of the subdomains and finally arrived at a specific path.

When you opened the desired path, a message was displayed requiring a username and password to access this path, which was received as a GET Base parameter.

I started searching Google and the Wayback Machine and GitHub and all the indexes, but I couldn’t find anything that pointed directly to this particular path in the target.com domain to maybe finds some sensitive information could be found.

While searching on Google, I came across some sites that seem to be using the source of the subdomain, but these domains were not in scope. To test I opened the directory in the out-of-scope domains. for one of them, my Wayback Machine extension was activated and some archived paths were detected.

I opened the archived paths and found a few usernames, passwords, and specific endpoints. I replaced them in the subdomain in scope and one of them worked correctly and I got access to the admin panel. Now I’m In.

Press enter or click to view image in full size

![]()

Thank you for following me here, Don’t forget to follow me for more write-ups.

[Twitter](https://twitter.com/M7arm4n) 🐦

[**AI-Powered Cyber Threat Detection and Response**](https://links.swapstack.co/wk5y)**:** SIEM and Compliance solution powered by AI, real-time correlation, and threat intelligence. Built for simplicity, reduced noise and affordability. [*Learn More*](https://links.swapstack.co/wk5y)

[Infosec](https://medium.com/tag/infosec?source=post_page-----55c3307141c6---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----55c3307141c6---------------------------------------)

[Bugs](https://medium.com/tag/bugs?source=post_page-----55c3307141c6---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----55c3307141c6---------------------------------------)

[Admin Panel](https://medium.com/tag/admin-panel?source=post_page-----55c3307141c6---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--55c3307141c6---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--55c3307141c6---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--55c3307141c6---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--55c3307141c6---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--55c3307141c6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![M7arm4n](https://miro.medium.com/v2/resize:fill:96:96/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---post_author_info--55c3307141c6---------------------------------------)

[![M7arm4n](https://miro.medium.com/v2/resize:fill:128:128/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---post_author_info--55c3307141c6---------------------------------------)

[## Written by M7arm4n](https://m7arm4n.medium.com/?source=post_page---post_author_info--55c3307141c6---------------------------------------)

[1.3K followers](https://m7arm4n.medium.com/followers?source=post_page---post_author_info--55c3307141c6---------------------------------------)

·[6 following](https://medium.com/%40m7arm4n/following?source=post_page---post_author_info--55c3307141c6---------------------------------------)

Maybe Hunter But absolutely a movie fan :)

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----55c3307141c6---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----55c3307141c6---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----55c3307141c6---------------------------------------)

[Careers](https://medium.com/jobs-at-me...
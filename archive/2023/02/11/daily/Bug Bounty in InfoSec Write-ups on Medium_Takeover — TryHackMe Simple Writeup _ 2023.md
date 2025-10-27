---
title: Takeover — TryHackMe Simple Writeup | 2023
url: https://infosecwriteups.com/takeover-tryhackme-simple-writeup-2023-f88ff3ed2578?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-11
fetch_date: 2025-10-04T06:20:12.020554
---

# Takeover — TryHackMe Simple Writeup | 2023

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff88ff3ed2578&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftakeover-tryhackme-simple-writeup-2023-f88ff3ed2578&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftakeover-tryhackme-simple-writeup-2023-f88ff3ed2578&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f88ff3ed2578---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f88ff3ed2578---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Takeover — TryHackMe | Simple Writeup | 2023

## TryHackMe’s Takeover Simple Walkthrough | Karthikeyan Nagaraj

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--f88ff3ed2578---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--f88ff3ed2578---------------------------------------)

3 min read

·

Jan 24, 2023

--

1

Listen

Share

[![]()](https://tryhackme.com/room/takeover)

### Room Description:

Hello there,

* I am the CEO and one of the co-founders of`futurevera.thm`.
* In Futurevera, we believe that the future is in space.
* We do a lot of space research and write`blogs` about it.
* We used to help students with space questions, but we are rebuilding our`support`.

Recently blackhat hackers approached us saying they could take over and are asking us for a big ransom. Please help us to find what they can take over.

Hint: Don’t forget to add the 10.10.218.33 in /etc/hosts for futurevera.thm ; )

Our website is located at [https://futurevera.thm](https://futurevera.thm/)

### Note:

> For this challenge, you don’t need to Enumerate subdomains via tools. Because, we can assume the sub-domains, which is mentioned in 4th step.
> ***Only for this Challenge!!****And, Some domains won’t work in chrome, In that cases use firefox*

> Connect to TryHackMe’s VPN and Make sure to add the subdomains to `/etc/hosts` with the corresponding IP

## Analysis:

Press enter or click to view image in full size

![]()

1. Nothing found on nmap Enumeration
2. Nothing was found in the Source code
3. Subdomain Enumeration through gobuster displays a subdomain portal.futurevera.thm

```
gobuster vhost -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u futurevera.thm -t 50 --append-domain
```

Press enter or click to view image in full size

![]()

4. Make sure to add the subdomain to`/etc/hosts`before opening

![]()

<http://portal.futurevera.thm>

Press enter or click to view image in full size

![]()

4. As per the room description, we can assume that there will be 2 subdomains → blog and support

5. Let’s add the Sub domain <https://blog.futurevera.thm> to`/etc/hosts` and Explore it further

`sudo echo <THM-IP> blog.futurevera.thm >> /etc/hosts`

if you get an error, try the below command

```
su
echo <THM-IP> blog.futurevera.thm >> /etc/hosts
```

Press enter or click to view image in full size

![]()

6. Inspecting Blog doesn’t provide anything useful. So Let’s move to `support`

7. The Room Description Expresses that they are rebuilding the`support` page, so there may be chances to obtain the flag

8. By Checking the certificate, we found a domain name

![]()

Press enter or click to view image in full size

![]()

9. On Opening the domain, we’ll get the flag

![]()

```
Flag: flag{beea0d6edfcee06a59b83fb50ae81b2f}
```

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

[![]()](https://www.buymeacoffee.com/Cyberw1ng)

Thank you for Reading!!

Happy Takeover ~

```
Author: Karthikeyan Nagaraj ~ Cyberw1ng
```

[Tryhackme](https://medium.com/tag/tryhackme?source=post_page-----f88ff3ed2578---------------------------------------)

[Domains](https://medium.com/tag/domains?source=post_page-----f88ff3ed2578---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----f88ff3ed2578---------------------------------------)

[Ctf](https://medium.com/tag/ctf?source=post_page-----f88ff3ed2578---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----f88ff3ed2578---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f88ff3ed2578---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f88ff3ed2578---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f88ff3ed2578---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f88ff3ed2578---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--f88ff3ed2578---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/resize:fill:96:96/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---post_author_info--f88ff3ed2578---------------------------------------)

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/resize:fill:128:128/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---post_author_info--f88ff3ed2578---------------------------------------)

[## Written by Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---post_author_info--f88ff3ed2578---------------------------------------)

[12.8K followers](https://cyberw1ng.medium.com/followers?source=post_page---post_author_info--f88ff3ed2578---------------------------------------)

·[1 following](https://medium.com/%40cyberw1ng/following?source=post_page---post_author_info--f88ff3ed2578---------------------------------------)

Entrepreneur | Wr...
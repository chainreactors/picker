---
title: Story of a $1k bounty — SSRF to leaking access token and other sensitive information
url: https://infosecwriteups.com/story-of-a-1k-bounty-ssrf-d5c4868680f5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-08
fetch_date: 2025-10-03T21:55:14.545829
---

# Story of a $1k bounty — SSRF to leaking access token and other sensitive information

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd5c4868680f5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstory-of-a-1k-bounty-ssrf-d5c4868680f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstory-of-a-1k-bounty-ssrf-d5c4868680f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d5c4868680f5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d5c4868680f5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Story of a $1k bounty — SSRF to leaking access token and other sensitive information

[![Faique](https://miro.medium.com/v2/resize:fill:64:64/1*Au-zV7w1ZEOy2HmvsBdVlQ.jpeg)](https://faique.medium.com/?source=post_page---byline--d5c4868680f5---------------------------------------)

[Faique](https://faique.medium.com/?source=post_page---byline--d5c4868680f5---------------------------------------)

4 min read

·

Nov 5, 2022

--

7

Listen

Share

Press enter or click to view image in full size

![]()

Hello and welcome everyone to my story of how I got my first bounty on HackerOne by exploiting an SSRF that leaked Google cloud access token and other sensitive data, Before moving forward I would like to thank this sweet community that has helped me in my overall journey.

I chose the target from my HackerOne’s private invitation list, therefore I cannot the disclose the target and so I’ll call it redacted.com. I started with recon, I created an automation tool that do my recon process like gathering subdomains, getting live hosts, running nuclei , directory brute forcing, nmap and getting waybackurls etc. After my automation was done i analyzed all the data like waybackurls and others.

The waybackurls seemed interesting so I quickly used gf patterns to get all ssrf endpoints that could be vulnerable

```
cat waybackurl | gf ssrf
```

Press enter or click to view image in full size

![]()

As the \_\_host field fetches some kind of data from the github, I tried testing ssrf, So I quickly opened my Burpsuite and put the burp collaborator link in the \_\_host field and send the request, I clicked on poll now button and yes I got an HTTP interaction and the burp collaborator response was reflected on the screen.

Press enter or click to view image in full size

![]()

I tried XSS with it by firing up an Apache server and uploading alert JavaScript payload

Press enter or click to view image in full size

![]()

But i stopped because XSS won’t be so impactful and started to look for ssrf, In the \_\_host parameter I put 169.254.169.254 and in the url I added */latest/meta-data/iam/security-credentials/*

```
https://redacted.redacted.com/latest/meta-data/iam/security-credentials/?__host=169.254.169.254&__proto=https
```

and sent the request. But it returned **502 BAD Gateway** I then changed \_\_proto value to http but it didn’t either worked.

Then I though of why not try other endpoints like google, digital ocean one’s, I took a help of a pdf that has all ssrf endpoints that I will provide down and finally google cloud endpoint gave a response other than 502.

The response contained

```
Missing required header: Metadata-Flavour
```

Press enter or click to view image in full size

![]()

So I quickly added this header and set the value of it to Google(took help from pdf) and send the request and *yesss!! it did work*

Press enter or click to view image in full size

![]()

I then tried to get access token using

```
GET /computeMetadata/v1/instance/service-accounts/default/token?__host=169.254.169.254&__proto=http
```

I screamed woah!! I got it, SSRF achieved :)

Press enter or click to view image in full size

![]()

I tried and got other details like scopes, emails, region and id etc.

### Reporting

I reported the vulnerability with all the Pocs and waited until next day, they responded & acknowledged it as a cool finding and rewarded me with $1000 bounty

Press enter or click to view image in full size

![]()

> PDF: [SSRF.pdf](https://github.com/faiqu3/ssrf/blob/main/SSRF.pdf)

Thank you for reading till here, I hope you guys learned something new from the write up. If you enjoyed make sure to give a clap and follow me on:

### Twitter: <https://twitter.com/imfaiqu3>

### Instagram: <https://www.instagram.com/faique.exe>

### LinkedIn: <https://www.linkedin.com/in/faiqu3/>

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----d5c4868680f5---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----d5c4868680f5---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----d5c4868680f5---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----d5c4868680f5---------------------------------------)

[Ctf](https://medium.com/tag/ctf?source=post_page-----d5c4868680f5---------------------------------------)

--

--

7

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d5c4868680f5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d5c4868680f5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d5c4868680f5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d5c4868680f5---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--d5c4868680f5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Faique](https://miro.medium.c...
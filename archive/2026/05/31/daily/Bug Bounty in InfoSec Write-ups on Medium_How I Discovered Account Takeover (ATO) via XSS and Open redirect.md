---
title: How I Discovered Account Takeover (ATO) via XSS and Open redirect
url: https://infosecwriteups.com/how-i-discovered-account-takeover-ato-via-xss-and-open-redirect-36f640760451?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-31
fetch_date: 2026-06-01T06:47:05.608135
---

# How I Discovered Account Takeover (ATO) via XSS and Open redirect

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-discovered-account-takeover-ato-via-xss-and-open-redirect-36f640760451&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-discovered-account-takeover-ato-via-xss-and-open-redirect-36f640760451&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-36f640760451---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-36f640760451---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# How I Discovered Account Takeover (ATO) via XSS and Open redirect

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*3UJihM4VvA-DeZOgGnYqLg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--36f640760451---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--36f640760451---------------------------------------)

2 min read

·

May 20, 2026

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D36f640760451&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-discovered-account-takeover-ato-via-xss-and-open-redirect-36f640760451&source=---header_actions--36f640760451---------------------post_audio_button------------------)

Share

Hello Everyone,

Today, I want to share my experience of discovering an account takeover (ATO) vulnerability through XSS and Open redirect. Let’s dive right in!

So, hunting starts with a random program selection let call it `example.xyz.`It is a crypto platform.

I started hunting with enumerating subdomain and checking if there is any possible subdomain takeover but there is nothing found.

## Get JEETPAL’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

I use my Wayback URLs to grab previous URL’s from the `example.xyz`and started hunting manually. I visited the signup page and started the registration process while registering on the site I notice a parameter called `callbackUrl`

```
https://example.xyz/sign-in?callbackUrl=
```

I decided to test this parameter with an open redirect payload.

```
https://example.xyz/sign-in?callbackUrl=https://example.xyz@evil.com
```

and this Open redirect works. After the signin. I was redirected to the evil.com. but this wasn’t sufficient for higher impact the max could go up to P3 /P4 so I decide to test for a xss. I use many payloads but the tags `<>`were filter out from the payload. So, I decided to use different payload i.e

```
javascript:alert(document.cookie)
```

and this one worked successfully I was able to pop-up an alert with session cookies. from here we can get those cookies into our server and use them.

Press enter or click to view image in full size

![]()

After this I prepared a report to submit to the program. and after few days I got a reply from the program manager.

Press enter or click to view image in full size

![]()

The report considers as duplicate of a 2024 report submitted by someone else on the platform.

Thank you for reading if you enjoy it clap 50 times

New articles Dropping soon

**Connect with me**
**Linkedin**: <https://www.linkedin.com/in/jeet-pal-22601a290/>
**Instagram:** <https://www.instagram.com/jeetpal.2007/>
**X/Twitter:** <https://x.com/Mr_mars_hacker>

[Bugbounty Writeup](https://medium.com/tag/bugbounty-writeup?source=post_page-----36f640760451---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----36f640760451---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----36f640760451---------------------------------------)

[Bug Bounty Hunter](https://medium.com/tag/bug-bounty-hunter?source=post_page-----36f640760451---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----36f640760451---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--36f640760451---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--36f640760451---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--36f640760451---------------------------------------)

[86K followers](/followers?source=post_page---post_publication_info--36f640760451---------------------------------------)

·[Last published 1 day ago](/i-stopped-trying-to-learn-everything-in-cybersecurity-d07449cee5e6?source=post_page---post_publication_info--36f640760451---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*3UJihM4VvA-DeZOgGnYqLg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--36f640760451---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*3UJihM4VvA-DeZOgGnYqLg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--36f640760451---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--36f640760451---------------------------------------)

[2.4K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--36f640760451---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--36f640760451---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com

[Help](https://help.medium.com/hc/en-us?source=post_page-----36f640760451---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----36f640760451---------------------------------------)

[About](https://medium.com/about?...
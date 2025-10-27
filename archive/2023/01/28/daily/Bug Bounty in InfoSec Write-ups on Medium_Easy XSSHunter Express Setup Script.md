---
title: Easy XSSHunter Express Setup Script
url: https://infosecwriteups.com/easy-xsshunter-express-setup-script-d5a66039f7b6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-28
fetch_date: 2025-10-04T05:03:14.355075
---

# Easy XSSHunter Express Setup Script

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd5a66039f7b6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Feasy-xsshunter-express-setup-script-d5a66039f7b6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Feasy-xsshunter-express-setup-script-d5a66039f7b6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d5a66039f7b6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d5a66039f7b6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Easy XSSHunter Express Setup Script

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:64:64/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---byline--d5a66039f7b6---------------------------------------)

[Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---byline--d5a66039f7b6---------------------------------------)

3 min read

·

Jan 14, 2023

--

1

Share

Recently XSSHunter.com decided to stop signups and soon stopping its services. You’ll need to host your own version of XSSHunter. I wrote an [article](https://adamjsturge.medium.com/xss-hunter-slack-alerts-c2c778a1da3f?sk=ca03c42e5883340ffaf1f7dc9de7d3c1) about my fork of XSSHunter Express. Since making that article I wanted to make the process of setting up XSSHunter easier so I made a script for it. I’ll be referencing my repo <https://github.com/adamjsturge/easy-xsshunter-express> throughout this article.

Note: Discord Integration was recently added and is included in the new setup script. I wrote a more in-depth write up below

[## Easy XSSHunter Discord Alerts

### This will be a setup guide for XSSHunter and integrating it with Discord

adamjsturge.medium.com](https://adamjsturge.medium.com/easy-xsshunter-discord-alerts-33fcff24a8f7?source=post_page-----d5a66039f7b6---------------------------------------)

Press enter or click to view image in full size

![]()

Easy XSSHunter Express Running

Before we get started, you’ll need a VPS. I recommend [VPSCheap](https://crm.vpscheap.net/aff.php?aff=27) and [Digital Ocean](https://m.do.co/c/a165a29be76c). You’ll also need a domain/subdomain that points to your VPS's IP.

### Installation

First step is to grab the script for Github.

```
curl -fsSL https://raw.githubusercontent.com/adamjsturge/easy-xsshunter-express/master/easy-xsshunter-express.sh -o easy-xsshunter-express.sh
```

Once we grab the script, we are going to run it with bash.

```
sudo bash easy-xsshunter-express.sh
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d5a66039f7b6---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d5a66039f7b6---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d5a66039f7b6---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d5a66039f7b6---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--d5a66039f7b6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:96:96/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--d5a66039f7b6---------------------------------------)

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:128:128/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--d5a66039f7b6---------------------------------------)

[## Written by Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---post_author_info--d5a66039f7b6---------------------------------------)

[369 followers](https://adamjsturge.medium.com/followers?source=post_page---post_author_info--d5a66039f7b6---------------------------------------)

·[21 following](https://medium.com/%40adamjsturge/following?source=post_page---post_author_info--d5a66039f7b6---------------------------------------)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d5a66039f7b6---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d5a66039f7b6---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d5a66039f7b6---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d5a66039f7b6---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d5a66039f7b6---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d5a66039f7b6---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d5a66039f7b6---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d5a66039f7b6---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d5a66039f7b6---------------------------------------)
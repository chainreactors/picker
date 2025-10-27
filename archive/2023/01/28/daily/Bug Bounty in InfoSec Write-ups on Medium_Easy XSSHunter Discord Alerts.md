---
title: Easy XSSHunter Discord Alerts
url: https://infosecwriteups.com/easy-xsshunter-discord-alerts-33fcff24a8f7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-28
fetch_date: 2025-10-04T05:03:11.862562
---

# Easy XSSHunter Discord Alerts

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F33fcff24a8f7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Feasy-xsshunter-discord-alerts-33fcff24a8f7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Feasy-xsshunter-discord-alerts-33fcff24a8f7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-33fcff24a8f7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-33fcff24a8f7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Easy XSSHunter Discord Alerts

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:64:64/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---byline--33fcff24a8f7---------------------------------------)

[Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---byline--33fcff24a8f7---------------------------------------)

2 min read

·

Jan 19, 2023

--

Share

This will be a setup guide for XSSHunter and integrating it with Discord Alerts. This will be very similar to [my other article](https://adamjsturge.medium.com/easy-xsshunter-express-setup-script-d5a66039f7b6?sk=52394aa4a2d66779ffcaeaf7cab63af9) but with more details

Press enter or click to view image in full size

![]()

XSSHunter Discord Alert

## Installation

The first step is to download the Github script.

```
curl -fsSL https://raw.githubusercontent.com/adamjsturge/easy-xsshunter-express/master/easy-xsshunter-express.sh -o easy-xsshunter-express.sh
```

Once we grab the script, we are going to run it with bash.

```
sudo bash easy-xsshunter-express.sh
```

## Script Setup Tutorial

You will first be prompted if you want to install Docker or not with the script. It’s easy to abort the Docker install, so don’t be afraid to try anything.

Press enter or click to view image in full size

![]()

XSSHunter Discord Alerts Terminal Setup

After Docker, pick the second option for my fork ([github repository](https://github.com/adamjsturge/xsshunter-express)). Since this is for my personal XSSHunter setup, I am going to say no to email and slack notifications but yes to discord notifications.

To get your webhook from Discord, you need to have your own Discord server and channel. By clicking Edit Channel, you can make the discord channel private. That webhook URL will be used…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--33fcff24a8f7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--33fcff24a8f7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--33fcff24a8f7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--33fcff24a8f7---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--33fcff24a8f7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:96:96/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--33fcff24a8f7---------------------------------------)

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:128:128/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--33fcff24a8f7---------------------------------------)

[## Written by Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---post_author_info--33fcff24a8f7---------------------------------------)

[369 followers](https://adamjsturge.medium.com/followers?source=post_page---post_author_info--33fcff24a8f7---------------------------------------)

·[21 following](https://medium.com/%40adamjsturge/following?source=post_page---post_author_info--33fcff24a8f7---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----33fcff24a8f7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----33fcff24a8f7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----33fcff24a8f7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----33fcff24a8f7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----33fcff24a8f7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----33fcff24a8f7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----33fcff24a8f7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----33fcff24a8f7---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----33fcff24a8f7---------------------------------------)
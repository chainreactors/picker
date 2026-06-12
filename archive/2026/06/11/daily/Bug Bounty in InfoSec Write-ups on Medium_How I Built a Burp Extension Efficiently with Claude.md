---
title: How I Built a Burp Extension Efficiently with Claude
url: https://infosecwriteups.com/how-i-built-a-burp-extension-efficiently-with-claude-85d43817b8f3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-11
fetch_date: 2026-06-12T06:26:10.079761
---

# How I Built a Burp Extension Efficiently with Claude

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-built-a-burp-extension-efficiently-with-claude-85d43817b8f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-built-a-burp-extension-efficiently-with-claude-85d43817b8f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-85d43817b8f3---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-85d43817b8f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# How I Built a Burp Extension Efficiently with Claude

[![Raymond Van Wart](https://miro.medium.com/v2/resize:fill:64:64/1*cjzkobnZF74HU2WAYmDr7g.jpeg)](https://raymondv.medium.com/?source=post_page---byline--85d43817b8f3---------------------------------------)

[Raymond Van Wart](https://raymondv.medium.com/?source=post_page---byline--85d43817b8f3---------------------------------------)

3 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D85d43817b8f3&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-built-a-burp-extension-efficiently-with-claude-85d43817b8f3&source=---header_actions--85d43817b8f3---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

The hardest part of building a Burp extension used to be the code — now it’s just coming up with the idea.

I recently used Claude to create a [Burp Extension](https://github.com/Raymond-JV/header-hunter) that highlights nonstandard HTTP Headers to help security researchers identify potential vectors for injection.

## Get Raymond Van Wart’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

Simply prompting Claude gave inspiration for the extension. I learned that common HTTP headers exist in the **IANA** registry and can be used as a filter.

Press enter or click to view image in full size

![]()

Brainstorming an idea

A few simple prompts allowed Claude to build a prototype from scratch.

Press enter or click to view image in full size

![]()

Claude suggests using **Montoya API**, the newer extension framework from Portswigger.

Press enter or click to view image in full size

![]()

Creating a prototype

Press enter or click to view image in full size

![]()

Highlighted requests

Ironically, the final 20% of fine tuning took the longest time. I simply suggested small features and implemented them gradually until the project was finished.

Press enter or click to view image in full size

![]()

Adding a configuration tab

Press enter or click to view image in full size

![]()

Configuration Tab

Press enter or click to view image in full size

![]()

Including support for adding and removing wordlists

Press enter or click to view image in full size

![]()

Updated repository

Press enter or click to view image in full size

![]()

Including regex patterns in filter

Press enter or click to view image in full size

![]()

Updated configuration

Building this extension with Claude was fast and fun. It felt like I was having a conversation most of the time.

Though, a word of caution, near the end I did encounter a few bugs that Claude couldn’t resolve. It is important that you know how to code well and are capable of manual analysis else you will hit a brick wall when things become too complex.

[Raymond-JV/header-hunter: Burp Suite extension that automatically flags non-standard HTTP headers in proxy traffic, helping you spot custom application headers that may reveal internal infrastructure, debug endpoints, or attack surface.](https://github.com/Raymond-JV/header-hunter)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----85d43817b8f3---------------------------------------)

[Web Application Security](https://medium.com/tag/web-application-security?source=post_page-----85d43817b8f3---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----85d43817b8f3---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----85d43817b8f3---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--85d43817b8f3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--85d43817b8f3---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--85d43817b8f3---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--85d43817b8f3---------------------------------------)

·[Last published 11 hours ago](/chaining-stored-xss-and-csrf-in-typemill-cms-a-deep-dive-into-attribute-injection-909d20edf903?source=post_page---post_publication_info--85d43817b8f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Raymond Van Wart](https://miro.medium.com/v2/resize:fill:96:96/1*cjzkobnZF74HU2WAYmDr7g.jpeg)](https://raymondv.medium.com/?source=post_page---post_author_info--85d43817b8f3---------------------------------------)

[![Raymond Van Wart](https://miro.medium.com/v2/resize:fill:128:128/1*cjzkobnZF74HU2WAYmDr7g.jpeg)](https://raymondv.medium.com/?source=post_page---post_author_info--85d43817b8f3---------------------------------------)

[## Written by Raymond Van Wart](https://raymondv.medium.com/?source=post_page---post_author_info--85d43817b8f3---------------------------------------)

[131 followers](https://raymondv.medium.com/followers?source=post_page---post_author_info--85d43817b8f3---------------------------------------)

·[9 following](https://medium.com/%40raymondv/following?source=post_page---post_author_info--85d43817b8f3---------------------------------------)

Bypassing security is fun.

[Help](https://help.medium.com/hc/en-us?source=post_page-----85d43817b8f3---------------------------------------)

...
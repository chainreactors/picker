---
title: How I Found an Exposed User Database via an Unprotected API (And How to Prevent It) in a private…
url: https://infosecwriteups.com/how-i-found-an-exposed-user-database-via-an-unprotected-api-and-how-to-prevent-it-in-a-private-77dd95a1101c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-11
fetch_date: 2025-10-02T19:57:44.815079
---

# How I Found an Exposed User Database via an Unprotected API (And How to Prevent It) in a private…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F77dd95a1101c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-exposed-user-database-via-an-unprotected-api-and-how-to-prevent-it-in-a-private-77dd95a1101c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-exposed-user-database-via-an-unprotected-api-and-how-to-prevent-it-in-a-private-77dd95a1101c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-77dd95a1101c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-77dd95a1101c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Found an Exposed User Database via an Unprotected API (And How to Prevent It) in a private bug bounty program

[![Be nice insabat](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*4PbEBGv0pYv2HfgQ)](https://medium.com/%40InsbatArshad?source=post_page---byline--77dd95a1101c---------------------------------------)

[Be nice insabat](https://medium.com/%40InsbatArshad?source=post_page---byline--77dd95a1101c---------------------------------------)

3 min read

·

Aug 31, 2025

--

1

Share

Assalam o alaikum for muslim brothers, sisters and hello for non muslims, i hope all of you are doing well and learning new things day by day.

i am back with another intresting finding story for increasing my following and for sharing my journey so without wasting any time lets start the main story

FREE LINK [https://medium.com/@InsbatArshad/how-i-found-an-exposed-user-database-via-an-unprotected-api-and-how-to-prevent-it-in-a-private-77dd95a1101c?sk=a46bb029e1d56ceac6aac98a70c20b8c](https://medium.com/%40InsbatArshad/how-i-found-an-exposed-user-database-via-an-unprotected-api-and-how-to-prevent-it-in-a-private-77dd95a1101c?sk=a46bb029e1d56ceac6aac98a70c20b8c)

## The Discovery: An Open Door to Sensitive Data

During a routine security assessment, Using ffuf I encountered an unauthenticated Django REST API endpoint at `api.example.com/user/`. To my surprise, it returned:

json { “count”: 150, “results”: [ { “email”: “admin@example.com”, “password”: “pbkdf2\_sha256$…”, “role”: “superuser” }, … ] }

Over 150 user records — including hashed passwords, emails, and roles — were publicly accessible. This wasn’t just a misconfiguration; it was a goldmine for attackers.

Command i used is

ffuf -u [https://exampe.target.com/FUZZ](https://uatportal.optimuscards.com/U.CSS.DCG/FUZZ) -w /usr/share/wordlists/dirb/common.txt -mc 200,302

FFUF is a powerfull tool and dont forget to test every subdomain with this, sometimes it is boring and time…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--77dd95a1101c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--77dd95a1101c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--77dd95a1101c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--77dd95a1101c---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--77dd95a1101c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Be nice insabat](https://miro.medium.com/v2/resize:fill:96:96/0*4PbEBGv0pYv2HfgQ)](https://medium.com/%40InsbatArshad?source=post_page---post_author_info--77dd95a1101c---------------------------------------)

[![Be nice insabat](https://miro.medium.com/v2/resize:fill:128:128/0*4PbEBGv0pYv2HfgQ)](https://medium.com/%40InsbatArshad?source=post_page---post_author_info--77dd95a1101c---------------------------------------)

[## Written by Be nice insabat](https://medium.com/%40InsbatArshad?source=post_page---post_author_info--77dd95a1101c---------------------------------------)

[297 followers](https://medium.com/%40InsbatArshad/followers?source=post_page---post_author_info--77dd95a1101c---------------------------------------)

·[106 following](https://medium.com/%40InsbatArshad/following?source=post_page---post_author_info--77dd95a1101c---------------------------------------)

penetration tester, ethical hacker, bug bounty hunter...

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----77dd95a1101c---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----77dd95a1101c---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----77dd95a1101c---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----77dd95a1101c---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----77dd95a1101c---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----77dd95a1101c---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----77dd95a1101c---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----77dd95a1101c---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----77dd95a1101c---------------------------------------)
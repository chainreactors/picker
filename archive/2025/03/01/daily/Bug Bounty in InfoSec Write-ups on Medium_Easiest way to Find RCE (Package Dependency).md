---
title: Easiest way to Find RCE (Package Dependency)
url: https://infosecwriteups.com/easiest-way-to-find-rce-package-dependency-d32efc70f2bf?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-03-01
fetch_date: 2025-10-06T21:57:41.919824
---

# Easiest way to Find RCE (Package Dependency)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd32efc70f2bf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Feasiest-way-to-find-rce-package-dependency-d32efc70f2bf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Feasiest-way-to-find-rce-package-dependency-d32efc70f2bf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d32efc70f2bf---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d32efc70f2bf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Easiest way to Find RCE (Package Dependency)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--d32efc70f2bf---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--d32efc70f2bf---------------------------------------)

4 min read

·

Jan 18, 2024

--

1

Share

[**Free Article**](https://medium.com/%40jeetpal2007/easiest-way-to-find-rce-package-dependency-d32efc70f2bf?sk=49407366f7d1616155408794a169672d)

Hello

Today I will show you the easiest way to find RCE via Package Dependency Confusion

Let’s Start

Requirements

* [RepoDownloader](https://github.com/jeetpal2007/Repodownloader)
* [RCE\_CODE](https://github.com/jeetpal2007/RCECODE)
* Burpsuite collaborator / [webhook](http://webhook.site/)
* [Nuclei](https://github.com/projectdiscovery/nuclei)
* [httpx](https://www.kali.org/tools/httpx-toolkit/)
* [subfinder](https://github.com/projectdiscovery/subfinder)
* [Nuclei-template](https://github.com/projectdiscovery/nuclei-templates/blob/83ce809e8d427d485f3e0f787886c0eb938736a6/exposures/configs/package-json.yaml)
* Remember when use RepoDownloader always use organization

> First let try this on a target name “target” and try 2 ways to find it

Way №1

First We need to find subdomains using subfinder

```
subfinder -d target.com -v -o target_subdomains.txt
```

Commands

* -d : Define the domain
* -v : verbose result
* -o : Output file name

Now use httpx

```
cat target_subdomains.txt | httpx-toolkit > Out_put_File_of_httpx.txt
```

Now use nuclei

```
nuclei -l Out_put_File_of_httpx.txt -t nuclei-templates/http/exposures/configs/package-json.yaml -o packages.txt -v
```

Commands

* -l : Define file name where subdomains are stored
* -t : Template name
* -o : Define output For it

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d32efc70f2bf---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d32efc70f2bf---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d32efc70f2bf---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d32efc70f2bf---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--d32efc70f2bf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--d32efc70f2bf---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--d32efc70f2bf---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--d32efc70f2bf---------------------------------------)

[2.3K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--d32efc70f2bf---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--d32efc70f2bf---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d32efc70f2bf---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d32efc70f2bf---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d32efc70f2bf---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d32efc70f2bf---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d32efc70f2bf---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d32efc70f2bf---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d32efc70f2bf---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d32efc70f2bf---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d32efc70f2bf---------------------------------------)
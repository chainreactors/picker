---
title: XXE with ChatGPT
url: https://infosecwriteups.com/xxe-with-chatgpt-3e4aa7c4b9c9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-14
fetch_date: 2025-10-04T09:28:48.550640
---

# XXE with ChatGPT

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F3e4aa7c4b9c9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxxe-with-chatgpt-3e4aa7c4b9c9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxxe-with-chatgpt-3e4aa7c4b9c9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-3e4aa7c4b9c9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-3e4aa7c4b9c9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# XXE with ChatGPT

## Generate Custom XXE Payloads with AI

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:64:64/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---byline--3e4aa7c4b9c9---------------------------------------)

[Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---byline--3e4aa7c4b9c9---------------------------------------)

3 min read

·

Mar 13, 2023

--

Share

![]()

**XXE** (XML External Entity) is a type of vulnerability that allows attackers to inject malicious **XML** code into an application. The following [**ChatGPT**](https://chat.openai.com/) prompts can make it easy to generate payloads for bug bounty and penetration testing.

### 1. Basic XXE

To get started, let’s start with a basic XXE payload customized for the particular XML structure used by the target web app.

**Prompt:**

> Provide an example of a safe XXE payload that you can use for testing purposes for a blind XXE PoC that uses `<burp collaborator>` for the domain for the following `.xml` file and maintain the structure of the XML content:
>
> `<insert XML>`

Press enter or click to view image in full size

![]()

**How it works:**

1. The XML document declares a new entity called `xxe` that points to a resource on the Burp Collaborator server.
2. The document then references this entity in a child element.
3. When the application parses the document, it will attempt to fetch the resource, which can be used to detect XXE vulnerabilities.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--3e4aa7c4b9c9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--3e4aa7c4b9c9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--3e4aa7c4b9c9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--3e4aa7c4b9c9---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--3e4aa7c4b9c9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:96:96/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--3e4aa7c4b9c9---------------------------------------)

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:128:128/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--3e4aa7c4b9c9---------------------------------------)

[## Written by Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---post_author_info--3e4aa7c4b9c9---------------------------------------)

[2.3K followers](https://taksec.medium.com/followers?source=post_page---post_author_info--3e4aa7c4b9c9---------------------------------------)

·[768 following](https://medium.com/%40taksec/following?source=post_page---post_author_info--3e4aa7c4b9c9---------------------------------------)

Pentester | Bug Bounty Hunter | AI Red Team <https://twitter.com/TakSec>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----3e4aa7c4b9c9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----3e4aa7c4b9c9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----3e4aa7c4b9c9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----3e4aa7c4b9c9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----3e4aa7c4b9c9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----3e4aa7c4b9c9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----3e4aa7c4b9c9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----3e4aa7c4b9c9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----3e4aa7c4b9c9---------------------------------------)
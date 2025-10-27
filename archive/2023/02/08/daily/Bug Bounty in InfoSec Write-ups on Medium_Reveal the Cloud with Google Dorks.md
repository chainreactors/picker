---
title: Reveal the Cloud with Google Dorks
url: https://infosecwriteups.com/uncover-hidden-gems-in-the-cloud-with-google-dorks-8621e56a329d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-08
fetch_date: 2025-10-04T05:58:01.187306
---

# Reveal the Cloud with Google Dorks

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8621e56a329d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funcover-hidden-gems-in-the-cloud-with-google-dorks-8621e56a329d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funcover-hidden-gems-in-the-cloud-with-google-dorks-8621e56a329d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8621e56a329d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8621e56a329d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Reveal the Cloud with Google Dorks

## Find sensitive data in Amazon AWS, Google Cloud, and more

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:64:64/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---byline--8621e56a329d---------------------------------------)

[Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---byline--8621e56a329d---------------------------------------)

3 min read

·

Feb 7, 2023

--

1

Share

![]()

Special Google searches called **“dorks”** can be used to reveal sensitive data and identify targets for **bug bounty** hunting and **penetration testing**.

## Cloud Storage Dorks

Cloud storage services like **Amazon S3**, **Microsoft Azure Blob Storage**, **Google Cloud**, and **Google Drive** can often contain sensitive information.

To find buckets and sensitive data, use the following dorks:

```
site:s3.amazonaws.com "example.com"
site:blob.core.windows.net "example.com"
site:googleapis.com "example.com"
site:drive.google.com "example.com"
```

Press enter or click to view image in full size

![]()

Add terms like `confidential`, `privileged`, `not for public release` to narrow your results.

## Bug Bounty Dorks

To find **Bug Bounty programs** and **Vulnerability Disclosure Programs** (VDPs), use the following dork:

```
"submit vulnerability report" | "powered by bugcrowd" | "powered by hackerone"
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8621e56a329d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8621e56a329d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8621e56a329d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8621e56a329d---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--8621e56a329d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:96:96/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--8621e56a329d---------------------------------------)

[![Mike Takahashi (TakSec)](https://miro.medium.com/v2/resize:fill:128:128/1*oeaksoi-GPEkdXjmR0uMFA.jpeg)](https://taksec.medium.com/?source=post_page---post_author_info--8621e56a329d---------------------------------------)

[## Written by Mike Takahashi (TakSec)](https://taksec.medium.com/?source=post_page---post_author_info--8621e56a329d---------------------------------------)

[2.3K followers](https://taksec.medium.com/followers?source=post_page---post_author_info--8621e56a329d---------------------------------------)

·[768 following](https://medium.com/%40taksec/following?source=post_page---post_author_info--8621e56a329d---------------------------------------)

Pentester | Bug Bounty Hunter | AI Red Team <https://twitter.com/TakSec>

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----8621e56a329d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8621e56a329d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8621e56a329d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8621e56a329d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8621e56a329d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----8621e56a329d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----8621e56a329d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----8621e56a329d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----8621e56a329d---------------------------------------)
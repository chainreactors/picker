---
title: Docker/Kubernetes (K8s)Penetration Testing Checklist
url: https://infosecwriteups.com/docker-kubernetes-k8s-penetration-testing-checklist-4d0a13c38495?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-05
fetch_date: 2025-10-06T19:37:28.539997
---

# Docker/Kubernetes (K8s)Penetration Testing Checklist

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4d0a13c38495&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdocker-kubernetes-k8s-penetration-testing-checklist-4d0a13c38495&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdocker-kubernetes-k8s-penetration-testing-checklist-4d0a13c38495&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4d0a13c38495---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4d0a13c38495---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Docker/Kubernetes (K8s)Penetration Testing Checklist

## **Docker/Kubernetes (K8s) Penetration Testing** involves identifying and assessing security vulnerabilities within containerized environments to ensure that they are secure against potential threats. These technologies are widely used for deploying, scaling, and managing applications. Their complexity, however, can introduce security risks if not configured properly.

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:64:64/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---byline--4d0a13c38495---------------------------------------)

[Ajay Naik](https://medium.com/%40ajaynaikhack?source=post_page---byline--4d0a13c38495---------------------------------------)

14 min read

·

Dec 3, 2024

--

Share

Press enter or click to view image in full size

![]()

==========================================================

## **Test Case 1: Verify Docker Container Privilege Escalation**

* **Description:** Test for the ability to escalate privileges within a Docker container.
* **Test Steps:**

1. Deploy a container with a standard user account.
2. Attempt to access /etc/shadow or modify system-level files.
3. Execute a container escape exploit (e.g., mounting the host file system inside the container).

* **Expected Result:**
* The container should not allow privilege escalation.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4d0a13c38495---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4d0a13c38495---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4d0a13c38495---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4d0a13c38495---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--4d0a13c38495---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:96:96/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--4d0a13c38495---------------------------------------)

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:128:128/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--4d0a13c38495---------------------------------------)

[## Written by Ajay Naik](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--4d0a13c38495---------------------------------------)

[313 followers](https://medium.com/%40ajaynaikhack/followers?source=post_page---post_author_info--4d0a13c38495---------------------------------------)

·[276 following](https://medium.com/%40ajaynaikhack/following?source=post_page---post_author_info--4d0a13c38495---------------------------------------)

Cyber security Expert with a Strong Focus on Penetration Testing, Threat Intelligence, and Bug Bounty Hunting.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----4d0a13c38495---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4d0a13c38495---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4d0a13c38495---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4d0a13c38495---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4d0a13c38495---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4d0a13c38495---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4d0a13c38495---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4d0a13c38495---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4d0a13c38495---------------------------------------)
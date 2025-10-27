---
title: Thunder CTF Walkthrough — Part 1
url: https://blog.appsecco.com/thunder-ctf-walkthrough-part-1-a17ab0012755?source=rss----e2adb3957733---4
source: Appsecco - Medium
date: 2023-02-24
fetch_date: 2025-10-04T08:00:56.149245
---

# Thunder CTF Walkthrough — Part 1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa17ab0012755&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.appsecco.com%2Fthunder-ctf-walkthrough-part-1-a17ab0012755&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.appsecco.com%2Fthunder-ctf-walkthrough-part-1-a17ab0012755&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Appsecco](https://blog.appsecco.com/?source=post_page---publication_nav-e2adb3957733-a17ab0012755---------------------------------------)

·

Follow publication

[![Appsecco](https://miro.medium.com/v2/resize:fill:76:76/1*-ERVMgF2P005dtPsm5nIqw.jpeg)](https://blog.appsecco.com/?source=post_page---post_publication_sidebar-e2adb3957733-a17ab0012755---------------------------------------)

Blog posts from the Security Testing Teams and DevSecOps Teams at Appsecco. Covering security around applications, Cloud environments like AWS, Azure, GCP, Kubernetes, Docker. Covering DevSecOps topics such as Secrets Management, Secure CI/CD Pipelines and more

Follow publication

Member-only story

# Thunder CTF Walkthrough — Part 1

[![Saumya Kasthuri](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*dIhpElR-5ASL5f2p)](https://medium.com/%40srkasthuri?source=post_page---byline--a17ab0012755---------------------------------------)

[Saumya Kasthuri](https://medium.com/%40srkasthuri?source=post_page---byline--a17ab0012755---------------------------------------)

6 min read

·

Feb 22, 2023

--

1

Share

Press enter or click to view image in full size

![]()

Image captured by me in last monsoon.

[Thunder CTF](https://thunder-ctf.cloud/) is a fantastic opportunity to challenge your skills, expand your knowledge, and test your understanding of GCP security. The competition is designed to simulate real-world scenarios, so the challenges you’ll face will be similar to the types of security issues that you might encounter in a real-world environment.

In this blog series, I’ll be covering each of the challenges presented in the Thunder CTF, and providing step-by-step solutions to help you complete each challenge successfully.

In part 1, I’ll be covering first 2 levels:

**Level 1 : Find the secret from the file stored in storage bucket**

**Level 2 : Find the credit card details of the specified user**

For set-up related details please have a look at <https://thunder-ctf.cloud/>

So, let’s get started and dive into the world of GCP security with the Thunder CTF challenges!

## **Level 1: Find the secret from the file stored in storage bucket**

Level 1 involves finding a secret that has been stored in a file in a Google Cloud Storage bucket. In this challenge, we have to access the contents of the storage bucket and locate the secret file within it.

--

--

1

[![Appsecco](https://miro.medium.com/v2/resize:fill:96:96/1*-ERVMgF2P005dtPsm5nIqw.jpeg)](https://blog.appsecco.com/?source=post_page---post_publication_info--a17ab0012755---------------------------------------)

[![Appsecco](https://miro.medium.com/v2/resize:fill:128:128/1*-ERVMgF2P005dtPsm5nIqw.jpeg)](https://blog.appsecco.com/?source=post_page---post_publication_info--a17ab0012755---------------------------------------)

Follow

[## Published in Appsecco](https://blog.appsecco.com/?source=post_page---post_publication_info--a17ab0012755---------------------------------------)

[1.8K followers](/followers?source=post_page---post_publication_info--a17ab0012755---------------------------------------)

·[Last published Mar 26, 2024](/backdooring-amis-for-fun-and-profit-e5a02f256983?source=post_page---post_publication_info--a17ab0012755---------------------------------------)

Blog posts from the Security Testing Teams and DevSecOps Teams at Appsecco. Covering security around applications, Cloud environments like AWS, Azure, GCP, Kubernetes, Docker. Covering DevSecOps topics such as Secrets Management, Secure CI/CD Pipelines and more

Follow

[![Saumya Kasthuri](https://miro.medium.com/v2/resize:fill:96:96/0*dIhpElR-5ASL5f2p)](https://medium.com/%40srkasthuri?source=post_page---post_author_info--a17ab0012755---------------------------------------)

[![Saumya Kasthuri](https://miro.medium.com/v2/resize:fill:128:128/0*dIhpElR-5ASL5f2p)](https://medium.com/%40srkasthuri?source=post_page---post_author_info--a17ab0012755---------------------------------------)

[## Written by Saumya Kasthuri](https://medium.com/%40srkasthuri?source=post_page---post_author_info--a17ab0012755---------------------------------------)

[250 followers](https://medium.com/%40srkasthuri/followers?source=post_page---post_author_info--a17ab0012755---------------------------------------)

·[31 following](https://medium.com/%40srkasthuri/following?source=post_page---post_author_info--a17ab0012755---------------------------------------)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----a17ab0012755---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a17ab0012755---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a17ab0012755---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a17ab0012755---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a17ab0012755---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a17ab0012755---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a17ab0012755---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a17ab0012755---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a17ab0012755---------------------------------------)
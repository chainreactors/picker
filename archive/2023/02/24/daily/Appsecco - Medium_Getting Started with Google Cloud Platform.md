---
title: Getting Started with Google Cloud Platform
url: https://blog.appsecco.com/getting-started-with-google-cloud-platform-410bb6145958?source=rss----e2adb3957733---4
source: Appsecco - Medium
date: 2023-02-24
fetch_date: 2025-10-04T08:00:53.239146
---

# Getting Started with Google Cloud Platform

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F410bb6145958&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.appsecco.com%2Fgetting-started-with-google-cloud-platform-410bb6145958&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.appsecco.com%2Fgetting-started-with-google-cloud-platform-410bb6145958&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Appsecco](https://blog.appsecco.com/?source=post_page---publication_nav-e2adb3957733-410bb6145958---------------------------------------)

·

Follow publication

[![Appsecco](https://miro.medium.com/v2/resize:fill:76:76/1*-ERVMgF2P005dtPsm5nIqw.jpeg)](https://blog.appsecco.com/?source=post_page---post_publication_sidebar-e2adb3957733-410bb6145958---------------------------------------)

Blog posts from the Security Testing Teams and DevSecOps Teams at Appsecco. Covering security around applications, Cloud environments like AWS, Azure, GCP, Kubernetes, Docker. Covering DevSecOps topics such as Secrets Management, Secure CI/CD Pipelines and more

Follow publication

Member-only story

# Getting Started with Google Cloud Platform

[![Saumya Kasthuri](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*dIhpElR-5ASL5f2p)](https://medium.com/%40srkasthuri?source=post_page---byline--410bb6145958---------------------------------------)

[Saumya Kasthuri](https://medium.com/%40srkasthuri?source=post_page---byline--410bb6145958---------------------------------------)

6 min read

·

Feb 21, 2023

--

Share

Press enter or click to view image in full size

![]()

Google Cloud Platform is a cloud-based computing platform that offers a variety of services for businesses and individuals, including computing, storage, and big data analytics.

In this blog, I will be diving into the process of creating a Google Cloud Platform (GCP) account and getting familiar with the gcloud command-line interface (CLI).

**Table of Contents**

1. Setting up a GCP account
2. Command line Tools : gcloud & gsutil
3. gsutil for Google Cloud Storage
4. gcloud — multi-purpose command-line tool
5. Configuring the gcloud CLI
6. Common gcloud CLI Commands
7. Common gsutil Commands

## Setting up a GCP account

1. Open [Google Cloud console](https://console.cloud.google.com/?_ga=2.89021723.1834943347.1674046608-1841177426.1672911538&_gac=1.27428430.1673234979.CjwKCAiA8OmdBhAgEiwAShr4072mcUcVrBUOqb-fl_ArUCgIaeIJiqpBPc-Clqu8_8RuyNcr4iVi7RoCs5UQAvD_BwE) in a browser.
2. When prompted to sign in, create a new account by clicking **Create account**:
3. Follow the instructions to register your corporate email address as a [Google account](https://support.google.com/accounts/answer/27441). Alternatively, you can use a Gmail account or other Google account.
4. Continue to the [Google Cloud console](https://console.cloud.google.com/) and accept the Google Cloud Platform terms presented.
5. Open the [Google Cloud console](https://console.cloud.google.com/) and log in with the account…

--

--

[![Appsecco](https://miro.medium.com/v2/resize:fill:96:96/1*-ERVMgF2P005dtPsm5nIqw.jpeg)](https://blog.appsecco.com/?source=post_page---post_publication_info--410bb6145958---------------------------------------)

[![Appsecco](https://miro.medium.com/v2/resize:fill:128:128/1*-ERVMgF2P005dtPsm5nIqw.jpeg)](https://blog.appsecco.com/?source=post_page---post_publication_info--410bb6145958---------------------------------------)

Follow

[## Published in Appsecco](https://blog.appsecco.com/?source=post_page---post_publication_info--410bb6145958---------------------------------------)

[1.8K followers](/followers?source=post_page---post_publication_info--410bb6145958---------------------------------------)

·[Last published Mar 26, 2024](/backdooring-amis-for-fun-and-profit-e5a02f256983?source=post_page---post_publication_info--410bb6145958---------------------------------------)

Blog posts from the Security Testing Teams and DevSecOps Teams at Appsecco. Covering security around applications, Cloud environments like AWS, Azure, GCP, Kubernetes, Docker. Covering DevSecOps topics such as Secrets Management, Secure CI/CD Pipelines and more

Follow

[![Saumya Kasthuri](https://miro.medium.com/v2/resize:fill:96:96/0*dIhpElR-5ASL5f2p)](https://medium.com/%40srkasthuri?source=post_page---post_author_info--410bb6145958---------------------------------------)

[![Saumya Kasthuri](https://miro.medium.com/v2/resize:fill:128:128/0*dIhpElR-5ASL5f2p)](https://medium.com/%40srkasthuri?source=post_page---post_author_info--410bb6145958---------------------------------------)

[## Written by Saumya Kasthuri](https://medium.com/%40srkasthuri?source=post_page---post_author_info--410bb6145958---------------------------------------)

[250 followers](https://medium.com/%40srkasthuri/followers?source=post_page---post_author_info--410bb6145958---------------------------------------)

·[31 following](https://medium.com/%40srkasthuri/following?source=post_page---post_author_info--410bb6145958---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----410bb6145958---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----410bb6145958---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----410bb6145958---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----410bb6145958---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----410bb6145958---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----410bb6145958---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----410bb6145958---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----410bb6145958---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----410bb6145958---------------------------------------)
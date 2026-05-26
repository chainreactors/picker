---
title: Testing SQL Injection Using Google gemma4:31b-cloud on PortSwigger’s Vulnerable Shop
url: https://infosecwriteups.com/testing-sql-injection-using-google-gemma4-31b-cloud-on-portswiggers-vulnerable-shop-ef9dc05dd1aa?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-25
fetch_date: 2026-05-26T06:09:36.734831
---

# Testing SQL Injection Using Google gemma4:31b-cloud on PortSwigger’s Vulnerable Shop

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftesting-sql-injection-using-google-gemma4-31b-cloud-on-portswiggers-vulnerable-shop-ef9dc05dd1aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftesting-sql-injection-using-google-gemma4-31b-cloud-on-portswiggers-vulnerable-shop-ef9dc05dd1aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ef9dc05dd1aa---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ef9dc05dd1aa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# Testing SQL Injection Using Google gemma4:31b-cloud on PortSwigger’s Vulnerable Shop

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:64:64/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---byline--ef9dc05dd1aa---------------------------------------)

[Bash Overflow](https://bashoverflow.com/?source=post_page---byline--ef9dc05dd1aa---------------------------------------)

5 min read

·

3 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Def9dc05dd1aa&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftesting-sql-injection-using-google-gemma4-31b-cloud-on-portswiggers-vulnerable-shop-ef9dc05dd1aa&source=---header_actions--ef9dc05dd1aa---------------------post_audio_button------------------)

Share

AI-assisted SQL Injection testing against a deliberately vulnerable e-commerce application.

🔓 [**Free Link**](https://bashoverflow.com/ef9dc05dd1aa?sk=5c26d628b2622cb7a14d6e14cf91f111)

Press enter or click to view image in full size

![SQL Injection Using Google gemma4]()

SQL Injection Using Google gemma4:31b-cloud

## Table of Contents

1. [**Overview**](#384b)
2. [**Proof of Concept (PoC)**](#b91b)

## Overview

SQL Injection (SQLi) remains one of the most impactful web application vulnerabilities because it allows attackers to manipulate backend database queries through unsanitized user input. In this lab, the testing environment uses the intentionally vulnerable website **ginandjuice.shop**, a training platform developed by PortSwigger specifically for practicing modern web exploitation techniques in a controlled environment.

The application simulates a realistic e-commerce platform containing multiple attack surfaces commonly found in production systems. One of the vulnerable components exposed in this lab is the **Accessories** product category, where user-controlled parameters are processed insecurely within SQL queries. This behavior creates an opportunity to test and validate SQL Injection techniques against the backend database logic.

Unlike conventional manual testing workflows, this assessment leverages **Ollama** integrated with the **Google gemma4:31b-cloud**…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ef9dc05dd1aa---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ef9dc05dd1aa---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ef9dc05dd1aa---------------------------------------)

[86K followers](/followers?source=post_page---post_publication_info--ef9dc05dd1aa---------------------------------------)

·[Last published 21 hours ago](/how-i-found-2-bugs-on-bbcs-subdomains-and-made-it-into-their-hall-of-fame-86fc4be89e68?source=post_page---post_publication_info--ef9dc05dd1aa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:96:96/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--ef9dc05dd1aa---------------------------------------)

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:128:128/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--ef9dc05dd1aa---------------------------------------)

[## Written by Bash Overflow](https://bashoverflow.com/?source=post_page---post_author_info--ef9dc05dd1aa---------------------------------------)

[427 followers](https://bashoverflow.com/followers?source=post_page---post_author_info--ef9dc05dd1aa---------------------------------------)

·[12 following](https://medium.com/%40bashoverflow/following?source=post_page---post_author_info--ef9dc05dd1aa---------------------------------------)

Cybersecurity Enthusiast | Sharing insights through some writeups | Passionate about advancing knowledge in the field of cybersecurity

[Help](https://help.medium.com/hc/en-us?source=post_page-----ef9dc05dd1aa---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ef9dc05dd1aa---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ef9dc05dd1aa---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ef9dc05dd1aa---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ef9dc05dd1aa---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ef9dc05dd1aa---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ef9dc05dd1aa---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ef9dc05dd1aa---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ef9dc05dd1aa---------------------------------------)
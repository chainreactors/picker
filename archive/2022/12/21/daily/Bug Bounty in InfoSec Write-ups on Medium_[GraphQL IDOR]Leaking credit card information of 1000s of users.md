---
title: [GraphQL IDOR]Leaking credit card information of 1000s of users
url: https://infosecwriteups.com/graphql-idor-leaking-credit-card-information-of-1000s-of-users-d07eec732979?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-21
fetch_date: 2025-10-04T02:04:58.635526
---

# [GraphQL IDOR]Leaking credit card information of 1000s of users

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd07eec732979&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgraphql-idor-leaking-credit-card-information-of-1000s-of-users-d07eec732979&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgraphql-idor-leaking-credit-card-information-of-1000s-of-users-d07eec732979&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d07eec732979---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d07eec732979---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# [GraphQL IDOR] Leaking credit card information of 1000s of users [External Audit]

[![Vipul Sahu](https://miro.medium.com/v2/resize:fill:64:64/1*s81_1pBeT2o5kQ2pvZsB6Q.jpeg)](https://medium.com/%40vipul_sahu?source=post_page---byline--d07eec732979---------------------------------------)

[Vipul Sahu](https://medium.com/%40vipul_sahu?source=post_page---byline--d07eec732979---------------------------------------)

3 min read

·

Dec 20, 2022

--

Listen

Share

Hey everyone

I was hunting on a web application. The program was private; for obvious reasons, let’s say the domain is redacted.com. I was able to find mass information by exploiting two different Graphql endpoints.

Press enter or click to view image in full size

![]()

## Finding Graphql IDOR

While performing initial recon on redacted.com, I found the web application used GraphQL for its API management.

For converting the query to a readable format, I used the graphql raider extension, which converts the graphql query and variables from the unreadable JSON body to a readable format in which the query and variables are displayed in separate tabs. Graphql raider extracted the ‘id’ variable as an insertion point. The response to this request contains users’ personal information, including credit card information.

I created two accounts and checked for IDOR. The application was vulnerable to IDOR, and I was able to get the personal information for my other account.

## Spotting a Weird functionality

ID variable is a 12-character long string, so I cannot guess/brute-force the value. I was searching for a way to get my hand on the id parameter, went through the burp suite repeater tabs, and found an exciting endpoint. The endpoint fetched my following list, and the response contains the id value and profile picture of the users I follow.

When a user creates an account on redacted.com, the user automatically follows some company executives.

When I clicked on the follower list of these executives, a graphql query was sent that fetches information from the user’s profile, and the response contains the user’s ID and profile picture of many users. I found a user with a million followers, which can also be exploited.

Press enter or click to view image in full size

![]()

## Exploitation

I collected an ‘id’ from the response of the following list of the company executive to create the POC.

Press enter or click to view image in full size

![]()

I observed no protection against brute force attacks for the graphql queries. After this, I grabbed the IDs using bash scripting and brute-forced using the burp Intruder and got thousands of users’ sensitive data.

## **Disclosure**

Reported on 26th December 2020

**Linkedin:** <https://www.linkedin.com/in/vipul-sahu-a7a420174/>

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Idor](https://medium.com/tag/idor?source=post_page-----d07eec732979---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----d07eec732979---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----d07eec732979---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----d07eec732979---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d07eec732979---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d07eec732979---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d07eec732979---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d07eec732979---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--d07eec732979---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vipul Sahu](https://miro.medium.com/v2/resize:fill:96:96/1*s81_1pBeT2o5kQ2pvZsB6Q.jpeg)](https://medium.com/%40vipul_sahu?source=post_page---post_author_info--d07eec732979---------------------------------------)

[![Vipul Sahu](https://miro.medium.com/v2/resize:fill:128:128/1*s81_1pBeT2o5kQ2pvZsB6Q.jpeg)](https://medium.com/%40vipul_sahu?source=post_page---post_author_info--d07eec732979---------------------------------------)

[## Written by Vipul Sahu](https://medium.com/%40vipul_sahu?source=post_page---post_author_info--d07eec732979---------------------------------------)

[134 followers](https://medium.com/%40vipul_sahu/followers?source=post_page---post_author_info--d07eec732979---------------------------------------)

·[2 following](https://medium.com/%40vipul_sahu/following?source=post_page---post_author_info--d07eec732979---------------------------------------)

Penetration Tester | IITJ <https://x.com/GodSpeed000123>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----d07eec732979---------------------------------------)

[Status](https://status.medium.com/?source...
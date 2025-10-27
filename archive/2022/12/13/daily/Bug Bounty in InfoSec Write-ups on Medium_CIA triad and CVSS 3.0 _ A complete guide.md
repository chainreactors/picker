---
title: CIA triad and CVSS 3.0 | A complete guide
url: https://infosecwriteups.com/cia-triad-and-cvss-3-0-a-complete-guide-91d6d63d44b0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-13
fetch_date: 2025-10-04T01:18:20.759774
---

# CIA triad and CVSS 3.0 | A complete guide

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F91d6d63d44b0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcia-triad-and-cvss-3-0-a-complete-guide-91d6d63d44b0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcia-triad-and-cvss-3-0-a-complete-guide-91d6d63d44b0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-91d6d63d44b0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-91d6d63d44b0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# CIA triad and CVSS 3.0 | A complete guide

[![Krishna Agarwal](https://miro.medium.com/v2/resize:fill:64:64/1*8OK6PdaPDW_tqCCK9QdaaA.jpeg)](https://kr1shna4garwal.medium.com/?source=post_page---byline--91d6d63d44b0---------------------------------------)

[Krishna Agarwal](https://kr1shna4garwal.medium.com/?source=post_page---byline--91d6d63d44b0---------------------------------------)

10 min read

·

Dec 11, 2022

--

2

Listen

Share

Hello folks, I am Krishna Agarwal (

[Kr1shna 4garwal](https://medium.com/u/491f9af79cca?source=post_page---user_mention--91d6d63d44b0---------------------------------------)

) from India 🇮🇳. An aspiring penetration tester and So called security researcher :)

So today I’m going to discuss about CIA triad and CVSS 3.0.

I don’t know for whom this write-up will be useful, maybe for bug hunters, developers or security professionals.

Don’t worry if you don’t know anything about CVSS and CIA, You will get familiar with it after reading and calculating score for your vulnerabilities.

Press enter or click to view image in full size

![]()

How can you imagine a write-up without banner xD

First let’s start with CIA triad:

### What is CIA triad?

The CIA triad is a model for understanding and assessing the security of computer systems. It consists of three components: **confidentiality**, **integrity**, and **availability**.

* **Confidentiality** means that only authorized parties can access the data.
* **Integrity** means that the data cannot be modified without authorization.
* **Availability** means that authorized parties can access the data when they need to.

Press enter or click to view image in full size

![]()

Examples Of Confidentiality:

use of encryption to protect data. For instance, when you send sensitive information, such as your credit card number, over the internet, it is typically encrypted using a secure protocol such as HTTPS. This encryption ensures that only the intended recipient, such as a website or online service, can read the data. Even if someone were to intercept the data as it is being transmitted, they would not be able to read it because it is encrypted. This helps to ensure the confidentiality of the data and prevent unauthorized access. Another example of confidentiality is the use of access controls to limit who can access certain data or systems. For example, a company might have a secure server that only certain employees are allowed to access. This might be achieved through the use of a login system that requires employees to enter a username and password in order to access the server. This ensures that only authorized parties can access the data on the server, protecting its confidentiality.

Example Of Integrity:

checksums to verify the integrity of a file. A checksum is a small piece of data that is derived from a larger block of data, such as a file. It is used to detect changes or modifications to the original data. When a file is transmitted over a network, the sender can compute a checksum for the file and include it with the transmission. The receiver can then compute their own checksum for the received file and compare it to the original checksum to verify that the file has not been modified in transit. If the two checksums match, it indicates that the file has not been modified and has retained its integrity. This helps to ensure the accuracy and completeness of the file, and prevents unauthorized parties from tampering with it.

Example Of Availability:

the ability of authorized users to access information and systems when they need to. This is an important aspect of cybersecurity because it ensures that users can access the information and systems they need to do their jobs and maintain the security of the network.

### CIA triad for bug bounty hunters

In the context of bug bounties, the CIA triad can be used to determine the potential impact of a vulnerability. Also, we can use CVSS 3.0 scoring system for more accurate impact. **If there is no impact on CIA triad by your vulnerability, Then that might not be an security vulnerability**. Some program may accept that as suggestion. Example: Missing security headers, Clickjacking on unauthenticated endpoints.

bug bounty hunters can better evaluate the severity of a vulnerability and the potential rewards that it may be eligible for.

First Example scenario: You found a endpoint where you are able to download some public file but there is signup or login need for downloading those public files. You just simply close that pop-up and downloaded your files.

What will be the affect on CIA triad by above scenario?

Confidentiality not effected, Because we are just downloading intended for public use files.

Integrity is not effected, Because we are just downloading files, not tempering anything.

Availability is not effected, Because we are stopping any user to access that download page.

Second Example scenario: You are found a [directory transversal](https://portswigger.net/web-security/file-path-traversal). And you are able to access the internal files of a system. In this case, Confidentiality is effected because we are able to access internal system’s files in unauthorized way. If we escalate this directory transversal to [Remote code execution](https://www.imperva.com/learn/application-security/remote-code-execution). Then all three components of CIA triad will be effected. Because we can access any files And we can delete or alter any files.

Press enter or click to view image in full size

![]()

### What is CVSS 3.0 ?

CVSS stands for **Common Vulnerability Scoring System**. It is a standardized method for evaluating the severity of vulnerabilities in a systems. The goal of CVSS is to provide a consistent, objective way of measuring the risk posed by a given vulnerability, so that organizations can prioritize their efforts to address it.

CVSS 3.0 provides a numerical score between 0 and 10 for each vulnerability, based on a number...
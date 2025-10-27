---
title: Applying Security Engineering to Make Phishing Harder - A Case Study
url: https://blog.doyensec.com/2024/09/19/phishing-case-study.html
source: Over Security - Cybersecurity news aggregator
date: 2024-09-20
fetch_date: 2025-10-06T18:29:50.021990
---

# Applying Security Engineering to Make Phishing Harder - A Case Study

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Applying Security Engineering to Make Phishing Harder - A Case Study

19 Sep 2024 - Posted by Szymon Drosdzol

# Introduction

Recently Doyensec was hired by a client offering a âCommunication Platform as a Serviceâ. This platform allows their clients to craft a customer service experience and to communicate with their own customers via a plethora of channels: email, web chats, social media and more.

While undoubtedly valuable, such a service introduces a unique threat model. Our clientâs users work with a vast amount of incoming correspondence from outside (often anonymous) users, on a daily basis. This makes them particularly vulnerable to phishing and other social engineering attacks.

While such threats cannot be fully eliminated, it is possible to minimize the possibilities for exploitation. Recognizing this, Doyensec was hired to performed a security review, specifically focused on social engineering attacks and phishing in particular. The engagement, performed earlier this year, has proven to be extremely valuable for both parties. Most importantly, our client used to the results to greatly increase their platformâs resilience against social engineering attacks. Additionally, Doyensec engineers had a great opportunity to unleash their creativity on bugs that are often overlooked, or at least heavily undervalued (looking at you, CVSS score!), during standard security audits as well as the opportunity to look at defending the application from a blue-team perspective.

The following case study will discuss some of the vulnerabilities that were addressed as part of this audit. Hopefully, this post will be useful for developers to understand what kind of vulnerabilities can be lurking in their platforms too. It also helps to demonstrate how valuable such focused engagements can be as an addition to standard web engagements.

# Attachments Handling

For any customer support organization, file attachment management is a crucial feature. On one hand, it is crucial for users to be able to share file samples, screenshots, etc. with their interlocutors. On the other hand, sharing files is always a hotbed for exploiting all manner of security bugs, especially when accepting files from untrusted parties. Therefore, hardening this part of the application will always require careful considerations as to how to ensure confidentiality and integrity without sacrificing usability.

## File Extension Restriction Bypass via Trailing Period

The tested platform employs a robust system designed to validate allowed file extensions and content types for file uploads, featuring a global ban list for inherently dangerous file types, such as executables (e.g., `.exe`). These measures are intended to prevent the uploading and distribution of potentially malicious files. However, by exploiting some browsersâ quirks, a vulnerability was discovered that allowed users to bypass these restrictions simply by appending a trailing period (âdangling dotâ) to the file extension.

It was possible to bypass this file extension restriction by crafting an upload request with a prohibited extension, such as `.exe.`. This resulted in the system accepting the file, since it ostensibly met the criteria for allowed uploads - which included an empty extension. However, Firefox and Chromium-based browsers remove the dangling dot (interestingly, Safari retains it). As a result, the file was saved with an original `.exe` extension on the victimâs filesystem:

![Dangling Dot Download Result](../../../public/images/dangling_dot.png)

The recommendation is simple here. Trailing dots should be removed from the filenames. It rarely has any use in real-world scenarios, therefore the usability tradeoff is minimal.

## Circumvention of Content Origin Restrictions via Subdomain Crafting

Platform chats have been created with a restriction, which allows link attachments from our clientâs subdomains only. This security control is designed to restrict uploads and references to images and attachments to a predefined set of origins, preventing the use of external sources that could be employed in phishing attacks. The intended validation process relies on an allowlist of domains.

However, when validating (sub)domains using regular expressions, itâs easy to forget the intricacies of this syntax, which can lead to hard-to-spot bypasses.

Doyensec observed that subdomains were matched using an `allowlist` of regular expressions similar to `/acme-attachments-1.com/`. Such a regular expression does not enforce the beginning and the end of the string and will therefore accept any domains that contain the desired subdomain. An attacker could create a subdomain similar to `acme-attachments-1.com.doyensec.com`, which would be accepted despite this security mechanism.

Another common (although not exploitable in this case) mistake is forgetting that the dot (.) character is treated as a wildcard by regular expressions. When one forgets to escape a dot in a domain regex, an attacker can register a domain which will bypass such a restriction. For instance, a regular expression similar to `downloads.acmecdn.com` would accept an attacker-controlled domain like `downloadsAacmecdn.com`.

It is worth noting that as innocuous as this vulnerability seems to be, it actually has great potential for creating successful phishing attacks. When a victim receives an attachment in a trusted platform, theyâre far more likely to follow the link. Also, a login page would not be surprising for a victim, further increasing the likelihood of them giving away their credentials.

## Antivirus Scan Bypass

The platform appropriately implements antivirus scanning on all incoming files. However, an attacker could obfuscate the true content of the payload by creating an encrypted archive: `$ zip -e test_encrypted.zip eicar.com`.

There is no simple solution to solve this issue. Banning encrypted archives altogether is a usability trade-off that might be unacceptable in some cases. Doyensec recommended clearly warning users against opening encrypted files at the very least. It might be also useful to allow the clients to choose which side of this trade-off is acceptable for them by creating a proper configuration switch.

# HTML Input Handling

When it comes to exchanging messages, it can be very useful to add formatting and give users more ways of expressing themselves. On the other hand, when messages are coming from untrusted sources, such a feature can enable attackers to craft sophisticated attacks that involve UI redressing, e.g., emulating UI elements within their messages.

Our client has found a great way to balance usability and security. While trusted users have a rich choice of input formatting options, untrusted users from outside the platform can only share basic plain-text messages. It also worth noting that even trusted users canât inject arbitrary HTML to their messages, given that HTML tags are properly parsed and encoded. There are however specific tags that are allowed and, in some cases, converted into more elaborate elements (e.g., link tags get converted into buttons).

Doyensec found this solution well-architected at the design level. However, due to an oversight in the implementation, the public messaging API also accepted a âhiddenâ (not used by the frontend) parameter which allowed some HTML elements. Doyensec was able to exploit the conversion ...
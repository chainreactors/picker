---
title: Reflected XSS on Admin Login Page
url: https://infosecwriteups.com/reflected-xss-on-admin-login-page-94960596ec88?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-22
fetch_date: 2025-10-04T10:15:30.595271
---

# Reflected XSS on Admin Login Page

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F94960596ec88&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-on-admin-login-page-94960596ec88&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-on-admin-login-page-94960596ec88&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-94960596ec88---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-94960596ec88---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Reflected XSS on Admin Login Page

[![Aswin KV](https://miro.medium.com/v2/resize:fill:64:64/1*FRePVrXU-ZBSpzBlr5sBvg.jpeg)](https://45w1nkv.medium.com/?source=post_page---byline--94960596ec88---------------------------------------)

[Aswin KV](https://45w1nkv.medium.com/?source=post_page---byline--94960596ec88---------------------------------------)

2 min read

·

Mar 21, 2023

--

Listen

Share

Hi! I’m Aswin,security researcher and a penetration tester.Here we are discussing reflected XSS in a private bug bounty program.

On the website [https://xyz.redacted.com/a6,](https://xyz.redacted.com/a6%2C) when you attempt to access secret sections,The URL on the parameter “win” redirects you to a login page with values from the URL mirrored in the DOM.

Press enter or click to view image in full size

![]()

Reflect XSS- Admin Login page

> A cross-site scripting attack might be launched against the application since there is no adequate handle for the data reflected, making it susceptible.

## What is reflected cross-site scripting?

Reflected Cross-Site Scripting occurs when the injected script is mirrored off the website, such as an error message, search result, or other response.
Reflected type assaults are given to victims or targets through another channel, such as email or phishing.
When the user is duped into clicking the malicious script or link, the browser is triggered.
The search field is a basic example of Reflected XSS.

To launch a successful Reflected XSS attack, an attacker looks for instances where user input is utilised directly to create a response.
This frequently includes the inclusion of event attributes such as onload and onmouseover to elements that are not supposed to host scripts, such as image tags (img>).

## Proof of Concept:

When you visit the current URL, an alert with your cookie will appear on the screen.

[https://xyz.redacted.com/a6/shared/popupLogin.jsp?win=%22%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E](https://td.intelliresponse.com/a6/shared/popupLogin.jsp?win=%22%3E%3Cscript%3Ealert%28document.cookie%29%3C%2Fscript%3E)

## Steps To Reproduce:

1. Navigate to [https://xyz.redacted.com/a6](https://td.intelliresponse.com/a6)
2. Now that you’ve been forwarded to the login page, look for the win parameter on the URL and replace it with some payload beginning with “>” and some text or script in front.
3. See the completed payload on your screen.

Press enter or click to view image in full size

![]()

POC

## Recommendation:

Remediation for XSS often entails cleaning data input (to ensure that no code is present), escaping all output (to ensure that data is not shown as code), and re-structuring applications such that code is loaded from well-defined destinations.

## Impact:

* Accessing sensitive data, or even gaining control of user accounts
* An attacker may create a payload to extract a user’s admin credentials or steal his session.

Happy Hacking..

[Xss Attack](https://medium.com/tag/xss-attack?source=post_page-----94960596ec88---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----94960596ec88---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----94960596ec88---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----94960596ec88---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----94960596ec88---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--94960596ec88---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--94960596ec88---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--94960596ec88---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--94960596ec88---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--94960596ec88---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aswin KV](https://miro.medium.com/v2/resize:fill:96:96/1*FRePVrXU-ZBSpzBlr5sBvg.jpeg)](https://45w1nkv.medium.com/?source=post_page---post_author_info--94960596ec88---------------------------------------)

[![Aswin KV](https://miro.medium.com/v2/resize:fill:128:128/1*FRePVrXU-ZBSpzBlr5sBvg.jpeg)](https://45w1nkv.medium.com/?source=post_page---post_author_info--94960596ec88---------------------------------------)

[## Written by Aswin KV](https://45w1nkv.medium.com/?source=post_page---post_author_info--94960596ec88---------------------------------------)

[559 followers](https://45w1nkv.medium.com/followers?source=post_page---post_author_info--94960596ec88---------------------------------------)

·[842 following](https://medium.com/%4045w1nkv/following?source=post_page---post_author_info--94960596ec88---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----94960596ec88---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----94960596ec88---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----94960596ec88-------...
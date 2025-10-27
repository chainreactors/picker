---
title: Found HTML Injection in Emails! Earned HOF
url: https://infosecwriteups.com/found-html-injection-in-emails-earned-hof-24a8a8223f29?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-22
fetch_date: 2025-10-06T20:07:13.530983
---

# Found HTML Injection in Emails! Earned HOF

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F24a8a8223f29&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffound-html-injection-in-emails-earned-hof-24a8a8223f29&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffound-html-injection-in-emails-earned-hof-24a8a8223f29&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-24a8a8223f29---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-24a8a8223f29---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 🚨 Found HTML Injection in Emails! Earned HOF 🏆

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:64:64/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---byline--24a8a8223f29---------------------------------------)

[cryptoshant🇮🇳](https://medium.com/%40dsmodi484?source=post_page---byline--24a8a8223f29---------------------------------------)

2 min read

·

Jan 20, 2025

--

3

Listen

Share

Hello Hackers, In the quick writeup I am going to disclose my recent finding of HTMLI in email in **Quickreel** through **comolho** bug bounty platform.

![]()

So, During testing the signup feature I found that **full name** field was vulnerable to HTML injection vulnerability so below are the steps how I perform the attack.

Steps to Reproduce

1. visit: [**https://app.quickreel.io/login**](https://app.quickreel.io/login)
2. Now click on **Register** button.
3. Now in name field add following payload

**Payload:**

```
<a href="https://attacker.com">
      <img src="https://shorturl.at/CsAH1" width="200">
  </a> <!--
```

4. Now enter email in which you want to execute the payload and then after entering password click on submit.

And the victim got this in their email:

Press enter or click to view image in full size

![]()

**Mitigations for HTMLI:**

1. **Sanitize User Input:** Ensure all user inputs are stripped of HTML or JavaScript before rendering in email templates. Libraries like DOMPurify can help sanitize input effectively.
2. **Encode Output:** Encode special characters in emails to prevent browser rendering.
3. **Restrict Input Fields:** Enforce character length limits and only allow plain text where HTML is unnecessary.
4. **Validate Content:** Conduct regular audits of email templates to ensure no unsafe content injection occurs.
5. **Use Security Headers:** Implement Content Security Policy (CSP) to block rendering of malicious scripts in emails.

And as expected again this report was also closed as **Duplicate 😥** but they still awarded me HOF for securing them and list my name into their bug bounty hof section 🥳.

Press enter or click to view image in full size

![]()

Rewarded HOF in Quickreel bug bounty program

I don’t know but till now none of my report was triaged! 2 are closed as Duplicates and 1 was closed as NA and 3 are still in pending from 16th Dec. I don’t know why this is happening 😕 in this platform.

> **Timeline:**
>
> **16–12–2024: Reported**
>
> **06–01–2025: Closed as Duplicate**
>
> **06–01–2025: Awarded HOF**

Thank you for reading. I will see you in next amazing one. Bye 👋

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----24a8a8223f29---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----24a8a8223f29---------------------------------------)

[HTML](https://medium.com/tag/html?source=post_page-----24a8a8223f29---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----24a8a8223f29---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----24a8a8223f29---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--24a8a8223f29---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--24a8a8223f29---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--24a8a8223f29---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--24a8a8223f29---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--24a8a8223f29---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:96:96/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---post_author_info--24a8a8223f29---------------------------------------)

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:128:128/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---post_author_info--24a8a8223f29---------------------------------------)

[## Written by cryptoshant🇮🇳](https://medium.com/%40dsmodi484?source=post_page---post_author_info--24a8a8223f29---------------------------------------)

[1.3K followers](https://medium.com/%40dsmodi484/followers?source=post_page---post_author_info--24a8a8223f29---------------------------------------)

·[55 following](https://medium.com/%40dsmodi484/following?source=post_page---post_author_info--24a8a8223f29---------------------------------------)

Ethical Hacker | Bug Hunter🐞 | Offensive Security | Student | Cybersecurity Enthusiast ⚡

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----24a8a8223f29---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----24a8a8223f29---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----24a8a8223f29---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----24a8a8223f29---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----24a8a8223f29---------------------------------...
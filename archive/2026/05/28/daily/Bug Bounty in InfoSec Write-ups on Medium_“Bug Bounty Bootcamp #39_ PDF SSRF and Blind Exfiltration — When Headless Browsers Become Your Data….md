---
title: “Bug Bounty Bootcamp #39: PDF SSRF and Blind Exfiltration — When Headless Browsers Become Your Data…
url: https://infosecwriteups.com/bug-bounty-bootcamp-39-pdf-ssrf-and-blind-exfiltration-when-headless-browsers-become-your-data-507d6543d167?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-28
fetch_date: 2026-05-29T06:04:51.185300
---

# “Bug Bounty Bootcamp #39: PDF SSRF and Blind Exfiltration — When Headless Browsers Become Your Data…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-39-pdf-ssrf-and-blind-exfiltration-when-headless-browsers-become-your-data-507d6543d167&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-39-pdf-ssrf-and-blind-exfiltration-when-headless-browsers-become-your-data-507d6543d167&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-507d6543d167---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-507d6543d167---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# “Bug Bounty Bootcamp #39: PDF SSRF and Blind Exfiltration — When Headless Browsers Become Your Data Mule”

## The invoice generator doesn’t show errors. The image fetcher hangs on invalid IPs. But with a single `<iframe>` and a JavaScript redirect, you can turn a blind SSRF into a full file read – no response needed.

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--507d6543d167---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--507d6543d167---------------------------------------)

5 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D507d6543d167&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-39-pdf-ssrf-and-blind-exfiltration-when-headless-browsers-become-your-data-507d6543d167&source=---header_actions--507d6543d167---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

[*Friend link | free link*](https://amannsharmaa.medium.com/bug-bounty-bootcamp-39-pdf-ssrf-and-blind-exfiltration-when-headless-browsers-become-your-data-507d6543d167?sk=f2df441cd2cfd39e67856be13877c621)

Welcome back. You’ve conquered SSRF with open redirects and localhost bypasses. Now we tackle the trickiest scenarios: SSRF in PDF generation where you have no direct output, and blind SSRF where the application never returns the fetched data. The solution? Inject JavaScript that forces the headless browser to exfiltrate data back to you — using `window.location`, `fetch`, and base64 encoding. This lesson will give you a repeatable playbook for turning blind SSRF into a full data extraction channel.

## The PDF Generator: A Hidden SSRF Goldmine

Many applications generate invoices, receipts, or reports as PDFs using your profile data. The server uses a headless browser (like Chrome) or a PDF library (like PrinceXML) to render HTML to PDF. If you can inject HTML into your profile — address, company name, notes —…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--507d6543d167---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--507d6543d167---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--507d6543d167---------------------------------------)

[86K followers](/followers?source=post_page---post_publication_info--507d6543d167---------------------------------------)

·[Last published 17 hours ago](/built-pentest-environment-on-your-mac-using-docker-bc37c3dcb7ac?source=post_page---post_publication_info--507d6543d167---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--507d6543d167---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--507d6543d167---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--507d6543d167---------------------------------------)

[1.5K followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--507d6543d167---------------------------------------)

·[22 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--507d6543d167---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

[Help](https://help.medium.com/hc/en-us?source=post_page-----507d6543d167---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----507d6543d167---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----507d6543d167---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----507d6543d167---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----507d6543d167---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----507d6543d167---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----507d6543d167---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----507d6543d167---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----507d6543d167---------------------------------------)
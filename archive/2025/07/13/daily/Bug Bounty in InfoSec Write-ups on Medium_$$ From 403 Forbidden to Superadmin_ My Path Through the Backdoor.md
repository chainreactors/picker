---
title: $$ From 403 Forbidden to Superadmin: My Path Through the Backdoor
url: https://infosecwriteups.com/from-403-forbidden-to-superadmin-my-path-through-the-backdoor-77b85774fee5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-13
fetch_date: 2025-10-06T23:27:43.349058
---

# $$ From 403 Forbidden to Superadmin: My Path Through the Backdoor

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F77b85774fee5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-403-forbidden-to-superadmin-my-path-through-the-backdoor-77b85774fee5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-403-forbidden-to-superadmin-my-path-through-the-backdoor-77b85774fee5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-77b85774fee5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-77b85774fee5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $$ From 403 Forbidden to Superadmin: My Path Through the Backdoor

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--77b85774fee5---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--77b85774fee5---------------------------------------)

4 min read

·

Jul 9, 2025

--

Share

Sometimes, all it takes is a little curiosity, some HTTP trickery, and an overlooked misconfiguration to move from being locked out to having the keys to the kingdom. Here’s how a simple 403 Forbidden page led to full superadmin access on a production system.

Press enter or click to view image in full size

![]()

## Phase 1: Reconnaissance — Start With What’s Public

The process began with gathering as much surface-level information as possible. In security testing, this is called *reconnaissance*. I used tools like `subfinder` to collect subdomains associated with the target, and then filtered the results using `httpx` to check which domains were live and what kind of HTTP status codes they returned.

```
subfinder -d target.com -silent > subs.txt
httpx -l subs.txt -mc 403,401,200 -tech-detect -title > live.txt
```

Next, I scanned the archive of known URLs using `gau` (GetAllUrls) to look for anything suspicious or admin-related:

```
gau --subs target.com | grep -iE 'admin|internal|dashboard' > gau_admin.txt
```

Among the results, one URL stood out:

```
https://secure.target.com/admin/settings
```

It returned a 403 Forbidden. That usually means access is blocked due to lack of permissions. But often, that’s where…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--77b85774fee5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--77b85774fee5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--77b85774fee5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--77b85774fee5---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--77b85774fee5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--77b85774fee5---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--77b85774fee5---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--77b85774fee5---------------------------------------)

[779 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--77b85774fee5---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--77b85774fee5---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----77b85774fee5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----77b85774fee5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----77b85774fee5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----77b85774fee5---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----77b85774fee5---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----77b85774fee5---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----77b85774fee5---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----77b85774fee5---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----77b85774fee5---------------------------------------)
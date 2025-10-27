---
title: “Day 24: The Polyglot Poison — How I Turned a Resume Upload into a Remote Shell”
url: https://infosecwriteups.com/day-24-the-polyglot-poison-how-i-turned-a-resume-upload-into-a-remote-shell-dc998722a328?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-02
fetch_date: 2025-10-02T19:30:48.962846
---

# “Day 24: The Polyglot Poison — How I Turned a Resume Upload into a Remote Shell”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdc998722a328&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-24-the-polyglot-poison-how-i-turned-a-resume-upload-into-a-remote-shell-dc998722a328&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-24-the-polyglot-poison-how-i-turned-a-resume-upload-into-a-remote-shell-dc998722a328&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dc998722a328---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dc998722a328---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 23: The Polyglot Poison — How I Turned a Resume Upload into a Remote Shell”

## Bypassing Modern File Upload Protections with a Multi-Headed File

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--dc998722a328---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--dc998722a328---------------------------------------)

5 min read

·

Aug 29, 2025

--

Share

The target was a job recruitment platform. They allowed users to upload resumes, proudly displaying a banner: “All files are scanned for viruses!” I knew they’d be checking for `.php` and `.exe` extensions. My goal was deeper. I didn't want to upload a shell; I wanted to upload a *resume* that was *also* a shell. By crafting a perfectly malicious polyglot file—a PDF that was simultaneously a valid PHP script—I bypassed their entire security stack. The result was remote code execution and a $4000 bounty. This is the art of the file format polyglot.

[free link](https://amannsharmaa.medium.com/day-24-the-polyglot-poison-how-i-turned-a-resume-upload-into-a-remote-shell-dc998722a328?sk=c5be8204d94549dab6b34e6984fd1b16)

Press enter or click to view image in full size

![]()

## Beyond the Extension: The Modern File Upload Landscape

Basic extension blacklists are obsolete. Modern defenses involve:

* Content-Type Verification: Checking the `Content-Type` header (e.g., `application/pdf`).
* Magic Number Validation: Reading the first few bytes of the file to verify its signature (e.g., `%PDF-` for PDFs).
* Content Sanitization: Attempting to parse the file and remove potentially malicious elements.
* Virus Scanning: Using AV engines to…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dc998722a328---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dc998722a328---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--dc998722a328---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--dc998722a328---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--dc998722a328---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--dc998722a328---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--dc998722a328---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--dc998722a328---------------------------------------)

[739 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--dc998722a328---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--dc998722a328---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----dc998722a328---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----dc998722a328---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----dc998722a328---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----dc998722a328---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----dc998722a328---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----dc998722a328---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----dc998722a328---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----dc998722a328---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----dc998722a328---------------------------------------)
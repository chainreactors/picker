---
title: Findings in Swiggy’s Codebase: Memory Leak and Google Maps API Key Exposure.
url: https://infosecwriteups.com/findings-in-swiggys-codebase-memory-leak-and-google-maps-api-key-exposure-bf3569ccedca?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-08-19
fetch_date: 2025-10-04T11:59:32.589291
---

# Findings in Swiggy’s Codebase: Memory Leak and Google Maps API Key Exposure.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fbf3569ccedca&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffindings-in-swiggys-codebase-memory-leak-and-google-maps-api-key-exposure-bf3569ccedca&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffindings-in-swiggys-codebase-memory-leak-and-google-maps-api-key-exposure-bf3569ccedca&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-bf3569ccedca---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-bf3569ccedca---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Findings in Swiggy’s Codebase: Memory Leak and Google Maps API Key Exposure.

[![Varshini Ramesh](https://miro.medium.com/v2/resize:fill:64:64/1*-wSL-BDp6P27gNRtYB5tgA.jpeg)](https://varshini-ramesh.medium.com/?source=post_page---byline--bf3569ccedca---------------------------------------)

[Varshini Ramesh](https://varshini-ramesh.medium.com/?source=post_page---byline--bf3569ccedca---------------------------------------)

3 min read

·

Aug 8, 2023

--

1

Listen

Share

Press enter or click to view image in full size

![]()

Greetings, **Infosec aficionados!** Today, we’re diving into the Swiggy’s tech oopsies, featuring not one but two delightful vulnerabilities.

![]()

> **1st Vulnerability:**

Google Maps API Key Exposure Swiggy, like many other apps, relies on various APIs to provide seamless services. In this case, they used the Google Maps Staticmap API and Streetview API to enhance their location-based features.

> **Reproduction:**

Curiosity often leads us to explore and test the boundaries. I was looking through source code I stumbled upon Swiggy’s API key in a JavaScript file URL. From there, it was easy to see that accessing the URLs directly revealed the vulnerable API key. Then i exploited using some tools and a code which was provided by google.

> **Tools used:**

1. To find any api keys<https://github.com/trufflesecurity/trufflehog>

2. Exploit the key **—** <https://github.com/streaak/keyhacks>

3. Gmap api scanner — <https://github.com/ozguralp/gmapsapiscanner>

4. <https://mapsplatform.google.com/maps-products/#maps-section>

Voilà! The key was exposed, leaving the door wide open for potential misuse.

> **Conclusion:**

Swiggy’s API key exposure may seem like a tiny flaw, but it highlights the importance of rigorous security practices.

Press enter or click to view image in full size

![]()

Report to swiggy regarding google maps api key exposure

> **2nd Vulnerability:**

When the program allocates memory to perform tasks, it forgets to free up that memory after use. As a result, memory usage keeps piling up like an ever-growing tower of blocks, slowly eating away the available resources.

> **Consequences:**

This memory trouble can cause slow performance, making the program slower than a sleepy sloth.With time, the continuous memory usage can push the program towards a crash.

> **Reproduction:**

Same as above when i was checking through some **.js** files found another one which was all about debugging and some monitoring information, which was sensitive and shouldn't be exposed.

> **Tools used:**

Using memory profiling tools like pprof or Valgrind.

<https://github.com/google/pprof>
[https://valgrind.org/](https://valgrind.org/info/tools.html)

> **Conclusion:**

Swiggy’s “Memory Leak” is a sneaky foe that can quietly cause mayhem if left unchecked.

Press enter or click to view image in full size

![]()

Report to swiggy regarding memory leak

> **Reply from Swiggy:**

Sadly, both of the vulnerabilities are duplicate. It’s disheartening to accept this fact, but it’s an opportunity for learning. So, I just wanted to give you a heads up on how I came across these duplicate vulnerabilities. It’s actually pretty cool because it adds to what we can learn from the whole experience.

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

**NOTE: Any automated tool cannot replace human’s brain so try to exploit on own, try doing without any automated tools so it enhances our skills and knowledge.**

**📫 Reach me if you wish to:**

![]()

**LinkedIn**: <https://www.linkedin.com/in/varshini~ramesh/>
**Twitter:** <https://twitter.com/varshiniramesh5>
**GitHub**: <https://github.com/varsh1408>

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----bf3569ccedca---------------------------------------)

[Responsible Disclosure](https://medium.com/tag/responsible-disclosure?source=post_page-----bf3569ccedca---------------------------------------)

[Infosec Write Ups](https://medium.com/tag/infosec-write-ups?source=post_page-----bf3569ccedca---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----bf3569ccedca---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----bf3569ccedca---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--bf3569ccedca---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--bf3569ccedca---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--bf3569ccedca---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--bf3569ccedca---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--bf3569ccedca---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Varshini Ramesh](https://miro.medium.com/v2/resize:fill:96:96/1*-wSL-BDp6P27gNRtYB5tgA.jpeg)](https://varshini-ramesh.medium.com/?source=post_page---post_author_info--bf3569ccedca---------------------------------------)

[![Varshini Ramesh](https://miro.medium.com/v...
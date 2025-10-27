---
title: HOW I HACKED NASA?
url: https://infosecwriteups.com/how-i-hacked-nasa-0715b6b5d7b8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-06-16
fetch_date: 2025-10-06T16:54:48.822393
---

# HOW I HACKED NASA?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0715b6b5d7b8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-nasa-0715b6b5d7b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-nasa-0715b6b5d7b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0715b6b5d7b8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0715b6b5d7b8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# HOW I HACKED NASA?

[![Krishnadev P Melevila](https://miro.medium.com/v2/resize:fill:64:64/1*QpBWYV2bZ8JJS9ZIHz-17A.png)](https://krishnadevpmelevila.medium.com/?source=post_page---byline--0715b6b5d7b8---------------------------------------)

[Krishnadev P Melevila](https://krishnadevpmelevila.medium.com/?source=post_page---byline--0715b6b5d7b8---------------------------------------)

3 min read

·

Jun 9, 2024

--

6

Listen

Share

Hi Guyz,

My name is Krishnadev P Melevila. I am a security researcher working for many startups. To know more about me, Just search me on Google.

It’s dream of every security researcher to be there on hall of fame page of NASA.

I also started researching on NASA’s infrastructure to grab that position.

The vulnerability should be minimum of P3 level to be there to get listed on HoF of NASA., I had submitted a total of 3 reports, where two of them got P5 and closed as informational, So with each submission my inner mind was crying hard for that HoF.

Press enter or click to view image in full size

![]()

That day came in.

I started with enumerating the subdomains of [nasa.gov.in](https://nasa.gov.in/), I used the tool called subdomainfinder <https://subdomainfinder.c99.nl/> .

Listed a large set of subdomains, But no luck, tried for days, weeks and months. I almost lost my hope.

Then I checked the scopes on bugcrowd, There was one domain called [globe.gov](https://datasearch.globe.gov/). I started enumerating subdomains of that domain.

And I came to a subdomain called: [datasearch.globe.gov](https://datasearch.globe.gov/)

Now its time to start:

Let’s put in the attacker’s shoe

## Steps to Reproduce

1. Visit: <https://datasearch.globe.gov/>
2. Click on Site filters
3. Type any “Site name” filter
4. Select any protocol filter
5. Setup the burpsuite proxy on and click on share button at top of page.
6. On the burp, modify the “text” parameter of key “0” of “filter\_list” parameter to <img src=x onerror=alert(1)>

![]()

![]()

Press enter or click to view image in full size

![]()

7. Don’t forget to encode the request as in 3rd figure,

8. Now forward the request and get the share link from browser.

Press enter or click to view image in full size

![]()

Now if we check this link: <https://vis.globe.gov/GLOBE/?vis_mode=adat&load_filter=1124768045844738315>

It will trigger XSS! (IT IS FIXED AS OF NOW!)

Press enter or click to view image in full size

![]()

TIMELINE:

Reported: 01 Mar 2024 04:33:14 UTC

Triaged: 01 Mar 2024 09:46:05 UTC

Press enter or click to view image in full size

![]()

First response from NASA: 04 Mar 2024 22:24:11 UTC

Press enter or click to view image in full size

![]()

Token of appreciation and HoF: 27 Mar 2024 13:16:14 UTC

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

***Don’t forget to follow me on Medium and other social media. Also please give your 50 claps for this write-up and that’s my inspiration to write more!!***

I need your support to write more, Buy me a coffee pls: <https://www.buymeacoffee.com/krishnadevpm>

*My Instagram handle:* [*https://instagram.com/krishnadev\_p\_melevila*](https://instagram.com/krishnadev_p_melevila)

*My Twitter handle:* [*https://twitter.com/Krishnadev\_P\_M*](https://twitter.com/Krishnadev_P_M)

*My LinkedIn handle:* [*https://www.linkedin.com/in/krishnadevpmelevila/*](https://www.linkedin.com/in/krishnadevpmelevila/)

[Bugbounty](https://medium.com/tag/bugbounty?source=post_page-----0715b6b5d7b8---------------------------------------)

[Hallof Fame](https://medium.com/tag/hallof-fame?source=post_page-----0715b6b5d7b8---------------------------------------)

[NASA](https://medium.com/tag/nasa?source=post_page-----0715b6b5d7b8---------------------------------------)

[Vdp](https://medium.com/tag/vdp?source=post_page-----0715b6b5d7b8---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----0715b6b5d7b8---------------------------------------)

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0715b6b5d7b8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0715b6b5d7b8---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0715b6b5d7b8---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0715b6b5d7b8---------------------------------------)

·[Last published 1 hour ago](/baby-dfc2547dc387?source=post_page---post_publication_info--0715b6b5d7b8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Krishnadev P Melevila](https://miro.medium.com/v2/resize:fill:96:96/1*QpBWYV2bZ8JJS9ZIHz-17A.png)](https://krishnadevpmelevila.medium.com/?source=post_page---post_author_info--0715b6b5d7b8---------------------------------------)

[![Krishnadev P Melevila](https://miro.medium.com/v2/resize:fill:128:128/1*QpBWYV2bZ8JJS9ZIHz-17A.png)](https://krishnadevpmelevila.medium.com/?source=post_page---post_author_info--0715b6b5d7b8---------------------------------------)

[## Written by Krishnadev P Melevila](https://krishnadevpmelevila.medium.com/?source=post_page---post_author_info--0715b6b5d7b8---------------------------------------)

[1.4K followers](https://krishnadevpmelevila.medium.com/followers?source=post_page---post_author_info--0715b6b5d7b8---------------------------------------)

·...
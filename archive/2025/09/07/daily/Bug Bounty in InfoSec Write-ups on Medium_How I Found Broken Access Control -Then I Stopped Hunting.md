---
title: How I Found Broken Access Control -Then I Stopped Hunting
url: https://infosecwriteups.com/how-i-found-broken-access-control-then-i-stopped-hunting-a48187e8702a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-07
fetch_date: 2025-10-02T19:47:24.237230
---

# How I Found Broken Access Control -Then I Stopped Hunting

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa48187e8702a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-broken-access-control-then-i-stopped-hunting-a48187e8702a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-broken-access-control-then-i-stopped-hunting-a48187e8702a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a48187e8702a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a48187e8702a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Found Broken Access Control -Then I Stopped Hunting

[![Umanhonlen Gabriel](https://miro.medium.com/v2/resize:fill:64:64/1*HOiKx3vWBSnQ9z_gn5WzDw.png)](https://medium.com/%40sudosu01?source=post_page---byline--a48187e8702a---------------------------------------)

[Umanhonlen Gabriel](https://medium.com/%40sudosu01?source=post_page---byline--a48187e8702a---------------------------------------)

2 min read

·

Sep 5, 2025

--

2

Listen

Share

I picked up a cryptocurrency platform subdomain xyz.REDACTED.net

Before starting, I already believed their security measures would be stringent, but little did I know that nothing is actually secure unless tested.

So I observed how the platform worked, looked beyond the fancy frontend, and tried to sign up with user@xyz.com.

Boom!!! I saw on my screen that a mail had been sent.

Good. Now time to hunt proper.

I set up all what was needed and registered.

I was looking around, tried cache deception, and found an endpoint that got cached by observing the network tab (HIT).

Wooow.

![]()

I was so happy and had to try it on incognito to see if it was actually cached to return my info but oh no, I got “session expired.”

I documented it to try cache poisoning later, but moved on to see what else I could do.

Then I noticed a tab to create a contact and here was my catch.

Created a contact for User A and noticed a contact ID.

Logout from User A and login as User B.

Create a contact for User B, but this time, swap the contact ID of User A into User B’s request.

Oh wowowooooooo!!!
I saw User A’s contact.

Tried User B’s again and saw User B’s contact.

![]()

I reported immediately but got a duplicate.

The triager said the fix is still pending in the pipeline, and the first researcher’s report has already been closed and awarded.

![]()

I was happy to get a broken access control flaw but the mode of communication made me stop on the platform.

Bug bounty hunting is becoming frustrating.
Most triagers get you pissed, but then, the skills will never leave you.

Until you land the big win one day, keep hunting.

**Feel Free to connect with me on LinkedIn or X :**

[https://www.linkedin.com/in/umanhonlen/](https://www.linkedin.com/in/umanhonlengabriel)

<https://x.com/sudosu01>

Thank you!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----a48187e8702a---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----a48187e8702a---------------------------------------)

[Hacker](https://medium.com/tag/hacker?source=post_page-----a48187e8702a---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----a48187e8702a---------------------------------------)

[Cryptocurrency](https://medium.com/tag/cryptocurrency?source=post_page-----a48187e8702a---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a48187e8702a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a48187e8702a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a48187e8702a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a48187e8702a---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--a48187e8702a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Umanhonlen Gabriel](https://miro.medium.com/v2/resize:fill:96:96/1*HOiKx3vWBSnQ9z_gn5WzDw.png)](https://medium.com/%40sudosu01?source=post_page---post_author_info--a48187e8702a---------------------------------------)

[![Umanhonlen Gabriel](https://miro.medium.com/v2/resize:fill:128:128/1*HOiKx3vWBSnQ9z_gn5WzDw.png)](https://medium.com/%40sudosu01?source=post_page---post_author_info--a48187e8702a---------------------------------------)

[## Written by Umanhonlen Gabriel](https://medium.com/%40sudosu01?source=post_page---post_author_info--a48187e8702a---------------------------------------)

[98 followers](https://medium.com/%40sudosu01/followers?source=post_page---post_author_info--a48187e8702a---------------------------------------)

·[41 following](https://medium.com/%40sudosu01/following?source=post_page---post_author_info--a48187e8702a---------------------------------------)

CyberSecurity Enthusiast | AppSec | Security Researcher | #SDG8 Advocate Empowering individuals and organizations against cyber threats.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----a48187e8702a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a48187e8702a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a48187e8702a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a48187e8702a---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a48187e8702a---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a48187e8702a---------------------------------------)

[...
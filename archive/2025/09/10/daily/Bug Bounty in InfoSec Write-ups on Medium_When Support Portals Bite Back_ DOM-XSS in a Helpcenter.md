---
title: When Support Portals Bite Back: DOM-XSS in a Helpcenter
url: https://infosecwriteups.com/when-support-portals-bite-back-dom-xss-in-a-helpcenter-4ac7e154ce4e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-10
fetch_date: 2025-10-02T19:54:17.479110
---

# When Support Portals Bite Back: DOM-XSS in a Helpcenter

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4ac7e154ce4e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-support-portals-bite-back-dom-xss-in-a-helpcenter-4ac7e154ce4e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-support-portals-bite-back-dom-xss-in-a-helpcenter-4ac7e154ce4e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4ac7e154ce4e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4ac7e154ce4e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# When Support Portals Bite Back: DOM-XSS in a Helpcenter

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:64:64/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---byline--4ac7e154ce4e---------------------------------------)

[Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---byline--4ac7e154ce4e---------------------------------------)

2 min read

·

Sep 8, 2025

--

1

Share

[FREE LINK](https://medium.com/bugbountywriteup/when-support-portals-bite-back-dom-xss-in-a-helpcenter-4ac7e154ce4e?sk=9f3bae9bcfb903c89f8ad5e35f51aba5)

You know what’s fun? Browsing boring helpcenter pages that look like they’d never hurt a fly, until you pop open DevTools and realize they’re basically handing you a free DOM-XSS sink.

That’s exactly what I stumbled upon at **support.example.com**, a Freshdesk-powered portal. Spoiler: no, I didn’t pwn ExampleCorp. Yes, I did get an `alert(document.domain)` out of it.

Press enter or click to view image in full size

![]()

## Step 1: Boredom + View Source

The page in question is a public knowledgebase article that proudly lists “secure servers.” Hidden inside the HTML was this neat little script block:

```
xmlHttp.open("GET","https://api.example.com/tunnels",true);
xmlHttp.responseType = "json";
xmlHttp.onload = function() {
  if (xmlHttp.status === 200) {
    var tunnels = xmlHttp.response;
    for (var tunnel of tunnels) {
      jQuery(".tunnel-list").append(
        "<li><span>"+tunnel.host+"</span><span><i>"+tunnel.ip+"</i></span></li>"
      );
    }
  }
};
```

Yes, you read that right. They take `tunnel.host` and `tunnel.ip` from the API and just **string-concat them straight into the DOM**. What could possibly go wrong?

## Step 2: Console Shenanigans

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4ac7e154ce4e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4ac7e154ce4e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4ac7e154ce4e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4ac7e154ce4e---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--4ac7e154ce4e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:96:96/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--4ac7e154ce4e---------------------------------------)

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:128:128/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--4ac7e154ce4e---------------------------------------)

[## Written by Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--4ac7e154ce4e---------------------------------------)

[78 followers](https://medium.com/%40devanshpatel930/followers?source=post_page---post_author_info--4ac7e154ce4e---------------------------------------)

·[9 following](https://medium.com/%40devanshpatel930/following?source=post_page---post_author_info--4ac7e154ce4e---------------------------------------)

Hacking legally so companies don’t get hacked illegally. Cybersecurity analyst | Bug bounty hunter | Breaking things so others can call it ‘secure’

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----4ac7e154ce4e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4ac7e154ce4e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4ac7e154ce4e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4ac7e154ce4e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4ac7e154ce4e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4ac7e154ce4e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4ac7e154ce4e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4ac7e154ce4e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4ac7e154ce4e---------------------------------------)
---
title: Don’t Give Up On XSS! | Fun Firefox XSS
url: https://infosecwriteups.com/dont-give-up-on-xss-fun-firefox-xss-3fce0ee297a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-02
fetch_date: 2025-10-04T05:28:46.723634
---

# Don’t Give Up On XSS! | Fun Firefox XSS

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F3fce0ee297a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdont-give-up-on-xss-fun-firefox-xss-3fce0ee297a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdont-give-up-on-xss-fun-firefox-xss-3fce0ee297a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-3fce0ee297a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-3fce0ee297a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Don’t Give Up On XSS! | Fun Firefox XSS

## There’s always a way to exploit xss in different contexts

[![Fırat](https://miro.medium.com/v2/resize:fill:64:64/1*SCkq2tULGFnERCJPAP-LXQ.jpeg)](https://medium.com/%40fiirat?source=post_page---byline--3fce0ee297a---------------------------------------)

[Fırat](https://medium.com/%40fiirat?source=post_page---byline--3fce0ee297a---------------------------------------)

2 min read

·

Feb 1, 2023

--

Listen

Share

## Story

I got an invite from a private program on hackerone and started searching for some vulnerabilites. After a while of searching, i found an url that had some interesting parameters. One of my inputs were reflecting inside of an *hidden* inputtag.

```
<input type="hidden" name="SourceName" id="SourceName" value="hey">
```

So i tried to espace the value attribute by adding a quote, and i was able escape it succesfully. Now the catch is, after i escaped the attribute; i tried to close the input tag and open up another tag, but the app was giving error 500 when i entered < > characters. So i tried to execute xss inside of another attribute. I thought `" onfocus="alert(1)" autofocus="` would do the job, but i was wrong. Even if i was able to succesfully inject the attribute; it wasn’t firing.

```
<input type="hidden" name="SourceName" id="SourceName" value="hey" onfocus="alert(1)" autofocus="">
```

## **Exploitation**

So after i made a quick googling, i learned that because the input type is *hidden* it would never gain the focus and therefore the onfocus handler would never fire.

So i started searching for an alternate solution, at this point; i was looking this as an xss challenge, i had to solve this. After searching for a while i came across an article published on [portswigger.net](https://portswigger.net/research/xss-in-hidden-input-fields)

So, to summarize the article: onclick events could be called on the hidden input when it activated via acces keys but only in firefox. So, after learning this my final payload was this:

```
<input type="hidden" accesskey="X" onclick="alert(1)">
```

With this payload, the user has to press ALT+SHIFT+X on his keyboard for this to fire. As i said earlier, this was like a challenge for me; as a result i learned a lot of new things. I would still be happy if this bug wasn’t accepted, since it needs a lot of user interaction.

As i said one of my write-ups: contexts are really important when it comes to searching for xss vulnerabilities.

I hope you guys learned something new by reading this write-up, if you have any questions; you can reach out to me via: [My Twitter](https://twitter.com/cartidropls)

Press enter or click to view image in full size

![]()

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----3fce0ee297a---------------------------------------)

[Xss Attack](https://medium.com/tag/xss-attack?source=post_page-----3fce0ee297a---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----3fce0ee297a---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----3fce0ee297a---------------------------------------)

[Hackerone](https://medium.com/tag/hackerone?source=post_page-----3fce0ee297a---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--3fce0ee297a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--3fce0ee297a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--3fce0ee297a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--3fce0ee297a---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--3fce0ee297a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Fırat](https://miro.medium.com/v2/resize:fill:96:96/1*SCkq2tULGFnERCJPAP-LXQ.jpeg)](https://medium.com/%40fiirat?source=post_page---post_author_info--3fce0ee297a---------------------------------------)

[![Fırat](https://miro.medium.com/v2/resize:fill:128:128/1*SCkq2tULGFnERCJPAP-LXQ.jpeg)](https://medium.com/%40fiirat?source=post_page---post_author_info--3fce0ee297a---------------------------------------)

[## Written by Fırat](https://medium.com/%40fiirat?source=post_page---post_author_info--3fce0ee297a---------------------------------------)

[105 followers](https://medium.com/%40fiirat/followers?source=post_page---post_author_info--3fce0ee297a---------------------------------------)

·[5 following](https://medium.com/%40fiirat/following?source=post_page---post_author_info--3fce0ee297a---------------------------------------)

web application security researcher

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----3fce0ee297a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----3fce0ee297a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----3fce0ee297a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----3fce0ee297a---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----3fce0ee29...
---
title: Bug Bounty Writeup: $2500 Reward for Session Hijack via Chained Attack
url: https://infosecwriteups.com/bug-bounty-writeup-2500-reward-for-session-hijack-via-chained-attack-2a4462e01d4d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-08-01
fetch_date: 2025-10-06T17:00:16.782658
---

# Bug Bounty Writeup: $2500 Reward for Session Hijack via Chained Attack

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2a4462e01d4d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-writeup-2500-reward-for-session-hijack-via-chained-attack-2a4462e01d4d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-writeup-2500-reward-for-session-hijack-via-chained-attack-2a4462e01d4d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2a4462e01d4d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2a4462e01d4d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bug Bounty Writeup: $2500 Reward for Session Hijack via Chained Attack

[![Anton (therceman)](https://miro.medium.com/v2/resize:fill:64:64/1*ya4CrhcriQRsR6QTK_3FJg.png)](https://therceman.medium.com/?source=post_page---byline--2a4462e01d4d---------------------------------------)

[Anton (therceman)](https://therceman.medium.com/?source=post_page---byline--2a4462e01d4d---------------------------------------)

6 min read

·

Jul 26, 2023

--

3

Listen

Share

A detailed Bug Bounty Writeup explaining a session hijack vulnerability that was exploited using Cross-Site Scripting (XSS), coupled with a Web Application Firewall (WAF) bypass and Server-Side Template Injection (SSTI). This in-depth analysis explores how these chained vulnerabilities were discovered, earning a $2500 reward.

![]()

Session Hijack via Chained Attack

Hello 👋

First of all, I’d like to thank [Martin Sparre-Enger](https://www.linkedin.com/in/mse89/) for sponsoring this Bug Bounty Writeup through my [BuyMeACoffee](https://www.buymeacoffee.com/therceman/wishlist) page.

Let’s dive in …

I’d been exploring a website for some time, uncovering a few bugs here and there, but I was curious to see if there was more to discover.

As usual, this involved navigating through all links and sections while keeping the Logger++ extension of my Burp Suite active.

After a while, I stumbled upon an interesting redirect URL that looked something like this: `https://example.com?redirect=${redirectURL}`

The last part caught my eye. It was clearly some kind of Template Language Expression that hadn’t been executed correctly. After noting this, I switched to the user profile page and began experimenting with the requests responsible for changing my username.

The first thing I tried was a mathematical expression `${2*2}`, to confirm the potential template injection vulnerability.

I changed my name to `John${2*2}`, and when the response output was `John4`, this confirmed the presence of a Server-Side Template Expression Language.

But what was it exactly? And what could I do with it?

After some time, I determined that it was the [JSP Expression Language](https://dotnettutorials.net/lesson/expression-language-jsp), and I found a few examples to test, thereby confirming its presence.

I think I spent several days, maybe even a week, reading documentation and examples, and trying out different functions and methods. The most interesting expression I found was `${header.cookie}`.By using this payload in your name you’ll receive a list of all cookies, including secured HTTP-only ones.

Upon discovering this SSTI (Server-Side Template Injection) vulnerability with cookies exfiltration payload, I decided to halt further exploration of the documentation and proceed with creating a PoC to demonstrate a Session Hijack vulnerability.

But… I’d overlooked one aspect… How could I perform a Session Hijack on another account without any interaction, or perhaps with at least minimal interaction?

As you might guess, we need a working XSS (Cross-Site Scripting) vulnerability that could change the victim’s name to `${header.cookie}`, and then exfiltrate (forward) all cookies to a domain under our control, thereby demonstrating the full impact of the vulnerability chain.

So, I started digging through the website for potential XSS vulnerabilities…

I had been inspecting the JS source code on the main page, switching to other pages, and repeating the process, but found nothing… until one day.

Accidentally, I clicked on something on the main page (maybe something had changed there, I’m not sure) and was redirected to a page with videos.

Opening the video, which appeared to be a live stream or a recording of one, I noticed an ‘id’ parameter in the URL, something like `videoId=w6exeqbemte`

The first, and most common, idea that came to mind was to append my favorite payload to the end of the parameter.

```
https://example.com/videos/?videoId=w6exeqbemteqwe'"<X</
```

After that, no video loaded, and an examination of the source code revealed that the `videoId` parameter was directly injected into the `src` attribute of the <iframe> element. My additional payload, `<x</`, had become an HTML attribute.

```
<iframe src="w6exeqbemteqwe'" <X</">
```

This was a good sign. It appeared that I had found a potential place for an XSS attack.

The next thing I tried was applying the following payload to this parameter.

```
?videoId=qwe"><img src onerror=alert(1)>
```

And… it was blocked by WAF :)

I knew this website had the most robust WAF I’d ever encountered, but… was it truly that strong?

All the classic payloads didn’t work here, I’ve spent a few days trying every possible trick that I know which turned into nothing…

Then I switched my approach and told myself — let’s try to keep our payload inside of an iframe tag and try experimenting further. We can’t override `src` attribute, all the class events like `onload` , `onmouseover` etc … are blocked by WAF.

But… the `srcdoc` param was not blocked by WAF.

This is where the battle with the WAF began :D

I knew that the basic XSS payload wouldn’t work within the ‘`srcdoc`’ parameter, just like before, since the WAF detected everything in the same way. I needed to somehow outsmart it…

I don’t remember exactly which part of the bypass was first, but to create the <script> tag inside an iframe, I utilized this payload:

```
?videoId=qwe"srcdoc="\u003ce<script%26Tab;e>"
```

This payload bypasses the WAF and creates a <script> tag.

The first part of the payload `\u003ce` tricks WAF with the fake opening of a non-existing tag `<e` . The issue with a WAF is that it attempts to decode everything first and then performs checks. In our case, the WAF will convert the Unicode text to a tag `<e` for a check. However, in reality, it remains as a text ‘`\u003ce`’ and doesn’t interfere with the opening of our script tag.

The second part of the paylo...
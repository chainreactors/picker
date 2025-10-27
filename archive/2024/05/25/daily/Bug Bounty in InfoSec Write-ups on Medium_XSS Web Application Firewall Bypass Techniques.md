---
title: XSS Web Application Firewall Bypass Techniques
url: https://infosecwriteups.com/xss-web-application-firewall-bypass-techniques-510b04a727b1?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-25
fetch_date: 2025-10-06T17:17:39.704593
---

# XSS Web Application Firewall Bypass Techniques

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F510b04a727b1&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxss-web-application-firewall-bypass-techniques-510b04a727b1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxss-web-application-firewall-bypass-techniques-510b04a727b1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-510b04a727b1---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-510b04a727b1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# XSS Web Application Firewall Bypass Techniques

[![Ott3rly](https://miro.medium.com/v2/resize:fill:64:64/1*3wMPJmhJUNOpqobsPBkS8g.jpeg)](https://ott3rly.medium.com/?source=post_page---byline--510b04a727b1---------------------------------------)

[Ott3rly](https://ott3rly.medium.com/?source=post_page---byline--510b04a727b1---------------------------------------)

7 min read

·

May 13, 2024

--

8

Listen

Share

We all hate web application firewall! Most likely you have encountered those while testing for cross-site-scripting. If you manage to get HTML injection which is the initial step, you know that there must be a bug out there. Let me help you to bypass this annoying thing and get that bounty on the table! It’s time to head dive into more techniques for bypassing some web protection. We will explore how those protections are implemented and how we can find ways to overcome them.

Check my YouTube video of this article ;)

## Initial Setup

This is the setup I will be using:

Press enter or click to view image in full size

![]()

On the left, we can see the client, a CloudFlare firewall in the middle will be as a proxy server to the CTF server on the right. The CTF server is [labs.hackxpert.com](https://labs.hackxpert.com/) which is made by [XSSRat](https://twitter.com/theXSSrat). He has some nice content related to XSS as well. Instead of going directly to **labs.hackxpert.com**, the requests will be sent through my CloudFlare, just to demonstrate from the defensive side, how it looks, how engineers are making blocking rules, to prevent those attacks, and the ways from the attacker side, how you can bypass those rules. I use this custom **k1t.uk** domain as a proxy for that CTF website built by Uncle Rat.

## User-Agent Blocks

The CloudFlare web application firewall comes with a lot of security tools out of the box. Before even setting up any rules, it usually checks for malicious user agents and one tool that actually has this own user agent is [sqlmap](https://github.com/sqlmapproject/sqlmap). Even though this post is meant for XSS, the sqlmap also detects for XSS! It will work the same for any other XSS CLI utility, just in case the CLI utility has a unique user agent.

If I run sqlmap, it will show a 403 error with a status code, with an access denied error:

Press enter or click to view image in full size

![]()

And if you try to check from the defensive side — the security events, it will show the user agent of sqlmap:

Press enter or click to view image in full size

![]()

To bypass this rule, I want to trick the web application firewall so that my requests look like coming from a regular browser. To check the user agent — you can use developer tools or like me, I’m using the [User Agent Editor](https://addons.mozilla.org/en-US/firefox/addon/user-agent-editor/) plugin:

![]()

Press enter or click to view image in full size

![]()

Copy this and try running sqlmap just by supplying a custom header:

Press enter or click to view image in full size

![]()

## IP and Country Blocks

After testing a single website for a while, you might send too many requests that could annoy the cyber security team. The security engineer could decide to create a custom rule — just to block your IP address. The IP block rule would look like this:

Press enter or click to view image in full size

![]()

If deploy this rule and try to access this website again, it will show that I am blocked:

![]()

My simplest solution for this is to use a VPN. I will use [NordVPN](https://ott3rly.com/NordVPN) service in my terminal to connect to Germany IP:

![]()

So in this case, I will use another IP address and try to refresh this page. As it uses a different IP, this rule will be bypassed:

Press enter or click to view image in full size

![]()

There could be another case — for example, when there is a rule just only accepts certain countries for that website, for instance, the United Kingdom. So once again, I use a VPN tool just for the United Kingdom, to bypass this:

Press enter or click to view image in full size

![]()

I have been using this VPN provider for 3 years already since they have a lot of servers and a lot of IPs for different countries like the United Kingdom. It will be a pretty low chance that you will end up on an already blocked IP. Whenever you are deciding which VPN to use, I recommend to avoid using free ones as they are mostly slow or contain many blacklisted IPs.

## Simple XSS Block Rules

If you bypass previous blocks which are most common, you’re finally ready to fuzz specific endpoints. Even before testing cross-site scripting, you want to start gently to be sure it’s worth more investigation. The first step is HTML injection. I think the best one is to use other tags like underlining or italics like this:

OR

Just check if this payload will be reflected somewhere and if I try to submit it on k1t.uk, as you can see, it is injected:

![]()

![]()

The next step is to try to use a script tag:

I’ve added **‘`”//>** characters because those are usually good for escaping the context, so if I hit, it passes to the query and it will be reflected back:

![]()

![]()

Sometimes the security engineers can take the naive approach and try to block by URL query string, which contains a **script** tag. The deployed WAF rule will look similar to this:

Press enter or click to view image in full size

![]()

That rule just checks if the URL query will contain words like this — “script”.

As the attacker, how you can avoid it? Just use some mix of uppercase and lowercase letters:

![]()

Press enter or click to view image in full size

![]()

A bit more advanced defense technique from cyber security engineers could be to create a rule which will convert URL query to lowercase and later compare it to the string “ **script** “.

Press enter or click to view image in full size

![]()

So in this case, even though you are using uppercase letters, the web appli...
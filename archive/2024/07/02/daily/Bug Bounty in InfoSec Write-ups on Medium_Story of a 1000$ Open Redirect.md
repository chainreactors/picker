---
title: Story of a 1000$ Open Redirect
url: https://infosecwriteups.com/story-of-a-1000-open-redirect-1405fb8a0e7a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-02
fetch_date: 2025-10-06T17:42:29.248330
---

# Story of a 1000$ Open Redirect

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1405fb8a0e7a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstory-of-a-1000-open-redirect-1405fb8a0e7a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstory-of-a-1000-open-redirect-1405fb8a0e7a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1405fb8a0e7a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1405fb8a0e7a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Story of a 1000$ Open Redirect

[![Debangshu Kundu](https://miro.medium.com/v2/resize:fill:64:64/1*fqBp7Dj3PDkaC90Ntv3cVA.jpeg)](https://medium.com/%40DK999?source=post_page---byline--1405fb8a0e7a---------------------------------------)

[Debangshu Kundu](https://medium.com/%40DK999?source=post_page---byline--1405fb8a0e7a---------------------------------------)

3 min read

·

Jul 1, 2024

--

2

Listen

Share

Hi all! Long time indeed ☺

Today I’ll talk about an Open Redirect that got us paid 1k$.

Nothing too complicated about the finding, just the right program ;)

Was invited to this SAAS program with great payouts for P3s and P4s too!

Press enter or click to view image in full size

![]()

Reward Range for the program

But firstly…

## Why Open Redirects?

> Open redirects enable an attacker to manipulate a user by redirecting them to a malicious site. A GET-based open redirect was identified which can impact users' ability to trust legitimate web pages. An attacker can send a phishing email that contains a link with a legitimate business name in the URL and the user will be redirected from the legitimate web server to any external domain. Users are less likely to notice subsequent redirects to different domains when an authentic URL with a valid SSL certificate can be used within the phishing link.
>
> This type of attack is also a precursor for more serious vulnerabilities such as Cross-Site Scripting (XSS), Server-Side Request Forgery (SSRF), Cross-Site Request Forgery (CSRF), or successful phishing attempts where an attacker can harvest users' credentials or gain users' OAuth access by relaying them through an Open Redirection, to a server they control (and can see the inbound requests from).

## The Vulnerability

Press enter or click to view image in full size

![]()

For confidentiality purposes, I can’t use specific folder names or client information, but I’ll try my best to explain!

Consider this :-

domain.com/abc/xyz/zyc/html/redirect.html

This accepts a `url=` parameter in Base64 encoded form.

Upon browsing to `redirect.html` we find this code :-

Press enter or click to view image in full size

![]()

Code of redirect.html

It first waits for an event to happen. Then, it retrieves the input url from the `url=` parameter and base64decodes it.

Now, it checks the input URL against a specified allowlist of certain domains, google.com, abc.com, etc. and if it matches the allowlist, it waits for 3 seconds (3000 mills) and redirects the user to the allowe domain. If not, it does nothing.

### Here comes the fault :-

> The regex is checking if the URL contains any of the listed domains. While this approach is straightforward, it can indeed lead to potential issues, including open redirects, because:

### Partial Matches:

> - The regex will match any URL that contains the specified domains as a substring. For instance, `malicious.com/google.com` or `phishing-abc.com` will also match.
>  - This partial matching can be exploited by attackers to craft malicious URLs that still pass the check.

And that’s exactly what we did!

We came up with the following payload :-

> https://domain.com/abc/xyz/zyc/html/redirect.html?url=<BASE64>https://evil.com#foobar</BASE64>

Resulting in :-

```
https://domain.com/abc/xyz/zyc/html/redirect.html?url=aHR0cHM6Ly9ldmlsLmNvbSNmb29iYXI=
```

The faulty regex allowed us to pass #foobar in the URL fragment, hence, bypassing the checks and arming us with a sweet open redirect ;)

There were multiple bypasses for the protection applied by the developers, stated below, but not limited to :-

*target.evil.com*

*evil.com?param=target*

*evil.com/target*

> This is because the script only matches the domain (target) name in the redirection, we can place it anywhere. They do not validate the TLDs, only the ‘target’, not even ‘target.com’.

Also, earning as a sweet bounty in the process!

Press enter or click to view image in full size

![]()

This bug was in collaboration with

[Aditya Sharma](https://medium.com/u/5900238e145d?source=post_page---user_mention--1405fb8a0e7a---------------------------------------)

(He was the mastermind, I just wrote the blog xD)

Follow us at :- <https://x.com/Assass1nmarcos> & <https://x.com/ThisIsDK999>

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----1405fb8a0e7a---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----1405fb8a0e7a---------------------------------------)

[Technology](https://medium.com/tag/technology?source=post_page-----1405fb8a0e7a---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----1405fb8a0e7a---------------------------------------)

[Medium](https://medium.com/tag/medium?source=post_page-----1405fb8a0e7a---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1405fb8a0e7a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1405fb8a0e7a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1405fb8a0e7a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1405fb8a0e7a---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--1405fb8a0e7a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https:/...
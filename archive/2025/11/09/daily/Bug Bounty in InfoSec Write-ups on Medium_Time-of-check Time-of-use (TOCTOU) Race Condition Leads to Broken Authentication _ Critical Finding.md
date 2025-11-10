---
title: Time-of-check Time-of-use (TOCTOU) Race Condition Leads to Broken Authentication | Critical Finding
url: https://infosecwriteups.com/time-of-check-time-of-use-toctou-race-condition-leads-to-broken-authentication-critical-finding-b55993c92abc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-09
fetch_date: 2025-11-10T03:17:40.665129
---

# Time-of-check Time-of-use (TOCTOU) Race Condition Leads to Broken Authentication | Critical Finding

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb55993c92abc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftime-of-check-time-of-use-toctou-race-condition-leads-to-broken-authentication-critical-finding-b55993c92abc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftime-of-check-time-of-use-toctou-race-condition-leads-to-broken-authentication-critical-finding-b55993c92abc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b55993c92abc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b55993c92abc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **Time-of-check Time-of-use (TOCTOU) Race Condition Leads to Broken Authentication**

[![Irsyad Muhammad Fawwaz](https://miro.medium.com/v2/resize:fill:64:64/1*QKd1iHWxJtcTgUZ40obagw.png)](https://irsyadsec.medium.com/?source=post_page---byline--b55993c92abc---------------------------------------)

[Irsyad Muhammad Fawwaz](https://irsyadsec.medium.com/?source=post_page---byline--b55993c92abc---------------------------------------)

3 min read

·

17 hours ago

--

Listen

Share

Press enter or click to view image in full size

![]()

source: portswigger.net

## How I started

I was bored and started poking at random public bug bounty programs. As usual I began with subdomain hunting to narrow the attack surface. My quick routine for bug bounty hunting is

```
subfinder -d example.com --all >> subdomain.txt
```

and then pipe into `aquatone`

```
cat subdomain.txt | aquatone
```

after that i found interesting subdomain that immediately redirected to a login/register page.

## Finding

I spent four days for just hoping i got the vulnerability, i test the site with regular testing(like xss, sqli, scanning, prototype pollution, etc.) and brute force experiments.

During four days of testing I observed anomalous behavior, the website was extremely slow and unresponsive at certain times, and the other times it was perfectly fast.

Seeing those two behaviours, I ran login brute force tests during the slow periods and again during the fast periods.

* At normal times everything behaved, wrong passwords got 401s, right password got 200 and a token
* But at certain times of day the site would crawl. Not “a little slow” full-on lag when doing login or register.

and then i figured it was the server being overloaded.

So I tried brute force again during both the fast windows and the slow windows.

* During fast windows it was boring and expected: everything rejected except the correct password.
* During slow windows something weird happened. I found five different passwords that all returned 200 and gave me valid tokens, none of those passwords were the real password.

Press enter or click to view image in full size

![]()

At first I thought I was seeing things, but I validated the tokens against protected endpoints and they worked.

After finding out, it wasn’t magic. It was a **TOCTOU race condition**. In plain short the function that checks whether a login is allowed and the part that actually issues the token aren’t synchronized. If the auth function is slower than the incoming requests, multiple requests can slip past the check before the system updates state, so several different wrong passwords can all look “valid” because requests overtake the function’s internal timing.

## What’s actually happening

Press enter or click to view image in full size

![]()

source: portswigger.net

Imagine the login flow as two streets:

* the “check” street

and

* the “use” street

The code first walks down the check street and says “cool, this account looks allowed right now,” then walks down the use street and says “okay, I’ll create a session/token.”

If these two steps happen back to back, everything works perfectly.

But if the check step is slow (heavy CPU, slow DB, blocked I/O, overloaded server), multiple incoming requests line up behind it. They all get told “cross” by the initial check *before* the token-creation step finishes.
 The result several requests reach the token-generation step even though the password validation should’ve failed.

In short:
 **when the auth function is slower than the incoming request rate, requests can overtake internal state and produce inconsistent results.**

## Why this happens in code terms

The core issue is a **non-atomic sequence**:

1. The code checks some condition (password, rate-limit, account state).
2. Later it issues a token based on that condition.
3. But the condition can change between step 1 and step 2.

Because there’s no per-account lock or atomic operation, multiple concurrent requests can all pass the check step before the state is updated. Some other common root causes include:

* Using `GET` → `SET` patterns in cache (non-atomic)
* Lack of Redis atomic ops / Lua scripts
* Offloading verification to async workers without synchronization
* Not using `SELECT ... FOR UPDATE` in DB transactions
* Stale reads under high concurrency

**TL;DR:** Database latency created a race window in the login flow: the password check ran slower than incoming requests, letting multiple wrong passwords reach the token creation step. Result real tokens issued for invalid logins.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b55993c92abc---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----b55993c92abc---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----b55993c92abc---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----b55993c92abc---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----b55993c92abc---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b55993c92abc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b55993c92abc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b55993c92abc---------------------------------------)

[73K followers](/followers?sourc...
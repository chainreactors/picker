---
title: Forced SSO Session Fixation
url: https://infosecwriteups.com/forced-sso-session-fixation-5d3b457b79cb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-17
fetch_date: 2025-10-06T18:04:21.608412
---

# Forced SSO Session Fixation

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5d3b457b79cb&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fforced-sso-session-fixation-5d3b457b79cb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fforced-sso-session-fixation-5d3b457b79cb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5d3b457b79cb---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5d3b457b79cb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Forced SSO Session Fixation

[![Serj Novoselov](https://miro.medium.com/v2/resize:fill:64:64/1*xkXww5XKPrnRqHwlho38eg.jpeg)](https://medium.com/%40s_novoselov?source=post_page---byline--5d3b457b79cb---------------------------------------)

[Serj Novoselov](https://medium.com/%40s_novoselov?source=post_page---byline--5d3b457b79cb---------------------------------------)

3 min read

·

Aug 16, 2024

--

Listen

Share

During a recent project, I encountered an interesting small issue that allowed for a one-click account takeover by fixating a session identifier and forcing a victim’s browser to initiate the first steps of a Single Sign-On (SSO) flow. This vulnerability was possible due to the absence of anti-CSRF token verification.

Press enter or click to view image in full size

![]()

### The Login Page

The login page exhibited the “Log in with SSO” feature:

Press enter or click to view image in full size

![]()

### Investigating the SSO Flow

Upon investigating the SSO flow, I discovered the following sequence of steps:

1. **Initiation of SSO process by clicking the button:**
   **GET** request to /idp/auth/mid-oidc?req=[UNIQUE\_ID]&redirect\_uri=[REDIRECT\_URI]
2. **SSO Service Provider process**
   Multiple requests made on the service provider domain, akin to signing in with Google where requests are sent to google.com. If the user was previously signed in, actions are performed automatically.
3. **Hitting callback URL**
   After authorization on the Service Provider side, a request to a callback URL is made:
   **GET** /idp/callback?code=[STUFF]&state=[STUFF].
   **However, this is not a last step, that returns the session token, one more additonal step was required.**
4. **Issue a session token**
   Request to get the session token.
   **GET** /idp/approval?req=**[UNIQUE\_ID]**The **UNIQUE\_ID** value is the same as was on the first step. This means, that if you know this value, you could hit this method and get a session. As no anti-csrf protection was present, so it was possible to perform a session fixation.

Press enter or click to view image in full size

![]()

### Exploitation Scenario

An “Attacker” opens the environment URL on their machine and extracts the “Log in with SSO” button link:

Press enter or click to view image in full size

![]()

From the copied link, the attacker extracts the “req” parameter and starts the self-written exploit:

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

The attacker then sends the link containing the “req” parameter to the “Victim”.

Upon opening the link in the browser, the “Victim” encounters an error message:

Press enter or click to view image in full size

![]()

### How does the exploit work?

The malicious script executed by the attacker utilizes 10 threads to make multiple requests to the **/idp/approval?req={req}.**

Initially, the server responses to these requests are **500** errors. However, when the victim initiates the SSO flow, but before handling the request to the “approval” URL, all subsequent requests to the mentioned endpoint return a **valid link with a session token.**

As a result of the exploit, the “Attacker” obtains the session URL and can complete the login flow, effectively logging in as the “Victim”:

Press enter or click to view image in full size

![]()

**By directly visiting the returned URL, the attacker finishes the login flow and logs in as “Victim”.**

### Remediation

The issue remediation can be done by:

1. Implementing Anti-CSRF Protection.
2. Validating Session Identifier at each step of the SSO process to prevent fixation.
3. Applying rate limiting on the /idp/approval endpoint to prevent rapid and unauthorized requests for session tokens.

🌐 My social networks: <https://linktr.ee/s_novoselov>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----5d3b457b79cb---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----5d3b457b79cb---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----5d3b457b79cb---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----5d3b457b79cb---------------------------------------)

[Writeup](https://medium.com/tag/writeup?source=post_page-----5d3b457b79cb---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5d3b457b79cb---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5d3b457b79cb---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5d3b457b79cb---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--5d3b457b79cb---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--5d3b457b79cb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Serj Novoselov](https://miro.medium.com/v2/resize:fill:96:96/1*xkXww5XKPrnRqHwlho38eg.jpeg)](https://medium.com/%40s_novoselov?source=post_page---post_author_info--5d3b457b79cb---------------------------------------)

[![Serj Novoselov](https://miro.medium.com/v2/resize:fill:128:128/1*xkXww5XKPrnRqHwlho38eg.jpeg)](https://medium.com/%40s_novosel...
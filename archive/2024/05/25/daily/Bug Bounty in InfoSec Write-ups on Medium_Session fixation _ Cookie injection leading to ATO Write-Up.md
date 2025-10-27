---
title: Session fixation | Cookie injection leading to ATO Write-Up
url: https://infosecwriteups.com/session-fixation-cookie-injection-leading-to-ato-write-up-98e29d2851b9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-25
fetch_date: 2025-10-06T17:17:36.955465
---

# Session fixation | Cookie injection leading to ATO Write-Up

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F98e29d2851b9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsession-fixation-cookie-injection-leading-to-ato-write-up-98e29d2851b9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsession-fixation-cookie-injection-leading-to-ato-write-up-98e29d2851b9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-98e29d2851b9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-98e29d2851b9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Session fixation | Cookie injection leading to ATO Write-Up

[![rAmpancist](https://miro.medium.com/v2/resize:fill:64:64/1*InjMQvPB8gvZW03UiL4VLQ.png)](https://rampancist.medium.com/?source=post_page---byline--98e29d2851b9---------------------------------------)

[rAmpancist](https://rampancist.medium.com/?source=post_page---byline--98e29d2851b9---------------------------------------)

3 min read

·

May 24, 2024

--

2

Listen

Share

Press enter or click to view image in full size

![]()

From GeeksForGeeks

There are numerous ways you can handle an authorization on your website. From session-based authentication to token-based authorization, any method you consider to use has to be properly configured or else the whole application might become prone to potential account takeovers.

In my case tho, although the target was horribly configured, it was not exploitable by itself. It had to be chained with other potential stuff to reach impact.

Lets call the main target I performed account takeover on `weakauth.main.com .`

Quite simply, the target was written in ASP.NET.

Upon first time visiting the website, you are issued a cookie called `ASP.NET_SessionId` which is totally unauthorized and unprivileged.

```
Set-Cookie: ASP.NET_SessionId=doonz8hcdquy72tkvfflqy34d;
```

Now this cookie has 0 privileges.

This is where vulnerability comes in play: when I authenticate myself in the website, I’m not issued a new session cookie. That previous cookie of mine stays, Its just upgraded now.

This allows me to perform the attack called **Session-Fixation**, if I find the right follow-up to chain vulnerabilities together.

### Session Fixation

Now what this attack is really about, is that I can simply set my cookie session for other users, and if they ever escalate their privileges by authenticating or authorizing, my session also gets upgraded.

Because the cookie session is living on both parties and its never renewed, anything happening to either side is applied to the session, from escalation to logging out.

Now in order to succeed in this attack you need to find **some way** to inject your session in victims browser. This is precisely called **Session Fixation**.

### Second Vulnerability | Cookie injection

Wonderfully enough, I found an endpoint on `optout.main.com` which was used to create an opt-out cookie. How ever it took the cookie name from my `client` parameter and appended `!disableClient` to it. So a normal response would look like this:

![]()

Normal Response

However, since the parameter lacked sanitization, I was able to inject character `;` , which precisely means I can evade the context and make my custom cookie in the scope of whole `main.com`, and turn all of the appended part to a useless attribute.

So a request with this parameter:

```
GET /optout?client=myDemoCookie%3dBadBadSession;+NotSoDemo
```

would have a response like this:

Press enter or click to view image in full size

![]()

Manipulated cookie

Notice how `!disableClient` is left out to a useless cookie attribute? This means we successfully created a custom cookie on whole `main.com` on victims browser.

### Chaining

Now finally chaining the 2 issues which are not vulnerability by themselves, to reach an impact.

I think the walk-through should be pretty straight forward now:

1. [Attacker] Visit <https://weakauth.main.com> . I now have my unauthenticated `ASP.SessionId`.
2. [Attacker] I put my SessionId inside the malicious link.

```
https://optout.main.com/optout?client=ASP.NET_SessionId%3doonz0ucdqujo2tkvfflqy34d%3b
```

3.[Victim] Opens the malicious URL. They now have a bad session attached to their browser.

4.[Victim] Opens https://weakauth.main.com/Login.aspx , selects “Click here to begin your application” to prompt for login page.

5.[Victim] After entering the user and password, Victim is redirected to their panel in https://weakauth.main.com/Panel.aspx.

6.[Attacker] Now if I visit the panel as the attacker, I can see my session is also upgraded and I have full access: <https://weakauth.main.com/Panel.aspx>

Press enter or click to view image in full size

![]()

Final panel access

The website also had very high privilege panels, which also lacked proper cookie generation and were most likely prone to this attack.

This issue was triaged with a CVSS score of 5.9 .

I hope you enjoyed reading this. I’d appreciate if you like and share it.

My twitter: <https://twitter.com/rampancist>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----98e29d2851b9---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----98e29d2851b9---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----98e29d2851b9---------------------------------------)

[Bugbounty Writeup](https://medium.com/tag/bugbounty-writeup?source=post_page-----98e29d2851b9---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----98e29d2851b9---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--98e29d2851b9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--98e29d2851b9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--98e29d2851b9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--98e29d2851b9---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--98e29d...
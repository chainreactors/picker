---
title: LmCompatibilityLevel and the PDC Trap
url: https://decoder.cloud/2026/04/15/lmcompatibilitylevel-and-the-pdc-trap/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-15
fetch_date: 2026-04-16T04:54:06.685698
---

# LmCompatibilityLevel and the PDC Trap

# [Decoder's Blog](https://decoder.cloud/ "Decoder's Blog")

Decoder's Blog

[Skip to content](#content "Skip to content")

* [Home](/)
* [Decoder’s Blog](https://decoder.cloud/)
* [Contact](https://decoder.cloud/contact/)

Search for:

Posted on [April 15, 2026](https://decoder.cloud/2026/04/15/lmcompatibilitylevel-and-the-pdc-trap/) by [Decoder](https://decoder.cloud/author/decoderblogblog/)

# LmCompatibilityLevel and the PDC Trap

**LmCompatibilityLevel** determines which NTLM and LM authentication protocols are accepted for inbound and outbound connections for Windows machines. On domain controllers, the minimum recommended setting is 3, but ideally it should be set to 5 to completely block incoming connections from clients still using the legacy NTLMv1 protocol.

In some cases, however, you may need to lower the level to support legacy hosts or applications that still rely on NTLMv1. Rather than weakening the configuration domain-wide, a common approach is to isolate those clients in a dedicated network segment, direct their traffic to a specific domain controller, and lower **LmCompatibilityLevel** only on that DC. This allows the rest of the domain to remain hardened.

At least, that was my assumption.

However, during testing I observed a completely unexpected behavior: when attempting authentication using NTLMv1 against other “hardened” domain controllers, the authentication still succeeded, which was both surprising and quite frustrating.

For my tests, I used a Python script to send raw NTLMv1 authentication packets, ensuring that this specific protocol was explicitly use

![](https://decoder.cloud/wp-content/uploads/2026/04/image.png?w=1024)

This was also confirmed in the Event Viewer: successful NTLMv1 authentication despite the LmCompatibilityLevel set to 5:

![](https://decoder.cloud/wp-content/uploads/2026/04/image-5.png?w=1024)

A quick look at wireshark capture showed something interesting

![](https://decoder.cloud/wp-content/uploads/2026/04/image-1.png?w=1024)

The authentication was forwarded to another domain controller via the **Netlogon secure channe**l (IP address 192.169.213.10), where `LmCompatibilityLevel` was set to 3. This DC had also the PDC emulator role.

By setting the `LmCompatibility` to 5 on the PDC, I got the expected Access Denied:

![](https://decoder.cloud/wp-content/uploads/2026/04/image-2.png?w=1024)

Also confirmed in Wirershark:

![](https://decoder.cloud/wp-content/uploads/2026/04/image-3.png?w=1024)

So what is happening here?

The problem is that this architecture does not work the way you think it does. After reverse-engineering `msv1_0.dll` and **ntlmshared.dll**, I found that a non-PDC domain controller configured with level 5 does not reject NTLMv1.

Because it is not authoritative for the decision, it silently forwards the authentication request to the PDC emulator and lets it make the final call.

Without going too much in details, inside `ntlmshared.dll`, `MsvpPasswordValidate`*()* contains a gate controlled by`GlobalSharedConfig` (which maps to`NtLmGlobalLmProtocolSupported`, derived from `LmCompatibilityLevel`):

![](https://decoder.cloud/wp-content/uploads/2026/04/image-6.png?w=1024)

When the level is 5, `bVar3` stays `false` and the NTLMv1 hash comparison is skipped entirely. The function returns false, causing `STATUS_WRONG_PASSWORD`. Back in `MsvpSamValidate() ,in msv1_0.dll` , the `Authoritative` flag is never set to `1` for this error, it stays at the default `0`.

Netlogon interprets `Authoritative=0` as “*this DC cannot give a definitive answer*” and forwards the NTLMv1 blob unchanged to the PDC emulator, which runs the same check under its own `LmCompatibilityLevel`.

![](https://decoder.cloud/wp-content/uploads/2026/04/image-7.png?w=1010)

This means that lowering the level on any DC effectively lowers it for the entire domain if that DC happens to be the PDC emulator, and more critically, **lowering it on the PDC emulator, even intentionally, even for a scoped use case, opens NTLMv1 acceptance for every client in the domain regardless of which DC they connect to**.

I tried to find documentation explaining or validating this behaviour but was unsuccessful, so I submitted it to MSRC as a security feature bypass. After an initial classification of “Important Security Feature Bypass”, they reconsidered and concluded it did not meet the bar for immediate servicing.

After further discussion explaining the real-world impact of inconsistent `LmCompatibilityLevel` configurations, they settled on medium severity with a fix planned for an upcoming future release.

My take: this is not something catastrophically dangerous on its own. But documenting this behaviour makes one thing clear, inconsistent `LmCompatibilityLevel` settings across domain controllers should always be avoided. The PDC emulator is the silent enforcement point for the entire domain, and administrators who believe they have contained NTLMv1 exposure to a single isolated DC may have a false sense of security.

This is also a good reminder that NTLM itself is on its way out , Microsoft has announced plans to deprecate it, and any remaining dependency on NTLMv1 in your environment is technical debt worth eliminating sooner rather than later.

That’s all 😉

### Share this:

* [Share on X (Opens in new window)
  X](https://decoder.cloud/2026/04/15/lmcompatibilitylevel-and-the-pdc-trap/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://decoder.cloud/2026/04/15/lmcompatibilitylevel-and-the-pdc-trap/?share=facebook)

Like Loading...

# Post navigation

[Previous Article What Windows Server 2025 Quietly Did to Your NTLM Relay](https://decoder.cloud/2026/02/25/what-windows-server-2025-quietly-did-to-your-ntlm-relay/)

### Leave a comment [Cancel reply](/2026/04/15/lmcompatibilitylevel-and-the-pdc-trap/#respond)

Δ

## Search

Search for:

[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)

* [Facebook](http://www.facebook.com)
* [LinkedIn](http://www.linkedin.com)
* [Twitter](http://www.twitter.com)
* [Instagram](http://www.instagram.com)

Privacy & Cookies: This site uses cookies. By continuing to use this website, you agree to their use.
To find out more, including how to control cookies, see here:
[Cookie Policy](https://automattic.com/cookies/)

* [Comment](https://decoder.cloud/2026/04/15/lmcompatibilitylevel-and-the-pdc-trap/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://s2.wp.com/i/logo/wpcom-gray-white.png?m=1479929237i) Decoder's Blog](https://decoder.cloud)

  Join 42 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2026%252F04%252F15%252Flmcompatibilitylevel-and-the-pdc-trap%252F)
* + [![](https://s2.wp.com/i/logo/wpcom-gray-white.png?m=1479929237i) Decoder's Blog](https://decoder.cloud)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2026%252F04%252F15%252Flmcompatibilitylevel-and-the-pdc-trap%252F)
  + [Copy shortlink](https://wp.me/p8ggv8-7H2)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://decoder.cloud/2026/04/15/lmcompatibilitylevel-and-the-pdc-trap/)
  + [View post in Reader](https://wordpress.com/reader/blogs/122087370/posts/29576)
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
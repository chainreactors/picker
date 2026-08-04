---
title: Attack Techniques: Fake Captive Portals
url: https://textslashplain.com/2026/08/03/attack-techniques-fake-captive-portals/
source: text/plain
date: 2026-08-03
fetch_date: 2026-08-04T05:00:02.207962
---

# Attack Techniques: Fake Captive Portals

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Fake Captive Portals

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-08-032026-08-03](https://textslashplain.com/2026/08/03/attack-techniques-fake-captive-portals/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [security](https://textslashplain.com/tag/security/)

When a device first joins a network, the upstream network hardware has full control over its traffic and can allow/block any packets sent from the device from reaching the Internet. Many public networks (typically Wi-Fi, but sometimes wired, located in hotels, coffee shops, mass transit, schools, etc.) require that the user accept Terms of Use or otherwise interact with a webpage before gaining broader/unrestricted access to the network.

The restricted client is called a “captive” and the webpages to allow removal of the access limitation are called [Captive Portals](https://textslashplain.com/2022/06/24/captive-portals/), the subject of a previous post.

When Windows detects that a network is blocking internet access with a Captive Portal, a link is provided to launch the captive user’s default browser:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image.jpg?resize=375%2C152&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image.jpg?ssl=1)

The captive browser is navigated to a non-secure HTTP url, and the network is expected to intercept the non-secure request and redirect to the Captive Portal webpage.

## The Attack

Over the last few years, there have been a series of attacks ([2025](https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/), [2026](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)) where attackers have used fake “captive portal” web pages that entice users to download and run malware…

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-2.png?resize=750%2C396&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-2.png?ssl=1)

… or [follow malicious instructions](https://textslashplain.com/2024/06/04/attack-techniques-trojaned-clipboard/) that result in compromise of the device, with this initial access being abused to steal credentials and move laterally within the victim’s organization.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-1.png?resize=750%2C404&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-1.png?ssl=1)

## Defenses

Beyond educating users not to follow any unusual instructions on captive portal pages, users can set [`ShellSmartScreenLevel` to `BLOCK`](https://textslashplain.com/2023/08/14/enforcing-smartscreen-with-policy/) to help prevent users from running downloaded malware when working offline with security services unreachable.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image.png?resize=618%2C578&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image.png?ssl=1)

With the policy set, users may not override the “SmartScreen Unreachable” warning dialog

For enterprise-managed devices, organizations can choose to prevent Wi-Fi connections to networks that have not been provisioned via MDM. See [AllowManualWifiConfiguration](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-wifi#allowmanualwificonfiguration).

## Threat Analysis

From a security perspective, untrusted networks attacks are *mostly* equivalent to the fake captive portal threat described here. In both, an attacker on the network path can observe and tamper with all non-secure (e.g. HTTP) requests, and can [partially-observe](https://textslashplain.com/2018/02/14/understanding-the-limitations-of-https/), block, or delay any secure (e.g. HTTPS, VPN) connections. Network attackers can behave selectively, allowing some connections while interfering with others.

Compared to traditional network attacks, the key differences for Captive Portal attacks are:

1. Users have been [primed](https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/) (by prior experience) to *expect* Captive Portal pages and *comply* with their instructions. There’s no standard for how Captive Portals behave and virtually every venue has different instructions for connections. This non-uniformity means that users are more easily socially-engineered into performing unsafe operations.
2. All captive portal flows *inherently* start with a non-secure HTTP request. Using HTTP is what allows a legitimate guest network to direct the user to the Captive Portal page because HTTPS encryption prevents tampering. Features like “automatic HTTPS upgrades” have to be disabled in Captive Portal scenarios because they break the expected flow.

   This non-secure protocol usage allows the network-based attacker to take over the flow.

---

Stay safe out there!

-Eric

### Share this:

* [Share on X (Opens in new window)
  X](https://textslashplain.com/2026/08/03/attack-techniques-fake-captive-portals/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2026/08/03/attack-techniques-fake-captive-portals/?share=facebook)

### Like this:

Like Loading…

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-08-032026-08-03](https://textslashplain.com/2026/08/03/attack-techniques-fake-captive-portals/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [security](https://textslashplain.com/tag/security/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Offboarding from Microsoft Defender for Endpoint](https://textslashplain.com/2026/07/22/offboarding-from-microsoft-defender-for-endpoint/)

[Next Post Next post:
Authenticode and UAC](https://textslashplain.com/2026/08/03/authenticode-and-uac/)

### Leave a Reply[Cancel reply](/2026/08/03/attack-techniques-fake-captive-portals/#respond)

## Search Text/Plain

Search for:

## Pages

* [About](https://textslashplain.com/about/)
* [Browse All Posts](https://textslashplain.com/browse-all-posts/)
* [Categories](https://textslashplain.com/categories/)
* [Cruises](https://textslashplain.com/cruises/)
* [IEInternals Archive](https://textslashplain.com/ieinternals-archive/)
* [Real-World Races](https://textslashplain.com/races/)

## RSS

[![RSS feed](https://textslashplain.com/wp-content/plugins/jetpack/images/rss/orange-small.png) RSS - Posts](https://textslashplain.com/feed/ "Subscribe to posts")

## Blog Stats

* 2,489,259 hits

## Categories

Categories
Select Category
bluebadge  (16)
books  (3)
browsers  (183)
design  (25)
dev  (87)
fiddler  (25)
life  (54)
perf  (20)
politics  (2)
privacy  (27)
reviews  (2)
running  (20)
security  (173)
storytelling  (48)
tech  (38)
travel  (9)
Uncategorized  (16)
web  (153)
windmills  (12)

![ericlaw](https://2.gravatar.com/avatar/89c27d27b73dd3690b3dad59f3a539d1?s=320)

#### [ericlaw](https://gravatar.com/ericlaw1979)

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my ow...
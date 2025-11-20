---
title: The Cloudflare Outage May Be a Security Roadmap
url: https://krebsonsecurity.com/2025/11/the-cloudflare-outage-may-be-a-security-roadmap/
source: Krebs on Security
date: 2025-11-19
fetch_date: 2025-11-20T03:10:24.305661
---

# The Cloudflare Outage May Be a Security Roadmap

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# The Cloudflare Outage May Be a Security Roadmap

November 19, 2025

[19 Comments](https://krebsonsecurity.com/2025/11/the-cloudflare-outage-may-be-a-security-roadmap/#comments)

An intermittent outage at **Cloudflare** on Tuesday briefly knocked many of the Internet’s top destinations offline. Some affected Cloudflare customers were able to pivot away from the platform temporarily so that visitors could still access their websites. But security experts say doing so may have also triggered an impromptu network penetration test for organizations that have come to rely on Cloudflare to block many types of abusive and malicious traffic.

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/cfoutage.png)

At around 6:30 EST/11:30 UTC on Nov. 18, Cloudflare’s status page acknowledged the company was experiencing “an internal service degradation.” After several hours of Cloudflare services coming back up and failing again, many websites behind Cloudflare found they could not migrate away from using the company’s services because the Cloudflare portal was unreachable and/or because they also were getting their domain name system (DNS) services from Cloudflare.

However, some customers did manage to pivot their domains away from Cloudflare during the outage. And many of those organizations probably need to take a closer look at their web application firewall (WAF) logs during that time, said **Aaron Turner**, a faculty member at **IANS Research**.

Turner said Cloudflare’s WAF does a good job filtering out malicious traffic that matches any one of [the top ten types of application-layer attacks](https://owasp.org/Top10/2025/0x00_2025-Introduction/), including credential stuffing, cross-site scripting, SQL injection, bot attacks and API abuse. But he said this outage might be a good opportunity for Cloudflare customers to better understand how their own app and website defenses may be failing without Cloudflare’s help.

“Your developers could have been lazy in the past for SQL injection because Cloudflare stopped that stuff at the edge,” Turner said. “Maybe you didn’t have the best security QA [quality assurance] for certain things because Cloudflare was the control layer to compensate for that.”

Turner said one company he’s working with saw a huge increase in log volume and they are still trying to figure out what was “legit malicious” versus just noise.

“It looks like there was about an eight hour window when several high-profile sites decided to bypass Cloudflare for the sake of availability,” Turner said. “Many companies have essentially relied on Cloudflare for the [OWASP Top Ten](https://owasp.org/Top10/2025/0x00_2025-Introduction/) [web application vulnerabilities] and a whole range of bot blocking. How much badness could have happened in that window? Any organization that made that decision needs to look closely at any exposed infrastructure to see if they have someone persisting after they’ve switched back to Cloudflare protections.”

Turner said some cybercrime groups likely noticed when an online merchant they normally stalk stopped using Cloudflare’s services during the outage.

“Let’s say you were an attacker, trying to grind your way into a target, but you felt that Cloudflare was in the way in the past,” he said. “Then you see through DNS changes that the target has eliminated Cloudflare from their web stack due to the outage. You’re now going to launch a whole bunch of new attacks because the protective layer is no longer in place.”

**Nicole Scott**, senior product marketing manager at the McLean, Va. based **Replica Cyber**, called yesterday’s outage “a free tabletop exercise, whether you meant to run one or not.”

“That few-hour window was a live stress test of how your organization routes around its own control plane and shadow IT blossoms under the sunlamp of time pressure,” Scott said in [a post](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7396624084958146560/) on LinkedIn. “Yes, look at the traffic that hit you while protections were weakened. But also look hard at the behavior inside your org.”

Scott said organizations seeking security insights from the Cloudflare outage should ask themselves:

1. What was turned off or bypassed (WAF, bot protections, geo blocks), and for how long?
2. What emergency DNS or routing changes were made, and who approved them?
3. Did people shift work to personal devices, home Wi-Fi, or unsanctioned Software-as-a-Service providers to get around the outage?
4. Did anyone stand up new services, tunnels, or vendor accounts “just for now”?
5. Is there a plan to unwind those changes, or are they now permanent workarounds?
6. For the next incident, what’s the intentional fallback plan, instead of decentralized improvisation?

In [a postmortem](https://blog.cloudflare.com/18-november-2025-outage/) published Tuesday evening, Cloudflare said the disruption was not caused, directly or indirectly, by a cyberattack or malicious activity of any kind.

“Instead, it was triggered by a change to one of our database systems’ permissions which caused the database to output multiple entries into a ‘feature file’ used by our Bot Management system,” Cloudflare CEO **Matthew Prince** wrote. “That feature file, in turn, doubled in size. The larger-than-expected feature file was then propagated to all the machines that make up our network.”

Cloudflare estimates that roughly 20 percent of websites use its services, and with much of the modern web relying heavily on a handful of other cloud providers including **AWS** and **Azure**, even a brief outage at one of these platforms can create a single point of failure for many organizations.

**Martin Greenfield**, CEO at the IT consultancy **Quod Orbis**, said Tuesday’s outage was another reminder that many organizations may be putting too many of their eggs in one basket.

“There are several practical and overdue fixes,” Greenfield advised. “Split your estate. Spread WAF and DDoS protection across multiple zones. Use multi-vendor DNS. Segment applications so a single provider outage doesn’t cascade. And continuously monitor controls to detect single-vendor dependency.”

*This entry was posted on Wednesday 19th of November 2025 09:07 AM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[Aaron Turner](https://krebsonsecurity.com/tag/aaron-turner/) [CloudFlare](https://krebsonsecurity.com/tag/cloudflare/) [IANS Research](https://krebsonsecurity.com/tag/ians-research/) [Martin Greenfield](https://krebsonsecurity.com/tag/martin-greenfield/) [Matthew Prince](https://krebsonsecurity.com/tag/matthew-prince/) [Nicole Scott](https://krebsonsecurity.com/tag/nicole-scott/) [OWASP Top 10](https://krebsonsecurity.com/tag/owasp-top-10/) [Quod Orbis](https://krebsonsecurity.com/tag/quod-orbis/) [Replica Cyber](https://krebsonsecurity.com/tag/replica-cyber/)

Post navigation

[← Microsoft Patch Tuesday, November 2025 Edition](https://krebsonsecurity.com/2025/11/microsoft-patch-tuesday-november-2025-edition/)

## 19 thoughts on “The Cloudflare Outage May Be a Security Roadmap”

1. DadJokes78 [Novembe...
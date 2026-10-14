---
title: Attacker Chains Three Ivanti Connect Secure Zero-Days for Root Access, Only Two Patched So Far
url: https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html
source: The Hacker News
date: 2026-10-13
fetch_date: 2026-10-14T06:53:24.280348
---

# Attacker Chains Three Ivanti Connect Secure Zero-Days for Root Access, Only Two Patched So Far

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Attacker Chains Three Ivanti Connect Secure Zero-Days for Root Access, Only Two Patched So Far](https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html)

**Swati Khandelwal**Oct 13, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZSH26NsXmSsQGaAbhNyJLMaBQKFCmabIbFZ_yi2sUGXjHQOVztQEQfXLarEAx1Fl9lRwGAryBE4zZEooJ4cochODcB4x8wQnPl3MRWiyBcpyEV6i8VPxvwcLHmShQVZVhuOcTjMXRhHAlx4Y0Uo85c74EVU4cea84YgXju02I9jlNzcGOFtLfa_am82Q/s1700-nu-rw-lo-l85-e365/ivanti-hack.jpg)

An attacker chained three zero-day flaws in Ivanti Connect Secure, a VPN appliance, to run commands as root without logging in, security firm [Volexity said](https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/) on October 13. Ivanti has released fixes for two of the flaws and told customers on affected versions to "act immediately." A fix for the third is still pending, according to Volexity.

Volexity, which reported the flaws to Ivanti, found the attack on one customer's appliance. The appliance was fully patched at the time and running version 22.8R2.4. The attacker, which Volexity tracks as UTA0576, began exploiting it on October 3.

[Ivanti said](https://www.ivanti.com/en-gb/blog/october-2026-security-update) on October 13 that it is aware of "limited exploitation in the wild."

The first two flaws are an authentication bypass and a remote code execution flaw, tracked together as [CVE-2026-104935](https://www.cve.org/CVERecord?id=CVE-2026-104935). Together they let an attacker run code as the appliance's cgi-server user, and the third flaw, a privilege escalation, raises that to root, Volexity said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The CVE record Ivanti filed shows which Connect Secure versions are affected:

* **Affected:** Connect Secure "before version 25.1.3.0"
* **Not affected:** version 22.7R2.14 "or prior"
* **Listed as unaffected:** versions 22.8R2.5, 25.1.3.0 and 25.1.3.1

Ivanti's [security advisory](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935) has more on the affected versions and the fixes.

The [release notes for 25.1.3.0](https://help.ivanti.com/ps/help/en_US/ICS/25.1.x/25.1.3.0/25.xICSRN.pdf) are dated July 2026. Customers already on that version are outside the range the CVE record gives.

Ivanti is working on a fix for the privilege escalation flaw, which will come "in a future release in the coming weeks," Volexity said. Its report does not say what risk that flaw carries on an appliance where the first two are fixed.

Ivanti tells customers to upgrade and to run its Integrity Checker Tool regularly. That tool misses this chain, Volexity said, because the exploit changes library code only in memory and restores the configuration data it alters. The attacker also took steps to stay hidden from the tool.

Confirming a compromise takes forensic investigation, including network and memory forensics, according to Volexity. These signs come from the one incident it investigated:

* **URL path:** /dana-na/auth/url\_default/welcome.cgi, requested in large numbers
* **HTTP header:** X-DSCGI-PATH on those requests, with a value that does not match the URL path
* **Directory:** /data/.icscap/
* **IP:** 108.165.147[.]64, the host the attacker used

In that incident, the attacker stole stored credentials, including LDAP domain credentials, searched Active Directory for passwords, and ran password-spraying attacks against its accounts. No backdoor or web shell was left behind. The attacker reran the entire exploit chain for each command.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Volexity's report and Ivanti's post do not name a temporary workaround for customers who cannot upgrade yet. They also do not say whether upgrading removes access an attacker has already gained.

Volexity assessed with low confidence that UTA0576's motive is criminal, not espionage. Neither company said how many customers were attacked.

Ivanti rates CVE-2026-104935 8.6 out of 10 on the CVSS severity scale. In its own entry in the CVE record, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) marks exploitation as "active" and the technical impact as "total."

Separately, the same Ivanti post covers fixes for two other products, Xtraction and Neurons Patch for Intune, and Ivanti said it is not aware of those flaws being exploited. Each has a flaw Ivanti rates 9.9 out of 10: [CVE-2026-106042](https://www.cve.org/CVERecord?id=CVE-2026-106042) in Xtraction before version 2026.4, and [CVE-2026-109412](https://www.cve.org/CVERecord?id=CVE-2026-109412) in Neurons Patch for Intune.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Authentication Security](https://thehackernews.com/search/label/Authentication%20Security), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [network security](https://thehackernews.com/search/label/network%20security), [Vul...
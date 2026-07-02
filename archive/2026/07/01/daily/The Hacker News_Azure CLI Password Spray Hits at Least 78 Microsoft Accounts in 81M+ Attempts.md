---
title: Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts
url: https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
source: The Hacker News
date: 2026-07-01
fetch_date: 2026-07-02T05:58:23.270542
---

# Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts](https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html)

**Ravie Lakshmanan**Jul 01, 2026Password Security / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlhMdp0ML_DO3inv2zhyphenhyphenoZ9CmB1ESRBbVh_YHPol3serW7D4zTsXPGVjF62GhEcvamH6fmTs0ZLguVOM72ynrL6ebpPxBgpCv3XeUJNCb4un1Ue4o1V5BjB4r9pEnW_t717d8d49ZdH4OPavLgNkov9VNaJDMruqwG65QoBkxpzFx8q7QofYHuH9gDie-O/s1700-e365/login.jpg)

Cybersecurity researchers have warned of a "massive, ongoing, automated password spray attack" aimed at Microsoft's Azure command-line interface (CLI), compromising dozens of accounts in the process.

The activity, per [Huntress](https://www.huntress.com/blog/lshiy-password-spray-attack), originates from an IPv6 address range ([2a0a:d683::/32](https://bgp.he.net/net/2a0a%3Ad683%3A%3A/32)) controlled by internet infrastructure provider [LSHIY LLC](https://bgp.he.net/AS32167#_prefixes6) (AS32167).

"Between June 12 and June 26, the threat actor behind it made more than 81 million login attempts and successfully compromised at least 78 Microsoft accounts across 64 organizations," the company said in a statement. "The targeting of these attacks seems to be based entirely on password prevalence on compromised password combo lists, and is not specific to business type or industry."

What makes the password spray attack noteworthy is not only the scale, but also the fact that many of the compromised organizations had Conditional Access policies enabled. Specifically, the campaign has been found to leverage a deprecated OAuth flow called Resource Owner Password Credentials (ROPC) to bypass Conditional Access Policy (CAP) protections.

[ROPC](https://auth0.com/docs/get-started/authentication-and-authorization-flow/resource-owner-password-flow) is a legacy OAuth 2.0 grant type where a user directly provides their username and password to a client application, which then sends these credentials to an authorization server to exchange them for an access token. It was deprecated in OAuth 2.1.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

In its documentation, Microsoft recommends customers against using the ROPC flow, arguing it's incompatible with multi-factor authentication (MFA).

"In most scenarios, more secure alternatives are available and recommended," the tech giant [says](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth-ropc). "This flow requires a very high degree of trust in the application, and carries risks that aren't present in other flows. You should only use this flow when more secure flows aren't viable."

The credential and token spray attacks are said to have resulted in a handful of successful logins per day between June 12 and 21, 2026, averaging two to four accounts being compromised daily, with the exception of June 19, when 12 user accounts (aka identities) were compromised. The steady cadence changed on June 22, with 30 identities across 23 businesses impacted.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQUx7KMPKzFOvJtti1B3Cf_EDXqPLn9Bd625_Wyhxi14AcT4ARcASD8qtOWbKsNS_yErwX5AhwMZbypZTKeOSuYuTWjwExQIZ0CNP4ECbYHeBGrNWnkpi7wKvcCopVPVwne5NSUn1ABHeYLFUyH5W19EfJo7b_F6YTHfowRb2VcW3UDgjfV5QUyBIg5FI7/s1700-e365/ls.jpg)

In all, 78 user accounts were compromised across 64 organizations as part of the campaign. The vast majority of the password spraying activity emanated from LSHIY LLC. Some of the IP addresses resolve to the U.S., while a few others resolve to China.

"These attacks are part of a large wave of credential spray attacks across a few different ASNs," Huntress said, adding it has witnessed the volume of credential spray attacks surge by over 155 times across its customer base. "Attacks surged in particular in late May through early June, with a current mean value of about 1,964 failed attacks per month per Huntress-protected tenant."

The activity appears to specifically weaponize old username/password combinations that were previously breached but had never been rotated. The use of the ROPC vector meant that the attackers were able to target enterprises that had implemented MFA, but it wasn't enforced or configured to account for Azure CLI ROPC logins.

This included scenarios where MFA wasn't triggered -

* Enforcing MFA only for specific apps, as opposed to "All Cloud Apps," thereby failing to cover Azure CLI logins used by the threat actors
* Enforcing MFA only for specific user groups, such as Admins
* Enforcing MFA only when requests originate from non-trusted locations

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

"It's worth noting that eight businesses impacted by the campaign had no MFA policy at all," Huntress said. "While threat actors in this campaign were able to get in despite MFA being set up, the takeaway should not be that MFA doesn't work at all; instead, organizations should ensure that their MFA policies are properly configured to address the authorization flow used across these incidents."

To counter this line of attack, organizations are advised to require MFA for All Users, All Cloud Apps, and All Client App types when enabling CAP, restrict the Azure CLI application for non-admin users, and prioritize response by credential validity.

"This attack reveals cracks in CAPs that haven't been appropriately configured," Huntress researchers concluded. "There are still potential weaknesses in how CAPs are deployed that can allow threat actors to slip through. One glaring error here is that legacy protocols like ROPC can...
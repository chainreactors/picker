---
title: OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials
url: https://thehackernews.com/2026/07/oauth-client-id-spoofing-lets-attackers.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:50:00.225555
---

# OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials

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

# [OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials](https://thehackernews.com/2026/07/oauth-client-id-spoofing-lets-attackers.html)

**Ravie Lakshmanan**Jul 14, 2026Cloud Security / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmB1bLC9cna7xlnvFdK0hUnsi8jeo6E7jMh20nj4XTvsF9ogpjbnlPCxx9QYQ1O2aS7JiSDQi4swIRNG6-Xjg2TGR4bn4Zn-KBkjsLTYcKUrXOD-rlGu4XYsvRx06eRqrT4duW0xwklKeYjZvRV1VSarJBKldBzN4DNhkWudVCGRdKPi9uVGrqEwL66mz5/s1700-e365/OAuth-ClientID.jpg)

At least two distinct threat actors are weaponizing a novel evasion technique called **OAuth client ID spoofing** in cloud campaigns, while slipping past telemetry.

The activity allows users to enumerate user accounts and validate stolen credentials in Microsoft Entra ID environments, without ever generating a successful sign-in event that would otherwise alert defenders. And bad actors have begun to exploit this gap to obtain unauthorized access to an organization's cloud services.

"A blind spot in cloud sign-in telemetry: Entra ID returns different error responses depending on whether a supplied OAuth client ID is valid," Proofpoint said in a statement. "Attackers exploit this to infer valid usernames and correct passwords at scale, effectively checking stolen credential lists without logging a successful login."

In other words, the attacks leverage the OAuth client ID, a globally unique identifier (GUID) assigned to applications when requesting access to user data, and is passed as "[client\_id](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow)" in authentication requests. By providing spoofed client IDs, it enables account enumeration without a registered OAuth application and permits attackers to infer both password and account validity without generating a successful sign-in event.

"The [Entra sign‑in logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins) are a primary telemetry source for identifying malicious authentication activity, including user enumeration, password spraying, and initial access attempts," Proofpoint researcher Rachel Rabin [said](https://www.proofpoint.com/us/blog/threat-insight/oauth-client-id-spoofing-why-fake-client-ids-are-gaining-traction-stealthy).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Threat clusters like [UNK\_CustomCloak](https://x.com/threatinsight/status/1976670442799939953) have been observed spoofing User-Agent strings to orchestrate brute-force campaigns targeting Microsoft Entra ID environments by exploiting a legacy, discontinued first-party application called Windows Live Custom Domains to bypass standard sign-in restrictions and probe user passwords across over 4,000 tenants.

But the latest efforts mark an evolution of this tradecraft by spoofing the OAuth client IDs via HTTP POST requests to Microsoft's OAuth 2.0 token endpoint using the Resource Owner Password Credentials ([ROPC](https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html)) flow. Specifically, this involves supplying a syntactically valid client ID but one that does not correspond to a real application.

In such scenarios, only the application ID is recorded in the Entra sign-in log without a corresponding application name. The response, which contains an Azure Active Directory Security Token Service ([AADSTS](https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes)) error code, can then be used to infer whether the account exists and whether the password is correct without a registered application.

"If the spoofed client ID is not a proper UUIDv4, Entra does not reject the request outright," Proofpoint explained. "Attackers can therefore analyze this error response to identify valid accounts and passwords, despite using malformed client IDs."

"When a spoofed client ID is used, no corresponding application name is recorded in the sign-in log. This means that detections that look for surges against a specific application name may miss this activity entirely, as the field is blank."

Armed with this information, attackers could identify accounts that could be exploited for stealthy access, at the same time making it challenging for defenders to identify suspicious activity.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

Proofpoint said it has identified two large campaigns that have independently adopted the technique towards the end of December 2025, indicating the approach is being increasingly incorporated into attacker tradecraft as opposed to being an isolated incident:

* **UNK\_pyreq2323** (from January to March 2026), which used more than 700,000 spoofed client IDs from Amazon Web Services (AWS) infrastructure to target more than 1 million accounts across nearly 4,000 tenants, causing lockouts for roughly 28% of targeted users due to failed attempts.
* **UNK\_OutFlareAZ** (starting Dec 2025), which leveraged Cloudflare infrastructure to target over 2 million users with 3.7 million randomized spoofed application IDs.

Both the campaigns have been observed using valid UUIDs rather than malformed identifiers and demonstrate patterns that align with precompiled username wordlists. That said, while UNK\_OutFlareAZ enumerated users alphabetically, UNK\_pyreq2323 did not. Another aspect in which they differed was in how the client IDs were spoofed.

UNK\_pyreq2323 is said to have modified the trailing digits of a known application ID, and then reused spoofed IDs across up to 12 users. In contrast, UNK\_OutFlareAZ generated a unique client ID per request.

"By fragmenting au...
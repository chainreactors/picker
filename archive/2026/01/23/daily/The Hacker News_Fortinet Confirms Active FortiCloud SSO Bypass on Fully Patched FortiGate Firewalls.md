---
title: Fortinet Confirms Active FortiCloud SSO Bypass on Fully Patched FortiGate Firewalls
url: https://thehackernews.com/2026/01/fortinet-confirms-active-forticloud-sso.html
source: The Hacker News
date: 2026-01-23
fetch_date: 2026-01-24T03:32:38.876034
---

# Fortinet Confirms Active FortiCloud SSO Bypass on Fully Patched FortiGate Firewalls

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

# [Fortinet Confirms Active FortiCloud SSO Bypass on Fully Patched FortiGate Firewalls](https://thehackernews.com/2026/01/fortinet-confirms-active-forticloud-sso.html)

**Ravie Lakshmanan**Jan 23, 2026Network Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWq72oFKp6biq3Hf_tsdl9xZeVhxI_BGzBaKfw1DiMD2ldey-KGb8qk27HJH9rt-pys9Ga94wnpRZfAYUdFW9g5_-ncNfIBaYtzsHD-GpGk0LtMaSZ0yD83PqptSkQlIuFNwa94qWlQvk3Yqz-eSpFchaeTh3VbYOXgRJ96sDTRz7dy-_ShXQu1jnzQXhx/s1600-e365/fortinet-exploit.jpg)

Fortinet has officially confirmed that it's working to completely plug a FortiCloud SSO authentication bypass vulnerability following reports of fresh exploitation activity on fully-patched firewalls.

"In the last 24 hours, we have identified a number of cases where the exploit was to a device that had been fully upgraded to the latest release at the time of the attack, which suggested a new attack path," Fortinet Chief Information Security Officer (CISO) Carl Windsor [said](https://www.fortinet.com/blog/psirt-blogs/analysis-of-sso-abuse-on-fortios) in a Thursday post.

The activity essentially mounts to a bypass for patches put in place by the network security vendor to address [CVE-2025-59718 and CVE-2025-59719](https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html), which could allow unauthenticated bypass of SSO login authentication via crafted SAML messages if the FortiCloud SSO feature is enabled on affected devices. The issues were originally addressed by Fortinet last month.

However, earlier this week, reports [emerged](https://thehackernews.com/2026/01/automated-fortigate-attacks-exploit.html) of renewed activity in which malicious SSO logins on FortiGate appliances were recorded against the admin account on devices that had been patched against the twin vulnerabilities. The activity is similar to [incidents](https://thehackernews.com/2025/12/fortinet-fortigate-under-active-attack.html) observed in December, shortly after the disclosure of the CVE-2025-59718 and CVE-2025-59719.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The activity involves the creation of generic accounts for persistence, making configuration changes granting VPN access to those accounts, and the exfiltration of firewall configurations to different IP addresses. The threat actor has been observed logging in with accounts named "cloud-noc@mail.io" and "cloud-init@mail.io."

As mitigations, the company is urging the following actions -

* Restrict administrative access of edge network device via the internet by applying a local-in policy
* Disable FortiCloud SSO logins by disabling "admin-forticloud-sso-login"

"It is important to note that while, at this time, only exploitation of FortiCloud SSO has been observed, this issue is applicable to all SAML SSO implementations," Fortinet said.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Firewall Security](https://thehackernews.com/search/label/Firewall%20Security)[Fortigate](https://thehackernews.com/search/label/Fortigate)[Fortinet](https://thehackernews.com/search/label/Fortinet)[network security](https://thehackernews.com/search/label/network%20security)[SAML](https://thehackernews.com/search/label/SAML)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Zero Trust](https://thehackernews.com/search/label/Zero%20Trust)

Trending News

[![⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More")

⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](https://thehackernews.com/2026/01/weekly-recap-fortinet-exploits-redline.html)

[![n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](data:image/svg+xml;base64... "n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens")

n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html)

[![New Advanced Linux VoidLink Malware Targets Cloud and container Environments](data:image/svg+xml;base64... "New Advanced Linux VoidLink Malware Targets Cloud and container Environments")

New Advanced Linux VoidLink Malware Targets Cloud and container Environments](https://thehackernews.com/2026/01/new-advanced-linux-voidlink-malware.html)

[![Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow](data:image/svg+xml;base64... "Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow")

Critical Node.js Vulnerability Can Cause Server Crashes via async\_hooks Stack Overflow](https://thehackernews.com/2026/01/critical-nodejs-vulnerability-can-cause.html)

[![Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution](data:image/svg+xml;base64... "Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution")

Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution](https://thehackernews.com/2026/01/fortinet-fixes-critical-fortisiem-flaw.html)

[![Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without Login](data:image/svg+xml;base64... "Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls ...
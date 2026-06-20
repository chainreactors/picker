---
title: CISA Warns Fortinet Customers as FortiBleed Hits 86,644 FortiGate Devices
url: https://thehackernews.com/2026/06/cisa-warns-fortinet-customers-as.html
source: The Hacker News
date: 2026-06-19
fetch_date: 2026-06-20T06:14:42.750618
---

# CISA Warns Fortinet Customers as FortiBleed Hits 86,644 FortiGate Devices

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [CISA Warns Fortinet Customers as FortiBleed Hits 86,644 FortiGate Devices](https://thehackernews.com/2026/06/cisa-warns-fortinet-customers-as.html)

**Ravie Lakshmanan**Jun 19, 2026Threat Intelligence / Firewall Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0NmhjowFYAIQws_hl2u1bMpkeyma6TUk8UumS90AdqbBjW_NJ5h97i1yV9uJ_GT6zT8A9jaruiGkhqvn0jb4LuaHDDbGtjZbB7tQQibuQmH4WTDeAI898xZnyDuUQOAvzPHooO7C2S2PQFPIvkmwZ8LTLO4xLUP5ygQVuZI3E0quggcAEvtOqKzx4zKdw/s1700-e365/cisa-fortinet.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Thursday [urged](https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure) Fortinet customers with FortiGate appliances to take steps to secure against ongoing malicious activity aimed at thousands of internet-accessible devices.

The sweeping campaign, believed to be the work of Russian-speaking threat actors, has been codenamed **[FortiBleed](https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html)**. The number of compromised devices stands at 86,644 as of June 19, 2026.

According to data from SOCRadar, generic admin accounts (35%) and built-in Fortinet system accounts (28.3%) together make up the majority of compromised credentials. Organization-specific accounts account for 36.7% of the remaining breached credentials.

"This points directly to a widespread failure to rename default accounts or rotate factory credentials, giving the attacker a highly reliable target list before any brute force was even needed," SOCRadar said.

"Org-specific accounts topping the list is significant. It means the attacker is not just harvesting default credentials but has also successfully compromised accounts created by the organizations themselves, possibly sourced from prior breaches where passwords were never changed."

Telecom, government, and education have emerged as the top three impacted sectors, with the most exposures located in India, the U.S., Mexico, Colombia, and Thailand.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The threat actor is said to have mass-scanned the internet for Fortinet remote login endpoints, and then employed a bespoke tool to spray those identified endpoints with known login and password combinations in an attempt to break into them.

The fully-automated attack is built around a self-sustaining, two-step approach -

* The threat actor attempts a curated list of leaked Fortinet passwords against devices across the internet.
* Once access is obtained, they passively monitor network traffic going through the devices to collect additional credentials, which are then used to compromise more appliances.

The credentials are legitimate and valid, with the attackers verifying each of them before they are added to a database of confirmed, working logins.

"The scale of this breach touches nearly every sector of the global economy, sparing no industry," Hudson Rock [said](https://www.infostealers.com/article/fortibleed-75000-fortinet-firewalls-compromised-global-enterprises-exposed-claim-your-ethical-disclosure/). "The threat actors have built a verified database of working credentials for some of the largest enterprises on the planet."

The U.K. National Cyber Security Centre (NCSC) has [described](https://www.ncsc.gov.uk/news/advice-following-global-targeting-of-fortinet-firewalls-and-vpn-gateways) FortiBleed as a global campaign targeting internet-facing Fortinet firewalls and VPN gateways using methods like brute-force, dictionary attack, and credential stuffing.

It's suspected that the threat actors likely exploited older credential hashing mechanisms and the way credentials have historically been stored within FortiGate configuration files to pull off the large-scale attack.

"Fortinet introduced PBKDF2-based password hashing for administrator credentials in FortiOS 7.2.11, 7.4.8, and 7.6.1, replacing the legacy SHA-256-based storage mechanism," Arctic Wolf [said](https://arcticwolf.com/resources/blog/active-fortibleed-campaign-impacting-fortinet-devices-across-194-countries/). "However, when upgrading from earlier versions, existing administrator passwords remain stored as SHA-256 hashes until the corresponding administrator successfully logs in following the upgrade."

"As a result, many organizations likely continue to store administrator credentials using older SHA-256 with Salt hashing mechanisms."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

In a statement shared with The Hacker News, a Fortinet spokesperson said "the data involved is likely a resharing of data from previous incidents, as well as brute-forcing of credentials, and not related to any current incident or advisory," urging organizations to follow best practices, including regularly rotating security credentials and enabling multi-factor authentication (MFA).

CISA has outlined the following recommendations to defend against the activity -

* Terminate all active SSL VPN and administrative sessions, reset all Fortinet VPN and administrative passwords, especially on internet-facing systems, and enforce strong password policies.
* Ensure use of the Password-Based Key Derivation Function 2 ([PBKDF2](https://community.fortinet.com/fortigate-3/technical-tip-enforcing-pbkdf2-as-hash-function-for-administrator-accounts-in-fortios-v7-2-11-and-later-220652)) algorithm to store administrator credentials and remove weaker legacy hashes.
* Review firewall, VPN, authentication, and domain controller logs for signs of suspicious actions, including unauthorized configuration changes.
* Enable phishing-resistant MFA on all external gateways and administrative interfaces.
* Reduce the attack surface and lock down management.

The FortiBleed incident first came to light last week after security researcher Volodymyr "Bob" Diachenko discovered a server containing the datab...
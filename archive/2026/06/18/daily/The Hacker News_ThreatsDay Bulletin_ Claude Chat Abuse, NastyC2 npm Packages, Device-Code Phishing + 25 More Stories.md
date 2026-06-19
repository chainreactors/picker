---
title: ThreatsDay Bulletin: Claude Chat Abuse, NastyC2 npm Packages, Device-Code Phishing + 25 More Stories
url: https://thehackernews.com/2026/06/threatsday-bulletin-claude-chat-abuse.html
source: The Hacker News
date: 2026-06-18
fetch_date: 2026-06-19T07:09:17.092958
---

# ThreatsDay Bulletin: Claude Chat Abuse, NastyC2 npm Packages, Device-Code Phishing + 25 More Stories

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

# [ThreatsDay Bulletin: Claude Chat Abuse, NastyC2 npm Packages, Device-Code Phishing + 25 More Stories](https://thehackernews.com/2026/06/threatsday-bulletin-claude-chat-abuse.html)

**Ravie Lakshmanan**Jun 18, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6k3CSWsyKHS6UdXmxX-w92fdsWjTSL7JR7xeaPBPh8d5G6rkZbMhmJHr9o3gxF5G2I2GojubOJnzhRqxjtKYxlXTrmlgrdRFRrmmyEEIi_zXAQXT3zpq5KNQqOFHrfGKhUFHzsMx1E2Eqs7S_jvTFfN3Jnz1YO58Ryvk0urKEDUZggoQgI07lKFWQDMfw/s1700-e365/threatss.jpg)

The internet did not break this week. It got used exactly as designed, which is worse.

Searches were siphoned through shady browser add-ons. AI chat links turned into malware delivery paths. macOS attacks ran in memory and left almost nothing behind. Cloud agents looked like helpers until attackers treated them like open shells.

Add exposed edge gear, poisoned packages, cash courier scams, stealers, loaders, and phishing that barely bothers pretending anymore. Here’s the full mess.

1. DoH lands in Windows Server 2025

   [Microsoft Makes DoH Generally Available on Windows DNS Server](https://techcommunity.microsoft.com/blog/networkingblog/doh-is-now-generally-available-on-windows-dns-server/4526839)

   Microsoft has announced that DNS-over-HTTPS (DoH) for Windows DNS Server is generally available on Windows Server 2025 for client-to-server DNS traffic. "With general availability, organizations can now deploy encrypted and authenticated client-to-resolver DNS traffic directly within their existing on-premises DNS infrastructure," the company [said](https://techcommunity.microsoft.com/blog/networkingblog/doh-is-now-generally-available-on-windows-dns-server/4526839). "The goal is to help improve privacy, reduce spoofing risk, and advance Zero Trust DNS without requiring a new resolver architecture. Enabling DoH on Windows DNS Server introduces encrypted communication for supported clients over HTTPS while preserving compatibility with most existing DNS deployments. Organizations can expect DoH traffic between DoH clients and Windows DNS Server to be encrypted via TLS, DNS queries to be transported as HTTPS requests, existing DNS functionality to continue operating as expected, and mixed environments, encrypted and traditional DNS, to be supported."
2. Search hijacks hide monetization layer

   [SearchJack Extensions Monetize Users' Searches](https://malext.io/reports/SearchJack/)

   A cluster of 23 deceptive Chrome browser extensions has been found stealthily overriding users' default search engines and routing queries through monetization middleware before delivering results. "Each extension presents a different advertised purpose - satellite imagery, productivity tools, news readers, maps – while the actual business is search affiliate revenue," security researcher Jean-Marie R. [said](https://malext.io/reports/SearchJack/). "The campaign spans at least 8 distinct monetization brokers and ~758,000 affected users. While this might look like simple adware, it is a real security risk. First, it is a massive privacy violation: every search a user makes is sent to anonymous third-party brokers. Second, because the operators control the web traffic, they can easily switch from showing regular search results to injecting phishing links or malicious downloads at any time – all without ever updating the extension code itself."
3. Fileless macOS ClickFix attack chain

   [macOS ClickFix Lures Deliver AppleScript Stealer and RAT](https://www.netskope.com/blog/macos-clickfix-lures-deploy-applescript-stealer-persistent-rat)

   A Russian-speaking attacker has been observed targeting victims mainly in Asia, North America, and Oceania across technology, media, and business services sectors using [ClickFix](https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html) lures to deliver an AppleScript-based infostealer to macOS users. The ClickFix pages masquerade as downloads for a malware scanning utility. "To evade detection, the entire infection chain, starting from the initial clipboard paste to payload execution, is completely fileless, leaving no static artifacts on disk until persistence is established," Netskope Threat Labs [said](https://www.netskope.com/blog/macos-clickfix-lures-deploy-applescript-stealer-persistent-rat). "Victims are socially engineered into executing a curl command that fetches a gzip-compressed stager, which pipes the second-stage AppleScript directly into osascript memory." The second-stage, codenamed "Meow (DEBUG)," uses a fake system dialog to harvest credentials, browser data, session cookies, and keychain contents. It's also equipped with capabilities to trojanize legitimate desktop cryptocurrency wallet applications and maintain persistent command-and-control (C2) access, allowing the operator to run arbitrary payloads.
4. Claude chat abuse fuels malware delivery

   [Claude Shared Chats Abused for ClickFix Malvertising Campaign](https://www.trendmicro.com/en_us/research/26/f/claudeai-shared-chat-abused-in-malvertising.html)

   In another ClickFix campaign, threat actors have been spotted weaponizing Anthropic Claude's [shared chat feature](https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html#ai-chat-guides-spread-stealers), abusing the trust associated with a legitimate domain to deliver the [MacSync](https://thehackernews.com/2025/12/new-macsync-macos-stealer-uses-signed.html) credential-stealing malware. "Cybercriminals hijacked Google Ads searches for popular AI developer tools to funnel over 2,000 victims toward malicious download pages before quietly moving their operation onto claude.ai's own platform, turning the trusted domain into a delivery mechanism for credential-stealing malware," Trend Micro [said](https://www.trendmicro.com/en_us/research/26/f/claudeai-shared-chat-abused-in-malvertising.html). "The Asia-Pacific region bore the brunt of the campaign, accounting for 67.2% of all confir...
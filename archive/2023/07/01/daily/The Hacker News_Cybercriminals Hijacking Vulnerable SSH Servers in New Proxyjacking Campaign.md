---
title: Cybercriminals Hijacking Vulnerable SSH Servers in New Proxyjacking Campaign
url: https://thehackernews.com/2023/06/cybercriminals-hijacking-vulnerable-ssh.html
source: The Hacker News
date: 2023-07-01
fetch_date: 2025-10-04T11:57:24.163468
---

# Cybercriminals Hijacking Vulnerable SSH Servers in New Proxyjacking Campaign

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Cybercriminals Hijacking Vulnerable SSH Servers in New Proxyjacking Campaign](https://thehackernews.com/2023/06/cybercriminals-hijacking-vulnerable-ssh.html)

**Jun 30, 2023**Ravie LakshmananServer Security / Cyber Threat

[![Proxyjacking Campaign](data:image/png;base64... "Proxyjacking Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ0Tr0FQXKBrWcLfAvG-bE1p5pe09JUuh0mRp6ilpyJjPCgHpeJ3wsd3sWIOHFcTzO_lPr8xoxGAhMDBlHkjSo5yxcVPWLFaJBg1FFFDDaIofuPBKc6rJTqGlLY6CYJu0Bwc1en0L7dPVExy7YJZ7KBxjk6tun548eqb9koc7jf0tDhJNMQVfuPkp-YqA/s790-rw-e365/ssh.jpg)

An active financially motivated campaign is targeting vulnerable SSH servers to covertly ensnare them into a proxy network.

"This is an active campaign in which the attacker leverages SSH for remote access, running malicious scripts that stealthily enlist victim servers into a peer-to-peer (P2P) proxy network, such as Peer2Profit or Honeygain," Akamai researcher Allen West [said](https://www.akamai.com/blog/security-research/proxyjacking-new-campaign-cybercriminal-side-hustle) in a Thursday report.

Unlike cryptojacking, in which a compromised system's resources are used to illicitly mine cryptocurrency, proxyjacking offers the ability for threat actors to leverage the victim's unused bandwidth to clandestinely run different services as a P2P node.

This offers two-fold benefits: It not only enables the attacker to monetize the extra bandwidth with a significantly reduced resource load that would be necessary to carry out cryptojacking, it also reduces the chances of discovery.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"It is a stealthier alternative to cryptojacking and has serious implications that can increase the headaches that proxied [Layer 7 attacks](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/) already serve," West said.

To make matters worse, the anonymity provided by [proxyware services](https://thehackernews.com/2023/05/captcha-breaking-services-with-human.html) can be a double-edged sword in that they could be abused by malicious actors to obfuscate the source of their attacks by routing traffic through intermediary nodes.

[![Proxyjacking Campaign](data:image/png;base64... "Proxyjacking Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6C9eSEnz9UqwE1nO_RKXP5y943t2bHHM7L95aq8mhEwFRZSHpbxE9IOZBDINFNaCaWWsHY8-M5rN3qjqTKmqc6at6LV4KVJGaXQyZsGUF_22_qwIpV1TUhdvLa9wdpX2kCKIzah5qwFpD4WnIsEOUSkhBk8ahPZH9DNysbdKr60bh1dsGv0r09_bseNE/s790-rw-e365/proxyware.jpg)

Akamai, which discovered the latest campaign on June 8, 2023, said the activity is designed to breach susceptible [SSH servers](https://www.akamai.com/blog/security-research/linux-lateral-movement-more-than-ssh) and deploy an obfuscated Bash script that, in turn, is equipped to fetch necessary dependencies from a compromised web server, including the curl command-line tool by camouflaging it as a CSS file ("csdark.css").

The stealthy script further actively searches for and terminates competing instances running bandwidth-sharing programs, before launching Docker services that share the victim's bandwidth for profits.

A further examination of the web server has revealed that it's also being used to host a cryptocurrency miner, suggesting that the threat actors are dabbling in both cryptojacking and proxyjacking attacks.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

While proxyware is not inherently nefarious, Akamai noted that "some of these companies do not properly verify the sourcing of the IPs in the network, and even occasionally suggest that people install the software on their work computers."

But such operations can also transcend into the realm of cybercrime when the applications are installed without the users' knowledge or consent, thereby allowing the threat actor to control several systems and generate illegitimate revenue.

"Old techniques remain effective, especially when paired with new outcomes," West said. "Standard security practices remain an effective prevention mechanism, including strong passwords, patch management, and meticulous logging."

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

[Akamai](https://thehackernews.com/search/label/Akamai)[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[layer 7 ddos attack](https://thehackernews.com/search/label/layer%207%20ddos%20attack)[Proxyjacking](https://thehackernews.com/search/label/Proxyjacking)[Proxyware](https://thehackernews.com/search/label/Proxyware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw...
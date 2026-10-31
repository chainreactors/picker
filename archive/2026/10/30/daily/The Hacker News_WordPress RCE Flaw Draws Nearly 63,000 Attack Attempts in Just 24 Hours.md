---
title: WordPress RCE Flaw Draws Nearly 63,000 Attack Attempts in Just 24 Hours
url: https://thehackernews.com/2026/10/wordpress-rce-flaw-draws-nearly-63000.html
source: The Hacker News
date: 2026-10-30
fetch_date: 2026-10-31T07:49:06.664668
---

# WordPress RCE Flaw Draws Nearly 63,000 Attack Attempts in Just 24 Hours

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [WordPress RCE Flaw Draws Nearly 63,000 Attack Attempts in Just 24 Hours](https://thehackernews.com/2026/10/wordpress-rce-flaw-draws-nearly-63000.html)

**Ravie Lakshmanan**Oct 30, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhf-pzflJO9HQoCdvBvYNtS12gwwEjAbM4dQ30ak7UYaIPzsVPN9MlFwvIDEFkbe9cWg4wQRFPbGfJ0YXjzGcBS6mUTwttwkQ8IR7OoHyTz3owZkVzYQOAObyJUqfjsC-PqMw2pv41_m68hb6ZkwJb56kGx-Ypv7GWZBtDzjyTTQ8L8i9NxA8_MDVoJSEba/s1700-nu-rw-lo-l85-e365/wp-hack.jpg)

Threat actors have been observed attempting to exploit a high-severity security flaw in WordPress Core shortly after patches were released.

The [vulnerability](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-4w3m-c66w-69mg), which does not have a CVE identifier, relates to a case of remote code execution impacting WordPress Core versions 4.7 through 7.1.3. It carries a CVSS score of 8.1 on the CVSS scoring system. Patches for the flaw were [released](https://wordpress.org/news/2026/10/wordpress-7-1-4/) on October 28, 2026.

"This is due to predictable, web-accessible staging paths used during full-package core upgrades," Wordfence [said](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/). "This makes it possible for unauthenticated attackers to execute code on the server during the upgrade window."

The WordPress security company noted that successful exploitation requires an "attacker to hit a very narrow window while WordPress is unpacking a complete Core update."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

The issue boils down to the fact that affected versions unpack new files part of a full-package Core update into a predictable directory under "wp-content/upgrade." This copy also includes the WordPress installer.

"Because the staging directory is web-accessible on many servers, an unauthenticated attacker who requests the installer at precisely the right moment can interact with the staged WordPress copy and progress to PHP code execution," Alex Thomas, who leads the Wordfence Threat Response Team, said.

A threat actor who is able to win the race condition can gain the ability to execute code on the server, assuming the following conditions are met -

* A full-package update containing the installer files
* Public web and PHP access to the staging tree
* A predictable or discovered staging path, and
* Adequate time to complete the attack before WordPress cleans up the temporary files

Although that window has been observed to last only seconds in normal lab environments, threat actors are polling vulnerable paths, such as "setup-config.php," repeatedly in an attempt to trigger the flaw. Over the past 24 hours, Wordfence said it has [blocked 62,969 attacks](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-core/wordpress-core-470-713-unauthenticated-upgrade-window-staged-installer-remote-code-execution) targeting the vulnerability.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

"Two of the largest sources repeatedly polled small groups of sites for roughly 14.5 hours, behavior consistent with trying to catch the brief upgrade window," Thomas said. "Other sources tested many staging-directory and version-name variations."

"Not every request used the exact vulnerable path, but the sustained polling and exact-layout probes show that attackers quickly understood the race condition and began targeting it."

With active exploitation attempts already underway, WordPress site owners are advised to update to version 7.1.4 as soon as possible and look for suspicious requests to PHP files located under "wp-content/upgrade," as well as unfamiliar administrator accounts, plugins, or PHP files.

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security), [WordPress](https://thehackernews.com/search/label/WordPress)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Unpatched Broadcom Wi-Fi Flaw Lets Attackers in Range Run Code as Root on Routers](https://thehackernews.com/2026/10/unpatched-broadcom-wi-fi-flaw-lets.html)

[![The Hacker News](data:image/svg+xml;base64...)

OpenCode Console Breach May Have Exposed OpenAI, Anthropic, and Google API Keys](https://thehackernews.com/2026/10/opencode-console-breach-may-have.html)

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: 98 Zero-Days, Rogue AI Agents, $100M Crypto Theft, 700 Supermarkets Hit and More](https://thehackernews.com/2026/10/weekly-recap-98-zero-days-rogue-ai.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Exploit Plex2Shell Flaws to Install Crypto Miners and Linux Proxy Backdoor](https://thehackernews.com/2026/10/hackers-exploit-plex2shell-flaws-to.html)

[![The Hacker News](data:image/svg+xml;base64...)

Hackers Hijack Five OVHcloud CLI Releases to Distribute Secret-Stealing Malware](https://thehack...
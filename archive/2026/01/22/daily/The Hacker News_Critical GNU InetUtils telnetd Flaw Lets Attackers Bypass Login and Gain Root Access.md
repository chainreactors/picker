---
title: Critical GNU InetUtils telnetd Flaw Lets Attackers Bypass Login and Gain Root Access
url: https://thehackernews.com/2026/01/critical-gnu-inetutils-telnetd-flaw.html
source: The Hacker News
date: 2026-01-22
fetch_date: 2026-01-23T03:33:35.956559
---

# Critical GNU InetUtils telnetd Flaw Lets Attackers Bypass Login and Gain Root Access

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

# [Critical GNU InetUtils telnetd Flaw Lets Attackers Bypass Login and Gain Root Access](https://thehackernews.com/2026/01/critical-gnu-inetutils-telnetd-flaw.html)

**Ravie Lakshmanan**Jan 22, 2026Vulnerability / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgswkkor42PbpMA2JvEug_zR_BOp1L3DrLlZ8GqcxlJchqNGqZZT7ndgNE51CVPI5YEhi1js3MsyDOYVmA19EKWA330OszynMa9IJpHJzDXtZ3iET5VPrCkCZHOZ2jhnV114UijsA4b2tgGiT8XBD7eRpZ9Su9UAYy-ay9qsmrysuw-v3KOIJkkhCXjStP7/s1600-e365/linux-unix.jpg)

A critical security flaw has been disclosed in the GNU InetUtils telnet daemon ([telnetd](https://linux.die.net/man/8/telnetd)) that went unnoticed for nearly 11 years.

The vulnerability, tracked as **[CVE-2026-24061](https://nvd.nist.gov/vuln/detail/CVE-2026-24061)**, is rated 9.8 out of 10.0 on the CVSS scoring system. It affects all versions of GNU InetUtils from version 1.9.3 up to and including version 2.7.

"Telnetd in GNU Inetutils through 2.7 allows remote authentication bypass via a '-f root' value for the USER environment variable," according to a description of the flaw in the NIST National Vulnerability Database (NVD).

In a [post](https://seclists.org/oss-sec/2026/q1/89) on the oss-security mailing list, GNU contributor Simon Josefsson said the vulnerability can be exploited to gain root access to a target system -

*The telnetd server invokes /usr/bin/login (normally running as root) passing the value of the USER environment variable received from the client as the last parameter.*

*If the client supply [sic] a carefully crafted USER environment value being the string "-f root", and passes the telnet(1) -a or --login parameter to send this USER environment to the server, the client will be automatically logged in as root bypassing normal authentication processes.*

*This happens because the telnetd server do [sic] not sanitize the USER environment variable before passing it on to login(1), and login(1) uses the -f parameter to by-pass normal authentication.*

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

Josefsson also noted that the vulnerability was introduced as part of a [source code commit](https://codeberg.org/inetutils/inetutils/commit/fa3245ac8c288b87139a0da8249d0a408c4dfb87) made on March 19, 2015, which eventually made it to version 1.9.3 release on May 12, 2015. Security researcher Kyu Neushwaistein (aka Carlos Cortes Alvarez) has been credited with discovering and reporting the flaw on January 19, 2026.

As mitigations, it's advised to apply the latest patches and restrict network access to the telnet port to trusted clients. As temporary workarounds, users can disable telnetd server, or make the InetUtils telnetd use a custom login(1) tool that does not permit use of the '-f' parameter, Josefsson added.

Data gathered by threat intelligence firm GreyNoise shows that [21 unique IP addresses](https://viz.greynoise.io/tags/inetutils-telnetd--f-auth-bypass-attempt?days=1) have been observed attempting to execute a remote authentication bypass attack by leveraging the flaw over the past 24 hours. All the IP addresses, which [originate](https://viz.greynoise.io/query/tags%3A%22Inetutils%20Telnetd%20-f%20Auth%20Bypass%20Attempt%22%20last_seen%3A1d) from Hong Kong, the U.S., Japan, the Netherlands, China, Germany, Singapore, and Thailand, have been flagged as malicious.

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

[CVE](https://thehackernews.com/search/label/CVE)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[linux](https://thehackernews.com/search/label/linux)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[telnet](https://thehackernews.com/search/label/telnet)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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
...
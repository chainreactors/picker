---
title: Experts Reports Sharp Increase in Automated Botnet Attacks Targeting PHP Servers and IoT Devices
url: https://thehackernews.com/2025/10/experts-reports-sharp-increase-in.html
source: The Hacker News
date: 2025-10-29
fetch_date: 2025-10-30T03:12:54.563765
---

# Experts Reports Sharp Increase in Automated Botnet Attacks Targeting PHP Servers and IoT Devices

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

# [Experts Reports Sharp Increase in Automated Botnet Attacks Targeting PHP Servers and IoT Devices](https://thehackernews.com/2025/10/experts-reports-sharp-increase-in.html)

**Oct 29, 2025**Ravie LakshmananVulnerability / Internet of Things

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivAUs8CWZuMjytXCzRiRr1Njj-R-Sv2PglgPmqZCLMHd71SMJyPl8hh9RPTqhzeZm7OJ7BdDEOO0b5bODPEvOl6uOB4cA1Hobq1j_O6uIsuFSqDMp-lyswH6W3-NIkX3fmGCsvU93B9OlouN-ngLew2lqxLFpQHA5NgedY2CQcyZQ-W4-GEtj-CK01hEb9/s790-rw-e365/php-site.jpg)

Cybersecurity researchers are calling attention to a spike in automated attacks targeting PHP servers, IoT devices, and cloud gateways by various botnets such as [Mirai](https://thehackernews.com/2025/01/mirai-botnet-launches-record-56-tbps.html), [Gafgyt](https://thehackernews.com/2024/08/new-gafgyt-botnet-variant-targets-weak.html), and [Mozi](https://thehackernews.com/2024/11/androxgh0st-malware-integrates-mozi.html).

"These automated campaigns exploit known CVE vulnerabilities and cloud misconfigurations to gain control over exposed systems and expand botnet networks," the Qualys Threat Research Unit (TRU) said in a report shared with The Hacker News.

The cybersecurity company said PHP servers have emerged as the most prominent targets of these attacks owing to the widespread use of content management systems like [WordPress](https://thehackernews.com/2025/10/hackers-exploit-wordpress-themes-to.html) and [Craft CMS](https://thehackernews.com/2025/05/mimo-hackers-exploit-cve-2025-32432-in.html). This, in turn, creates a large attack surface as many PHP deployments can suffer from misconfigurations, outdated plugins and themes, and insecure file storage.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the prominent weaknesses in PHP frameworks that have been exploited by threat actors are listed below -

* **[CVE-2017-9841](https://nvd.nist.gov/vuln/detail/cve-2017-9841)** - A Remote code execution vulnerability in PHPUnit
* **[CVE-2021-3129](https://nvd.nist.gov/vuln/detail/cve-2021-3129)** - A Remote code execution vulnerability in Laravel
* **[CVE-2022-47945](https://nvd.nist.gov/vuln/detail/CVE-2022-47945)** - A Remote code execution vulnerability in ThinkPHP Framework

Qualys said it has also observed exploitation efforts that involve the use of "/?XDEBUG\_SESSION\_START=phpstorm" query string in HTTP GET requests to initiate an [Xdebug debugging session](https://www.jetbrains.com/help/phpstorm/simultaneous-debugging-sessions.html#ensure-a-debugger-session-is-started-for-secondary-requests) with an integrated development environment (IDE) like PhpStorm.

"If Xdebug is unintentionally left active in production environments, attackers may use these sessions to gain insight into application behavior or extract sensitive data," the company said.

Alternatively, threat actors are continuing to look for credentials, API keys, and access tokens in internet-exposed servers to take control of susceptible systems, as well as leverage known security flaws in IoT devices to co-opt them into a botnet. These include -

* **[CVE-2022-22947](https://nvd.nist.gov/vuln/detail/cve-2022-22947)** - A Remote code execution vulnerability in Spring Cloud Gateway
* **[CVE-2024-3721](https://nvd.nist.gov/vuln/detail/CVE-2024-3721)** - A Command injection vulnerability in TBK DVR-4104 and DVR-4216
* A Misconfiguration in MVPower TV-7104HE DVR that allows unauthenticated users to execute arbitrary system commands via an HTTP GET request

The scanning activity, Qualys added, often originates from cloud infrastructures like Amazon Web Services (AWS), Google Cloud, Microsoft Azure, Digital Ocean, and Akamai Cloud, illustrating how threat actors are abusing legitimate services to their advantage while obscuring their true origins.

"Today's threat actors don't need to be highly sophisticated to be effective," it noted. "With widely available exploit kits, botnet frameworks, and scanning tools, even entry-level attackers can cause significant damage."

To safeguard against the threat, it's advised that users keep their devices up-to-date, remove development and debug tools in production environments, secure secrets using AWS Secrets Manager or HashiCorp Vault, and restrict public access to cloud infrastructure.

"While botnets have previously been associated with large-scale DDoS attacks and occasional crypto mining scams, in the age of identity security threats, we see them taking on a new role in the threat ecosystem," James Maude, field CTO at BeyondTrust, said.

"Having access to a vast network of routers and their IP addresses can allow threat actors to perform credential stuffing and password spray attacks a huge scale. Botnets can also evade geolocation controls by stealing a user's credentials or hijacking a browser session and then using a botnet node close to the victim's actual location and maybe even using the same ISP as the victim to evade unusual login detections or access policies."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as NETSCOUT classified the DDoS-for-hire botnet known as [AISURU](https://thehackernews.com/2025/10/researchers-warn-rondodox-botnet-is.html) as a new class of malware dubbed TurboMirai that can launch DDoS attacks that exceed 20 terabits per second (Tbps). The botnet primarily comprises consumer-grade broadband access routers, online CCTV and DVR systems, and other customer premise equipment (CPE).

"These botnets incorporate additional dedicated DDoS attack capabilities and multi-use functions, enabling both DDoS attacks and other illicit activities such as credential stuffing, artificial intelligence (AI)-driven web scraping, spamming, and phishing," the company [said](https://www.netscout.com/blog/asert/asert-threat-summary-aisuru-and-related-turbomirai-botnet-ddos).

"AISURU includes an onboard residential proxy service used to reflect HTTP...
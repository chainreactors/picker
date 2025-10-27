---
title: Exposed Selenium Grid Servers Targeted for Crypto Mining and Proxyjacking
url: https://thehackernews.com/2024/09/exposed-selenium-grid-servers-targeted.html
source: The Hacker News
date: 2024-09-13
fetch_date: 2025-10-06T18:31:07.821009
---

# Exposed Selenium Grid Servers Targeted for Crypto Mining and Proxyjacking

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

# [Exposed Selenium Grid Servers Targeted for Crypto Mining and Proxyjacking](https://thehackernews.com/2024/09/exposed-selenium-grid-servers-targeted.html)

**Sep 12, 2024**Ravie LakshmananCryptocurrency / Network Security

[![Crypto Mining and Proxyjacking](data:image/png;base64... "Crypto Mining and Proxyjacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoGuKEpZPKqpXBEZT4m-90_NLm-CmkYZO4pnu41ogEtQo1IdLp9TdRSbjX9iGoBSrxxy8-d1DA_sMwZtsumx-XUWvsiohNA4tYTkYYkVNxxBL3CRE5ZkMsgGFUDnSp_mbLmG4El44nz7UmIoYHC_822B_lYrrnt6XkhKxePkMD1ZiR7qAt7VkKZhUQJOxJ/s790-rw-e365/crypto.png)

Internet-exposed Selenium Grid instances are being targeted by bad actors for illicit cryptocurrency mining and [proxyjacking](https://thehackernews.com/2023/08/new-labrat-campaign-exploits-gitlab.html) campaigns.

"Selenium Grid is a server that facilitates running test cases in parallel across different browsers and versions," Cado Security researchers Tara Gould and Nate Bill [said](https://www.cadosecurity.com/blog/from-automation-to-exploitation-the-growing-misuse-of-selenium-grid-for-cryptomining-and-proxyjacking) in an analysis published today.

"However, Selenium Grid's default configuration lacks authentication, making it vulnerable to exploitation by threat actors."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The abuse of publicly-accessible Selenium Grid instances for deploying crypto miners was previously highlighted by cloud security firm Wiz in late July 2024 as part of an activity cluster dubbed [SeleniumGreed](https://thehackernews.com/2024/07/ongoing-cyberattack-targets-exposed.html).

Cado, which observed two different campaigns against its honeypot server, said the threat actors are exploiting the lack of authentication protections to carry out a diverse set of malicious actions.

The first of them leverages the "[goog:chromeOptions](https://developer.chrome.com/docs/chromedriver/capabilities)" dictionary to inject a Base64-encoded Python script that, in turn, retrieves a script named "y," which is the open-source [GSocket](https://github.com/hackerschoice/gsocket) reverse shell.

[![Crypto Mining and Proxyjacking](data:image/png;base64... "Crypto Mining and Proxyjacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi45nDi2KGBe76rfXK9fWqnYav6fkHQMv5WckJ9C_xrhx5Ubg_9b5gpIRWVkMBj4UjXPUS26Ms-K2VTnvUvVlPRQDGxMrWDUIdOYA0Oops1ObH8ta19HmujuIcWdneaC8Ncuw7Yi9BzsmvulnP53on8p9r8YTI7dnVSmJ1pAi7r_qEDBaX2cwqaP7lH0ysT/s790-rw-e365/unnamed.png)

The reverse shell subsequently serves as a medium for introducing the next-stage payload, a bash script named "pl" that retrieves IPRoyal Pawn and EarnFM from a remote server via curl and wget commands.

"IPRoyal Pawns is a residential proxy service that allows users to sell their internet bandwidth in exchange for money," Cado said.

"The user's internet connection is shared with the IPRoyal network with the service using the bandwidth as a residential proxy, making it available for various purposes, including for malicious purposes."

EarnFM is also a proxyware solution that's advertised as a "ground-breaking" way to "generate passive income online by simply sharing your internet connection."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The second attack, like the proxyjacking campaign, follows the same route to deliver a bash script via a Python script that checks if it's running on a 64-bit machine and then proceeds to drop a Golang-based ELF binary.

The ELF file subsequently attempts to escalate to root by leveraging the [PwnKit](https://thehackernews.com/2022/06/cisa-warns-of-active-exploitation-of.html) flaw (CVE-2021-4043) and drops an XMRig cryptocurrency miner called perfcc.

"As many organizations rely on Selenium Grid for web browser testing, this campaign further highlights how misconfigured instances can be abused by threat actors," the researchers said. "Users should ensure authentication is configured, as it is not enabled by default."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Infrastructure Security](https://thehackernews.com/search/label/Infrastructure%20Security)[IT security](https://thehackernews.com/search/label/IT%20security)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[vulnerability management](https://thehackernews.com/search/label/vulnerability%20management)[Web Testing](https://thehackernews.com/search/label/Web%20Testing)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.c...
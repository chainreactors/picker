---
title: LastPass Reveals Second Attack Resulting in Breach of Encrypted Password Vaults
url: https://thehackernews.com/2023/02/lastpass-reveals-second-attack.html
source: The Hacker News
date: 2023-03-01
fetch_date: 2025-10-04T08:23:32.009711
---

# LastPass Reveals Second Attack Resulting in Breach of Encrypted Password Vaults

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

# [LastPass Reveals Second Attack Resulting in Breach of Encrypted Password Vaults](https://thehackernews.com/2023/02/lastpass-reveals-second-attack.html)

**Feb 28, 2023**Ravie LakshmananPassword Security / Data Breach

[![LastPass](data:image/png;base64... "LastPass")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-uGMUB3tHhy0O3xzEdAO3UIFLmHRNyaAqPd7cEEz8sbfWX4dbXt5U1qXp9OS7FB4zyhmW0pxhzIbUHDhFDHhWVT8RUF5kYDYXsY3tlfW0UOX52iBrR9QM827L2b0vv-1-Tw6YOZ22FJ0hg3Dp7D6c6uXELAhWCzWdHKmveE67uQDUA-BjlB1EUNFE/s790-rw-e365/lastpass.png)

LastPass, which in December 2022 disclosed a severe data breach that allowed threat actors to access encrypted password vaults, said it happened as a result of the same adversary launching a second attack on its systems.

The company said one of its DevOps engineers had their personal home computer hacked and infected with a keylogger as part of a sustained cyber attack that exfiltrated sensitive data from its Amazon AWS cloud storage servers.

"The threat actor leveraged information stolen during the first incident, information available from a third-party data breach, and a vulnerability in a third-party media software package to launch a coordinated second attack," the password management service [said](https://support.lastpass.com/help/incident-2-additional-details-of-the-attack).

This intrusion targeted the company's infrastructure, resources, and the aforementioned employee from August 12, 2022, to October 26, 2022. The original incident, on the other hand, ended on August 12, 2022.

The [August breach](https://thehackernews.com/2022/08/hackers-breach-lastpass-developer.html) saw the intruders accessing source code and proprietary technical information from its development environment by means of a single compromised employee account.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In December 2022, LastPass [revealed](https://thehackernews.com/2022/12/lastpass-suffers-another-security.html) that the threat actor leveraged the stolen information to access a cloud-based storage environment and get hold of "certain elements of our customers' information."

Later in the same month, the unknown attacker was [disclosed](https://thehackernews.com/2022/12/lastpass-admits-to-severe-data-breach.html) as having obtained access to a backup of customer vault data that it said was protected using 256-bit AES encryption. It did not divulge how recent the backup was.

GoTo, the parent company of LastPass, also [fessed up to a breach](https://thehackernews.com/2023/01/lastpass-parent-company-goto-suffers.html) last month stemming from unauthorized access to the third-party cloud storage service.

Now according to the company, the threat actor engaged in a new series of "reconnaissance, enumeration, and exfiltration activities" aimed at its cloud storage service between August and October 2022.

"Specifically, the threat actor was able to leverage valid credentials stolen from a senior DevOps engineer to access a shared cloud storage environment," LastPass said, adding the engineer "had access to the decryption keys needed to access the cloud storage service."

This allowed the malicious actor to obtain access to the AWS S3 buckets that housed backups of LastPass customer and encrypted vault data, it further noted.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The employee's passwords are said to have been siphoned by targeting the individual's home computer and leveraging a "vulnerable third-party media software package" to achieve remote code execution and plant a keylogger software.

"The threat actor was able to capture the employee's master password as it was entered, after the employee authenticated with MFA, and gain access to the DevOps engineer's LastPass corporate vault," LastPass said.

LastPass did not reveal the name of the third-party media software used, but indications are that it could be Plex [based](https://twitter.com/troyhunt/status/1562318321479204865) on the fact that it [suffered a breach of its own](https://techcrunch.com/2022/08/24/plex-streaming-breach-passwords/) in late August 2022.

In the aftermath of the incident, LastPass said it upgraded its security posture by rotating critical and high privilege credentials and reissuing certificates obtained by the threat actor, and that it applied extra S3 hardening measures to put in place logging and alerting mechanisms.

LastPass users are highly recommended to change their master passwords and all the passwords stored in their vaults to mitigate potential risks, if not done already.

## **Update**

Plex shared the following statement with The Hacker News after the publication of the story -

*We have not been contacted by LastPass so we cannot speak to the specifics of their incident. We take security issues very seriously, and frequently work with external parties who report issues big or small using our* [*guidelines and bug bounty program*](https://support.plex.tv/articles/reporting-security-issues/)*. When vulnerabilities are reported following responsible disclosure we address them swiftly and thoroughly, and we've never had a critical vulnerability published for which there wasn't already a patched version released. And when we've had incidents of our own, we've always chosen to communicate them quickly. We are not aware of any unpatched vulnerabilities, and as always, we invite people to disclose issues to us following the guidelines linked above. Given recent articles about the LastPass incident, although we are not aware of any unpatched vulnerabilities, we have reached out to LastPass to be sure.*

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#l...
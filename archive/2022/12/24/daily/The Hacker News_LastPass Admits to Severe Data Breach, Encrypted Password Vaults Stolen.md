---
title: LastPass Admits to Severe Data Breach, Encrypted Password Vaults Stolen
url: https://thehackernews.com/2022/12/lastpass-admits-to-severe-data-breach.html
source: The Hacker News
date: 2022-12-24
fetch_date: 2025-10-04T02:28:00.160981
---

# LastPass Admits to Severe Data Breach, Encrypted Password Vaults Stolen

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

# [LastPass Admits to Severe Data Breach, Encrypted Password Vaults Stolen](https://thehackernews.com/2022/12/lastpass-admits-to-severe-data-breach.html)

**Dec 23, 2022**Ravie LakshmananPassword Management / Data Breach

[![LastPass hacked](data:image/png;base64... "LastPass hacked")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCTdxbQKamrLeVc8hOKLC92sJOQ58eChoyDPWiw2hlEPTuoWmCxQ34r8VEIAQ_2djIHM4_TUUWcuV46iloiI94oT2Zi6KYfs9SWDRzZjvw6708AY3Jh8S_Bx1UFHAZ08As4A3KCe4j-mGRRRx9iwnAOwMZWF_aRI0FmMaqgFdmTYG6WFoDI0qjxaCQ/s790-rw-e365/lastpass.png)

The [August 2022 security breach](https://thehackernews.com/2022/08/hackers-breach-lastpass-developer.html) of LastPass may have been more severe than previously disclosed by the company.

The popular password management service on Thursday revealed that malicious actors obtained a trove of personal information belonging to its customers that include their encrypted password vaults by using data siphoned from the earlier break-in.

Among the data stolen are "basic customer account information and related metadata including company names, end-user names, billing addresses, email addresses, telephone numbers, and the IP addresses from which customers were accessing the LastPass service," the company [said](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/).

The August 2022 incident, which [remains](https://thehackernews.com/2022/12/lastpass-suffers-another-security.html) a subject of an ongoing investigation, involved the miscreants accessing source code and proprietary technical information from its development environment via a single compromised employee account.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

LastPass said this permitted the unidentified attacker to obtain credentials and keys that were subsequently leveraged to extract information from a backup stored in a cloud-based storage service, which it emphasized is physically separate from its production environment.

On top of that, the adversary is said to have copied customer vault data from the encrypted storage service. It's stored in a "proprietary binary format" that contains both unencrypted data, such as website URLs, and fully-encrypted fields like website usernames and passwords, secure notes, and form-filled data.

These fields, the company explained, are protected using 256-bit AES encryption and can be decoded only with a key derived from the users' [master password](https://support.lastpass.com/help/about-password-iterations-lp030027) on the users' devices.

LastPass confirmed that the security lapse did not involve access to unencrypted credit card data, as this information was not archived in the cloud storage container.

The company did not divulge how recent the backup was, but warned that the threat actor "may attempt to use brute-force to guess your master password and decrypt the copies of vault data they took," as well as target customers with social engineering and credential stuffing attacks.

It bears noting at this stage that the success of the brute-force attacks to predict the [master passwords](https://support.lastpass.com/help/what-is-the-lastpass-master-password-lp070014) is inversely proportional to their strength, meaning the easier it is to guess the password, the lesser the number of attempts required to crack it.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"If you reuse your master password and that password was ever compromised, a threat actor may use dumps of compromised credentials that are already available on the internet to attempt to access your account," LastPass cautioned.

The fact that website URLs are in plaintext means that a successful decryption of the master password could give the attackers a sense of the websites a particular user holds accounts with, enabling them to mount additional phishing or credential theft attacks.

The company further said that it notified a small subset of its business customers – which amounts to less than 3% – to take certain unspecified action based on their account configurations.

The development comes days after Okta [acknowledged](https://thehackernews.com/2022/12/hackers-breach-oktas-github.html) that threat actors gained unauthorized access to its Workforce Identity Cloud (WIC) repositories hosted on GitHub and copied the source code.

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

[data breach](https://thehackernews.com/search/label/data%20breach)[LastPass](https://thehackernews.com/search/label/LastPass)[Password Management](https://thehackernews.com/search/label/Password%20Management)[password manager](https://thehackernews.com/search/label/password%20manager)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)
...
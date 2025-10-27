---
title: Fake Recruiter Emails Target CFOs Using Legit NetBird Tool Across 6 Global Regions
url: https://thehackernews.com/2025/06/fake-recruiter-emails-target-cfos-using.html
source: The Hacker News
date: 2025-06-03
fetch_date: 2025-10-06T23:07:25.178563
---

# Fake Recruiter Emails Target CFOs Using Legit NetBird Tool Across 6 Global Regions

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

# [Fake Recruiter Emails Target CFOs Using Legit NetBird Tool Across 6 Global Regions](https://thehackernews.com/2025/06/fake-recruiter-emails-target-cfos-using.html)

**Jun 02, 2025**Ravie LakshmananIdentity Theft / Email Securi

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWn7SW71gQyY_mzVDYAwaMg_TJSWfoFbEeuD38JaphaNfGTNNltBofWK6fcA8r6dPnUwiaccob5M0-UJYIsQuQPSJNtpHujuqWuRzGZ1lTgzudT4LP1YMnisoO9ba0IbKcgJpMQXqjjIiamFUXSekuPddifz8z5mx49YbavMa7izzhJfp5TNZ3Dc_gBe3_/s790-rw-e365/email.jpg)

Cybersecurity researchers have warned of a new spear-phishing campaign that uses a legitimate remote access tool called Netbird to target Chief Financial Officers (CFOs) and financial executives at banks, energy companies, insurers, and investment firms across Europe, Africa, Canada, the Middle East, and South Asia.

"In what appears to be a multi-stage phishing operation, the attackers aimed to deploy NetBird, a legitimate wireguard-based remote access tool on the victim's computer," Trellix researcher Srini Seethapathy [said](https://www.trellix.com/en-in/blogs/research/a-flyby-on-the-cfos-inbox-spear-phishing-campaign-targeting-financial-executives-with-netbird-deployment/) in an analysis.

The activity, first detected by the cybersecurity company in mid-May 2025, has not been attributed to a known threat actor or group.

The starting point of the attack is a phishing email that impersonates a recruiter from Rothschild & Co. and claims to offer a "strategic opportunity" with the company. The email is designed to entice the recipients into opening a purported PDF attachment that, in reality, is a phishing link that redirects them to a Firebase app-hosted URL.

What's notable about the infection is that the real redirect URL is stored in the page in encrypted form and is accessible only after the victim solves a CAPTCHA verification check, ultimately leading to the download of a ZIP archive.

"Solving the puzzle executes a [JavaScript] function that decrypts it with a hard-coded key and redirects the user to the decrypted link," Seethapathy said. "Attackers are leaning on these custom CAPTCHA gates more and more, hoping to slip past defenses that already flag phishing sites protected by Cloudflare Turnstile or Google reCAPTCHA."

Present within the archive is a Visual Basic Script (VBScript) that's responsible for retrieving a next-stage VBScript from an external server and launching it via "wscript.exe." This second-stage VBScript downloader then fetches another payload from the same server, renames it to "trm.zip," and extracts two MSI files from it: NetBird and OpenSSH.

The last phase involves installing the two programs on the infected host, creating a hidden local account, enabling remote desktop access, and persisting NetBird via scheduled tasks such that it automatically launches on system reboot. The malware also removes any NetBird desktop shortcuts to ensure that the compromise is not detected by the victim.

Trellix said it identified another redirect URL that has been active for nearly a year and serves the same VBScript payload, indicating that the campaign may have been around for some time.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The findings once again show how adversaries are [increasingly relying](https://cofense.com/blog/new-weapon-of-choice-how-threat-actors-hijack-legitimate-remote-access-tools) on legitimate remote access applications such as ConnectWise ScreenConnect, Atera, Splashtop, FleetDeck, and LogMeIn Resolve to establish persistence and use it to burrow into the victim's network, while simultaneously evading detection.

"This attack isn't your typical phishing scam," Seethapathy said. "It's well-crafted, targeted, subtle, and designed to slip past technology and people. It is a multi-stage attack where the adversary uses social engineering and defense evasion techniques to create and maintain persistent access to the victim system."

The disclosure coincides with the discovery of various email-based social engineering campaigns in the wild -

* Attacks that [abuse](https://ravenmail.io/blog/nifty-phishing) a trusted domain associated with a well-known Japanese internet service provider (ISP) to send phishing messages from the email address "company@nifty[.]com" in an attempt to get past email authentication checks and harvest credentials
* Attacks that [abuse](https://cofense.com/blog/behind-the-script-unmasking-phishing-attacks-using-google-apps-script) the Google Apps Script development platform to host phishing pages that look legitimate and steal Microsoft login credentials by employing invoice-themed email lures
* Attacks that [mimic](https://cofense.com/blog/phishing-in-the-multiverse-analyzing-a-malicious-email-targeting-apple-and-yahoo-users) an Apple Pay invoice to steal sensitive user data, including credit card details and Yahoo Mail account details
* Attacks that [abuse](https://any.run/cybersecurity-blog/adversary-telegram-bot-abuse/) Notion workspaces to host phishing pages that trick users into clicking on links that take the victims to a fake Microsoft login page under the guise of viewing a shared document and exfiltrate the credentials via a Telegram bot
* Attacks that [exploit](https://www.fortinet.com/blog/threat-research/infostealer-malware-formbook-spread-via-phishing-campaign) a years-old security flaw in Microsoft Office ([CVE-2017-11882](https://thehackernews.com/2023/12/hackers-exploiting-old-ms-excel.html)) to deliver the Formbook malware variant hidden in a fake PNG file and steal sensitive data from compromised hosts

### PhaaS Services Lower the Bar

The findings also come as Trustwave detailed the operational connections between [Tycoon](https://thehackernews.com/2024/03/alert-new-phishing-attack-delivers.html) and [DadSec](https://thehackernews.com/2024/11/phishing-as-service-rockstar-2fa.html) (aka Phoenix) phishing kits, highlighting their infrastructural overlaps and the use ...
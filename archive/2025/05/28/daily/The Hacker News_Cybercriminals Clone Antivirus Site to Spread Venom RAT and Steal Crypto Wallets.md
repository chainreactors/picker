---
title: Cybercriminals Clone Antivirus Site to Spread Venom RAT and Steal Crypto Wallets
url: https://thehackernews.com/2025/05/cybercriminals-clone-antivirus-site-to_4.html
source: The Hacker News
date: 2025-05-28
fetch_date: 2025-10-06T22:31:19.900430
---

# Cybercriminals Clone Antivirus Site to Spread Venom RAT and Steal Crypto Wallets

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

# [Cybercriminals Clone Antivirus Site to Spread Venom RAT and Steal Crypto Wallets](https://thehackernews.com/2025/05/cybercriminals-clone-antivirus-site-to_4.html)

**May 27, 2025**Ravie LakshmananMalware / Cybersecurity

[![Cybercriminals Clone Antivirus](data:image/png;base64... "Cybercriminals Clone Antivirus")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnO11JT-9DXziGxoFd8W8F7uRVN8Qe6vQbOp0V-jxYq828nmFhIsrY78TLWx_zoZ8yG9jGYPtFwVLUQ7f52W7cM3y_tXyGt96nuOPXHJXx-hHGb9NWI7NgJOXe_clPlBng9IZxVczW309ZUqvabxMxCOl05ADZA-kOOokZQsON5MD0Hpc06ODyctBNy_Qo/s790-rw-e365/antivirus.jpg)

Cybersecurity researchers have disclosed a new malicious campaign that uses a fake website advertising antivirus software from Bitdefender to dupe victims into downloading a remote access trojan called Venom RAT.

The campaign indicates a "clear intent to target individuals for financial gain by compromising their credentials, crypto wallets, and potentially selling access to their systems," the DomainTools Intelligence (DTI) team [said](https://dti.domaintools.com/VenomRAT) in a new report shared with The Hacker News.

The website in question, "bitdefender-download[.]com," advertises site visitors to download a Windows version of the Antivirus software. Clicking on the prominent "Download for Windows" button initiates a file download from a Bitbucket repository that redirects to an Amazon S3 bucket. The Bitbucket account is no longer active.

The ZIP archive ("BitDefender.zip") contains an executable called "StoreInstaller.exe," which includes malware configurations associated with Venom RAT, as well as code related to the open-source post-exploitation framework SilentTrinity and [StormKitty](https://thehackernews.com/2023/03/new-macstealer-macos-malware-steals.html) stealer.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[Venom RAT](https://thehackernews.com/2024/04/massive-phishing-campaign-strikes-latin.html) is an offshoot of Quasar RAT that comes with capabilities to harvest data and provide persistent remote access to attackers.

DomainTools said the decoy website masquerading as Bitdefender shares temporal and infrastructure overlaps with other malicious domains spoofing banks and generic IT services that have been used as part of phishing activity to harvest login credentials associated with Royal Bank of Canada and Microsoft .

"These tools work in concert: Venom RAT sneaks in, StormKitty grabs your passwords and digital wallet info, and SilentTrinity ensures the attacker can stay hidden and maintain control," the company said.

"This campaign underscores a constant trend: attackers are using sophisticated, modular malware built from open-source components. This 'build-your-own-malware' approach makes these attacks more efficient, stealthy, and adaptable."

The disclosure comes as Sucuri warned of a [ClickFix](https://thehackernews.com/2025/05/hackers-use-tiktok-videos-to-distribute.html)-style campaign that employs bogus Google Meet pages to deceive users into installing noanti-vm.bat RAT, a heavily obfuscated Windows batch script that grants remote control over the victim's computer.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNPpIKRaLu3ab-KXWPIk9HrUD7myPXnDcZ5Q_KqfNaHp9wGf5pWqYBRsMLSGjBrQB4HF3sqZNAnPw8p8YihK8-cW3oSS3bLIxVWQyuyFmGNaGx0KY4ki30WNmrkUu-5dCjUtmV8sbqNkeKfDn7tAHKca3EjJBSyoy3sCWLfeAUeefGrxCLhobABO2PbtJY/s790-rw-e365/meet.png)

"This fake Google Meet page doesn't present a login form to steal credentials directly," security researcher Puja Srivastava [said](https://blog.sucuri.net/2025/05/fake-google-meet-page-tricks-users-into-running-powershell-malware.html). "Instead, it employs a social engineering tactic, presenting a fake 'Microphone Permission Denied' error and urging the user to copy and paste a specific PowerShell command as a 'fix.'"

It also follows a spike in phishing attacks that exploit Google's AppSheet no-code development platform to mount a highly targeted, sophisticated campaign impersonating Meta.

"Utilizing state-of-the-art tactics such as polymorphic identifiers, advanced man‑in‑the‑middle proxy mechanisms and multi-factor authentication bypass techniques, the attackers aim to harvest credentials and two-factor authentication (2FA) codes, enabling real-time access to social media accounts," the KnowBe4 Threat Lab [said](https://blog.knowbe4.com/impersonating-meta-powered-by-appsheet-a-rising-phishing-campaign-exploits-trusted-platforms-to-evade-detection) in a report.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The campaign entails the use of AppSheet to deliver phishing emails at scale, allowing the threat actors to bypass email security defenses such as SPF, DKIM, and DMARC owing to the fact that the messages originate from a valid domain ("noreply@appsheet[.]com").

Furthermore, the emails claim to be from Facebook Support and employ account deletion warnings to trick users into clicking on fake links under the pretext of submitting an appeal within a 24-hour time period. The booby-trapped links lead victims to an adversary-in-the-middle (AitM) phishing page designed to harvest their credentials and two-factor authentication (2FA) codes.

"To further evade detection and complicate remediation, the attackers leverage AppSheets' functionality for generating unique IDs, shown as Case IDs in the body of the email," the company said.

"The presence of unique polymorphic identifiers in each phishing email ensures every message is slightly different, helping them bypass traditional detection systems that rely on static indicators such as hashes or known malicious URLs."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exc...
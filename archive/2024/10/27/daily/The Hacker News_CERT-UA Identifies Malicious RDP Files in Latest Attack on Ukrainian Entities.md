---
title: CERT-UA Identifies Malicious RDP Files in Latest Attack on Ukrainian Entities
url: https://thehackernews.com/2024/10/cert-ua-identifies-malicious-rdp-files.html
source: The Hacker News
date: 2024-10-27
fetch_date: 2025-10-06T18:52:54.603149
---

# CERT-UA Identifies Malicious RDP Files in Latest Attack on Ukrainian Entities

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

# [CERT-UA Identifies Malicious RDP Files in Latest Attack on Ukrainian Entities](https://thehackernews.com/2024/10/cert-ua-identifies-malicious-rdp-files.html)

**Oct 26, 2024**Ravie LakshmananCyber Attack / Threat Intelligence

[![Malicious RDP Files](data:image/png;base64... "Malicious RDP Files")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdU8bqKBkqMgeEvriXq5eSBkHEmgPPpkQgJWJl8MQEf8lBf-2k3h3iS3P0Onfo04BMrvT4bqsOb5hoGMW7tI0meRe6Knf6PmEuWaD9eTK6oBjoI7B9DXefnEmx7q6uVGaTLUP-jGqsoVcUJzhMfk4S-jdle4CjUih4jxeLTbiiXb0Wmw_dutoe329cIazE/s790-rw-e365/cyberattack.png)

The Computer Emergency Response Team of Ukraine (CERT-UA) has detailed a new malicious email campaign targeting government agencies, enterprises, and military entities.

"The messages exploit the appeal of integrating popular services like Amazon or Microsoft and implementing a zero-trust architecture," CERT-UA [said](https://cert.gov.ua/article/6281076). "These emails contain attachments in the form of Remote Desktop Protocol ('.rdp') configuration files."

Once executed, the RDP files establish a connection with a remote server, enabling the threat actors to gain remote access to the compromised hosts, steal data, and plant additional malware for follow-on attacks.

Infrastructure preparation for the activity is believed to have been underway since at least August 2024, with the agency stating that it's likely to spill out of Ukraine to target other countries.

CERT-UA has attributed the campaign to a threat actor it tracks as UAC-0215. Amazon Web Services (AWS), in an advisory of its own, linked it to the Russian nation-state hacking group known as [APT29](https://thehackernews.com/2024/08/russian-hackers-exploit-safari-and.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Some of the domain names they used tried to trick the targets into believing the domains were AWS domains (they were not), but Amazon wasn't the target, nor was the group after AWS customer credentials," CJ Moses, Amazon's chief information security officer, [said](https://aws.amazon.com/blogs/security/amazon-identified-internet-domains-abused-by-apt29/). "Rather, APT29 sought its targets' Windows credentials through Microsoft Remote Desktop."

The tech giant said it also seized the domains the adversary was using to impersonate AWS in order to neutralize the operation. Some of the domains used by APT29 are listed below -

* ca-west-1.mfa-gov[.]cloud
* central-2-aws.ua-aws[.]army
* us-east-2-aws.ua-gov[.]cloud
* aws-ukraine[.]cloud
* aws-data[.]cloud
* aws-s3[.]cloud
* aws-il[.]cloud
* aws-join[.]cloud
* aws-meet[.]cloud
* aws-meetings[.]cloud
* aws-online[.]cloud
* aws-secure[.]cloud
* s3-aws[.]cloud
* s3-fbi[.]cloud
* s3-nsa[.]cloud, and
* s3-proofpoint[.]cloud

The development comes as CERT-UA also warned of a large-scale cyber attack aimed at stealing confidential information of Ukrainian users. The threat has been cataloged under the moniker UAC-0218.

The starting point of the attack is a phishing email containing a link to a booby-trapped RAR archive that purports to be either bills or payment details.

Present within the archive is a Visual Basic Script-based malware dubbed HOMESTEEL that's designed to exfiltrate files matching certain extensions ("xls," "xlsx," "doc," "docx," "pdf," "txt," "csv," "rtf," "ods," "odt," "eml," "pst," "rar," and "zip") to an attacker-controlled server.

"This way criminals can gain access to personal, financial and other sensitive data and use it for blackmail or theft," CERT-UA [said](https://cert.gov.ua/article/6281095).

Furthermore, CERT-UA has [alerted](https://cert.gov.ua/article/6281123) of a [ClickFix](https://thehackernews.com/2024/10/beware-fake-google-meet-pages-deliver.html)-style campaign that's designed to trick users into malicious links embedded in email messages to drop a PowerShell script that's capable of establishing an SSH tunnel, stealing data from web browsers, and downloading and launching the Metasploit penetration testing framework.

Users who click the link are directed to a fake reCAPTCHA verification page that prompts them to verify their identity by clicking on a button. This action copies the malicious PowerShell script ("Browser.ps1") to the user's clipboard and displays a popup window with instructions to execute it using the Run dialog box in Windows.

CERT-UA said it has an "average level of confidence" that the campaign is the work of another Russian advanced persistent threat actor known as [APT28](https://thehackernews.com/2024/08/apt28-targets-diplomats-with-headlace.html) (aka UAC-0001).

The cyber offensives against Ukraine come amidst a [report](https://www.bloomberg.com/news/articles/2024-10-21/how-russia-s-spies-hacked-the-entire-nation-of-georgia) from Bloomberg that detailed how Russia's [military intelligence agency](https://thehackernews.com/2022/09/russian-sandworm-hackers-impersonate.html) and Federal Security Service (FSB) systematically targeted Georgia's infrastructure and government as part of a series of digital intrusions between 2017 to 2020. Some of the attacks have been pinned on [Turla](https://thehackernews.com/2024/05/turla-group-deploys-lunarweb-and.html).

### Microsoft Warns of APT29 Campaign

Microsoft, in a report published on October 29, 2024, corroborated aforementioned findings from CERT-UA, stating it observed the APT29 actor sending a series of highly targeted spear-phishing emails to individuals in government, academia, defense, non-governmental organizations, and other sectors.

The activity has been ongoing since October 22, and the spear-phishing emails are estimated to have been sent to thousands of targets in over 100 organizations located in the United Kingdom, Europe, Australia, and Japan.

The emails "contained a signed Remote Desktop Protocol (RDP) configuration file that connected to an actor-controlled server," the Microsoft Threat Intelligence team [said](https://www.microsoft.com/en-us/security/blog/2024/...
---
title: Phishing Campaigns Use Real-Time Checks to Validate Victim Emails Before Credential Theft
url: https://thehackernews.com/2025/04/phishing-campaigns-use-real-time-checks.html
source: The Hacker News
date: 2025-04-15
fetch_date: 2025-10-06T22:09:11.586978
---

# Phishing Campaigns Use Real-Time Checks to Validate Victim Emails Before Credential Theft

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

# [Phishing Campaigns Use Real-Time Checks to Validate Victim Emails Before Credential Theft](https://thehackernews.com/2025/04/phishing-campaigns-use-real-time-checks.html)

**Apr 14, 2025**Ravie LakshmananEmail Security / Cyber Attack

[![Phishing Campaigns Use Real-Time Checks](data:image/png;base64... "Phishing Campaigns Use Real-Time Checks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmW3JR7o2QmGAfqPgoWm5Tlr_s7l7wqYOmOBeu0UgCXN6fBHw11Liw5Riy5TBZAhASOWFwG0eYQ72mcDNzF60PUtHq90NDay0GeaZrUYFBDSdRT99M8kMD8SAnvSZfUxxNb_HwJDLhA-1tsgSk2D75yDXHW4NUhBnTGh13gr1qFzmUeFSpatDj5jUYNZMY/s790-rw-e365/phish.jpg)

Cybersecurity researchers are calling attention to a new type of credential phishing scheme that ensures that the stolen information is associated with valid online accounts.

The technique has been codenamed precision-validating phishing by Cofense, which it said employs real-time email validation so that only a select set of high-value targets are served the fake login screens.

"This tactic not only gives the threat actors a higher success rate on obtaining usable credentials as they only engage with a specific pre-harvested list of valid email accounts," the company [said](https://cofense.com/blog/the-rise-of-precision-validated-credential-theft-a-new-challenge-for-defenders).

Unlike "spray-and-pray" credential harvesting campaigns that typically involve the bulk distribution of spam emails to obtain victims' login information in an indiscriminate fashion, the latest attack tactic takes spear-phishing to the next level by only engaging with email addresses that attackers have verified as active, legitimate, and high-value.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In this scenario, the email address entered by the victim in a phishing landing page is validated against the attacker's database, after which the bogus login page is displayed. If the email address does not exist in the database, the page either returns an error or the user is redirected to an innocuous page like Wikipedia so as to evade security analysis.

The checks are carried out by integrating an API- or JavaScript-based validation service into the phishing kit that confirms the email address before proceeding to the password capture step.

"It increases the efficiency of the attack and the likelihood that stolen credentials belong to real, actively used accounts, improving the quality of harvested data for resale or further exploitation," Cofense said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9_TlHVTXl0MSNkxZJ5yg6uMoQsVF2hFYWwrK3HkSBXU9b2s1OROrAsZT-RB56ABbQKW8_x-9Oqa_q9EFpFvYGrzkIFXgPdLyOqsRiFxxaW9I8LRQ17N6o8MqYrGDpSz-bNrOh9kHE-Yy81A9uFfMlEwu61W94wvL-ReXht6VDojpcTOcBnEv1O2wzuvFQ/s790-rw-e365/phish.PNG)

"Automated security crawlers and sandbox environments also struggle to analyze these attacks because they cannot bypass the validation filter. This targeted approach reduces attacker risk and extends the lifespan of phishing campaigns."

The development comes as the cybersecurity company also revealed details of an email phishing campaign that uses file deletion reminders as a lure to grab credentials as well as deliver malware.

The two-pronged attack leverages an embedded URL that seemingly points to a PDF file that's scheduled to be deleted from a legitimate file storage service called files.fm. Should the message recipient click on the link, they are taken to legitimate files.fm link from where they can download the purported PDF file.

However, when the [PDF is opened](https://blog.checkpoint.com/research/the-weaponization-of-pdfs-68-of-cyberattacks-begin-in-your-inbox-with-22-of-these-hiding-in-pdfs/), users are presented with two options to either preview or download the file. Users who opt for the former are taken to a bogus Microsoft login screen that's designed to steal their credentials. When the download option is selected, it drops an executable that claims to be Microsoft OneDrive, but, in reality, is the ScreenConnect remote desktop software from ConnectWise.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's "almost as if the threat actor intentionally designed the attack to trap the user, forcing them to choose which 'poison' they will fall for," Cofense [said](https://cofense.com/blog/pick-your-poison-a-double-edged-email-attack). "Both options lead to the same outcome, with similar goals but different approaches to achieving them."

The findings also follow the discovery of a sophisticated multi-stage attack that combines vishing, remote access tooling, and living-off-the-land techniques to gain initial access and establish persistence. The tradecraft observed in the activity is consistent with clusters tracked as [Storm-1811 and STAC5777](https://thehackernews.com/2025/01/qakbot-linked-bc-malware-adds-enhanced.html).

"The threat actor exploited exposed communication channels by delivering a malicious PowerShell payload via a Microsoft Teams message, followed by the use of [Quick Assist](https://thehackernews.com/2024/05/cybercriminals-exploiting-microsofts.html) to remotely access the environment," Ontinue [said](https://www.ontinue.com/resource/blog-signed-sideloaded-compromised/). "This led to the deployment of signed binaries (e.g., TeamViewer.exe), a sideloaded malicious DLL (TV.dll), and ultimately a JavaScript-based C2 backdoor executed via Node.js."

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
[**Share on T...
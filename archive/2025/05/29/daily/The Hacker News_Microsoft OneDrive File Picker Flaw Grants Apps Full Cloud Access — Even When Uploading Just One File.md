---
title: Microsoft OneDrive File Picker Flaw Grants Apps Full Cloud Access — Even When Uploading Just One File
url: https://thehackernews.com/2025/05/microsoft-onedrive-file-picker-flaw.html
source: The Hacker News
date: 2025-05-29
fetch_date: 2025-10-06T22:32:01.548684
---

# Microsoft OneDrive File Picker Flaw Grants Apps Full Cloud Access — Even When Uploading Just One File

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

# [Microsoft OneDrive File Picker Flaw Grants Apps Full Cloud Access — Even When Uploading Just One File](https://thehackernews.com/2025/05/microsoft-onedrive-file-picker-flaw.html)

**May 28, 2025**Ravie LakshmananData Privacy / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPLbR4sH-j7QtWZbtLY4GhFAJgtNF5VNOsBIaiY5hoyukMHq_rrwX0GWbElmoKW7qxikNJYSeJpWJui7mT2_PEdoheEqj3-rt8W0yK10sxD8D3dWH8FYAP3jwgFcNzdchoR9J6yL0fJGyn_p3gzh7oISMLTEjYOSaGKVRy7H5yP4CWXgOX-UCl6-s6zSBr/s790-rw-e365/drive.jpg)

Cybersecurity researchers have discovered a security flaw in Microsoft's OneDrive File Picker that, if successfully exploited, could allow websites to access a user's entire cloud storage content, as opposed to just the files selected for upload via the tool.

"This stems from overly broad OAuth scopes and misleading consent screens that fail to clearly explain the extent of access being granted," the Oasis Research Team [said](https://www.oasis.security/resources/blog/onedrive-file-picker-security-flaw-oasis-research) in a report shared with The Hacker News. "This flaw could have severe consequences, including customer data leakage and violation of compliance regulations."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's assessed that several apps are affected, such as ChatGPT, Slack, Trello, and ClickUp, given their integration with Microsoft's cloud service.

The problem, Oasis said, is the result of excessive permissions requested by the OneDrive File Picker, which seeks read access to the entire drive, even in cases only a single file is uploaded due to the absence of fine-grained OAuth scopes for OneDrive.

Compounding matters further, the consent prompt users are presented with prior to a file upload is vague and does not adequately convey the level of access being granted, thereby exposing users to unexpected security risks.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQ4X0Xg9rtS1ud7LSLlJT4zMnOcjKLEhiWdC7CnEJGXQseooZGQ01cuMY3NmllTdga5D38P8ldwWquVY4aHdzBdxuOgVJ_QI7ML0qEvcEKgqS8O5Ot7tSVUqVpAvkcaTY6DwqCwSTpv8NUat8CtvTbiPGVn5IAEAQOPkERmbxtFtNsRWTk3doppTTID-lz/s790-rw-e365/chatgpt.jpg)

"The lack of fine-grained scopes makes it impossible for users to distinguish between malicious apps that target all files and legitimate apps that ask for excessive permissions simply because there is no other secure option," Oasis noted.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwtX45ElbEc7nBthFkgABXQjYkiyI9NGcLSIgjz_RTijQyJqAWQN_jpC6d8tT5kmndy_cc3Z-t-nf5qSn4_h4hPvYvEyKCXCCSeerSs-se8UPiFlsEhUGu9L8njUOLAdHmuhPSGQR53GFQ2LjB6YjzSuFzwtZXuCRa7ohUfBbvalFUhU-YGU7FFUh6iqD1/s790-rw-e365/auth.jpg)

The New York-based security company further pointed out that the OAuth tokens used to authorize access are often stored insecurely, adding they are saved in the browser's session storage in plaintext format.

Another potential pitfall is that the authorization workflows may also involve issuing a refresh token, granting the application ongoing access to user data by allowing it to get new access tokens without having to ask the user to log in again when the current token expires.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Following responsible disclosure, Microsoft has acknowledged the problem, although there is no fix as yet. In the interim, it's worth considering temporarily removing the option to upload files using OneDrive through OAuth until a secure alternative is in place. Alternately, it's advised to avoid using refresh tokens and store access tokens in a secure manner and get rid of them when no longer needed.

When reached for comment, Microsoft said: "We appreciate the partnership with Oasis security in responsibly disclosing this issue. This technique does not meet our bar for immediate servicing as a user must provide consent to the application before any access is allowed. We will consider improvements to the experience in a future release."

"The lack of fine-grained OAuth scopes combined with Microsoft's vague user prompt is a dangerous combination that puts both personal and enterprise users at risk," Oasis said. "This discovery reinforces the importance of continuous vigilance in OAuth scope management, regular security assessments, and proactive monitoring to protect user data."

*(The story was updated after publication to include a response from Microsoft.)*

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

[Application Security](https://thehackernews.com/search/label/Application%20Security)[Compliance](https://thehackernews.com/search/label/Compliance)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data privacy](https://thehackernews.com/search/label/data%20privacy)[Microsoft](https://thehackernews.com/search/label/Microsoft)[OAuth](https://thehackernews.com/search/label/OAuth)[OneDrive](https://thehackernews.com/search/label/OneDrive)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defens...
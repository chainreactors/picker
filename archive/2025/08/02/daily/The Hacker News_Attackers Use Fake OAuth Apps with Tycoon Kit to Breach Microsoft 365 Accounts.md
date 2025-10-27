---
title: Attackers Use Fake OAuth Apps with Tycoon Kit to Breach Microsoft 365 Accounts
url: https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html
source: The Hacker News
date: 2025-08-02
fetch_date: 2025-10-07T00:52:20.933932
---

# Attackers Use Fake OAuth Apps with Tycoon Kit to Breach Microsoft 365 Accounts

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

# [Attackers Use Fake OAuth Apps with Tycoon Kit to Breach Microsoft 365 Accounts](https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html)

**Aug 01, 2025**Ravie LakshmananIdentity Theft / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiJoO5nhRUNdg1XVq65Ny72ufGfHE7bdZiieoBTxevOAP9HK3TA1n-KqTIM34qFWAAW236Mpj5nx-ZchXYRWAiOvbx0YX_L0w7SVMRDUD01HgIIf1UDmfv-VCBds8VxOsvN_s6ahnZdCXFDIHqLBio3pLLsvFgQadtQlzEBbJU8fC86w_t3VplLRxzrRxL/s790-rw-e365/ms365.jpg)

Cybersecurity researchers have detailed a new cluster of activity where threat actors are impersonating enterprises with fake [Microsoft OAuth applications](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow) to facilitate credential harvesting as part of account takeover attacks.

"The fake Microsoft 365 applications impersonate various companies, including RingCentral, SharePoint, Adobe, and Docusign," Proofpoint [said](https://www.proofpoint.com/us/blog/threat-insight/microsoft-oauth-app-impersonation-campaign-leads-mfa-phishing) in a Thursday report.

The ongoing campaign, first detected in early 2025, is designed to use the OAuth applications as a gateway to obtain unauthorized access to users' Microsoft 365 accounts by means of [phishing kits](https://blog.sekoia.io/global-analysis-of-adversary-in-the-middle-phishing-threats/) like [Tycoon](https://thehackernews.com/2025/06/fake-recruiter-emails-target-cfos-using.html) and ODx that are capable of conducting multi-factor authentication (MFA) phishing.

The enterprise security company said it observed the approach being used in email campaigns with more than 50 impersonated applications.

The attacks begin with phishing emails sent from compromised accounts and aim to trick recipients into clicking on URLs under the pretext of sharing requests for quotes (RFQ) or business contract agreements.

Clicking on these links directs the victim to a Microsoft OAuth page for an application named "iLSMART" that asks them to grant it permissions to view their basic profile and maintain continued access to the data that they have been granted access to.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

What makes this attack notable is the impersonation of ILSMart, a legitimate online marketplace for aviation, marine, and defense industries to buy and sell parts and repair services.

"The applications' permissions would provide limited use to an attacker, but it is used for setting up the next stage of the attack," Proofpoint said.

Regardless of whether the target accepted or denied the permissions requested, they are first redirected to a CAPTCHA page and then to a phony Microsoft account authentication page once the verification is complete.

This fake Microsoft page makes use of adversary-in-the-middle (AitM) phishing techniques powered by the Tycoon Phishing-as-a-Service (PhaaS) platform to harvest the victim's credentials and MFA codes.

As recently as last month, Proofpoint said it detected another campaign impersonating Adobe in which the emails are sent via Twilio SendGrid, an email marketing platform, and are engineered with the same goal in mind: To gain user authorization or trigger a cancellation flow that redirects the victim to a phishing page.

The campaign represents just a drop in the bucket when compared to overall Tycoon-related activity, with the multiple clusters leveraging the toolkit to perform account takeover attacks. In 2025 alone, attempted account compromises affecting nearly 3,000 user accounts spanning more than 900 Microsoft 365 environments have been observed.

"Threat actors are creating increasingly innovative attack chains in an attempt to bypass detections and obtain access to organizations globally," the company said, adding it "anticipates threat actors will increasingly target users' identity, with AiTM credential phishing becoming the criminal industry standard."

As of last month, Microsoft has [announced](https://mc.merill.net/message/MC1097272) plans to update default settings to improve security by blocking legacy authentication protocols and requiring admin consent for third-party app access. The updates are expected to be completed by August 2025.

"This update will have a positive impact on the landscape overall and will hamstring threat actors that use this technique," Proofpoint pointed out.

The disclosure follows Microsoft's [decision](https://mc.merill.net/message/MC1125497) to disable external workbook links to blocked file types by default between October 2025 and July 2026 in an attempt to enhance workbook security.

The findings also come as spear-phishing emails bearing purported payment receipts are used to deploy by means of an AutoIt-based injector a piece of .NET malware called [VIP Keylogger](https://thehackernews.com/2025/01/hackers-hide-malware-in-images-to.html) that can steal sensitive data from compromised hosts, Seqrite [said](https://www.seqrite.com/blog/spear-phishing-campaign-delivers-vip-keylogger-via-email-attachment/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Over the course of several months, spam campaigns have been spotted concealing installation links to remote desktop software inside PDF files so as to bypass email and malware defenses. The campaign is believed to have been ongoing since November 2024, primarily targeting entities in France, Luxembourg, Belgium, and Germany.

"These PDFs are often disguised to look like invoices, contracts, or property listings to enhance credibility and lure victims into clicking the embedded link," WithSecure [said](https://labs.withsecure.com/publications/email-delivered-rmm). "This design was intended to create the illusion of legitimate content that has been obscured, prompting the victim to install a program. In this case, the program was FleetDeck RMM."

Other Remote Monitoring and Management (RMM) tools deployed as p...
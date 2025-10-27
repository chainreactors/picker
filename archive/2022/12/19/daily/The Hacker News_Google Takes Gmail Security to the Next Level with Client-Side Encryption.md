---
title: Google Takes Gmail Security to the Next Level with Client-Side Encryption
url: https://thehackernews.com/2022/12/gmail-encryption.html
source: The Hacker News
date: 2022-12-19
fetch_date: 2025-10-04T01:55:11.205710
---

# Google Takes Gmail Security to the Next Level with Client-Side Encryption

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

# [Google Takes Gmail Security to the Next Level with Client-Side Encryption](https://thehackernews.com/2022/12/gmail-encryption.html)

**Dec 18, 2022**Ravie LakshmananEncryption / Email Security

[![gmail Client-Side Encryption](data:image/png;base64... "gmail Client-Side Encryption")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjh5ScFnGPyjEzMWtj02IG8Hr2VwK9r9qCFQCt9xY-BAibwfGLK9h_OQZeBwEbEZRsXaVzjCQeQSjX1urP_CGVPMWTeJ-08lO53yNsUeWnVH_reSFT22zCorEbLZLBZcHhAhOQ05NYyJ2fG_SdL4216uP6cRljOkljHRrixbj1jC87LkkKNh51rj9mB/s790-rw-e365/gmail-end-to-end-encryption.png)

Google on Friday announced that its client-side encryption for Gmail is in beta for Workspace and education customers as part of its efforts to secure emails sent using the web version of the platform.

The development comes at a time when concerns about online privacy and data security are at an all-time high, making it a welcome change for users who value the protection of their personal data.

To that end, Google Workspace Enterprise Plus, Education Plus, and Education Standard customers can apply to sign up for the beta until January 20, 2023. It's not available to personal Google Accounts.

"Using client-side encryption in Gmail ensures sensitive data in the email body and attachments are indecipherable to Google servers," the company [said](https://workspaceupdates.googleblog.com/2022/12/client-side-encryption-for-gmail-beta.html) in a post. "Customers retain control over encryption keys and the identity service to access those keys."

It is important to know that the latest safeguards offered by Gmail is different from end-to-end encryption.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Client-side encryption, as the name implies, is a way to protect data at rest. It [allows organizations](https://support.google.com/a/answer/10741897) to encrypt data on Google services with their own cryptographic keys. The data is decrypted on the client-side using keys that are generated and managed by a key management service, which is hosted in the cloud.

Google's opt-in feature requires administrators to [set up an encryption key service](https://support.google.com/a/answer/10801691) through one of the company's partners — which are offered by Flowcrypt, Fortanix, Futurex, Stormshield, Thales, or Virtru — or alternatively, build their own service using its [client-side encryption](https://developers.google.com/workspace/cse) API.

This means the data is protected from unauthorized access, even from the server or the service provider. However, the organization or administrator has control over the keys and can [monitor users' encrypted files](https://support.google.com/a/answer/12768895) or revoke a user's access to the keys, even if they were generated by the user themselves.

On the other hand, end-to-end encryption ([E2EE](https://en.wikipedia.org/wiki/End-to-end_encryption)) is a method of communication in which information is encrypted on the sender's device and can be decrypted only on the recipient's device with a key known only to the sender and the recipient.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

With that said, the new option – limited to the web browser for now – permits users to send and receive encrypted emails both within and outside of their domains. The encryption covers email body and attachments, including inline images, but not the subject and recipient lists.

Gmail is not the only Google product with client-side encryption turned on. The tech giant enabled the same functionality for [Google Drive](https://thehackernews.com/2021/06/google-workspace-now-offers-client-side.html) last year and [Google Meet](https://workspaceupdates.googleblog.com/2022/08/client-side-encryption-for-google-meet.html) earlier this August. A similar test for [Google Calendar](https://workspaceupdates.googleblog.com/2022/10/client-side-encryption-beta-google-calendar.html) ended on November 11, 2022.

It's worth noting that Google Drive apps for desktop as well as Android and iOS support client-side encryption. Google said that the feature will be integrated into mobile apps for Meet and Calendar in an upcoming release.

"Client-side encryption helps strengthen the confidentiality of your data while helping to address a broad range of data sovereignty and compliance needs," the company further added.

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

[email encryption](https://thehackernews.com/search/label/email%20encryption)[email encryption software](https://thehackernews.com/search/label/email%20encryption%20software)[end-to-end encryption](https://thehackernews.com/search/label/end-to-end%20encryption)[gmail](https://thehackernews.com/search/label/gmail)[Gmail Encryption](https://thehackernews.com/search/label/Gmail%20Encryption)[Google](https://thehackernews.com/search/label/Google)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Executio...
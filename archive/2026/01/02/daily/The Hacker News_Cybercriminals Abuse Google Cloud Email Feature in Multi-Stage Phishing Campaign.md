---
title: Cybercriminals Abuse Google Cloud Email Feature in Multi-Stage Phishing Campaign
url: https://thehackernews.com/2026/01/cybercriminals-abuse-google-cloud-email.html
source: The Hacker News
date: 2026-01-02
fetch_date: 2026-01-03T03:23:09.050237
---

# Cybercriminals Abuse Google Cloud Email Feature in Multi-Stage Phishing Campaign

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Cybercriminals Abuse Google Cloud Email Feature in Multi-Stage Phishing Campaign](https://thehackernews.com/2026/01/cybercriminals-abuse-google-cloud-email.html)

**Jan 02, 2026**Ravie LakshmananCloud Security / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYs3DrTLoxNKDEunQc4yjZyAmnuhSyJGccrpxhneZyB6iJ29zkbfcoDpsPZlJYL59ZNTX09BS4FmbV_Yv2WjkB-mptBp_vVyYa4PpPY5jk73XydEvhAdyS-oHdUzSmbCobA7Gnnf6Iogvs3YdR2yC0XkkCGzdz3e9PQ3qg5kaVRVmn3OKxLbfaT2b0SIld/s790-rw-e365/phishing-email.jpg)

Cybersecurity researchers have disclosed details of a phishing campaign that involves the attackers impersonating legitimate Google-generated messages by abusing Google Cloud's [Application Integration](https://cloud.google.com/application-integration) service to distribute emails.

The activity, Check Point said, takes advantage of the trust associated with Google Cloud infrastructure to send the messages from a legitimate email address ("noreply-application-integration@google[.]com") so that they can bypass traditional email security filters and have a better chance of landing in users' inboxes.

"The emails mimic routine enterprise notifications such as voicemail alerts and file access or permission requests, making them appear normal and trustworthy to recipients," the cybersecurity company [said](https://blog.checkpoint.com/research/phishing-campaign-leverages-trusted-google-cloud-automation-capabilities-to-evade-detection/).

Attackers have been observed sending 9,394 phishing emails targeting approximately 3,200 customers over a 14-day period observed in December 2025, with the affected organizations located in the U.S., Asia-Pacific, Europe, Canada, and Latin America.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

At the heart of the campaign is the abuse of Application Integration's "[Send Email](https://docs.cloud.google.com/application-integration/docs/configure-send-email-task)" task, which allows users to send custom email notifications from an integration. Google notes in its support documentation that only a maximum of 30 recipients can be added to the task.

The fact that these emails can be configured to be sent to any arbitrary email addresses demonstrates the threat actor's ability to misuse a legitimate automation capability to their advantage and send emails from Google-owned domains, effectively bypassing [DMARC and SPF checks](https://thehackernews.com/2025/01/neglected-domains-used-in-malspam-to.html).

"To further increase trust, the emails closely followed Google notification style and structure, including familiar formatting and language," Check Point said. "The lures commonly referenced voicemail messages or claims that the recipient had been granted access to a shared file or document, such as access to a 'Q4' file, prompting recipients to click embedded links and take immediate action."

The attack chain is a multi-stage redirection flow that commences when an email recipient clicks on a link hosted on storage.cloud.google[.]com, another trusted Google Cloud service. The effort is seen as another effort to lower user suspicion and give it a veneer of legitimacy.

The link then redirects the user to content served from googleusercontent[.]com, presenting them with a fake CAPTCHA or image-based verification that acts as a barrier by blocking automated scanners and security tools from scrutinizing the attack infrastructure, while allowing real users to pass through.

Once the validation phase is complete, the user is taken to a fake Microsoft login page that's hosted on a non-Microsoft domain, ultimately stealing any credentials entered by the victims.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

In response to the findings, Google has blocked the phishing efforts that abuse the email notification feature within Google Cloud Application Integration, adding that it's taking more steps to prevent further misuse.

Check Point's analysis has revealed that the campaign has primarily targeted manufacturing, technology, financial, professional services, and retail sectors, although other industry verticals, including media, education, healthcare, energy, government, travel, and transportation, have been singled out.

"These sectors commonly rely on automated notifications, shared documents, and permission-based workflows, making Google-branded alerts especially convincing," it added. "This campaign highlights how attackers can misuse legitimate cloud automation and workflow features to distribute phishing at scale without traditional spoofing."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[email security](https://thehackernews.com/search/label/email%20security)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[Google Cloud](https://thehackernews.com/search/label/Google%20Cloud)[identity theft](https://thehackernews.com/search/label...
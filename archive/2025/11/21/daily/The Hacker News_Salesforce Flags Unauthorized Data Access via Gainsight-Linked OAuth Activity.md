---
title: Salesforce Flags Unauthorized Data Access via Gainsight-Linked OAuth Activity
url: https://thehackernews.com/2025/11/salesforce-flags-unauthorized-data.html
source: The Hacker News
date: 2025-11-21
fetch_date: 2025-11-22T03:09:00.381568
---

# Salesforce Flags Unauthorized Data Access via Gainsight-Linked OAuth Activity

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Salesforce Flags Unauthorized Data Access via Gainsight-Linked OAuth Activity](https://thehackernews.com/2025/11/salesforce-flags-unauthorized-data.html)

**Nov 21, 2025**Ravie LakshmananData Breach / SaaS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHdytMLXEXAyU2NJK6I9fULfbh3_5LHXiwqUiFrPD9dP1oEttB2sIbilhx2JTfRV70qGw9NTB4a4C3iqkAfnoR5m4lLxxKBNBWTI6DVQYP3wwHPQHFBkAec9GjKXpzFgMrne79uyQeVa31-yB4vx1nG3FDWsCj3ZHxxLUfk17qAx95t0IeqCSPVu47pILv/s790-rw-e365/salesforce.jpg)

Salesforce has warned of detected "unusual activity" related to Gainsight-published applications connected to the platform.

"Our investigation indicates this activity may have enabled unauthorized access to certain customers' Salesforce data through the app's connection," the company [said](https://status.salesforce.com/generalmessages/20000233) in an advisory.

The cloud services firm said it has taken the step of revoking all active access and refresh tokens associated with Gainsight-published applications connected to Salesforce. It has also temporarily removed those applications from the AppExchange as its investigation continues.

Salesforce did not disclose how many customers were impacted by the incident, but said it has notified them.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

"There is no indication that this issue resulted from any vulnerability in the Salesforce platform," the company added. "The activity appears to be related to the app's external connection to Salesforce."

Out of an abundance of caution, the Gainsight app has been [temporarily pulled](https://status.gainsight.com/incidents/gvng0kly8vwf) from the HubSpot Marketplace and Zendesk connector access has been revoked. "This may also impact Oauth access for customer connections while the review is taking place," Gainsight said. "No suspicious activity related to Hubspot has been observed at this point."

In a post shared on LinkedIn, Austin Larsen, principal threat analyst at Google Threat Intelligence Group (GTIG), described it as an "emerging campaign" targeting Gainsight-published applications connected to Salesforce by compromising third-party OAuth tokens to potentially gain unauthorized access.

The activity is assessed to be tied to threat actors associated with the ShinyHunters (aka UNC6240) group, mirroring a similar set of attacks [targeting Salesloft Drift instances](https://thehackernews.com/2025/09/github-account-compromise-led-to.html) earlier this August.

According to DataBreaches.Net, ShinyHunters has [confirmed](https://databreaches.net/2025/11/20/threat-actors-have-reportedly-launched-yet-another-campaign-involving-an-application-connected-to-salesforce/) the campaign is their doing and stated that the Salesloft and Gainsight attack waves allowed them to steal data from nearly 1000 organizations.

Interestingly, Gainsight previously [said](https://www.gainsight.com/security/) it was also one of the Salesloft Drift customers impacted in the previous attack. But it's not clear at this stage if the earlier breach played a role in the current incident.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

In that hack, the attackers accessed business contact details for Salesforce-related content, including names, business email addresses, phone numbers, regional/location details, product licensing information, and support case contents (without attachments).

"Adversaries are increasingly targeting the OAuth tokens of trusted third-party SaaS integrations," Larsen [pointed out](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7397331617578610690/).

In light of the malicious activity, organizations are advised to review all third-party applications connected to Salesforce, revoke tokens for unused or suspicious applications, and rotate credentials if anomalies are flagged from an integration.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Incident response](https://thehackernews.com/search/label/Incident%20response)[SaaS Security](https://thehackernews.com/search/label/SaaS%20Security)[Salesforce](https://thehackernews.com/search/label/Salesforce)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-aws-ai-security)

Trending News

[![⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More")

⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](https://thehackernews.com/2025/11/weekly-recap-hyper-v-malware-malicious.html)

[![Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic](data:image/svg+xml;base64... "Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic")

Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic](https://thehackernews.com/2025/11/microsoft-uncovers-w...
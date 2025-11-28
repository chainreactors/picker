---
title: Gainsight Expands Impacted Customer List Following Salesforce Security Alert
url: https://thehackernews.com/2025/11/gainsight-expands-impacted-customer.html
source: The Hacker News
date: 2025-11-27
fetch_date: 2025-11-28T03:13:19.486361
---

# Gainsight Expands Impacted Customer List Following Salesforce Security Alert

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

# [Gainsight Expands Impacted Customer List Following Salesforce Security Alert](https://thehackernews.com/2025/11/gainsight-expands-impacted-customer.html)

**Nov 27, 2025**Ravie LakshmananRansomware / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLmTJUwBQylR2JxQKyRPwiaWc6Ia-71wvno8Z5H4N6-8KX7WBGjZLU2ONRBc4Qd7vpIOcWXWkcrekIsNcFhS75LB7IwPMOvGMQPY3xe2yl0qPlgoly_1tEdy99a_glYDj599U0nR2KHQoBkgx49tGys8tsIT_hosQpkSZsiLSXCUFJkCCDWn26eg_jxMpd/s790-rw-e365/sales.jpg)

Gainsight has disclosed that the recent suspicious activity targeting its applications has affected more customers than previously thought.

The company [said](https://communities.gainsight.com/community-news-2/salesforce-security-advisory-relating-to-gainsight-faqs-29809) Salesforce initially provided a list of 3 impacted customers and that it has "expanded to a larger list" as of November 21, 2025. It did not reveal the exact number of customers who were impacted, but its CEO, Chuck Ganapathi, [said](https://www.gainsight.com/blog/supporting-our-customers-and-community-an-update-on-the-recent-security-advisory-related-to-gainsight/) "we presently know of only a handful of customers who had their data affected."

The development comes as Salesforce warned of detected "unusual activity" related to Gainsight-published applications connected to the platform, prompting the company to revoke all access and refresh tokens associated with them. The breach has been claimed by a notorious cybercrime group known as ShinyHunters (aka Bling Libra).

A number of other precautionary steps have been enacted to contain the incident. This includes Zendesk, Gong.io, and HubSpot temporarily suspending their Gainsight integrations, and Google disabling OAuth clients with callback URIs like gainsightcloud[.]com. HubSpot, in its own advisory, [said](https://trust.hubspot.com/?tcuUid=8558d1b8-1314-4a67-a90c-063d8f995ff9) it found no evidence to suggest any compromise of its own infrastructure or customers.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

In an FAQ, Gainsight has also listed the products for which the ability to read and write from Salesforce has been temporarily unavailable -

* Customer Success (CS)
* Community (CC)
* Northpass - Customer Education (CE)
* Skilljar (SJ)
* Staircase (ST)

The company, however, emphasized that Staircase is not affected by the incident and that Salesforce removed the Staircase connection out of caution in response to an ongoing investigation.

Both Salesforce and Gainsight have published indicators of compromise (IoCs) associated with the breach, with one user agent string, "Salesforce-Multi-Org-Fetcher/1.0", used for unauthorized access, also flagged as previously employed in the Salesloft Drift activity.

According to [information](https://help.salesforce.com/s/articleView?id=005229029&type=1) from Salesforce, reconnaissance efforts against customers with compromised Gainsight access tokens were first recorded from the IP address "3.239.45[.]43" on October 23, 2025, followed by subsequent waves of reconnaissance and unauthorized access starting November 8.

To further secure their environments, customers are asked to follow the steps below -

* Rotate the S3 bucket access keys and other connectors like BigQuery, Zuora, Snowflake etc., used for connections with Gainsight
* Log in to Gainsight NXT directly, rather than through Salesforce, until the integration is fully restored
* Reset NXT user passwords for any users who do not authenticate via SSO.
* Re-authorize any connected applications or integrations that rely on user credentials or tokens

"These steps are preventative in nature and are designed to ensure your environment remains secure while the investigation continues," Gainsight said.

The development comes against the backdrop of a new ransomware-as-a-service (RaaS) platform called [ShinySp1d3r](https://thehackernews.com/2025/08/cybercrime-groups-shinyhunters.html) (also spelled Sh1nySp1d3r) that's being developed by Scattered Spider, LAPSUS$, and ShinyHunters (SLSH). Data from ZeroFox has revealed that the cybercriminal alliance has been responsible for at least 51 cyberattacks over the past year.

"While the ShinySp1d3r encryptor has some features common to other encryptors, it also boasts features that have never been seen before in the RaaS space," the company said.

"These include: Hooking the EtwEventWrite function to prevent Windows Event Viewer logging, terminating processes that keep files open – which would normally prevent encryption – by iterating over processes before killing them, [and] filling free space in a drive by writing random data contained in a .tmp file, likely to overwrite any deleted files."

ShinySp1d3r also comes with the ability to [search](https://hackyourmom.com/en/novyny/shinyhunters-stvoryly-novyj-potuzhnyj-raas-detali-majbutnih-atak-uzhe-vidomi/) for open network shares and encrypt them, as well as propagate to other devices on the local network through deployViaSCM, deployViaWMI, and attemptGPODeployment.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

In a report published Wednesday, independent cybersecurity journalist Brian Krebs [said](https://krebsonsecurity.com/2025/11/meet-rey-the-admin-of-scattered-lapsus-hunters/) the individual responsible for releasing the ransomware is a core SLSH member named "Rey" (aka [@ReyXBF](https://web.archive.org/web/20250418062459/https%3A//twitter.com/ReyXBF/status/1913116530658705661)), who is also one of the three administrators of the group's Telegram channel. Rey was previously an administrator of [BreachForums](https://thehackernews.com/2025/09/doj-resentences-breachforums-founder-to.html) and the data leak website for [HellCat ransomware](https://thehackernews.com/2025/01/experts-find-shared-codebase-linking.html).

Rey, whose identity has been unmasked as Saif Al-Din Khader, told Krebs that ShinySp1d3r is a rehash of H...
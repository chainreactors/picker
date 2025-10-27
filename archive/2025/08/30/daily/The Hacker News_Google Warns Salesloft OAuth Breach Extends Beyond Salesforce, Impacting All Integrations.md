---
title: Google Warns Salesloft OAuth Breach Extends Beyond Salesforce, Impacting All Integrations
url: https://thehackernews.com/2025/08/google-warns-salesloft-oauth-breach.html
source: The Hacker News
date: 2025-08-30
fetch_date: 2025-10-07T00:50:28.731956
---

# Google Warns Salesloft OAuth Breach Extends Beyond Salesforce, Impacting All Integrations

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

# [Google Warns Salesloft Drift Breach Impacts All Drift Integrations Beyond Salesforce](https://thehackernews.com/2025/08/google-warns-salesloft-oauth-breach.html)

**Aug 29, 2025**Ravie LakshmananData Breach / Salesforce

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1BrY04SOKYqiKho0jAJ2fts4l0kJBcbJX3b8rvpSFpfGWI_6FC-RjehD9IluFyQRBxkQ70M7AacScxgWVx-1y2O99UETJpo_ONjJIk8WgpMwcaXWqj_2EpThn_l7aIzNQc3knKlUabLII91blrb9j9LY75wVPm9aKq-6RnHu9-PyyHSvKDpP7CMA4kHFa/s790-rw-e365/data-breach.jpg)

Google has revealed that the [recent wave of attacks](https://thehackernews.com/2025/08/salesloft-oauth-breach-via-drift-ai.html) targeting Salesforce instances via Salesloft Drift is much broader in scope than previously thought, stating it impacts all integrations.

"We now advise all Salesloft Drift customers to treat any and all authentication tokens stored in or connected to the Drift platform as potentially compromised," Google Threat Intelligence Group (GTIG) and Mandiant [said](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift) in an updated advisory.

The tech giant said the attackers also used stolen OAuth tokens to access email from a small number of Google Workspace email accounts on August 9, 2025, after compromising the OAuth tokens for the "Drift Email" integration. It's worth noting that this is not a compromise of Google Workspace or Alphabet itself.

"The only accounts that were potentially accessed were those that had been specifically configured to integrate with Salesloft; the actor would not have been able to access any other accounts on a customer's Workspace domain," Google added.

Following the discovery, Google said it notified impacted users, revoked the specific OAuth tokens granted to the Drift Email application, and disabled the integration functionality between Google Workspace and Salesloft Drift amid ongoing investigation into the incident.

The company is also urging organizations using Salesloft Drift to review all third-party integrations connected to their Drift instance, revoke and rotate credentials for those applications, and investigate all connected systems for signs of unauthorized access.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The broadening of the attack radius comes shortly after Google [exposed](https://thehackernews.com/2025/08/salesloft-oauth-breach-via-drift-ai.html) what it described as a widespread and opportunistic data theft campaign that allowed the threat actors, an emerging activity cluster dubbed UNC6395, to leverage compromised OAuth tokens associated with Salesloft Drift to target Salesforce instances from August 8 to 18, 2025.

Salesloft has since [revealed](https://trust.salesloft.com/?uid=Drift+Security+Update%3A+Salesforce+Integrations+%283%3A30PM+ET%29) that Salesforce has temporarily disabled the Drift integration between Salesforce, Slack, and Pardot, only to [follow it up nearly three hours later](https://trust.salesloft.com/?uid=Salesloft+Security+Update%3A+Salesforce+Integrations+%286%3A15PM+ET%29), saying Salesforce has "elected to temporarily [disable all Salesloft integrations](https://status.salesforce.com/generalmessages/20000217?locale=en-US) with Salesforce."

"Based on the investigation to date, there is no evidence of malicious activity detected in the Salesloft integrations related to the Drift incident," it noted. "Additionally, at this time, there are no indications that the Salesloft integrations are compromised or at risk."

### Update

Cybersecurity firm Zcaler has [disclosed](https://www.zscaler.com/blogs/company-news/salesloft-drift-supply-chain-incident-key-details-and-zscaler-s-response) that it's the latest victim stemming from the Salesloft Drift breach after threat actors gained access to its Salesforce instance and stole customer information, including the contents of some support cases.

The activity is part of a campaign that involves stealing OAuth tokens connected to Salesloft Drift to obtain access to Salesforce instances for information theft. Google has attributed the activity to a cluster codenamed UNC6395.

The information accessed was limited to commonly available business contact details for points of contact and specific Salesforce related content, including:

* Names
* Business email addresses
* Job titles
* Phone numbers
* Regional/location details
* Zscaler product licensing and commercial information
* Plain text content from certain support cases [this does NOT include attachments, files, and images]

Zscaler said it has not found any evidence to suggest misuse of this information at this stage, and that swiftly acted to revoke Salesloft Drift's access to Zscaler's Salesforce data and rotate other API access tokens.

In a similar alert, Palo Alto Networks revealed itself to be another victim of the attack campaign leveraging the Salesloft Drift integration to compromise customer Salesforce instances. It also said it's reaching out to a "limited number of customers" that have potentially more sensitive data exposed.

"Our investigation confirms the incident was isolated to our CRM platform; no Palo Alto Networks products or services were impacted, and they remain secure and fully operational," the company [said](https://www.paloaltonetworks.com/blog/2025/09/salesforce-third-party-application-incident-response/). "The data involved includes mostly business contact information, internal sales account and basic case data related to our customers."

Palo Alto Networks Unit 42, which [detailed](https://unit42.paloaltonetworks.com/threat-brief-compromised-salesforce-instances/) the threat actor's modus operandi, said its observations indicate mass exfiltration of sensitive data from various Salesforce objects, including Account, Contact, Case and Opportunity records, with the attackers actively scanning the acquired data for credentials to further expand their access.

[![CIS Build K...
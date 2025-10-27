---
title: Salesloft OAuth Breach via Drift AI Chat Agent Exposes Salesforce Customer Data
url: https://thehackernews.com/2025/08/salesloft-oauth-breach-via-drift-ai.html
source: The Hacker News
date: 2025-08-28
fetch_date: 2025-10-07T00:50:59.337182
---

# Salesloft OAuth Breach via Drift AI Chat Agent Exposes Salesforce Customer Data

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

# [Salesloft OAuth Breach via Drift AI Chat Agent Exposes Salesforce Customer Data](https://thehackernews.com/2025/08/salesloft-oauth-breach-via-drift-ai.html)

**Aug 27, 2025**Ravie LakshmananCloud Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA3n8i-3R37szxYM-Mqk74uLkPqAJJ7NQ-xmiwzE4y4k8YT5ZLkYdiGwQM9JVcN4vAaGr26LBDkX9YyJlhv_e_mQG3YMJleeyLxX75rAmf1gzjRwzBqVTrpRrdzzEAXsfBM7KmRuoFeO1KcdpRfbGdgieIEs8t-RBsZDCPhwmCdFxHUq4MJejn0swFEzMn/s790-rw-e365/sales.png)

A widespread data theft campaign has allowed hackers to breach sales automation platform **Salesloft** to steal OAuth and refresh tokens associated with the Drift artificial intelligence (AI) chat agent.

The activity, assessed to be opportunistic in nature, has been attributed to a threat actor tracked by Google Threat Intelligence Group (GTIG) and Mandiant, tracked as UNC6395. GTIG told The Hacker News that it's aware of over 700 potentially impacted organizations.

"Beginning as early as August 8, 2025, through at least August 18, 2025, the actor targeted Salesforce customer instances through compromised OAuth tokens associated with the Salesloft Drift third-party application," researchers Austin Larsen, Matt Lin, Tyler McLellan, and Omar ElAhdan [said](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift/).

In these attacks, the threat actors have been observed exporting large volumes of data from numerous corporate Salesforce instances, with the likely aim of harvesting credentials that could be then used to compromise victim environments. These include Amazon Web Services (AWS) access keys (AKIA), passwords, and [Snowflake](https://thehackernews.com/2024/06/snowflake-breach-exposes-165-customers.html)-related access tokens.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

UNC6395 has also demonstrated operational security awareness by deleting query jobs, although Google is urging organizations to review relevant logs for evidence of data exposure, alongside revoking API keys, rotating credentials, and performing further investigation to determine the extent of compromise.

Salesloft, in an advisory issued August 20, 2025, said it identified a security issue in the Drift application and that it has proactively revoked connections between Drift and Salesforce. The incident does not affect customers who do not integrate with Salesforce.

"A threat actor used OAuth credentials to exfiltrate data from our customers' Salesforce instances," Salesloft [said](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Update). "The threat actor executed queries to retrieve information associated with various Salesforce objects, including Cases, Accounts, Users, and Opportunities."

The company is also recommending that administrators re-authenticate their Salesforce connection to re-enable the integration. The exact scale of the activity is not known. However, Salesloft said it has notified all affected parties.

In a statement Tuesday, Salesforce said a "small number of customers" were impacted, stating the issue stems from a "compromise of the app's connection."

"Upon detecting the activity, Salesloft, in collaboration with Salesforce, invalidated active Access and Refresh Tokens, and removed Drift from AppExchange. We then notified affected customers," Salesforce [added](https://status.salesforce.com/generalmessages/20000217?locale=en-US).

The development comes as [Salesforce instances](https://thehackernews.com/2025/06/google-exposes-vishing-group-unc6040.html) have [become an active target](https://thehackernews.com/2025/08/cybercrime-groups-shinyhunters.html) for financially motivated threat groups like [UNC6040 and UNC6240](https://www.obsidiansecurity.com/blog/shinyhunters-and-scattered-spider-a-merger-of-chaos-in-the-2025-salesforce-attacks) (aka ShinyHunters), the latter of which has since joined hands with Scattered Spider (aka UNC3944) to secure initial access.

Austin Larsen, principal threat analyst at GTIG, said UNC6395 is a new emerging cluster, adding "we have not observed any compelling evidence connecting them to other groups at this time."

"What's most noteworthy about the UNC6395 attacks is both the scale and the discipline," Cory Michal, CSO of AppOmni, said. "This wasn't a one-off compromise; hundreds of Salesforce tenants of specific organizations of interest were targeted using stolen OAuth tokens, and the attacker methodically queried and exported data across many environments."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"They demonstrated a high level of operational discipline, running structured queries, searching specifically for credentials, and even attempting to cover their tracks by deleting jobs. The combination of scale, focus, and tradecraft makes this campaign stand out."

Michal also pointed out that many of the targeted and compromised organizations were themselves security and technology companies, indicating that the campaign may be an "opening move" as part of a broader supply chain attack strategy.

"By first infiltrating vendors and service providers, the attackers put themselves in position to pivot into downstream customers and partners," Michal added. "That makes this not just an isolated SaaS compromise, but potentially the foundation for a much larger campaign aimed at exploiting the trust relationships that exist across the technology supply chain."

### Update

Saleloft, in a follow-up alert, said it has engaged the services of Mandiant and Coalition to investigate the breach and to facilitate containment and remediation efforts. It's also urging Drift customers to update their API keys for each connected Drift integration.

"We are recommending that all Drift customers who manage their own Drift connections to third-party applications via API key, proactively revoke the existing key and reconne...
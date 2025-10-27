---
title: Data Breach Reporting for regulatory requirements with Microsoft Data Security Investigations​​
url: https://techcommunity.microsoft.com/blog/microsoft-security-blog/%E2%80%8B%E2%80%8Bdata-breach-reporting-for-regulatory-requirements-with-microsoft-data-security/4424950
source: Microsoft Security Blog
date: 2025-06-19
fetch_date: 2025-10-06T22:57:04.701222
---

# Data Breach Reporting for regulatory requirements with Microsoft Data Security Investigations​​

[Skip to content](#main-content)[![Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](/)

[Tech Community](/)[Community Hubs](/Directory)

[Products](/)

[Topics](/)

[Blogs](/Blogs)[Events](/Events)

[Microsoft Learn](/category/MicrosoftLearn)

[Community](/)

[Register](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2F%25E2%2580%258B%25E2%2580%258Bdata-breach-reporting-for-regulatory-requirements-with-microsoft-data-security%2F4424950)[Sign In](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2F%25E2%2580%258B%25E2%2580%258Bdata-breach-reporting-for-regulatory-requirements-with-microsoft-data-security%2F4424950)

1. [Microsoft Community Hub](/)
3. [Communities](/category/communities)[Products](/category/products-services)[Microsoft Security](/category/microsoft-security)
5. [Microsoft Security](/category/microsoft-security-product)
7. [Microsoft Security Community Blog](/category/microsoft-security-product/blog/microsoft-security-blog)

## Blog Post

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDI0OTUwLUhUcVZxcQ?revision=5&image-dimensions=2000x2000&constrain-image=true)

Microsoft Security Community Blog

5 MIN READ

# ​​Data Breach Reporting for regulatory requirements with Microsoft Data Security Investigations​​

[![SteveVandenberg's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS00NjUwOTMtMTBHREsx?image-coordinates=0%2C155%2C1920%2C2075&image-dimensions=50x50)](/users/stevevandenberg/465093)

[SteveVandenberg](/users/stevevandenberg/465093)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Jun 18, 2025

## Organizations face demanding data breach reporting requirements under regulations like GDPR and SEC rules. Use Microsoft Purview DSI to efficiently scope breaches​ with AI.

Seventy-four percent of organizations surveyed experienced at least one data security incident with their business data exposed in the previous year as reported in Microsoft’s [Data Security Index: Trends, insights, and strategies to secure data](https://aka.ms/datasecurityindex) report.  Despite the best people, process and technology we can apply to prevent it, confidential information is sometimes improperly exposed.  Depending on the specifics of the incident, organizations must report these breaches to regulators, customers or other stakeholders.

##### **A Challenging Landscape for Data Breach Reporting**

Regulatory standards like General Data Protection Regulation (GDPR), Gramm-Leach Bliley Safeguards (GLBA), Payment Card Industry Data Security Standard (PCI-DSS), Health Insurance Portability and Accountability Act (HIPAA), Network and Information Systems Directive 2 (NIS2), SEC Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure rules and an ever increasing list of others require disclosure of data breaches to regulators and potentially to customers or other stakeholders.

The requirements to report after an organization discovers the breach can be demanding.  For instance, under GDPR, any breach requires notification to the EU data protection authorities and potentially individual affected users within 72 hours from the time the breach is discovered.

NIS2 requires and initial notification to the relevant national authority within 24 hours of detecting a significant cyber event and a detailed report within 72 hours.

PCI-DSS requires merchants and service providers to immediately notify the credit card companies in the event of a breach.

Under the SEC rules, a company must file a Form 8-K within four business days of having discovered a material breach which must be done “without unreasonable delay.”  Materiality is determined by management based on the risk posed to shareholders by the exposed data.

##### **Scoping the Breach and Understanding the Risk**

Organizations discover they’ve had a data breach from their security tools, unusual system behavior, reports from employees, customers or law enforcement.  Available information is often incomplete and scattered across systems.  Understanding the true scope of the breach is challenging.

Scoping the breach is an exercise not only in enumerating files and instances of sensitive information but also understanding the context, what data is sensitive, and the degree of risk the various exposed data presents to the organization and its stakeholders.

Management often turns to the CISO to understand the scope and risk of the data exposed to inform the organization’s reporting.

There can be a huge volume of information available from the organization’s IT systems that must be reasoned over in a short time.  Context is important as are semantics to understand the scope of the breach and risk to the organization, customers, other data subjects, employees and shareholders.  There will be high demand on the information security team and its service providers.  A force multiplier, in the form of artificial intelligence is needed to scope data breaches accurately and efficiently.

##### **Microsoft Purview Data Security Investigations (DSI)**

DSI, an integrated part of the Microsoft Purview Data Security solution, allows an administrator to search Microsoft 365, locates documents, emails, Teams messages, Copilot prompts and prompt returns relevant to a data breach.  Customers can also upload non-Microsoft 365 data to a SharePoint site for analysis.

DSI reasons over the impacted data with Azure OpenAI, categorizes it in terms of the specific risks it poses to the organization e.g. credentials, customer information, health, financials and a range of other types of data exposed.  It goes beyond keywords using deep content analysis to understand the nature and risk severity of the data.  This can be part of determining the materiality of a breach for reporting purposes.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDI0OTUwLVR6WE5XOA?image-dimensions=999x558&revision=5)Figure 1 - Exposed data is automatically categorized and assessed for risk severity by AI

DSI can categorize and report on data based on predefined risks.  It can also search for custom categories important to the investigator.  It uses vector based semantic search to identify similar information and user intent even in the absence of keywords.

DSI understands data in multiple languages so it can categorize and respond to questions on data even if the investigator doesn’t.  DSI uses Copilot to assist the investigator throughout the examination with interactive answers to questions in natural language.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDI0OTUwLVowakM4Rw?image-dimensions=999x562&revision=5)Figure 2 - DSI investigation page with scope and progress of the investigation with risk and mitigation reporting

##### **An integrated part of the Microsoft Purview Solution**

Data breaches can result from the actions of external bad actors or trusted insiders.  They can result from intentional or accidental exposure.  DSI helps organizations to investigate all of these.

DSI can launch an investigation directly from a case in Purview Insider Risk Management, coming soon, or an incident in Microsoft Defender XDR.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDI0OTUwLWxaZVZ3VA?image-dimensions=999x555&revision=5)Figure 3 - DSI investigation will be able to initiate directly from a Purview Insider Risk Management case

DSI can also initiate an investigation from its own part of the Purview Portal with or without the use of predefined search templates.

We’re focusing on data breach reporting in this article but DSI is a full scope...
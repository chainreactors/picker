---
title: Sandfly 5.5 - AI-Powered Analysis, Advanced BPFDoor Detection, and Smarter Scanning
url: https://sandflysecurity.com/blog/sandfly-5-5-ai-powered-analysis-advanced-bpfdoor-detection-and-smarter-scanning
source: Sandfly Security Blog RSS Feed
date: 2025-07-17
fetch_date: 2025-10-06T23:38:56.678818
---

# Sandfly 5.5 - AI-Powered Analysis, Advanced BPFDoor Detection, and Smarter Scanning

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.5 - AI-Powered Analysis, Advanced BPFDoor Detection, and Smarter Scanning

16 July 2025

Product Update

Sandfly 5.5 announces AI analysis for security events, enhanced coverage for BPFDoor, and scanning performance upgrades.

We’ve implemented AI Large Language Model (LLM) integrations for all major vendors and also on-prem LLM solutions for customers. This is a very powerful new feature and is not just hype. We recommend customers read more about this new feature below to see if it is a fit for your organization.

Further, we have expanded detection coverage for updated BPFDoor malware. This malware is still impacting many critical infrastructure providers and our new detections expand our already existing coverage.

Finally, we’ve made performance improvements to areas such as scheduled scans that now feature a default “trickle” mode. This mode will spread out scans over the time window to lower network and host loads.

### AI for Linux Security

We often get asked by customers what a particular alert means, how to investigate it, etc. This is especially true for teams that have limited access to personnel with deep Linux forensics understanding. After watching and experimenting with the new generation of AI LLMs, we feel we're at a place where we can offer a powerful new AI security analyst feature for our customers that helps answer these questions.

### Good Data for Good Results

At Sandfly we saw that many LLMs were getting a bad reputation because they were being asked to analyze and draw conclusions from bad data. LLMs with bad data will always provide bad results when asked to interpret it (the same way a human would). However, Sandfly is different for two very important reasons:

1. We are in total control of our data quality because we generate it ourselves.
2. We know what questions to ask of that data.

These points are critical for good and reliable LLM usage in security contexts.

Understand that the data we obtain for Linux forensics is sourced by us directly and is the best in the industry. Our exclusive focus on Linux means we are not distracted with other platforms or need to worry about what a third party is throwing over the wall for us to handle in random logs. Our tools are purpose-built to collect Linux forensics data accurately and fast without relying on anyone else. Issues around LLM hallucinations and incorrect analysis are minimized as a result.

### AI Analysis in Action

Our AI analysis is available in the host and results sections. For host analysis the LLM will summarize the state of the system and incorporate any alerts into the report. For results, the AI can be passed one or more entries and it will analyze each and attach the report to the result data. Let's demonstrate on actual malware.

#### Analyzing BPFDoor with AI

We'll show how our new LLM integration works with our old friend *BPFDoor*. On our test system we have started *BPFDoor* Version 2. It is memory resident and hiding waiting for activation of the backdoor with a magic packet. Sandfly has found this suspicious process and it's part of the host results showing multiple alerts as seen below.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![BPFDoor results detected by Sandfly](https://www.datocms-assets.com/56687/1752637622-results-bpfdoor2.png?auto=format&dpr=2&q=60&w=920 "BPFDoor results detected by Sandfly")

#### Initiating AI Assistance

To begin, we go to our host and activate the *Analyze Host* button. This button will only be active if you have put in an API key to your preferred LLM provider. This can be a commercial cloud offering like *Gemini*, *OpenAI*, or *Grok*. Or, it can be an internal version of an LLM you choose.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Analyzing a host in Sandfly.](https://www.datocms-assets.com/56687/1752637687-llm-host-analysis-button.png?auto=format&dpr=2&q=60&w=920 "Analyzing a host in Sandfly.")

Our analysis is now returned. Sandfly has created a host summary along with relevant alert data in an easy to understand summary seen below. You'll see several sections that we'll discuss.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![AI LLM host analysis completed.](https://www.datocms-assets.com/56687/1752637832-llm-host-analysis-overview.png?auto=format&dpr=2&q=60&w=920 "AI LLM host analysis completed.")

#### Brief and Overview

All analyses begin with a brief and overview section. The brief gives you a one sentence synopsis of the problem with a full summary of the situation in the overview. Below we see our host situation is neatly summarized and we have a suspicious process that was identified.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Brief and overview of detected Linux threat.](https://www.datocms-assets.com/56687/1752637913-llm-host-analysis-brief-and-overview.png?auto=format&dpr=2&q=60&w=920 "Brief and overview of detected Linux threat.")

#### Details

The details section lays out specifics about what is happening in easy to interpret points. Our host has many significant problems identified and summarized by the LLM in a way operators can easily understand.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Details of a malicious process on a host.](https://www.datocms-assets.com/56687/1752624817-llm-host-details.png?auto=format&dpr=2&q=60&w=920 "Details of a malicious process on a host.")

#### Investigation

Next, we provide several areas to help guide the operator on how to investigate the suspicious activity on the host. These suggestions are non-destructive and can help gather additional information to add to an incident report before deciding actions. The investigative commands suggested here will often be installed by default so there is no need to load additional tools on systems to do an investigation.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![LLM investigation suggestions for suspicious Linux process.](https://www.datocms-assets.com/56687/1752624938-llm-result-investigation.png?auto=format&dpr=2&q=60&w=920 "LLM investigation suggestions for suspicious Linux process.")

#### Recommended Actions

We will then provide a list of simple and again non-destructive actions operators may want to take. They can vary depending on the attack type, but often involve ideas around host isolation, gathering forensic data, and more.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Recommended response actions.](https://www.datocms-assets.com/56687/1752637974-llm-result-recommended-actions.png?auto=format&dpr=2&q=60&w=920 "Recommended response actions.")

#### Suggested Items to Investigate

Finally, we'll give you a list of other items we suggest you investigate that may not be directly part of the existing forensic data, but often provide valuable information to help investigate root cause analysis. These recommendations again are non-destructive and built-in commands on most Linux hosts or may be available in your security stack elsewhere (e.g. network activity to the host).

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Suggested items to investigate on a compromised Linux host.](https://www.datocms-assets.com/56687/1752625209-llm-host-analysis-suggested-items-to-investigate.png?auto=format&dpr=2&q=60&w=920 "Suggested items to investigate on a compromised Linux host.")

#### Result Analysis

Analyzing individual results follows a similar procedure to host analysis, but can provide more specific insights into individual alerts. Users can send in multiple alerts for parallel analysis. The analysis data will remain with the alert result until deleted.

#### Ask T...
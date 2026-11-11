---
title: Fireworks AI Confirms Wider Breach Affecting Customer Datasets, Model Weights and Notion AI Chats
url: https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html
source: The Hacker News
date: 2026-11-10
fetch_date: 2026-11-11T08:35:39.886905
---

# Fireworks AI Confirms Wider Breach Affecting Customer Datasets, Model Weights and Notion AI Chats

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Fireworks AI Confirms Wider Breach Affecting Customer Datasets, Model Weights and Notion AI Chats](https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html)

**Ravie Lakshmanan**Nov 10, 2026Cybercrime / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-mBJN_E4CjW3MXyjYYdeCGcyR052aVnG3uUWjaEfafvPAdatcJhn9LbtngqXBb5JsVwJVoorc8i41nTbYR9UcwVrwWNzU-WAfVk2yL32hYW1elVMJtwauW53nhRG37EwbovnFCW8InensI8tKoR9pqcWnZx54t6xOU_HsjjR9KWTLwVr_MBcknFeGShZU/s1700-nu-rw-lo-l85-e365/fire.jpg)

Fireworks AI disclosed on Monday that its investigation into a security incident first reported early last month uncovered further malicious activity, affecting account and billing information, alongside secrets, datasets, and incomplete models for a "limited set of accounts."

In a notice [published](https://fireworks.ai/security/bulletins/october-2026-security-incident) on October 10, 2026, the company said it detected unauthorized use of internal Fireworks credentials that allowed an unauthorized third-party to access environment variables used in evaluation jobs in a limited number of customer accounts. The activity was detected on October 6, 2026, at 9 a.m. PDT.

At that time, the AI infrastructure provider said it only found evidence that environment variables, including API keys and tokens stored as secrets, were captured in certain affected accounts, adding that there were no signs that customer models, datasets, training data, inference traffic, or personal information were accessed.

In response to the incident, Fireworks AI took the step of revoking the compromised internal credentials and rotating service account tokens, along with affected Fireworks API keys and keys created by the threat actor.

The latest bulletin from the company reveals that the scope of the breach may have been broader than previously thought. The company said attackers reached its development environment via an unnamed third-party cloud provider that hosted Fireworks research and development (R&D) machines on October 23, 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

"On October 24, the unauthorized third party used it to reach Fireworks development machines and then run an unauthorized workload that led to additional customer data impact," it [added](https://fireworks.ai/security/bulletins/october-2026-security-incident-update). "As of October 25, we have not detected further evidence of successful unauthorized access by the threat actor on the Fireworks platform customers use."

The breach is said to have provided access to the following types of information -

* Resource metadata: Fireworks resource identifiers, display names, descriptions, and creation time
* Billing information: billing and shipping addresses, invoice and payment history, account balance, and credit usage
* Model weights and datasets: a subset of incomplete model weights and datasets for certain customers

Fireworks AI said payment card numbers are not stored by the company and were not impacted by the security incident. It also said it's alerting customers whose data was impacted.

The company also noted that it has implemented security hardening procedures, such as credential revocation and rotation; isolating affected systems to prevent further unauthorized activity and lateral movement; tightening access controls; and improving its logging and monitoring systems.

"The evidence indicates links to a cybercriminal threat actor group, which is financially motivated and aimed at selling tokens from unauthorized access to large language models (LLMs) to illicit routing gateways," it said.

The activity is assessed to be part of an emerging threat known as [LLMjacking](https://thehackernews.com/2026/11/google-warns-llmjacking-attacks-are.html), which refers to the act of hijacking a victim's LLM through stolen credentials to fuel a criminal enterprise that thrives on peddling the access to other threat actors, while leaving the legitimate owner to pay the bill.

Last week, Google issued a warning that threat actors are increasingly targeting AI infrastructure for LLMjacking in North America, South America, and Asia Pacific across the financial services, retail, technology, and transportation sectors.

### Notion Impacted by Fireworks AI Incident

Popular productivity and note-taking application Notion has [disclosed](https://www.notion.com/en-us/security/advisories/security-incident-involving-a-third-party-ai-vendor) that the security incident targeting Fireworks AI impacted "fewer than 1% of Notion workspaces." In a post shared on Reddit, one user [said](https://www.reddit.com/r/Notion/comments/1xsddi7/important_security_notice_about_the_fireworks_ai/): "looks like all of us are part of that <1%."

While the initial assessment was that the breach allowed the threat actor to access Notion AI synthetic testing data, it has since come to light that it may also have involved potential customer data.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"Upon analysis of the new data, we discovered that it included Notion AI chat transcripts used for the Insights feature, which for the vast majority of impacted workspaces were unattributable," it said. "'Unattributable' means the chats weren't labeled with who wrote them or which workspace they came from, and the transcripts did not contain tool call results."

Notion has also emphasized that no other features across its platform were affected by the incident. The Insights feature has since been disabled as it continues to investigate the breach and the company is no longer serving open-weight models through Fireworks.

Affected customers are advised to review the impacted data securely inside their workspace. If those with affected workspaces have pasted sensitive information, passwords, API keys, or other credentials during the attack window, it's recommended to ro...
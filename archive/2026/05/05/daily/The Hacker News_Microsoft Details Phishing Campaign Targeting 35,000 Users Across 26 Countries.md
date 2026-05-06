---
title: Microsoft Details Phishing Campaign Targeting 35,000 Users Across 26 Countries
url: https://thehackernews.com/2026/05/microsoft-details-phishing-campaign.html
source: The Hacker News
date: 2026-05-05
fetch_date: 2026-05-06T05:09:55.445888
---

# Microsoft Details Phishing Campaign Targeting 35,000 Users Across 26 Countries

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Microsoft Details Phishing Campaign Targeting 35,000 Users Across 26 Countries](https://thehackernews.com/2026/05/microsoft-details-phishing-campaign.html)

**Ravie Lakshmanan**May 05, 2026

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAfU-GpnCdjg1P2f40nj2Y7eLLpsjWNa1TnSlNm3m9F7VkOryT5etD2BouMGxbfatdzukMzeCPXsDagasXWNbcwUPJNkDY-sBox3DkrA0bTYjAEOk4JV8OySSD1_Ni2DgEnoWih83X65e9K1foEaEUetNxoyXFJnGx4Np8VQWrZSnxo2UMmR0Y68L-qf0y/s1700-e365/ms-hook.jpg)

Microsoft has disclosed details of a large-scale credential theft campaign that has leveraged a combination of code of conduct-themed lures and legitimate email services to direct users to attacker-controlled domains and steal authentication tokens.

The multi-stage campaign, observed between April 14 and 16, 2026, targeted more than 35,000 users across over 13,000 organizations in 26 countries, with 92% of the targets located in the U.S. The majority of phishing emails were directed against healthcare and life sciences (19%), financial services (18%), professional services (11%), and technology and software (11%) sectors.

"The lures in this campaign used polished, enterprise-style HTML templates with structured layouts and preemptive authenticity statements, making them appear more credible than typical phishing emails and increasing their plausibility as legitimate internal communications," the Microsoft Defender Security Research Team and Microsoft Threat Intelligence [said](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/).

"Because the messages contained accusations and repeated time-bound action prompts, the campaign created a sense of urgency and pressure to act."

The email messages used in the campaign employ lures related to code of conduct reviews, using display names like "Internal Regulatory COC," "Workforce Communications," and "Team Conduct Report." Subject lines associated with these emails include "Internal case log issued under conduct policy" and "Reminder: employer opened a non-compliance case log."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

"At the top of each message, a notice stated that the message had been 'issued through an authorized internal channel' and that links and attachments had been 'reviewed and approved for secure access,' reinforcing the email's purported legitimacy," Microsoft explained.

It's assessed that the emails are sent from a legitimate email delivery service. The messages also come with a PDF attachment that purportedly gives additional information about the conduct review, luring victims to click on a link within the document to initiate the credential harvesting flow.

The attack chain has been found directing victims through multiple rounds of CAPTCHA and intermediate pages that are designed to lend the scheme a veneer of legitimacy, at the same time keeping out automated defenses.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhh-ZxdAVoqDpIQvz0Q6SYjCZo6zSbdAwVkEooQSeQwk8qdSmdUNgxdY6bmS10g0CPNuDCQRGIxv_x7LxUSYt5zNL_-7M3CyUOJhjcuN1nMVg-iXmKdV3_5lXpvlSkyBxzPXPSdLBe7htr8nAt86EyOCZxByNVgkJog2t7cuZCnXQ3-EVe4D6xTfADUk6xp/s1700-e365/ms-phish.jpg)

Ultimately, it ends with a sign-in experience that leverages adversary‑in‑the‑middle (AiTM) phishing tactics to harvest Microsoft credentials and tokens in real-time, effectively allowing the threat actors to bypass multi-factor authentication (MFA). The final destination, per Microsoft, depends on whether the malicious flow was triggered from a mobile device or a desktop system.

### Phishing Trends in 2026

The disclosure comes as Microsoft's analysis of the email threat landscape between January and March 2026 revealed that QR code phishing emerged as the fastest-growing attack vector, while CAPTCHA-gated phishing evolved "rapidly" across payload types. In all, the tech giant said it detected about 8.3 billion email-based phishing threats.

Of these, nearly 80% were link-based, where large HTML and ZIP files accounted for a huge chunk of the malicious payloads distributed via phishing emails. The end goal of a vast majority of these attacks was credential harvesting, with malware delivery declining to a mere 5-6% by the end of the quarter.

Microsoft also said the operators of the Tycoon 2FA phishing-as-a-service (PhaaS) platform have attempted to shift hosting providers and domain registration patterns following a [coordinated disruption operation](https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html) in March 2026.

"Toward the end of March, we saw Tycoon 2FA moving away from Cloudflare as a hosting service and now hosts most of its domains across a variety of alternative platforms, suggesting the group is attempting to find replacement services that offer comparable anti-analysis protections," it [added](https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBZqfXKwkQjqaIMDbBQCJW8OwSGb7wQkZROAeHGeAHwwCDfYvGW4THIhj4Ll3XELMa0RK2qt17_z1_AlD34PExbZ6rMFL2ZRhC_Bd-2uBdcXpiaTG5SVLDKEcAz_hrHQ8vqexNuulHm7hX7rh93h63JhXLh4hdNxM1x2ArckNPIrVZl5o-1V7yyqPUo17H/s1700-e365/QR.png)

In a report published back in February, Palo Alto Networks Unit 42 [highlighted](https://unit42.paloaltonetworks.com/qr-codes-as-attack-vector/) how threat actors are abusing QR codes as URL shorteners to disguise malicious destinations, in-app deep links to steal account credentials, and bypass app store security by linking to direct downloads of malicious apps.

Data from Microsoft shows a massive surge in QR code phishing during the three-month time period, as attack volumes jumped from 7.6 million in January to 18.7 million in March, representing a 146% increase. One notable developmen...
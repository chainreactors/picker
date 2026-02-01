---
title: Mandiant Finds ShinyHunters-Style Vishing Attacks Stealing MFA to Breach SaaS Platforms
url: https://thehackernews.com/2026/01/mandiant-finds-shinyhunters-using.html
source: The Hacker News
date: 2026-01-31
fetch_date: 2026-02-01T04:27:21.151062
---

# Mandiant Finds ShinyHunters-Style Vishing Attacks Stealing MFA to Breach SaaS Platforms

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

# [Mandiant Finds ShinyHunters-Style Vishing Attacks Stealing MFA to Breach SaaS Platforms](https://thehackernews.com/2026/01/mandiant-finds-shinyhunters-using.html)

**Ravie Lakshmanan**Jan 31, 2026Social Engineering / SaaS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2lnJbnFaov0GE_74eq7mb52_5L4JzxpsP2dS-QqlaAJ8aSuWL-QRFQhkHSS_oso_YVwAUrLjhG_V2oVRGfxZuZjrf4dfYkkGI-e-OXJUq3exOdhCJC8I00T3cmSuQGdK52eeajtBJryw95T-fl27BXaYYewKTAhgZPKj_ZWcaQDJhbSkj59dV4l0SZe8G/s1700-e365/vishing.jpg)

Google-owned Mandiant on Friday [said](https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft) it identified an "expansion in threat activity" that uses tradecraft consistent with extortion-themed attacks orchestrated by a financially motivated hacking group known as ShinyHunters.

The attacks leverage advanced [voice phishing](https://thehackernews.com/2026/01/threatsday-bulletin-new-rces-darknet.html#human-in-the-loop-mfa-bypass) (aka vishing) and bogus credential harvesting sites mimicking targeted companies to gain unauthorized access to victim environments by collecting sign-on (SSO) credentials and multi-factor authentication (MFA) codes.

The end goal of the attacks is to target cloud-based software-as-a-service (SaaS) applications to siphon sensitive data and internal communications and extort victims.

The tech giant's threat intelligence team said it's tracking the activity under multiple clusters, including UNC6661, UNC6671, and [UNC6240](https://thehackernews.com/2025/11/salesforce-flags-unauthorized-data.html) (aka ShinyHunters), so as to account for the possibility that these groups could be evolving their modus operandi or mimicking previously observed tactics.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

"While this methodology of targeting identity providers and SaaS platforms is consistent with our prior observations of threat activity preceding ShinyHunters-branded extortion, the breadth of targeted cloud platforms continues to expand as these threat actors seek more sensitive data for extortion," Mandiant noted.

"Further, they appear to be escalating their extortion tactics with recent incidents, including harassment of victim personnel, among other tactics."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_5Ws1TFQXojWMV2ICgbzFKj29-R72rAsIXrSMISHdhJxonhBIemPKPb_jBMTslfVzRww5vDmOzuX8m0cKTjih0DyI56AQcXaBLdEDlWpseM3OjKYcmwv9A2BkGxqUJb5kC1LhnfgwbRagqtw9cIGHQcQq9BLVmPCBZjnglu9g9gy__NZCt2ycca_SVuRG/s1700-e365/google.png)

Details of the vishing and credential theft activity are as follows -

* UNC6661 has been observed pretending to be IT staff in calls to employees at targeted victim organizations, directing them to credential harvesting links under the guise of instructing them to update their multi-factor authentication (MFA) settings. The activity was recorded between early and mid-January 2026.
* The stolen credentials are then used to register their own device for MFA and then move laterally across the network to exfiltrate data from SaaS platforms. In at least one case, the threat actor weaponized their access to compromised email accounts to send more phishing emails to contacts at cryptocurrency-focused companies. The emails were subsequently deleted to cover up the tracks. This is followed by extortion activity conducted by UNC6240.
* UNC6671 has also been identified as impersonating IT staff to deceive victims as part of efforts to obtain their credentials and MFA authentication codes on victim-branded credential harvesting sites since early January 2026. In at least some instances, the threat actors gained access to Okta customer accounts. UNC6671 has also leveraged PowerShell to download sensitive data from SharePoint and OneDrive.
* The differences between UNC6661 and UNC6671 relate to the use of different domain registrars for registering the credential harvesting domains (NICENIC for UNC6661 and Tucows for UNC6671), as well as the fact that an extortion email sent following UNC6671 activity did not overlap with known UNC6240 indicators.
* This indicates that different sets of people may be involved, illustrating the amorphous nature of these cybercrime groups. What's more, the targeting of cryptocurrency firms suggests that the threat actors may also be looking to explore further avenues for financial gain.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

To counter the threat posed to SaaS platforms, Google has [outlined](https://cloud.google.com/blog/topics/threat-intelligence/defense-against-shinyhunters-cybercrime-saas) a long list of hardening, logging, and detection recommendations -

* Improve help desk processes, including requiring personnel to require a live video call to verify their identity
* Limit access to trusted egress points and physical locations; enforce strong passwords; and remove SMS, phone call, and email as authentication methods
* Restrict management-plane access, audit for exposed secrets and enforce device access controls
* Implement logging to increase visibility into identity actions, authorizations, and SaaS export behaviors
* Detect MFA device enrollment and MFA life cycle changes; look for OAuth/app authorization events that suggest mailbox manipulation activity using utilities like [ToogleBox Email Recall](https://www.tooglebox.com/features/email-recall), or identity events occurring outside normal business hours

"This activity is not the result of a security vulnerability in vendors' products or infrastructure," Google said. "Instead, it continues to highlight the effectiveness of social engineering and underscores the importance of organizations moving towards phishing-resistant MFA where possible. Methods such as FIDO2 security keys or passkeys are resistant to social engineering in ways that push-based, or SMS authentication are not."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share...
---
title: PlayPraetor Reloaded: CTM360 Uncovers a Play Masquerading Party
url: https://thehackernews.com/2025/04/playpraetor-reloaded-ctm360-uncovers.html
source: The Hacker News
date: 2025-04-11
fetch_date: 2025-10-06T22:07:13.802347
---

# PlayPraetor Reloaded: CTM360 Uncovers a Play Masquerading Party

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

# [PlayPraetor Reloaded: CTM360 Uncovers a Play Masquerading Party](https://thehackernews.com/2025/04/playpraetor-reloaded-ctm360-uncovers.html)

**Apr 10, 2025**The Hacker NewsFinancial Fraud / Mobile Security

[![](data:image/png;base64...)](https://www.ctm360.com/reports/playpraetor-trojan-report)

### **Overview of the PlayPraetor Masquerading Party Variants**

[CTM360](https://www.ctm360.com) has now identified a much larger extent of the ongoing Play Praetor campaign. What started with 6000+ URLs of a very specific banking attack has now grown to 16,000+ with multiple variants. This research is ongoing, and much more is expected to be discovered in the coming days.

As before, all the newly discovered play impersonations are mimicking legitimate app listings, deceiving users into installing malicious Android applications or exposing sensitive personal information. While these incidents initially appeared to be isolated, further investigation has revealed a globally coordinated campaign that poses a significant threat to the integrity of the Play Store ecosystem.

### **Evolution of the Threat**

[This report](https://www.ctm360.com/reports/playpraetor-trojan-report) expands on the earlier research into PlayPraetor, highlighting the discovery of five newly identified variants. These variants reveal the campaign's increasing sophistication in terms of attack techniques, distribution channels, and social engineering tactics. The continuous evolution of PlayPraetor demonstrates its adaptability and persistent targeting of the Android ecosystem.

### **Variant-Specific Targeting and Regional Focus**

In addition to the original PlayPraetor Banking Trojan, five new variants—**Phish**, **RAT**, **PWA**, **Phantom**, and **Veil**—have been identified. These variants are distributed through fake websites that closely resemble the Google Play Store. Although they share common malicious behaviors, each variant exhibits unique characteristics tailored to specific regions and use cases. Targeted regions include the Philippines, India, South Africa, and various global markets.

These variants employ a mix of credential phishing, remote access capabilities, deceptive web app installations, abuse of Android accessibility services, and stealth techniques that hide malicious activity behind legitimate branding.

### **Attack Objectives and Industry Focus**

While each variant has unique features and regional targeting, a common theme across all PlayPraetor samples is their focus on the **financial sector**. Threat actors behind these variants seek to steal banking credentials, credit/debit card details, digital wallet access, and, in some cases, execute fraudulent transactions by transferring funds to mule accounts. These monetization strategies indicate a well-organized operation focused on financial gain.

### **Variant Summary and Detection Insights**

The five new variants—**Phish**, **RAT**, **PWA**, **Phantom**, and **Veil**—are currently under active investigation. Some variants have confirmed detection statistics, while others are still being analyzed. A comparative table summarizing these variants, their capabilities, and regional targets is included in the following section, along with detailed technical analysis.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Variant Name** | **Functionality** | **Description** | **Target Industry** | **Detected Cases (Approx.)** |
| PlayPraetor PWA | Deceptive Progressive Web App | Installs a fake PWA that mimics legitimate apps, creates shortcuts on the home screen, and triggers persistent push notifications to lure interaction. | Technology Industry, Financial Industry, Gaming Industry, Gambling Industry, e-commerce Industry | 5400+ |
| PlayPraetor Phish | WebView phishing | A WebView-based app that launches a phishing webpage to steal user credentials. | Financial, Telecommunication, Fast Food Industry | 1400+ |
| PlayPraetor Phantom | Stealthy Persistence & Command Execution | Exploits Android accessibility services for persistent control. Runs silently, exfiltrates data, hides its icon, blocks uninstallation, and poses as a system update. | Financial Industry, Gambling Industry, Technology Industry | These variants are currently under investigation to determine their exact identities. |
| PlayPraetor RAT | Remote Access Trojan | Grants attackers full remote control of the infected device, enabling surveillance, data theft, and manipulation. | Financial Industry |
| PlayPraetor Veil | Regional & Invitation-based Phishing | Disguises itself using legitimate branding, restricts access via invite codes, and imposes regional limitations to avoid detection and increase trust among local users. | Financial Industry, Energy Industry |

### **Geographic Distribution and Targeting Patterns**

CTM360's analysis indicates that while PlayPraetor variants are being distributed globally, certain strains exhibit broader outreach strategies than others. Notably, the **Phantom-WW** variant stands out for its global targeting approach. In this case, threat actors impersonate a widely recognized application with global appeal, allowing them to cast a wider net and increase the likelihood of victim engagement across multiple regions.

Among the identified variants, the **PWA** variant emerged as the most prevalent, with detection across a wide array of geographic regions. Its reach spans **South America, Europe, Oceania, Central Asia, South Asia**, and parts of the **African continent**, underscoring its role as the most widespread variant within the PlayPraetor campaign.

Other variants showed more specific regional targeting. The **Phish** variant was also distributed across multiple regions, though with slightly less saturation than PWA. In contrast, the **RAT** variant exhibited a notable concentration of activity in **South Africa**, suggesting a region-specific focus. Similarly, the **Veil** variant was observed primarily in the **United States** and select **African nations**, reflecting a more ...
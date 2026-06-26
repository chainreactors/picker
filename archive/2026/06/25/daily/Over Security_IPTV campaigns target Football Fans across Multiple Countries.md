---
title: IPTV campaigns target Football Fans across Multiple Countries
url: https://www.threatfabric.com/blogs/iptv-campaigns-target-football-fans-across-multiple-countries
source: Over Security
date: 2026-06-25
fetch_date: 2026-06-26T06:09:25.290578
---

# IPTV campaigns target Football Fans across Multiple Countries

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* [PARTNERS](https://www.threatfabric.com/partners)
* [WEBINARS](https://www.threatfabric.com/webinars)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
  + [FUSION FIRESIDE](https://www.threatfabric.com/fusion-fireside)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research

## IPTV campaigns target Football Fans across Multiple Countries

25 June 2026

![](https://www.threatfabric.com/hubfs/TF_Soccer_Other.jpg)

### Jump to

Earlier this month, we shared findings on [an upcoming threat in Spain that used football piracy as a lure to distribute mobile malware](https://www.threatfabric.com/blogs/own-goal-piracy-as-an-attack-vector-to-target-football-fans). Since then, we have identified similar activity in several other countries, pointing to a wider and ongoing effort rather than a single regional case.

The timing is notable. The **FIFA World Cup is still underway**, drawing large global audiences and driving demand for free online streams based on pirated content. This creates the right conditions for attackers. While these campaigns are not limited to sports content, large tournaments act as a **strong catalyst**, increasing both reach and effectiveness of malicious campaigns. There is little reason to expect this to stop after the tournament as long as the Fraud Kill Chain (from initial ad upload to fraudulent transaction) is not disrupted.

## Why Pirated Content, and Why IPTV Apps?

The appeal of pirated content is persistent, and IPTV apps play a central role in how it is accessed today.

* **Broadcast rights are fragmented**, spreading quality content across multiple platforms
* **Subscription costs add up** when users need access to several services
* **Geo-restrictions limit availability** depending on location
* **Users often search last minute**, just before matches begin

IPTV apps are presented as a simple and user-friendly. They promise access to live channels, sports, and premium content in one place, and – while the content is often pirated – this is actually very convenient for end users. This makes the IPTV apps attractive not only for sports, but for entertainment more broadly.

For attackers, this creates a reliable entry point. Instead of linking directly to a stream, they promote **applications that appear to offer full IPTV functionality**, but actually deliver malware.

## Same Approach, Different Countries

We observed campaigns in Portugal, Italy, Turkey and India that follow the same basic flow as in Spain:

* **Social media ads** used for scale and targeting, and themed around popular content like football, premium movies or general IPTV access.
* **Call-to-action (CTA) to a website mimicking a trusted source** stimulating the installation of an app. The app requests permissions (usually for Accessibility Services) that are unrelated to streaming, putting the door wide open for the malware.
* **Mobile malware** is embedded in the downloaded application, often aimed at stealing money or collecting personal data.

The theme is often adapted to the region, but the structure remains consistent:

#### **🇵🇹 Portugal – Antidot**

* Ads lead to a website mimicking an official application store
* IPTV or streaming app presented as legitimate
* **Payload:** Antidot malware ([discovered in 2025](https://www.brighttalk.com/webcast/20214/636507))

![facebook-ad-antidot-pt](https://www.threatfabric.com/hs-fs/hubfs/facebook-ad-antidot-pt.png?width=360&height=572&name=facebook-ad-antidot-pt.png)

![](https://www.threatfabric.com/hs-fs/hubfs/undefined-Jun-24-2026-06-31-46-3349-AM.png?width=360&height=260&name=undefined-Jun-24-2026-06-31-46-3349-AM.png)

### ![facebook-ad-multiple-pt](https://www.threatfabric.com/hs-fs/hubfs/facebook-ad-multiple-pt.png?width=740&height=245&name=facebook-ad-multiple-pt.png)

#### **🇮🇹 Italy – Medusa**

* Football-themed ads used as entry point
* Streaming-style application offered
* Website now offline, indicating short-lived infrastructure
* **Payload:** Medusa ([discovered in 2022](https://www.threatfabric.com/blogs/partners-in-crime-medusa-cabassous))

![facebook-ad-medusa-it](https://www.threatfabric.com/hs-fs/hubfs/facebook-ad-medusa-it.png?width=360&height=502&name=facebook-ad-medusa-it.png)

###

#### **🇹🇷 Turkey – Suspected Malware Campaign**

* Delivery pattern matches other regions
* Landing page unavailable during analysis
* **Assessment:** Highly likely malicious based on consistent indicators

![facebook-ad-tr](https://www.threatfabric.com/hs-fs/hubfs/facebook-ad-tr.png?width=360&height=516&name=facebook-ad-tr.png)

###

###

#### **🇮🇳 India – BTMOB**

* Multiple ads observed, including football-related lures
* Redirection to a “Relaxation TV” website
* App positioned as a general streaming/IPTV solution
* **Payload:** BTMOB malware

![facebook-ad-btmob-india](https://www.threatfabric.com/hs-fs/hubfs/facebook-ad-btmob-india.png?width=360&height=307&name=facebook-ad-btmob-india.png)

![facebook-ad-multiple-india](https://www.threatfabric.com/hs-fs/hubfs/facebook-ad-multiple-india.png?width=740&height=128&name=facebook-ad-multiple-india.png)

![malicious-website-btmob-india](https://www.threatfabric.com/hs-fs/hubfs/malicious-website-btmob-india.png?width=360&height=600&name=malicious-website-btmob-india.png)

## Alignment with the Bigger Picture

In [an earlier article](https://www.threatfabric.com/blogs/massiv-when-your-iptv-app-terminates-your-savings) we already showed that the number of malicious apps masquerading as IPTV apps is growing. Moreover, the newly discovered countries attacked by IPTV-driven malware campaigns also rank high in our general top list of **Countries Most Targeted by Mobile Malware**.

While the real-life impact of the malware campaigns depends on many factors for both attackers, victims and banks, this shows that criminals smell an opportunity in these countries.

**![Blog_Piracy_FollowUp_Countries](https://www.threatfabric.com/hs-fs/hubfs/Blog_Piracy_FollowUp_Countries.jpg?width=740&height=416&name=Blog_Piracy_FollowUp_Countries.jpg)**

## So what can you do?

Like already mentioned [in our original blog](https://www.threatfabric.com/blogs/own-goal-piracy-as-an-attack-vector-to-target-football-fans), the underlying issue is not only the existence of pirated content, a specific tournament or campaign per country. It is **the decision to access that content through unofficial apps**, which removes the protections designed to keep devices and users safe.

Criminals rely on that step and structure their distribution around it.

For banks, a few points remain important:

* **Keep yourself updated** on Mobile Malware trends.
* **Get tactical intel on campaigns** to understand when they're targeting your online channels, especially around major sports tournaments like the FIFA World Cup.
* **Build a feedback loop** between Mobile Threat Intelligence and Fraud Detection.
* **Consider warning your customers about IPTV apps** if you are actively targeted.
* **[Reach out to us](https://www.threatfabric.com/contact/)** if you require more insigh...
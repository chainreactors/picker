---
title: [StalkPhish.io] Phishing Kit family enrichment
url: https://stalkphish.com/2024/10/10/stalkphish-io-phishing-kit-family-enrichment/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-11
fetch_date: 2025-10-06T18:54:30.006158
---

# [StalkPhish.io] Phishing Kit family enrichment

[![StalkPhish – phishing, scam and brand impersonation detection](https://stalkphish.com/wp-content/uploads/2021/03/stalkphish-incl-200x60-txt-white.png)](https://stalkphish.com/)

[StalkPhish – phishing, scam and brand impersonation detection](https://stalkphish.com/)

StalkPhish – We provide B2B tools, data and knowledge for a better phishing and brand impersonation detection.

* [Home](https://stalkphish.com/)
* [Products](https://stalkphish.com/portfolio/products/)
* [Projects](https://stalkphish.com/products/)
  + [PhishingKit-Yara-Rules](https://stalkphish.com/products/phishingkit-yara-rules/)
  + [PhishingKitHunter](https://stalkphish.com/products/phishingkithunter/)
  + [StalkPhish OSS](https://stalkphish.com/products/stalkphish/)
* [Blog](https://stalkphish.com/blog-feed/)
* [Contact](https://stalkphish.com/contact/)
* [About](https://stalkphish.com/about-2/)
* [Press & Media](https://stalkphish.com/press-media/)

* [Twitter](https://twitter.com/Stalkphish_io)
* [LinkedIn](https://www.linkedin.com/company/stalkphish)
* [GitHub](https://github.com/t4d/StalkPhish)
* [Youtube](https://www.youtube.com/channel/UC5hb1CaRdmbSWpN0wTz6SFw)

Show search form
Menu- Select Page -HomeProductsProjects - PhishingKit-Yara-Rules - PhishingKitHunter - StalkPhish OSSBlogContactAboutPress & Media

Search for:

 Hide search form

![stalkphish.io-phishing-kit-family-enrichment](https://stalkphish.com/wp-content/uploads/2024/10/stalkphish.io-phishing-kit-family-enrichment.png?w=972)

# [StalkPhish.io] Phishing Kit family enrichment

![StalkPhish's avatar](https://2.gravatar.com/avatar/2ecf84df3d23b66e9e3dc59759be2600c71c9cd576b072248f211024b06278a3?s=35&d=identicon&r=G) By [StalkPhish](https://stalkphish.com/author/stalkphish/)

in [CERT](https://stalkphish.com/category/cert/), [CSIRT](https://stalkphish.com/category/csirt/), [cti](https://stalkphish.com/category/cti/), [hunting](https://stalkphish.com/category/hunting/), [investigation](https://stalkphish.com/category/investigation/), [OSINT](https://stalkphish.com/category/osint/), [phishing kit](https://stalkphish.com/category/phishing-kit/), [PhishingKit-Yara-Rules](https://stalkphish.com/category/tool/phishingkit-yara-rules/), [soc](https://stalkphish.com/category/soc/), [StalkPhish.io](https://stalkphish.com/category/tool/stalkphish-io/), [threat analysis](https://stalkphish.com/category/threat-analysis/), [threat intelligence](https://stalkphish.com/category/threat-intelligence/), [tool](https://stalkphish.com/category/tool/)

on [10/10/202410/11/2024](https://stalkphish.com/2024/10/10/stalkphish-io-phishing-kit-family-enrichment/)

[No comments](https://stalkphish.com/2024/10/10/stalkphish-io-phishing-kit-family-enrichment/#respond)

Since last summer, **[StalkPhish.io](https://www.stalkphish.io)**, our advanced platform dedicated to combating bank fraud, phishing, and scams, has been upgraded with a system for classifying phishing kits. This enhancement allows us to effectively categorize phishing kits collected through our infrastructure, bringing a new level of insight and prevention for businesses facing phishing threats.

## PhishingKit-Yara-Rules: An Open Source Initiative

At the heart of this system is the **[PhishingKit-Yara-Rules](https://stalkphish.com/products/phishingkit-yara-rules/)** project, an open-source initiative developed by StalkPhish. We’ve made this project freely accessible to the public under an open-source license, enabling companies and security professionals to integrate these tools into their own systems.

By leveraging **Yara rules**, a popular tool for identifying and classifying malware, the platform **classifies phishing kits** **automatically** as they are downloaded. These Yara rules allow for quick identification of phishing kits, helping users stay ahead of malicious actors.

## What are Phishing Kits

The StalkPhish.io platform – in addition to its various detection functions – is designed to harvest the sources of phishing kits when they are available and left accessible (hidden or not) by the threat actor.

![A phishingkit zip file - StalkPhish](https://stalkphish.com/wp-content/uploads/2020/12/e409e-16z5wlq7eccjo3zpw0f6kjq.png?w=655)

A Phishing Kit sources Zip file (Crédit Agricole – z0n51)

These phishing kits reveal a great deal of information about the threat, whether it’s the threat itself: the **usurped brand**, the **harvested data**, the **exfiltration vectors** for stolen data, etc.
Or the different ways of detecting the kits and paths used by this kit, which is very useful for **detecting deployed URLs** using the same phishing kit. At StalkPhish, we regularly analyze the kits we’ve collected in order to share our expertise in this field.

## Insightful Analysis via PhishingKit-Yara-Rules

The **PhishingKit-Yara-Rules** project is a powerful public resource aimed at companies and cybersecurity experts. It offers a comprehensive set of **Yara rules** designed to identify phishing kit sources, with over a hundred new phishing kits analyzed daily by StalkPhish.io.

One of the key benefits of these rules is that they operate solely on the **headers** of ZIP files containing phishing kits, such as file paths, names, and directories within the archive. This approach enables quick analysis without the need to decompress or open the files, saving time and resources.

![](https://stalkphish.com/wp-content/uploads/2024/10/pk-yara.png?w=506)

A phishing kit Yara rule detecting a Chase phishing kit

For example, when a Yara rule detects a phishing kit designed to impersonate a major financial institution, our system flags this activity, allowing rapid classification and response.

For more details, see the video presentation of StalkPhish projects at the [Pass The Salt 2024](https://cfp.pass-the-salt.org/pts2024/talk/EYG3MS/) conference: [https://passthesalt.ubicast.tv/videos/2024-hunt-for-phishing-urls-scammers-and-their-materials/](https://passthesalt.ubicast.tv/videos/2024-hunt-for-phishing-urls-scammers-and-their-materials/#timeline) where [Thomas Damonneville](https://www.linkedin.com/in/thdamon/) presents several free and open-source tools dedicated to detection and investigation on phishing.

## Integration into StalkPhish.io

The data is available via the StalkPhish.io **REST API**: the API generates a **JSON** stream where you can find all the information **collected, enriched and analyzed** by the StalkPhish.io backend. We’ve recently added the “***phishingkit\_family***” JSON key:

![](https://stalkphish.com/wp-content/uploads/2024/10/json-stalkphish-pro2.png?w=645)

New *phishingkit\_family* JSON key available through Stalkphish.io API (Pro plan viiew)

This JSON key contains the name(s) of the **Yara rule**(s) **triggered** when analyzing the sources of the harvested phishing kit. The advantage of such information is that it enables our customers to **quickly assess the threat** detected and the **brand impersonated**.

Knowing the phishing kit involved not only allow you to learn more about the threat, as seen above, but also to pivot on the campaign. For example, now that you know the Yara rule, you could use it to find out if other campaigns have been detected, where and when, as some internal portals or applications allow this kind of retro-hunting.

### About Stalkphish

We propose free, open source and downloadable tools, mainly focused on anti-phishing and brand identity theft (StalkPhish OSS, PhishingKit-Yara-Rules, PhishingKitHunter), [check our dedicated page](https://stalkphish.com/products/).

We provide enriched data related to these massive phishing campaigns, through our [StalkPhish.io](https://StalkPhish.io) REST API, dedicated to digital detection and investigation of actors and their infrastructures.

Also, we regularly share knowledge and analysis of phishing kits on our StalkPhish.com (this) blog.

You can contact us for more information via our [contact page](https://stalkphish.com/contact/).

---

### Discover more from StalkPhish...
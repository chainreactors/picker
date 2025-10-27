---
title: SilentSelfie: Uncovering a major watering hole campaign against Kurdish websites
url: https://blog.sekoia.io/silentselfie-uncovering-a-major-watering-hole-campaign-against-kurdish-websites/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-26
fetch_date: 2025-10-06T18:40:11.518649
---

# SilentSelfie: Uncovering a major watering hole campaign against Kurdish websites

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# SilentSelfie: Uncovering a major watering hole campaign against Kurdish websites

Our investigation uncovered 25 kurdish websites compromised by four different variants of a malicious script, ranging from the simplest, which obtains the device's location, to the most complex, which prompts selected users to install...

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR, Felix Aimé and Maxime A.](#molongui-disabled-link)
September 25 2024

0

15 minutes reading

## Key Takeaways

* In early 2024, Sekoia Threat Detection & Research team (TDR) was contacted about a suspicious script on a Kurdish website, which prompted users to activate their webcams and share their locations.

* Our investigation uncovered 25 kurdish websites compromised by four different variants of a malicious script, ranging from the simplest, which obtains the device’s location, to the most complex, which prompts selected users to install a malicious Android application.

* Despite the lack of sophisticated techniques like zero-day exploits, the campaign was notable for its scale and duration before being noticied. The earliest signs of compromise date back to the end of 2022.

* This particular campaign did not match any known TTPs associated with previous attacks in the region. This suggests the emergence of a previously unknown activity cluster targeting the Kurdish community.

## Table of contents

* [Introduction](#h-introduction)
* [Watering holes analysis](#h-watering-holes-analysis)
* [RojNews malicious APK analysis](#h-rojnews-malicious-apk-analysis)
* [Hunting for additional infrastructure](#h-hunting-for-additional-infrastructure)
* [Victimology analysis](#h-victimology-analysis)
* [Conclusion](#h-conclusion)
* [Indicators of compromise](#h-indicators-of-compromise)

## **Introduction**

At the beginning of 2024, Sekoia Threat Detection & Research team (TDR) was put in relation with members of the **Kurdish minority** regarding a suspicious script on a legitimate website named **nuceciwan129[.]xyz**. This script, when visited, prompted users to activate their webcams and share their locations, arousing suspicion among some users. After a first investigation, our contacts discovered an obfuscated JavaScript code sending reconnaissance data to a PHP script hosted on the nuceciwan129[.]xyz server.

Following this initial discovery, we began a dedicated investigation to understand the attack chain and identify any other websites compromised by the same script or its variants. During this investigation, **we discovered 25 compromised websites linked to the Kurdish community** with four different variants of the framework found on nuceciwan129[.]xyz. These ranged from the simplest, which merely stole the **user’s location**, to more complex ones that recorded images from the **selfie camera** and led selected users **to install a malicious APK**, i.e an application used on Android.

Even though **no sophisticated code was used in this attack**, such as using zero-day exploits to compromise the target’s devices, it is worth mentioning **the size and duration of this campaign which makes it unique**. The first observations of compromised websites date back to the end of 2022. Therefore, some websites have been stealing users’ locations for **over a year before being noticed**.

Cyber attacks against the Kurdish minority aiming to collect intelligence are common, often attributed to the StrongPity intrusion set in open sources. However, after days of investigation, **we found no links to previous StrongPity campaigns**, and the TTPs (Tactics, Techniques, and Procedures) used in these watering holes and the discovered APK do not match any known intrusion set active in the Middle East. **Therefore, we believe that a previously unknown activity cluster has been discovered**.

**If you are not interested by the technical analysis, you can directly jump to the victimology analysis by [clicking here](#h-victimology-analysis).**

## Watering holes analysis

Across the 25 compromised kurdish websites, we identified **four distinct variants of a same script designed to gather intelligence from online visitors**. These scripts ranged from simple ones that exfiltrated the visitors’ locations to more complex frameworks that accessed **the selfie camera to take pictures of the user** and redirected a selection of them to **a malicious APK installation web page**.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/09/websites.png)

It is worth noting that **these variants share multiple modules**, and different versions may have been deployed on the same website over time. For instance, the website **rojnews[.]news** has encountered three variants of these scripts since its initial compromise in December 2022, from the first variant to the fourth variant in November 2023 till today.

**Variant 1 – Getting the user location**

We found this first variant on seventeen **websites**. The code is quite minimalistic: when the webpage is loaded, its body invokes the gL() (getLocation) method to execute the malicious JavaScript embedded in it. If the User-Agent is an Android or an iPhone, the current location of the user is retrieved – which requires the user’s validation – and the location is sent to a PHP script hosted on the compromised website, often located under /wp-includes/ms-menu.php.

![Malicious javascript code related to the first variant namely: get the user's location. Source: Sekoia's article on the influencer campaign targeting Kurdish community](data:image/svg+xml...)![Malicious javascript code related to the first variant namely: get the user's location. Source: Sekoia's article on the influencer campaign targeting Kurdish community](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/...
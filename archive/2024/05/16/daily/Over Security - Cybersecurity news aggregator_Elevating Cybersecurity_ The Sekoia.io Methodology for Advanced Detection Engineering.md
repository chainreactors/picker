---
title: Elevating Cybersecurity: The Sekoia.io Methodology for Advanced Detection Engineering
url: https://blog.sekoia.io/elevating-cybersecurity-the-sekoia-io-methodology-for-advanced-detection-engineering/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-16
fetch_date: 2025-10-06T17:17:36.854768
---

# Elevating Cybersecurity: The Sekoia.io Methodology for Advanced Detection Engineering

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

# Elevating Cybersecurity: The Sekoia.io Methodology for Advanced Detection Engineering

[![](data:image/svg+xml...)![](https://secure.gravatar.com/avatar/84082f9ec5dba5602eed5952f8636442f7073fb5f16d6539b5f9b493c879ccab?s=52&d=mm&r=g)](#molongui-disabled-link)

[Thomas M. and Sekoia TDR](#molongui-disabled-link)
May 15 2024

0

4 minutes reading

## Table of contents

* [The Art and Expertise Behind Our Detection Rules](#h-the-art-and-expertise-behind-our-detection-rules)
* [Prioritizing Depth Over Breadth](#h-prioritizing-depth-over-breadth)
  + [Metric #1 – MITRE ATT&CK Coverage](#h-metric-1-mitre-att-amp-ck-coverage)
  + [Metric #2 – False Positive Rate](#h-metric-2-false-positive-rate)
  + [Metric #3 – Client-Specific Coverage](#h-metric-3-client-specific-coverage)

In the constantly evolving cybersecurity landscape, Sekoia.io is at the forefront of crafting sophisticated detection engineering strategies. This blog post dives into our approach to security and more specifically in the creation of detection rules. Aimed at both our existing and future users, this article unveils the complexities of detection engineering.

We will showcase how Sekoia.io does not only meet the current security demands but also anticipate future threats.

## **The Art and Expertise Behind Our Detection Rules**

**Central to Sekoia.io’s strategy is a robust process for crafting detection rules that stand the test of time and threat evolution**. Our approach is deeply rooted in the examination of emerging threats and cybersecurity trends by our Threat Detection & Research team (TDR). These seasoned cyber experts leverage cutting-edge tools and methodologies to foresee potential threats, ensuring that our rules are not merely reactive but also detect known attacks in real-time.

**This extensive research translates into the development of actionable detection rules within the [Sekoia SOC Platform](https://www.sekoia.io/en/homepage/)**, each subjected to strict testing for efficiency and relevance. Our methodology is iterative, meaning that our detection engineers refine new and existing rules based on feedback from end-users, but also based on the ever-changing threat landscape that the TDR team follows day after day. The outcome is a curated catalog of more than 860 rules at this time of writing, each designed for maximum impact and adaptability (each rule can be finetuned based on different criteria).

## **Prioritizing Depth Over Breadth**

**To prioritize its workload on detection rules engineering, Sekoia.io focuses on the depth and specificity of each rule rather than the sheer volume**. Our catalog emphasizes the relevance of each rule to ensure they address specific security concerns based on our Cyber Threat Intelligence. This is why Sekoia.io firmly believes quantitative metrics – such as the strict number of rules – should not be the sole basis for evaluating the expertise of a vendor. Customers should seek a balanced assessment, considering both standardized metrics and the unique value a vendor offers beyond these criteria. We will now explore the most frequent metrics as perceived by our customers, discussing their advantages and drawbacks.

### **Metric #1 – MITRE ATT&CK Coverage**

Sekoia.io meticulously evaluates the MITRE ATT&CK framework, understanding that while comprehensive coverage is advantageous for mapping out defensive strategies against known attack vectors, it does not equate to a bulletproof security solution. Our selective application of the framework emphasizes protections that are most relevant to our clients, based on our intelligence and expertise. This nuanced approach brings substantial benefits, such as providing a broad perspective on potential threats (comprehensive insight) while aligning with an industry-standard framework (industry benchmark). However, it also comes with its challenges. A sole focus on the MITRE framework coverage might lead to a false sense of security, as it doesn’t account for new, emerging threats not yet included in the framework. Additionally, striving for complete coverage can demand significant resources (resource intensiveness), potentially detracting from addressing other crucial security needs.

### **Metric #2 – False Positive Rate**

At Sekoia.io, we monitor false positives rates in order to finetune our rules. High precision in our detection rules means reducing the noise of unnecessary alerts, allowing security teams to focus on genuine threats. This commitment to accuracy enhances operational efficiency and mitigates alert fatigue, ensuring that real threats are promptly and effectively addressed. However, the journey to minimize false positives involves complex calibration, requiring continuous refinement to strike the right balance between sensitivity and specificity. Moreover, there’s a risk of over-tuning the detection rules, which might lead to missing broader or evolving attack techniques.

### **Metric #3 – Client-Specific Coverage**

Understanding that each client’s security landscape is unique, Sekoia.io places a premium on allowing customized protection. By refining our rules or by creating new ones, our partners and end-users can ensure their defenses are not just robust but also precisely tailored to their situation. This approach allows for targeted defense, making efficient use of resources by focusing efforts where they are most needed. However, customizing detection to fit each client’s specific context is resource-intensive (resource intensive for customization), requiring a significant investment in time and expertise. In this sense, the “One-to-many” model in which Sekoia.io pushes rules to its end-user while offering the possibility to finetune these very rules, shown to be the best win-win scenario for all.

**To conclude, we can say that** “**because the...
---
title: Detection engineering at scale: one step closer (part one)
url: https://blog.sekoia.io/detection-engineering-at-scale-one-step-closer-part-one/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-17
fetch_date: 2025-10-06T19:42:17.471084
---

# Detection engineering at scale: one step closer (part one)

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

[Detection Engineering](https://blog.sekoia.io/category/detection-engineering/ "Detection Engineering")

# Detection engineering at scale: one step closer (part one)

Security Operations Center (SOC) and Detection Engineering teams frequently encounter challenges in both creating and maintaining detection rules, along with their associated documentation, over time. These difficulties stem largely from the sheer number of...

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Guillaume C., Erwan Chevalier and Sekoia TDR](#molongui-disabled-link)
December 16 2024

0

6 minutes reading

## Table of contents

* [A Two-Faced issue](#h-a-two-faced-issue)
  + [Attackers on the rise](#h-attackers-on-the-rise)
  + [Defense all over the place](#h-defense-all-over-the-place)
  + [Practical example](#h-practical-example)
* [Conclusion](#h-conclusion)

Security Operations Center (SOC) and Detection Engineering teams frequently encounter challenges in both creating and maintaining detection rules, along with their associated documentation, over time. These difficulties stem largely from the sheer number of detection rules required to address a wide range of technologies.

Sekoia.io introduces this series of articles aiming to present an approach designed to address these challenges. It introduces our detection approach and some related problems, outlines the regular and automated actions performed through CI/CD pipelines, and highlights the importance of incorporating ongoing monitoring and review into the detection engineering process, despite these measures.

## A Two-Faced issue

The challenges faced by detection engineers today can be viewed as twofold: on one hand, the number and complexity of attacks continue to increase; on the other hand, enterprise environments are expanding, transitioning to hybrid models, and exposing a larger attack surface.

In the first article of this series, we will discuss the challenges at hand and provide practical examples to illustrate them.

### Attackers on the rise

The cyber threat landscape has evolved significantly over the past decade. This evolution has resulted in a dramatic increase in both the number of attackers and the variety of Techniques, Tactics, and Procedures (TTPs) they employ. Fortunately, not every new attacker introduces a unique TTP. Attackers often reuse existing TTPs, which helps streamline the work of detection engineers.

From a defender perspective, it is essential to follow all of these TTPs, and try to detect the most used ones. As an example, the Sekoia.io rules catalog currently lists almost [a thousand rules](https://docs.sekoia.io/xdr/features/detect/built_in_detection_rules/) mapped to the MITRE ATT&CK matrix. Still, this does not fully cover the matrix, which is continually evolving, as demonstrated by regular updates to the [MITRE ATT&CK](https://attack.mitre.org/resources/updates/) framework. Furthermore, attackers frequently seek to avoid detection, for instance by leveraging legitimate binaries, underscoring the importance of this issue. The [LOLBAS](https://lolbas-project.github.io/) (Living Off The Land Binaries, Scripts, and Libraries) project, along with other comparable initiatives, provides valuable insights into the scope of this challenge.

An important point for defenders building detection rules for various customers is also that not every rule can be deployed everywhere for a given TTP. A recent example is [the ClickFix social engineering tactic](https://blog.sekoia.io/clickfix-tactic-the-phantom-meet/). This tactic involves displaying fake error messages in web browsers to deceive users into copying and executing a given malicious PowerShell code, finally infecting their systems. If detection engineers only rely on the common host and network events, it will result in difficulties to build a generic approach and would need some heavily customised filters. For further in depth details, please check our [related blogpost](https://blog.sekoia.io/clickfix-tactic-revenge-of-detection/).

### Defense all over the place

On the other side, enterprise environments have also changed, with organisations now operating in hybrid setups and utilising a diverse array of products. While these advancements sometimes enhance security and provide access to a greater volume of logs, they also pose significant issues for detection engineers.

The access to large volumes of logs presents significant challenges in processing data and applying detection rules at scale. Additionally, it becomes increasingly difficult for both detection engineering and integration teams to analyse the logs, parse them, and develop effective detection rules.

The lack of standardisation in the logs generated by hundreds of different products, combined with the sheer volume of data, makes parsing and normalisation particularly difficult. These processes, which have always been critical to detection, have become increasingly complex over time. As a result, detection rules often face issues such as multiple conditions required to handle improperly normalised fields or, more frequently, values.

When it comes to cloud-related detection rules, normalisation often becomes an unattainable goal. Each cloud provider – whether AWS, GCP, Azure, or others – employs unique event structures and fields, making standardisation across providers extremely challenging.

This complexity is one of the primary reasons why many detection engineering teams accumulate hundreds, if not thousands, of detection rules over time. These rules become difficult to manage and nearly impossible to confidently delete, posing maintenance constraints. This situation benefits no one, as it often leads to alert fatigue for SOC analysts, who must contend with frequent false positives triggered by an overabundance of detection rules.

The schema below summarises these two key issues, providing an overview before delving into some...
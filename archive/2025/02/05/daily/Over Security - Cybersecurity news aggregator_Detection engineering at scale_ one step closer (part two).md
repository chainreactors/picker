---
title: Detection engineering at scale: one step closer (part two)
url: https://blog.sekoia.io/detection-engineering-at-scale-one-step-closer-part-two/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-05
fetch_date: 2025-10-06T20:36:59.850223
---

# Detection engineering at scale: one step closer (part two)

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

# Detection engineering at scale: one step closer (part two)

In this article, we will build upon the previous discussion of our detection approach and associated challenges by detailing the regular and automated actions implemented through our CI/CD pipelines.

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Guillaume C., Erwan Chevalier and Sekoia TDR](#molongui-disabled-link)
February 4 2025

0

9 minutes reading

## Table of contents

* [The catalyst: an approach to detection engineering at scale](#h-the-catalyst-an-approach-to-detection-engineering-at-scale)
* [Detection rule creation](#h-detection-rule-creation)
  + [Alerting and Detection Strategy Framework (ADS)](#h-alerting-and-detection-strategy-framework-ads)
  + [CI/CD and versioning](#h-ci-cd-and-versioning)
  + [Continuous tests](#h-continuous-tests)
  + [Automatically built documentation](#h-automatically-built-documentation)
* [Conclusion](#h-conclusion)

In this article, we will build upon the [previous discussion](https://blog.sekoia.io/detection-engineering-at-scale-one-step-closer-part-one/) of our detection approach and associated challenges by detailing the regular and automated actions implemented through our CI/CD pipelines.

## The catalyst: an approach to detection engineering at scale

Our approach serves as a catalyst to help you scale efficiently with minimal challenges; however, it is not a universal solution to all problems. It demands careful attention and expertise from detection engineers and is designed to align closely with practices commonly employed by developers and DevOps teams.

This methodology is structured around five key steps, as outlined below:

![The catalyst: an approach to detection engineering at scale](data:image/svg+xml...)![The catalyst: an approach to detection engineering at scale](https://lh7-qw.googleusercontent.com/docsz/AD_4nXctrh8IdkFiLrkkOQ0Y6CWAhT1bSO7tdWZd3rgBFyKuPXoP_csgegEVKor4pM5XNCM_-uZ_qMy0xv_Q9sFOf1Du6rH807_2ibd3cvI52nV6a_OtkB3SCUCuWZScvwIUeApnnkS12Q?key=2U72rcZwKqM_A3CJujCrl04J)

We will now take a closer look at each step.

## Detection rule creation

This may seem like an obvious step, but the details involved are often less straightforward. A detection rule, irrespective of the language used, comprises two key components: the metadata and the detection pattern.

At Sekoia.io, we use Sigma as our detection language, meaning the files are written in YAML. Each file is a detection rule, composed of selections that are evaluated based on a condition defined at the end. While this approach is effective, it poses a challenge: if a detection engineer wants to add a filter to exclude a false positive, the modification will affect the entire detection pattern. This limitation is common across most detection languages, where filters are not separated from the core detection logic. This is a crucial consideration for the “Continuous Tests” section of this blog, as it necessitates testing the syntax and the logic of the detection rule after every single change.

It is important to emphasise that we have deliberately [chosen](https://docs.sekoia.io/xdr/FAQ/intelligence/Detection_qa/#have-you-created-rules-for-specific-vulnerabilities-cves-why-not) to avoid creating certain types of detection rules that are excessively complex to manage over time and offer relatively low usefulness. Our focus is exclusively on detecting Technics, Tactics and Procedures (TTPs), as we strongly believe these will remain relevant regardless of the specific circumstances. For instance, when a new vulnerability emerges, a detection rule is created only if it is deemed highly critical, such as the case of ZeroLogon in the past.

Similarly, we refrain from creating what we refer to as “IoC detection rules”, where a specific file name is flagged for a particular intrusion set. This decision is based on two key considerations. First, our CTI feed is capable of handling such detections, and we believe it is more effective to manage them in the STIX format. STIX allows us to add validity dates to an indicator, furthermore our CTI feed can be consumed separately, allowing us to protect more customers. Second, from a long-term perspective, these rules tend to be cumbersome to maintain and manage, making them less practical in our approach to scalable detection engineering.

The metadata associated with detection rules are equally as important as the detection patterns themselves, particularly for automation purposes. In the process of creating detection rules, it is highly recommended to carefully consider the metadata based on your specific automation requirements. In essence, ask yourself: what metadata will be necessary for newly created detection rules? Additionally, what information should be maintained or updated with each modification of an existing detection rule?

All this metadata is then used in CI/CD pipelines to automatically generate documentation and testing frameworks, which is described later in this article.

Once a detection rule is created – or more often, concurrently – the detection engineer documents their research in an **Alerting and Detection Strategy** file.

### Alerting and Detection Strategy Framework (ADS)

This framework, developed by Palantir and slightly adapted to suit our needs, is designed to encourage detection engineers to carefully consider various aspects when creating detection rules and to document their thought process. We will not go into detail about this framework, as it is thoroughly documented [here](https://github.com/palantir/alerting-detection-strategy-framework/blob/master/ADS-Framework.md). This approach benefits rule reviewers and provides valuable context for future detection engineers who may need to work with rules that are several years old.

Every aspect of this framework is imp...
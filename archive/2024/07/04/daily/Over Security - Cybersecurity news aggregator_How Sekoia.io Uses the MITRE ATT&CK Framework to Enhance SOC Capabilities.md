---
title: How Sekoia.io Uses the MITRE ATT&CK Framework to Enhance SOC Capabilities
url: https://blog.sekoia.io/how-sekoia-io-uses-the-mitre-attck-framework-to-enhance-soc-capabilities/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-04
fetch_date: 2025-10-06T17:45:44.062432
---

# How Sekoia.io Uses the MITRE ATT&CK Framework to Enhance SOC Capabilities

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

[SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/ "SOC Insights & Other News")

# How Sekoia.io Uses the MITRE ATT&CK Framework to Enhance SOC Capabilities

At Sekoia.io, the integration of the MITRE ATT&CK framework into our Security Operations Center (SOC) platform is a cornerstone of our approach to cybersecurity. The ATT&CK framework serves as a comprehensive knowledge base of...

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/06/Fabien-Domabrd-Author-Sekoia-Blog.png)](#molongui-disabled-link)

[Fabien Dombard](#molongui-disabled-link)
July 3 2024

0

5 minutes reading

This blogpost is part of a series of articles covering our vision of cybersecurity and analyzing the benefits of SOC platforms for modern organizations. Take a look at the previous article on efficiency-driven SOC operations [here](https://blog.sekoia.io/efficiency-driven-soc-operations/).

At [Sekoia.io](https://sekoia.io/), the integration of the MITRE ATT&CK framework into [our Security Operations Center (SOC) platform](https://www.sekoia.io/en/homepage/) is a cornerstone of our approach to cybersecurity. The ATT&CK framework serves as a comprehensive knowledge base of cyber adversary behavior and a taxonomy for adversarial actions across their lifecycle. It consists of two main parts: ATT&CK for Enterprise, which covers behaviors against enterprise IT networks and cloud environments, and ATT&CK for Mobile, focusing on behaviors against mobile devices. By meticulously evaluating this framework, we ensure that our defenses are not only comprehensive but also relevant to our clients’ unique needs. This method offers substantial benefits, providing a broad perspective on potential threats while aligning with industry standards. Let’s see why and how.

## **What is the MITRE ATT&CK framework?**

The MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) framework is a comprehensive matrix that catalogs the tactics and techniques employed by cyber adversaries. It was originally developed by the U.S. Department of Homeland Security in collaboration with the MITRE Corporation in 2015 as an open reference standard to help all defenders improve their security postures against modern adversaries in cyberspace. Indeed, this framework is pivotal for threat modeling and enhancing security defenses, enabling organizations to understand the security risks linked to specific threats and refine their detection and prevention strategies. On the [official MITRE ATT&CK Framework page](https://attack.mitre.org/matrices/enterprise/), you’ll find this extensive matrix.

![Mittre Att&ck framework](data:image/svg+xml...)![Mittre Att&ck framework](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/2024-06-18-144000_3764x1624_scrotmatrix-1024x442.png)

The top horizontal columns of the matrix outline various Tactics, beginning with Initial Access, Execution, Persistence, among others. Each tactic is linked to documented techniques, which are derived from observations of different Adversary Groups, as shared by cybersecurity researchers in threat intelligence reports.

The MITRE ATT&CK framework serves multiple purposes, including:

* Enhancing existing detection technologies within an organization.
* Assessing an organization’s visibility against potential attacks.
* Strengthening the organization’s current threat intelligence capabilities.
* Facilitating adversary simulations between Red and Blue Teams to identify weaknesses.
* Advancing the maturity of an organization’s Threat Hunting Program.

It’s essential to understand that the tactics and techniques documented in the MITRE ATT&CK matrix represent knowledge that is widely recognized within the cybersecurity community. There might be other tactics and techniques not yet documented. As such, the ATT&CK matrix continually evolves, incorporating new tactics and techniques over time.

The primary goal of the MITRE ATT&CK framework is to deepen the understanding of adversaries’ characteristics and actions, including the tactics, techniques, and tools they use. This insight helps stakeholders and system owners improve their awareness and enhance their protection and detection mechanisms. Moreover, MITRE aims to establish a standardized taxonomy for identifying and labeling threat actors based on their operational methods, fostering better information sharing between communities and organizations.

## **Implementing ATT&CK in Sekoia.io’s SOC Platform**

At Sekoia.io, we leverage the ATT&CK framework in several key ways. Our journey begins with exclusive threat intelligence, systematically modeling adversary tactics, techniques, and procedures (TTPs) using ATT&CK. This comprehensive modeling helps us understand and anticipate adversary behaviors, enhancing our defensive strategies.

![At Sekoia.io, we leverage the ATT&CK framework in several key ways. Source: Sekoia.io SOC platform](data:image/svg+xml...)![At Sekoia.io, we leverage the ATT&CK framework in several key ways. Source: Sekoia.io SOC platform](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/2024-06-18-134647_5113x2201_scrot22-1-1024x441.png)

One of the standout features of our implementation is the ATT&CK mapping over our SIGMA rules. Our rule catalogue, which includes approximately 900 detections at the date of writing this article, is meticulously mapped to specific techniques. This mapping is key for a threat-centric understanding of our customers attack surface detection. It allows us to filter rules based on TTPs and identify coverage gaps within the ATT&CK matrix, providing a clear overview of both our strengths and areas needing improvement.

![One of the standout features of our SOC platform is the ATT&CK mapping over our SIGMA rules. Source: Sekoia.io SOC platform](data:image/svg+xml...)![One of the standout features of our SOC platform is the ATT&CK map...
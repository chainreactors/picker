---
title: $540 Bounty: How a Misconfigured Warning Endpoint in Apache Airflow Exposed DAG Secrets
url: https://infosecwriteups.com/540-bounty-how-a-misconfigured-warning-endpoint-in-apache-airflow-exposed-dag-secrets-ceafdad57673?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-03
fetch_date: 2025-10-06T22:51:43.818877
---

# $540 Bounty: How a Misconfigured Warning Endpoint in Apache Airflow Exposed DAG Secrets

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fceafdad57673&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F540-bounty-how-a-misconfigured-warning-endpoint-in-apache-airflow-exposed-dag-secrets-ceafdad57673&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F540-bounty-how-a-misconfigured-warning-endpoint-in-apache-airflow-exposed-dag-secrets-ceafdad57673&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ceafdad57673---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ceafdad57673---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $540 Bounty: How a Misconfigured Warning Endpoint in Apache Airflow Exposed DAG Secrets

## CVE-2023–42780: An Improper Access Control Bug That Let Low-Privileged Users View DAG Import Errors and Stack Traces

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--ceafdad57673---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--ceafdad57673---------------------------------------)

3 min read

·

Jun 2, 2025

--

Share

Press enter or click to view image in full size

![]()

> **Intro**

When it comes to access control, “read-only” shouldn’t mean “see everything.” But in Apache Airflow versions before 2.7.2, a subtle misconfiguration did just that — allowing low-privileged users to view all DAG warnings, even for DAGs they didn’t have permission to access. This oversight was reported by security researcher balis0ng and awarded $540 under the Internet Bug Bounty program.

Let’s dive into how a misbehaving /dagWarnings endpoint became an unintentional leak of internal DAG metadata and error stack traces.

> **TL;DR**

* Target: Apache Airflow (pre-2.7.2)
* CVE ID: CVE-2023–42780
* Vulnerability: Improper Access Control
* Impact: Low-privileged users could list warnings of all DAGs (import errors, dag\_ids, stack traces)
* Bounty: $540
* Reported by: balis0ng
* Report ID: [2208647](https://hackerone.com/reports/2208647)

> **What Was the Bug?**

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ceafdad57673---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ceafdad57673---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ceafdad57673---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ceafdad57673---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--ceafdad57673---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--ceafdad57673---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--ceafdad57673---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--ceafdad57673---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--ceafdad57673---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--ceafdad57673---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----ceafdad57673---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ceafdad57673---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ceafdad57673---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ceafdad57673---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ceafdad57673---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ceafdad57673---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ceafdad57673---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ceafdad57673---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ceafdad57673---------------------------------------)
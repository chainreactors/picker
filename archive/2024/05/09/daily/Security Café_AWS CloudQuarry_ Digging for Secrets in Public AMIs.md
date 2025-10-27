---
title: AWS CloudQuarry: Digging for Secrets in Public AMIs
url: https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/
source: Security Café
date: 2024-05-09
fetch_date: 2025-10-06T17:16:17.922417
---

# AWS CloudQuarry: Digging for Secrets in Public AMIs

[Skip to content](#content)

[Security Café](https://securitycafe.ro/)

Security Research and Services

* [Things we do on a daily basis](https://securitycafe.ro/security-services-for-business/)
  + [Red Team (DORA/TIBER) exercises](https://securitycafe.ro/security-services-for-business/dora-tiber-exercises/)
  + [Web Application Penetration Testing](https://securitycafe.ro/security-services-for-business/web-application-penetration-testing/)
  + [Mobile Application Penetration Testing](https://securitycafe.ro/security-services-for-business/mobile-application-penetration-testing/)
  + [Infrastructure Penetration Testing](https://securitycafe.ro/security-services-for-business/infrastructure-penetration-testing/)
  + [Vulnerability Assessment](https://securitycafe.ro/security-services-for-business/vulnerability-assessment/)
* [CVEs, Talks and Tools](https://securitycafe.ro/cves-talks-and-tools/)
* [Contact](https://securitycafe.ro/contact/)
* [About](https://securitycafe.ro/about/)

[![](https://securitycafe.ro/wp-content/uploads/2015/01/cropped-cropped-coffee-banner-2-4.jpg)](https://securitycafe.ro/)

![](https://securitycafe.ro/wp-content/uploads/2024/04/479d564d-512e-430f-898c-382c8c0331fd.jpeg?w=840)

# AWS CloudQuarry: Digging for Secrets in Public AMIs

[May 8, 2024](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/ "9:30 am") [Eduard Agavriloae](https://securitycafe.ro/author/eagavriloae/ "View all posts by Eduard Agavriloae") [aws](https://securitycafe.ro/category/cloud-security/aws/), [Cloud Security](https://securitycafe.ro/category/cloud-security/), [Research](https://securitycafe.ro/category/research/) [2 comments](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#comments)

Money, secrets and mass exploitation: This research unveils a quarry of sensitive data stored in public AMIs. Digging through each AMI we managed to collect 500 GB of credentials, private repositories, access keys and more. The present article is the detailed analysis of how we did it and what the data represents.

We did a coordinated disclosure with AWS’s security team before publishing this article.

Researchers and article authors:

* Eduard Agavriloae (<https://www.linkedin.com/in/eduard-k-agavriloae/>, [@saw\_your\_packet](https://twitter.com/saw_your_packet))
* Matei Josephs (<https://www.linkedin.com/in/matei-anthony-josephs-325ba5199/>)

## Before you begin

The results and methodology of this research could have been presented in a short summary along with 1-2 diagrams. However, we decided to go for a lengthy article that will describe our methodology, our thinking, trade-offs and results.

We invite you to challenge our approach and find aspects that we missed out or could have been improved. You can contact us through our LinkedIn profiles, through the comment section or through the Security Cafe media channels that you can find in the Contact page.

## TABLE OF CONTENTS

1. [Introduction](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-introduction)
   1. [Some words from AWS security team](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-1-some-words-from-aws-security-team)
   2. [Research Idea – Origins](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-1-research-idea-origins)
   3. [Relevant Details About AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-2-relevant-details-about-amis)
   4. [Previous Work](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-3-previous-work)
   5. [Rules & Objectives](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#1-4-rules-objectives)
2. [Collecting all Public AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#2-collecting-all-public-amis)
3. [Processing the Collected AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-processing-the-collected-amis)
   1. [Making sense of what we have](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-1-making-sense-of-what-we-have)
   2. [Filtering out AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-filtering-out-amis)
      1. [AMIs from Marketplace](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-1-amis-from-marketplace)
      2. [AMIs owned by AWS](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-3-amis-owned-by-aws)
      3. [AMIs with RootDeviceType set to “instance-store”](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-3-amis-with-rootdevicetype-set-to-instance-store)
      4. [Owners with more than 50 Public AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-4-owners-with-more-than-50-public-amis)
      5. [Sanity Checks](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#3-2-5-sanity-checks)
4. [Accessing the AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-accessing-the-amis)
   1. [Failed Options](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-1-failed-options)
      * [Option 1](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#option-1)
      * [Option 2](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#option-2)
      * [Option 3](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#option-3)
   2. [Working method](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-2-working-method)
   3. [Architecture for scale scanning](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-3-architecture-for-scale-scanning)
   4. [Final considerations](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#4-4-final-considerations)
5. [Digging for secrets](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#5-digging-for-secrets)
   1. [Mounting](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#5-1-mounting)
   2. [Finding secrets](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#5-2-finding-secrets)
   3. [Looking through private Git repositories](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#5-3-looking-through-private-git-repositories)
6. [Results](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#6-results)
   1. [AWS Keys](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#6-1-aws-keys)
   2. [Secrets extracted from Git repositories](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#6-2-secrets-extracted-from-git-repositories)
   3. [Secrets from config files](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#6-3-secrets-from-config-files)
7. [Impact](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#7-impact)
8. [Responsible disclosure](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#7-responsible-disclosure)
   1. [Owners of AWS access keys](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#7-1-owners-of-aws-access-keys)
      * [Working with AWS’s security team](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/#8-1-1-working-with-aws-s-security-team)
   2...
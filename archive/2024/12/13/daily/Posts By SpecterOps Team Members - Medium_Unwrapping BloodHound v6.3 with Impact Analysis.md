---
title: Unwrapping BloodHound v6.3 with Impact Analysis
url: https://posts.specterops.io/unwrapping-bloodhound-v6-3-with-impact-analysis-acb44b5f0731?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-12-13
fetch_date: 2025-10-06T20:04:05.734240
---

# Unwrapping BloodHound v6.3 with Impact Analysis

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Facb44b5f0731&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Funwrapping-bloodhound-v6-3-with-impact-analysis-acb44b5f0731&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Funwrapping-bloodhound-v6-3-with-impact-analysis-acb44b5f0731&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-acb44b5f0731---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-acb44b5f0731---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Unwrapping BloodHound v6.3 with Impact Analysis

## Just in time for the holidays, sharper tools for faster defense

[![Justin Kohler](https://miro.medium.com/v2/resize:fill:64:64/1*XPoVyXgjHWwNZDzHiDBR0w.jpeg)](https://justin-prime.medium.com/?source=post_page---byline--acb44b5f0731---------------------------------------)

[Justin Kohler](https://justin-prime.medium.com/?source=post_page---byline--acb44b5f0731---------------------------------------)

5 min read

·

Dec 12, 2024

--

Listen

Share

Today, the SpecterOps team rolled out a number of new features, product enhancements, and recommendations intended to help users of BloodHound Enterprise and BloodHound Community Edition more easily visualize attack paths and show improvements in identity risk reduction over time. Scroll down to learn more about v6.3.0 and related changes to BloodHound Enterprise and BloodHound Community Edition.

## BloodHound Enterprise Updates

### **Report on attack path risk with Revamped Posture page**

The BloodHound Enterprise team has completely redesigned the Posture page, delivering several significant enhancements:

* Enhanced visibility into resolved attack paths
* New metrics to track remediation progress over time
* New filter and search capabilities to highlight specific improvements
* Consolidated view of relevant data into a single page, reducing unnecessary scrolling

Press enter or click to view image in full size

![]()

The new Posture page in BloodHound Enterprise provides visibility into resolved attack paths and additional metrics for board-level reporting.

Press enter or click to view image in full size

![]()

The new Posture page in light mode — this author’s unpopular, but preferred version :)

### **Improved Analysis Algorithm**

This is a *massive* upgrade to BloodHound Enterprise’s risk analysis capability with a new algorithm we call “Butterfly”:

* Enhanced risk scoring with “Impact” analysis
* Granular risk measurement per finding for better prioritization
* Support for hybrid attack path risk analysis

Let’s get more specific with the first two bullets; Enhanced risk scoring and better prioritization.

### ***Enhanced risk scoring with “Impact” analysis***

BloodHound Enterprise has historically assessed the risk of attack paths by modeling the principals that can target specific identities and resources:

![]()

Starting with v6.3, BloodHound will also incorporate Impact analysis — the principals that can be attacked by a target node:

![]()

This new bi-directional risk analysis significantly improves BloodHound Enterprise capabilities in determining severity for attack paths:

Press enter or click to view image in full size

![]()

The “Butterflly” algorithm as we call it internally

For example, here is the improved analysis in action with Kerberoastable Users:

Press enter or click to view image in full size

![]()

BloodHound Enterprise identifying Kerberoastable users, incorporating Impact analysis to determine risk

A quick refresher on Kerberoast attack: A **Kerberoast attack** exploits the Kerberos authentication protocol by targeting service account passwords in a Windows Active Directory environment. An attacker requests Kerberos service tickets for Service Principal Names (SPNs), extracts them, and performs offline password cracking since the tickets are encrypted with the service account’s NTLM hash. If successful, the attacker gains the plaintext service account credentials, which can be used for lateral movement or privilege escalation.

Anyone can request the service ticket for a kerberoastable account which means the **exposure** is always 100%. The risk of this finding is what an attacker could do with access to that account with a successful crack. Therefore, the risk is determined by the **impact**; or what can be attacked once the attacker has control of the account.

### **Granular risk measurement per finding for better prioritization**

BloodHound Enterprise delivers better prioritization by analyzing risk per finding with v6.3. Historically, risk was calculated per attack path type:

Press enter or click to view image in full size

![]()

BHE v6.2 (previous version) with no granular risk measurements per finding.

Now, BloodHound Enterprise will assess the risk of **every** finding, allowing you to pinpoint where to start first:

Press enter or click to view image in full size

![]()

BHE v6.3 (new version) with enhanced risk analysis and granularity at the finding level

In the example above, one particular login is more risky than the others and should be prioritized. BloodHound Enterprise is simplifying the analysis for you to enable better prioritization. In this case, APP4.TITANCORP.LOCAL is prioritized above the rest as DOMAIN USERS has the ability to RDP into the host and capture the user session:

Press enter or click to view image in full size

![]()

100% of users with access to a computer with a user session from SVCINTRUST (a Tier Zero account)

This granularity is on every finding. Let’s look again at a large list of Kerberoastable users. Thanks to this improvement, we now know where to prioritize our efforts:

Press enter or click to view image in full size

![]()

BloodHound Enterprise prioritizing Kerberoastable users for remediation based on Impact

## **BloodHound Common Updates**

All enhancements listed below are available to both BloodHound Community and BloodHound Enterprise users.

### **Node/Edge Label Toggle makes for more flexible public reporting**

A long-requested feature has returned to BHCE and also available in BHE, allowing users to show or hide sensitive node and edge labels directly in the UI. This was contributed by the community member @palt — whom we give major kudos to!

Press enter or click to view image in full size

![]()

The Node/Edge label toggle has returned due to popular demand. This feature allows users to show or hide sensitive node and edge labels directly in the UI.

### **New CoerceToTGT Edge Type**

This new edge type provides more visibility into unconstrained delegation scenarios:

* Indicates principals configured for pot...
---
title: The Power of Reporting: How to write effective reports
url: https://hbothra22.medium.com/the-power-of-reporting-how-to-write-effective-reports-4034d6c87eca?source=rss-54fa249211d2------2
source: Stories by Harsh Bothra on Medium
date: 2023-08-07
fetch_date: 2025-10-04T11:59:23.233985
---

# The Power of Reporting: How to write effective reports

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4034d6c87eca&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fhbothra22.medium.com%2Fthe-power-of-reporting-how-to-write-effective-reports-4034d6c87eca&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fhbothra22.medium.com%2Fthe-power-of-reporting-how-to-write-effective-reports-4034d6c87eca&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# The Power of Reporting: How to write effective reports

[![Harsh Bothra](https://miro.medium.com/v2/resize:fill:64:64/1*2XDnpgCT3Ims0bIAn-Zp6g.jpeg)](/?source=post_page---byline--4034d6c87eca---------------------------------------)

[Harsh Bothra](/?source=post_page---byline--4034d6c87eca---------------------------------------)

6 min read

·

Aug 6, 2023

--

1

Listen

Share

The bulwark of our digital ecosystem, Penetration Testing (pentesting), has the arduous task of staving off numerous cyber threats. An effectively drafted pentest report is one of its most potent weapons, which serves as an insightful blueprint for a robust and secure network. This article aims to dissect the key elements of a high-quality pentest report that can resonate with a broad range of audiences, from top-tier executives and software developers to cybersecurity researchers and business stakeholders.

## The Power of a Well-Drafted Report

A comprehensive and precise report is more than an information-laden document in cybersecurity; it ignites the drive for security enhancement.

**Executives:** A stark warning like “Critical SQL injection vulnerability could result in a wide-ranging data breach” could accelerate executives’ decision-making and prompt necessary action.

**Engineers and Developers:** For these technical experts, understanding the details of a vulnerability is critical. An effective report demystifies this, assisting them in comprehending the root cause and devising a remedy, thereby fortifying the application.

**Cybersecurity Engineers:** The report is a valuable guide to cybersecurity professionals, helping to identify probable snags and chart a secure course ahead.

**Stakeholders:** Stakeholders perceive a comprehensive report as a testament to the organization’s commitment to safeguarding valuable assets, enhancing their trust in the entity’s resolve.

## Key Elements of an Effective Pentest Report

## Description

The description delivers the core message of the vulnerability. A detailed and impactful description vividly portrays the vulnerability, its presence, and its potential repercussions. For example, the description for a Reflected XSS vulnerability could read: “The user login page appears vulnerable to a Reflected XSS attack due to inadequate sanitization of user input, enabling an attacker to embed harmful scripts that get executed during login, potentially leading to unauthorized access and data theft.”

## Affected Endpoints

Identifying the affected endpoints aids in directing remediation strategies effectively. For the aforementioned Reflected XSS vulnerability, a detailed list could read: “Vulnerable Endpoints: User Login Page (/user\_login), Password Reset Portal (/password\_reset)”.

## Severity

Severity is the alarm bell, signalling the potential extent of the damage. Accurate severity assessment aids in prioritizing remediation actions. Industry standards like the Common Vulnerability Scoring System (CVSS) and the OWASP Risk Rating offer methodologies for this purpose.

### CVSS (Common Vulnerability Scoring System)

CVSS offers a standardized process for assessing vulnerabilities. Its three distinct components include Base Score metrics (attack vector, attack complexity, and others), Temporal Score metrics (exploit code maturity, remediation level, and others), and Environmental Score metrics (modified base metrics, confidentiality, integrity, availability, and others).

**Example:** For a Reflected XSS vulnerability, using the CVSS v3.1 framework, the vulnerability might receive a score of 6.1 (Medium), taking into account factors like attack vector (network), attack complexity (low), user interaction (required), and others. The recalibration of these factors in CVSS v4.0 might lead to a different score.

### OWASP Risk Rating

OWASP’s model combines the probability of an attack with its potential aftermath. The probability includes the threat agent’s capabilities and the vulnerability’s susceptibility, while the aftermath considers the technical impact and business implications.

**Example:** For a Reflected XSS vulnerability, assessing aspects like threat agent skills (average), vulnerability detectability (easy), technical impact (moderate), and business impact (financial data processed) can help determine the overall risk score.

## Vulnerability Classification

Classifying vulnerabilities aids in comprehending the nature of the weakness in a systematic manner. Widely recognized classification standards include CWE, STRIDE, and DREAD.

### Common Weakness Enumeration (CWE)

The CWE is a list of widespread software and hardware weaknesses developed by the community.

**Example:** A Reflected XSS vulnerability could be categorized as “CWE-79: Inadequate Neutralization of Input During Web Page Generation (‘Cross-site Scripting’)”.

### STRIDE

Microsoft’s STRIDE categorizes threats into Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.

**Example:** A Reflected XSS vulnerability can be assigned to the Spoofing (misrepresentation of identity) and Information Disclosure (leakage of sensitive data) categories.

**DREAD**

The DREAD model assists in risk computation by evaluating Damage Potential, Reproducibility, Exploitability, Affected Users, and Discoverability.

**Example:** For a Reflected XSS vulnerability, each aspect is evaluated on a 1–10 scale, with the overall risk rating derived from these scores.

## Steps to Reproduce

It’s vital to document the process of reproducing the vulnerability. This crucial information bridges the understanding between identifying the problem and devising a solution.

Consider the following steps to reproduce a Reflected XSS vulnerability:

1. Visit the following URL: “<http://example.com/login/?redirect=>”

2. In the “redirect=” field, input a payload such as “javascript:alert(origin)”

3. Provide the valid credentials and click ‘Login’

4. Observe an alert box with the message application host was reflected.

**Note:** Add relevant screenshots, code snippets, and short videos to ease reproducing the vulnerability.

## Assessing the Impact

The impact answers the question, ‘What could go wrong?’.

**Example:** A Reflected XSS could be written as: “This vulnerability enables a malefactor to run malicious scripts in the victim’s session context, facilitating sensitive data theft or user account takeover.”

## Remediation

The remediation plan illuminates the path to resolving the identified vulnerability.

**Example:** For a Reflected XSS, it could be: “Apply robust input validation and output encoding techniques to sanitize user inp...
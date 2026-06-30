---
title: Improving Transparency and Assurance in the Web PKI: Mozilla Root Store Policy v3.1
url: https://blog.mozilla.org/security/2026/06/29/improving-transparency-and-assurance-in-the-web-pki-mozilla-root-store-policy-v3-1/
source: Mozilla Security Blog
date: 2026-06-29
fetch_date: 2026-06-30T06:08:46.628171
---

# Improving Transparency and Assurance in the Web PKI: Mozilla Root Store Policy v3.1

[Mozilla](https://www.mozilla.org/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav "Visit mozilla.org")

Menu

* [About Mozilla](https://www.mozilla.org/about/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Products](https://www.mozilla.org/firefox/products/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Give](https://donate.mozilla.org/?presets=50,30,20,10&amount=30&currency=usd&utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Discover Firefox](https://www.mozilla.org/firefox/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)

[#### Mozilla Security Blog](https://blog.mozilla.org/security/ "Go to the front page")

* Search this site

  Search

**Categories:**
[Announcements](https://blog.mozilla.org/security/category/announcements/) [CA Program](https://blog.mozilla.org/security/category/ca-program/)

# Improving Transparency and Assurance in the Web PKI: Mozilla Root Store Policy v3.1

Ben Wilson
June 29, 2026

Mozilla remains committed to maintaining a secure, trustworthy, and transparent Web PKI. Today we are announcing the publication of [Mozilla Root Store Policy](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/policy/) (MRSP) version 3.1, effective July 1, 2026.

While previous policy updates focused heavily on certificate revocation, automation, and operational resilience, MRSP v3.1 focuses on a different challenge: ensuring that Certification Authority (CA) operations are sufficiently transparent, understandable, and auditable.

Trust in the Web PKI depends not only on technical requirements, but also on the ability of Mozilla, auditors, and the broader community to understand how CA systems are designed, operated, and assessed. MRSP v3.1 introduces new requirements intended to improve the quality of CA documentation and strengthen independent assurance of the design and effectiveness of controls that protect CA systems.

## **Improving CP/CPS Documentation**

Certification Practice Statements (CPSes) and combined Certificate Policy / Certification Practice Statement documents (CP/CPSes) are among the most important public documents published by a CA. They describe how a CA conducts its operations and meets industry requirements.

Over the years, we have seen significant variation in the quality, structure, and level of detail provided in CP/CPS documentation. Some documents provide extensive implementation detail, while others rely heavily on incorporation by reference or provide only high-level descriptions of CA practices.

The revised policy will continue to require conformance with RFC 3647, as modified by applicable CA/Browser Forum requirements. Improvements to section 3.3 in the MRSP will establish clearer expectations regarding the content and quality of CP/CPS documentation. The new requirements emphasize that documentation must be explicit, bounded, auditable, and sufficiently detailed to describe the CA operator’s certificate issuance and management activities, while also establishing requirements for version control, accessibility, and ongoing maintenance. The objective is to ensure that a technically competent reviewer will be better-able to determine what commitments the CA has made, how those commitments are implemented, and whether the documented practices support technical, operational, and performance oversight.

Mozilla believes that these new CP/CPS requirements will improve transparency, reduce misunderstandings, support more effective audits, and help reduce the risk of certificate misissuance by ensuring that operational practices are documented accurately, consistently, and in sufficient detail to permit meaningful review.

## **Introducing Detailed Controls Reports**

A second major enhancement in MRSP v3.1 is the introduction of Detailed Controls Reports (DCRs). Traditional WebTrust and ETSI audit reports provide valuable independent assurance regarding compliance with established criteria. However, they generally provide only limited visibility into the specific controls, testing procedures, and operational environments that support those conclusions.

Beginning with audit periods starting on or after July 1, 2027, CA operators with root certificates enabled for TLS website authentication will be required to obtain a DCR. The purpose of the DCR is to provide CA management, auditors, and Mozilla with greater visibility into the controls, testing, and operating effectiveness of CA systems that support compliance with the CA/Browser Forum’s TLS Baseline Requirements and Network and Certificate System Security Requirements. Mozilla generally expects to review DCRs only on an as-needed basis, such as during compliance reviews, incident investigations, root inclusion evaluations, or other oversight activities.

A DCR must include:

* The scope and boundaries of the audited CA systems;
* Applicable audit criteria;
* Controls implemented by the CA;
* The auditor’s testing procedures;
* Results of control testing; and
* Information regarding control exceptions or deficiencies.

Mozilla expects that DCRs will complement existing audit reports and strengthen transparency and assurance by providing additional detail regarding system boundaries, control implementation, testing procedures, and control effectiveness that is not typically available in traditional audit reports. Effective compliance requires more than documented policies and successful audits; it also requires management understanding, oversight, and engagement. By providing greater visibility into CA systems, controls, testing activities, and operational risks, DCRs can help reinforce a strong tone at the top regarding compliance expectations, support informed decision-making and resource allocation, enable earlier identification of weaknesses, and promote a culture of continuous improvement. The intent is not to replace existing audit reports, but to provide additional information that supports effective governance, oversight, and informed trust decisions.

## **Additional Clarifications and Improvements**

MRSP v3.1 also includes several targeted clarifications and refinements:

* aligns Mozilla’s mass revocation planning requirements with the corresponding CA/Browser Forum Baseline Requirements, helping ensure consistency across compliance frameworks;
* clarifies audit expectations for root inclusion requests, including requirements relating to audit continuity and root key generation ceremonies;
* requires root CA key pairs submitted for inclusion to have been generated within the previous five years, helping ensure that newly included roots are based on contemporary cryptographic practices and controls; and
* clarifies expectations when ownership or operational control of a CA changes, helping ensure that Mozilla receives timely notice and can evaluate the impact of acquisitions or organizational changes on continued compliance.

## **Looking Forward**

Mozilla recognizes that these changes will require preparation by CA operators, auditors, and other ecosystem participants. To support implementation, Mozilla is publishing accompanying wiki guidance regarding both [CP/CPS Documentation](https://wiki.mozilla.org/CA/CP-CPS_Guidance) and [Detailed Controls Reports](https://wiki.mozilla.org/CA/DCRs).

As with previous policy updates, these changes were informed by discussions with CA operators, auditors, and members of the Web PKI community. We appreciate the feedback received during the review process and look forward to continued collaboration as the ecosystem evolves.

Mozilla has a longstanding focus on building confidence in the Web PKI through transparency, accountability, and continuous improvement. By requiring higher-quality CP/CPS documentation and strengthening independent assurance, MRSP v3.1 advances Mozilla’s commitment to protecting its users and maintaining their trust in the systems that help se...
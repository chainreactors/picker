---
title: ADCS Attack Paths in BloodHound — Part 3
url: https://posts.specterops.io/adcs-attack-paths-in-bloodhound-part-3-33efb00856ac?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-09-12
fetch_date: 2025-10-06T18:35:55.196923
---

# ADCS Attack Paths in BloodHound — Part 3

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F33efb00856ac&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fadcs-attack-paths-in-bloodhound-part-3-33efb00856ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fadcs-attack-paths-in-bloodhound-part-3-33efb00856ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-33efb00856ac---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-33efb00856ac---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# ADCS Attack Paths in BloodHound — Part 3

[![Jonas Bülow Knudsen](https://miro.medium.com/v2/resize:fill:64:64/1*u6t-VnEyHLkNpvCeL5hiyQ.png)](https://medium.com/%40jonasblowknudsen?source=post_page---byline--33efb00856ac---------------------------------------)

[Jonas Bülow Knudsen](https://medium.com/%40jonasblowknudsen?source=post_page---byline--33efb00856ac---------------------------------------)

18 min read

·

Sep 11, 2024

--

Listen

Share

In [Part 1](/adcs-attack-paths-in-bloodhound-part-1-799f3d3b03cf) of this series, we explained how we incorporated Active Directory Certificate Services (ADCS) objects into [BloodHound](https://github.com/SpecterOps/BloodHound) and demonstrated how to effectively use BloodHound to identify attack paths, including the ESC1 domain escalation technique. [Part 2](/adcs-attack-paths-in-bloodhound-part-2-ac7f925d1547) covered the Golden Certificates and the ESC3 techniques.

In this blog post, we will continue to explore more of the new edges we have introduced with ADCS support in BloodHound. More specifically, we will cover how we have incorporated the ESC6, ESC9, and ESC10 domain escalation techniques.

[Keyfactor Technical Team](https://www.keyfactor.com/author-results/?authors=keyfactor-team) published a blog post in 2016, [Hidden Dangers: Certificate Subject Alternative Names (SANs)](https://www.keyfactor.com/blog/hidden-dangers-certificate-subject-alternative-names-sans/), which describes the dangerous configuration that enables the domain escalation technique [Will Schroeder](https://twitter.com/harmj0y) and [Lee Chagolla-Christensen](https://twitter.com/tifkin_) later named “ESC6” in their ADCS whitepaper [Certified Pre-Owned](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf). [Oliver Lyak](https://x.com/ly4k_) found and described ESC9 and ESC10 in the blog post [Certipy 4.0: ESC9 & ESC10, BloodHound GUI, New Authentication and Request Methods — and more!](https://research.ifcr.dk/certipy-4-0-esc9-esc10-bloodhound-gui-new-authentication-and-request-methods-and-more-7237d88061f7). Much kudos to these people for sharing their research with the community.

The configuration of *implicit certificate mapping* is a common factor impacting the three techniques, and it is the first topic we will explore.

## Certificate Mapping

When you use a password to authenticate in Active Directory (AD), you must specify both a username and a password. A domain controller (DC) will look up the AD account with a matching username and verify that the password you provided is correct for this account.

When you use a certificate instead of a password to authenticate, the DC performs “*certificate mapping*” to verify that the certificate “maps” to the AD account you specified.

### Implicit Certificate Mapping

When AD user Alice enrolls a certificate from ADCS, the Certificate Authority (CA) includes the `userPrincipalName` (UPN) of her account in the issued certificate Subject Alternative Name (SAN). When Alice attempts to authenticate with her username and the certificate, the DC finds Alice’s AD account with the username and verifies that the certificate maps to the account by confirming the certificate SAN UPN matches the AD account’s UPN.

Not all users have a UPN. To account for that, the DC attempts to map the SAN UPN without the “@domain.name” part to the `sAMAccountName` of the AD account as a second try. As a last try, the DC repeats the second attempt but with a “$” added, which gives a match if Alice is a computer since the `sAMAccountName` of computers end with “$”.

The DC will check if there are any other accounts with a matching attribute for the given SAN value before moving to the second and third try. If that is the case, then the authentication attempt will fail.

This concept is known as *UPN mapping*. There is a similar concept known as *DNS mapping*, where the `dnsHostName` (DNS) attribute is used instead. In that case, the DC will attempt mapping the hostname part of the SAN DNS value to the `sAMAccountName`.

### Abusing Implicit Certificate Mapping

Oliver Lyak found that he could abuse weaknesses in the implicit mapping logic to enroll a certificate as one account and authenticate as another. You can read about Oliver’s cool finding here: [Certifried: Active Directory Domain Privilege Escalation (CVE-2022–26923)](https://research.ifcr.dk/certifried-active-directory-domain-privilege-escalation-cve-2022-26923-9e098fe298f4).

TLDR: You can change an AD victim account’s UPN or DNS attribute to match the `sAMAccountName` of any target account, such that when you enroll a certificate as the victim, the certificate will contain the manipulated attribute value which maps to the target account. You can then use this certificate to login as the target account.

The overall steps of the attack are:

1. Modify a victim account’s UPN/DNS attribute to match a target’s `sAMAccountName`
2. Enroll a certificate as the victim
3. Authenticate as the target account using the certificate

If you are modifying the DNS attribute in step 1, then you first remove any `servicePrincipalNames` (SPNs) that contains the victim account’s DNS name. The DC will automatically attempt to update those SPNs if not deleted, which causes a conflict with the target’s SPN and the DNS change failing.

If you are modifying the UPN attribute in step 1, then you have to change the victim’s UPN once again after step 2 to avoid the certificate mapping to the victim.

Here is an animation example of how the abuse goes with Kerberos UPN mapping:

### The Patch

Microsoft patched the vulnerability by making enterprise CAs add a new certificate extension (i.e., `szOID_NTDS_CA_SECURITY_EXT`) to new certificates containing the enrollee’s SID. The extension is commonly referred to as the SID (or security) extension. The extension enables the DC to verify that the account that enrolled the certificate is also the account the certificate maps to and otherwise disallow the authentication attempt. Microsoft refers to the use of the SID extension as *strong* mapping.

Microsoft could not enforce strong mappin...
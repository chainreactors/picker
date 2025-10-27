---
title: Certificates and Pwnage and Patches, Oh My!
url: https://posts.specterops.io/certificates-and-pwnage-and-patches-oh-my-8ae0f4304c1d?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2022-11-10
fetch_date: 2025-10-03T22:17:42.452978
---

# Certificates and Pwnage and Patches, Oh My!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8ae0f4304c1d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fcertificates-and-pwnage-and-patches-oh-my-8ae0f4304c1d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fcertificates-and-pwnage-and-patches-oh-my-8ae0f4304c1d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-8ae0f4304c1d---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-8ae0f4304c1d---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Certificates and Pwnage and Patches, Oh My!

[![Will Schroeder](https://miro.medium.com/v2/resize:fill:64:64/1*idzSM22ouVWVRLUiU5Kpkg.jpeg)](https://harmj0y.medium.com/?source=post_page---byline--8ae0f4304c1d---------------------------------------)

[Will Schroeder](https://harmj0y.medium.com/?source=post_page---byline--8ae0f4304c1d---------------------------------------)

16 min read

·

Nov 9, 2022

--

3

Listen

Share

***This post was written by*** [***Will Schroeder***](https://twitter.com/harmj0y) ***and*** [***Lee Christensen***](https://twitter.com/tifkin_)***.***

A lot has happened since we released the “*Certified Pre-Owned*” [blog post](/certified-pre-owned-d95910965cd2) and [whitepaper](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf) in June of last year. While the paper details a LOT of tradecraft ranging from credential theft to domain persistence, the part that caught most people’s attention were the eight domain escalation primitives we detailed as ESC1-ESC8. A lot of organizations (and a lot of pentesters ;) definitely realized how pervasive misconfigurations in Active Directory Certificate Service are and how easy it is now to enumerate and abuse these issues.

![]()

Nothing to see here, please move along

In summer of this year, [Oliver Lyak](https://twitter.com/ly4k_) discovered the “[Certifried](https://research.ifcr.dk/certifried-active-directory-domain-privilege-escalation-cve-2022-26923-9e098fe298f4)” vulnerability ([CVE-2022–26923](https://www.semperis.com/blog/ad-vulnerability-cve-2022-26923/)) that allowed for Active Directory domain privilege escalation. In response, Microsoft released the [KB5014754 patch](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16) which non-trivially alters how certificates are mapped to identities when used for authentication in Active Directory. Oliver’s other great post “[*Certipy 4.0: ESC9 & ESC10, BloodHound GUI, New Authentication and Request Methods — and more!*](https://research.ifcr.dk/certipy-4-0-esc9-esc10-bloodhound-gui-new-authentication-and-request-methods-and-more-7237d88061f7)” has some **excellent** detail on the patch, as well as two new escalations he discovered titled ESC9 and ESC10. [Atanur Serkan Elmasoğlu](https://www.linkedin.com/in/atanur-serkan-elmaso%C4%9Flu-771672a5/) also alerted us to some additional caveats for some of the escalations that we’ll cover, and Pablo Martínez and Kurosh Dabbagh detailed some additional ways to exploit ESC7 in their “[*AD CS: from ManageCA to RCE*](https://www.tarlogic.com/blog/ad-cs-manageca-rce/)” post that we’ll briefly touch on as well. Oh, a ton of new tools from a number of researchers came out too!

With all of these changes, we wanted to revisit some of the offensive AD CS attacks, detail how the patch has affected some of the existing escalations, and clarify a few details that we were previously unclear on.

## ESC9 and ESC10 Background

The [KB5014754 patch](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16) introduced the concept of “strong” and “weak” user identity mappings, along with a new certificate extension that we’ll talk about shortly. Oliver does a much better job than we could [detailing all of this](https://research.ifcr.dk/certipy-4-0-esc9-esc10-bloodhound-gui-new-authentication-and-request-methods-and-more-7237d88061f7), but as a summary, certificates can be mapped to an Active Directory principal either implicitly or explicitly. Implicit mappings concern using the subject alternative name (SAN) to map the certificate to a user identity. If you read the [whitepaper](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf) or [previous blog post](/certified-pre-owned-d95910965cd2), you’ll recall that SAN abuse was the crux of several of the escalation attacks.

Explicit mappings are a bit different and use the **altSecurityIdentities** property of a principal to map a certificate to an identity. Three of these (X509IssuerSerialNumber, X509SKI, and X509SHA1PublicKey) are now considered “strong” mappings, which means that, “[*…they are based on identifiers that you cannot reuse.*](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16#bkmk_certmap)” All other altSecurityIdentities and previous implicit mappings are now considered “weak”.

In order to facilitate strong identity mappings in all situations, for *most* certificate templates the CA will now insert a [szOID\_NTDS\_CA\_SECURITY\_EXT](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wcce/e563cff8-1af6-4e6f-a655-7571ca482e71) (OID 1.3.6.1.4.1.311.25.2) extension value into the resulting certificate (more information on this processing logic [can be found here](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wcce/a1f27ffb-7f74-4fa1-8841-7cde4ba0bcfe)). This extension contains the SID of the requesting user and is meant to be used if there are no existing strong mappings in the certificate:

Press enter or click to view image in full size

![]()

The new szOID\_NTDS\_CA\_SECURITY\_EXT extension in an issued certificate.

The idea with this extension is a domain controller can compare the SID of the authenticating user (or the SID of the user account specified in the SAN) against the SID contained in szOID\_NTDS\_CA\_SECURITY\_EXT. This is used as a type of bootstrap “strong” identity mapping that we’ll talk about shortly, but how exactly this extension is used by the DC for Kerberos or SChannel authentication depends upon the value(s) of two registry keys.

The [***StrongCertificateBindingEnforcement***](https://support.microsoft.com/en-us/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16#bkmk_kdcregkey)value located at [**HKLM\SYSTEM\CurrentControlSet\Services\Kdc**](https://suppo...
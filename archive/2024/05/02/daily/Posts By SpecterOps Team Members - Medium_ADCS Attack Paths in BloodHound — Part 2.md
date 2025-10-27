---
title: ADCS Attack Paths in BloodHound — Part 2
url: https://posts.specterops.io/adcs-attack-paths-in-bloodhound-part-2-ac7f925d1547?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-05-02
fetch_date: 2025-10-06T17:27:06.936749
---

# ADCS Attack Paths in BloodHound — Part 2

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fac7f925d1547&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fadcs-attack-paths-in-bloodhound-part-2-ac7f925d1547&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fadcs-attack-paths-in-bloodhound-part-2-ac7f925d1547&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-ac7f925d1547---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-ac7f925d1547---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# ADCS Attack Paths in BloodHound — Part 2

[![Jonas Bülow Knudsen](https://miro.medium.com/v2/resize:fill:64:64/1*u6t-VnEyHLkNpvCeL5hiyQ.png)](https://medium.com/%40jonasblowknudsen?source=post_page---byline--ac7f925d1547---------------------------------------)

[Jonas Bülow Knudsen](https://medium.com/%40jonasblowknudsen?source=post_page---byline--ac7f925d1547---------------------------------------)

11 min read

·

May 1, 2024

--

Listen

Share

In [Part 1](/adcs-attack-paths-in-bloodhound-part-1-799f3d3b03cf) of this series, we explained how we incorporated Active Directory Certificate Services (ADCS) objects into BloodHound and demonstrated how to effectively use BloodHound to identify attack paths including the ESC1 abuse technique.

In this blog post, we will continue to explore more of the new edges we have introduced with ADCS support in BloodHound. More specifically, we will cover how we have incorporated the [Golden Certificate](#1d3f) and the [ESC3](#479e) abuse technique.

I have written this blog post on behalf of the BloodHound Enterprise team at SpecterOps, which has designed and implemented the BloodHound edges described in this blog post. Thanks to everyone on the team who helped out with this effort!

## Hosts and Golden Certificate

The computer hosting a certificate authority (CA) service holds the private key of its CA certificate. The key must be there for the CA to sign and issue certificates. This makes CA hosts a very lucrative target. As [Will Schroeder](https://twitter.com/harmj0y) and [Lee Chagolla-Christensen](https://twitter.com/tifkin_) described under DPERSIST1 in the ADCS whitepaper [Certified Pre-Owned](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf), it is possible to craft “golden certificates” with the private key of the CA certificate, which then allows you to authenticate as anyone just as ESC1.

The AD enterprise CA object holds the DNS name of its CA host in its `dNSHostName` attribute. This enables us to look up the corresponding AD computer object. To represent the relationship between the AD computer object and the enterprise CA object in BloodHound, we create a non-traversable edge named *HostsCAService*, going from the Computer node to the EnterpriseCA node.

For an attacker to craft a golden certificate that works for domain authentication, the enterprise CA’s certificate must chain up to a trusted root CA for the domain, and the NTAuth store must include the enterprise CA certificate, just as with ESC1. If these conditions are met, we create a traversable *GoldenCert* edge from the CA Computer node to the domain:

Press enter or click to view image in full size

![]()

The GoldenCert edge makes it easy to identify attack paths leading to a domain compromise through a CA host.

Many organizations do not protect enterprise CA hosts as well as they should. It is a common misunderstanding that only root CAs are Tier Zero, and not issuing CAs and intermediate CAs. Both issuing CAs and intermediate CAs are enterprise CAs, and will by default meet the requirements for the GoldenCert edge. We strongly recommend treating all CA hosts as Tier Zero.

Press enter or click to view image in full size

![]()

There are exceptions to the statement in the above meme; for example, hardware protection on the CA host may prevent you from obtaining the CA private key. However, it is still possible to compromise the environment most likely, as an enterprise CA host can publish certificate templates, approve certificate requests the CA has denied, and more.

Press enter or click to view image in full size

![]()

We will dive further into the edges in the above screenshot in a future blog post about ESC5 and ESC7.

There are even scenarios where an attacker can abuse a compromised CA host **not** trusted for NT authentication. An attacker may compromise users configured with an explicit certificate mapping of the type X509IssuerSubject, X509IssuerSerialNumber, X509SKI, or X509SHA1PublicKey as [Hans-Joachim Knobloch](https://www.linkedin.com/in/hans-joachim-knobloch-165527267/) called out and described in this blog post: [Kleines Nilpferd trampelt über Microsofts PKI-Webdienste](https://pkiblog.knobloch.info/nilpferde-ndes-und-goldene-zertifikate-als-schluessel-zum-ad). The attacker can also compromise any group set up with Authentication Mechanism Assurance (AMA), as [Carl Sörqvist](https://www.linkedin.com/in/carlsorqvist/) explains in this blog post: [Forest Compromise Through AMA Abuse](https://blog.qdsecurity.se/2024/04/07/forest-compromise-through-ama-abuse/).

## ESC3

ESC3 is similar to ESC1 in the sense that you as an attacker enroll a certificate as a targeted principal of your choice, which you then use to perform domain authentication. In ESC3, we abuse the ADCS concept of *enrollment agents*. Let us dive into the requirements.

### Enrollment Agent Templates

An enrollment agent can enroll certificates on behalf of other principals. The most frequent use case for the enrollment agent concept is for an administrator who needs to issue smart cards to employees of the organization. The administrator will obtain an enrollment agent certificate and use that to enroll certificates on behalf of employees who need a smart card. This is a more secure solution than using an ESC1-type certificate template, as the enrollment agent setup enables you to restrict the targeted certificate templates and the targeted principals, as we will explore [later in this blog post](#68b4).

To become an enrollment agent, you need an enrollment agent certificate containing the extended key usage (EKU): *Certificate Request Agent* (1.3.6.1.4.1.311.20.2.1). Such a certificate allows you to enroll on behalf of other principals in all certificate templates of schema version 1. Additionally, targeted templates of schema version 1 also allow the enroll-on-behalf-of functionality if you present a certificate with the Any Purpose EKU or no EKUs (ESC2 certificate). As explained in the [Part 1 blog post](/adcs-attack-paths-in-bloodhound-part-1-799f3d3b03cf), you can view the effective EKUs of certifica...
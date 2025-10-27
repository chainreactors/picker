---
title: The Security Principle Every Attacker Needs to Follow
url: https://posts.specterops.io/the-security-principle-every-attacker-needs-to-follow-905cc94ddfc6?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-07-23
fetch_date: 2025-10-06T17:46:08.513140
---

# The Security Principle Every Attacker Needs to Follow

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F905cc94ddfc6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fthe-security-principle-every-attacker-needs-to-follow-905cc94ddfc6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fthe-security-principle-every-attacker-needs-to-follow-905cc94ddfc6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-905cc94ddfc6---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-905cc94ddfc6---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# The Security Principle Every Attacker Needs to Follow

[![Elad Shamir](https://miro.medium.com/v2/resize:fill:64:64/1*ocQXH46k-rk5MSdLEXKXfA.jpeg)](https://medium.com/%40elad.shamir?source=post_page---byline--905cc94ddfc6---------------------------------------)

[Elad Shamir](https://medium.com/%40elad.shamir?source=post_page---byline--905cc94ddfc6---------------------------------------)

11 min read

·

Jul 22, 2024

--

1

Listen

Share

Earlier this year, I was tasked with developing a follow-on course for our renowned [Adversary Tactics: Red Team Operations course](https://specterops.io/training/red-team-operations/). The [new course](https://specterops.io/training/identity-driven-offensive-tradecraft/) needed to cover the advanced tradecraft we perform on engagements and teach students how to navigate highly secure environments.

I decided to focus on “[Identity-Driven Offensive Tradecraft](https://specterops.io/training/identity-driven-offensive-tradecraft/)”, which ultimately became the course name. In this post, I will explain what I mean by that and why it is so central to attack paths and red team operations. I will also answer the question “What turns a path into an attack path?” and discuss the principle behind the framework we teach in our [new IDOT course](https://specterops.io/training/identity-driven-offensive-tradecraft/): the Clean Source Principle.

This will be a less technical post than my usual, but it’s important to understand the theory behind the practice.

## Access Control Fundamentals

Every modern technological ecosystem has a mechanism, or a set of mechanisms, that govern access to resources. These mechanisms must be able to perform the following most fundamental tasks:

* **Identification**: Recognizing a principal (e.g., matching a username or email address to an account)
* **Authentication**: Verifying the identity of the principal (e.g., verifying that the client is in possession of the principal’s password)
* **Authorization**: Determining whether the principal is permitted to perform an action on a resource in the current state

In practice, identification is part of the authentication process, but most literature recognizes them as different processes.

I’m intentionally leaving out Accounting, as it is less relevant to the main point of this post.

## Authentication

Authentication can be performed locally by the system or delegated to another system, such as Active Directory or an Identity Provider (IdP), either on-premises (e.g., Active Directory Federation Services — AD FS) or in the cloud (e.g., Entra ID or Okta).

When authentication is delegated to another system, an authentication protocol is usually utilized to ensure credentials are exchanged securely. On-premises, this is typically done via Kerberos or NTLM, which avoids sending raw credential material to the authentication server or the resource server. In the cloud and with third-party software, it is typically done via SAML or OIDC, which rely on signed tokens.

## Authorization

Authorization essentially boils down to a set of access control rules that apply to the principal or the resource and are enforced by the system’s Identity and Access Management (IAM) components. In Windows, the Security Reference Monitor (SRM) performs this service. These rules are comprised of variations of the following elements:

* **Subject**: The principal that seeks access
* **Action**: What the rule allows/denies the subject to do
* **Object**: The resource that the subject can/cannot perform the action on
* **Conditions**: Additional requirements that must be met in the current state of the subject or the resource (e.g., time or location restrictions)
* **Decision**: Allow or Deny

For example, the following rules depict a policy that grants the Domain Admins group Full Control access to the Production DB Server and the Global Admins role Full Control access to the Storage Account if access is initiated from a compliant device with multi-factor authentication (MFA).

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

## What is Identity-Driven Offensive Tradecraft?

Identity-driven offensive tradecraft is Tactics, Techniques, and Procedures (TTPs) motivated by, centered around, and strategically guided by the abuse of identity and access management. This focus on identity as the key vector for achieving offensive goals defines this approach.

Attackers ultimately seek to impact the target environment, steal data, or, in the case of red teamers, demonstrate their ability to do so. Virtually all attack paths require navigating the access control mechanisms, primarily in one of the following ways:

* Credential abuse or similar TTPs that lead to user impersonation
* Access policy/ACL modification or configuration changes to allow access
* Exploitation or manipulation of components with permitted access to the attacker’s ultimate objective or in support of performing one of the above

That is why most threat actors seek to gain “Enterprise Identity Dominance,” e.g., Domain Admin in Active Directory or Global Admin in Entra ID. Once they gain such dominance, they can control or impersonate principals with access to their ultimate objectives. Such privileged access potentially enables rapid lateral movement for a smash-and-grab operation, allows installing hard-to-find persistence for long-term operations, and often hinders incident response efforts because relatively few people in the organization have such privileged access, making containment and eradication more complex.

Going back to the previous example, we can fill in the gaps and depict a very simple attack path that demonstrates how an attacker could abuse the access policy:

Press enter or click to view image in full size

![]()

The attacker gains initial access to a Domain Admin’s workstation and abuses their credentials/session to gain Full Control access to the Production DB Server. At that point, the attacker can also gain access to the Entra ID Privileged Access Workstation, a compliant device with a...
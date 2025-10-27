---
title: Precious Gemstones: The New Generation of Kerberos Attacks
url: https://buaq.net/go-139727.html
source: unSafe.sh - 不安全
date: 2022-12-13
fetch_date: 2025-10-04T01:17:10.483400
---

# Precious Gemstones: The New Generation of Kerberos Attacks

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/a3aafb9b7c085abae63119f80eb38679.jpg)

Precious Gemstones: The New Generation of Kerberos Attacks

Executive SummaryUnit 42 res
*2022-12-12 22:0:49
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-139727.htm)
阅读量:46
收藏*

---

![An illustrative example of Kerberos attacks using golden, diamond, or sapphire tickets](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/Vulnerability-r3d2-1.png)

## Executive Summary

Unit 42 researchers show new detection methods that help improve detection of a new line of Kerberos attacks, which allow attackers to modify Kerberos tickets to maintain privileged access. The most well-known example of this is the Golden Ticket attack, which allows threat actors to forge a ticket to masquerade as a high-privileged user.

These two newer attacks extend the Golden Ticket attack in that the forged tickets are not created from scratch, but instead based on modifying an existing ticket to include high-privileged access. We’ll discuss the difference between these three types of attacks, to explain why the newer ones are harder to detect.

The broad usage of Active Directory has made Kerberos attacks the bread and butter of many threat actors. Researchers have discovered the following new attack techniques that allow an adversary to gain unconstrained access to all services and resources within an Active Directory (AD) domain:

* Diamond Ticket
* Sapphire Ticket

Because of their similarity to the well-known Golden Ticket attack, threat actors might also use these attacks in future campaigns. People can better protect themselves by employing the new detection methods we’ll discuss for these new Kerberos attacks.

Palo Alto Networks customers receive improved detection for the attacks discussed in this blog through Cortex XDR.

## Table of Contents

[Kerberos Refresher](#post-126011-_gp8q46kj9por)

## Kerberos Refresher

To understand the ticket attacks and their implications, it helps to understand a few things about how Kerberos works. This includes some common terms for features used in these attacks, as well as the structure of how tickets are used.

[Kerberos](https://en.wikipedia.org/wiki/Kerberos_%28protocol%29) is a network authentication protocol that is primarily used in [Active Directory (AD)](https://en.wikipedia.org/wiki/Active_Directory) environments. [Thousands of companies across different industries](https://discovery.hgdata.com/product/microsoft-active-directory) use Active Directory technology for managing user accounts and other resources within an organization. Active Directory’s first version was released in Windows Server 2000 and since then, it has become particularly common in businesses and other large organizations that have a significant number of users and resources to manage.

Kerberos provides strong authentication by issuing tickets to authenticate users and allow access to services. The tickets are distributed by the [key distribution center (KDC)](https://www.techopedia.com/definition/12883/key-distribution-center-kdc-cryptography). In most environments, the KDC is installed on the [domain controller (DC)](https://en.wikipedia.org/wiki/Domain_controller).

During the initial authentication, a [Ticket Granting Ticket (TGT)](https://doubleoctopus.com/security-wiki/authentication/ticket-granting-tickets/) is a ticket assigned to a user. The TGT is later used to authenticate the user to the KDC and request a service ticket from the [Ticket Granting Service (TGS)](https://www.techopedia.com/definition/27186/ticket-granting-server-tgs#:~:text=A%20ticket%20granting%20server%20(TGS)%20is%20a%20logical%20key%20distribution,such%20as%20network%20service%20access.). Service tickets are granted for authentication against services.

A Kerberos authentication would consist of the following steps:

1. The user requests (AS-REQ) a TGT from the KDC and the KDC verifies and validates the credentials and user information.
2. After authenticating the user, the KDC sends an encrypted TGT back to the requester (AS-REP).
3. The user presents the TGT to the DC and requests a TGS (TGS-REQ).
4. The TGS is encrypted and sent back to the requesting user (TGS-REP).
5. The user connects to the server hosting the service requested and presents the TGS (AP-REQ) in order to access the service.
6. The application server sends an (AP-REP) to the client.

![Image 1 shows the request flow between the user workstation, the domain controller, and the application server for Kerberos authentication](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-28.png)

Figure 1. Kerberos authentication.

### What Components Are in a Kerberos Ticket?

Each [Kerberos ticket](https://www.rfc-editor.org/rfc/rfc4120#section-5.3) contains the following fields:

|  |  |
| --- | --- |
| **Kerberos Ticket** | |
| **Tkt-vno** | Version number for the ticket format. |
| **Realm** | The realm that issued a ticket. |
| **sname** | Server name. All the components of the name are part of the server's identity. |
| **Enc-part** | Encrypted with the server's secret key. |

*Table 1. Kerberos ticket.*

The enc-part contains different fields but we will focus on the following:

1. cname – The name part of the client's principal identifier.
2. authorization-data – used to pass authorization data from the principal on whose behalf a ticket was issued to the application service. This part includes the Privileged Attribute Certificate (PAC).

### What Is a Kerberos Privilege Attribute Certificate (PAC)?

As [Microsoft’s documentation](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-pac/54d570b1-fc54-4c54-8218-f770440ec334) states, the [PAC](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-pac/54d570b1-fc54-4c54-8218-f770440ec334) is a structure that conveys authorization-related information provided by DCs. The PAC is used by authentication protocols that verify identities to transport authorization information, which controls access to resources.

The DC includes authorization data such as [security identifiers (SIDs)](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-pac/f2ef15b6-1e9b-48b5-bf0b-019f061d41c8#gt_83f2020d-0804-4840-a5ac-e06439d50f8d) and [relative identifiers (RIDs)](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-pac/f2ef15b6-1e9b-48b5-bf0b-019f061d41c8#gt_df3d0b61-56cd-4dac-9402-982f1fedc41c) in the PAC.

### Kerberos Delegation

A common use case for [Kerberos delegation](https://blog.netwrix.com/2021/11/30/what-is-kerberos-delegation-an-overview-of-kerberos-delegation/#:~:text=Kerberos%20Delegation%20is%20a%20security,account%20for%20any%20other%20network) is a web server fetching user data from a database server. The database server can grant access to the user data only for the user. In this scenario, the web server will need to impersonate the user. This impersonation is called Kerberos delegation.

We will focus on constrained delegation in this blog, but you can read about the different Kerberos delegation methods in [Protecting Against the Bronze Bit Vulnerability with Cortex XDR](https://www.paloaltonetworks.com/blog/security-operations/bronze-bit-vulnerability-xdr/).

**Constrained Delegation:** Microsoft has implemented Kerberos extensions in order to avoid keeping the user’s TGT in memory. This extension is called [S4U](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/4a624fb5-a078-4d30-8ad1-e9ab71e0bc47#gt_083a5403-f654-4db6-b17e-9c10dc5cd420) (Service for User), and it consists of [S4U2Self](https://learn.microsoft.com/en-us/openspecs/window...
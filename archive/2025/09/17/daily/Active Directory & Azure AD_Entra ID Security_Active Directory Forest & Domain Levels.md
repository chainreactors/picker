---
title: Active Directory Forest & Domain Levels
url: https://adsecurity.org/?p=4661
source: Active Directory & Azure AD/Entra ID Security
date: 2025-09-17
fetch_date: 2025-10-02T20:16:12.889190
---

# Active Directory Forest & Domain Levels

Toggle search form

Search for:

![Active Directory & Azure AD/Entra ID Security](https://adsecurity.org/wp-content/themes/graphene/images/headers/fluid.jpg "Active Directory & Azure AD/Entra ID Security")

Toggle navigation

[Active Directory & Azure AD/Entra ID Security](https://adsecurity.org "Go back to the front page")

Active Directory & Azure AD/Entra ID: Enterprise Security, Methods to Secure Active Directory, Attack Methods & Effective Defenses, PowerShell, Tech Notes, & Geek Trivia…

* [Home](https://adsecurity.org/)
* [About](https://adsecurity.org/?page_id=8)
* [AD Resources](https://adsecurity.org/?page_id=41)
* [Attack Defense & Detection](https://adsecurity.org/?page_id=4031)
* [Mimikatz](https://adsecurity.org/?page_id=1821)
* [Presentations](https://adsecurity.org/?page_id=1352)
* [Schema Versions](https://adsecurity.org/?page_id=195)
* [Security Resources](https://adsecurity.org/?page_id=399)
* [SPNs](https://adsecurity.org/?page_id=183)
* [Top Posts](https://adsecurity.org/?page_id=2532)

[Detecting Active Directory Password Spraying Article](https://adsecurity.org/?p=4638)

[Active Directory Security Tip #3: Computer Accounts](https://adsecurity.org/?p=4583)

Sep
15
2025

# Active Directory Forest & Domain Levels

* By [Sean Metcalf](https://adsecurity.org/?author=2) in [ActiveDirectorySecurity](https://adsecurity.org/?cat=565), [Technical Reference](https://adsecurity.org/?cat=2)

An important Active Directory setting determines what security capabilities are available which relates to the level of the forest and/or domain. This post collects the relevant capabilities of Windows domain and forest functional levels.

**Forest Functional Level Features:**

* [Windows 2000](https://en.wikipedia.org/wiki/Windows_2000)
* [Windows 2003](https://en.wikipedia.org/wiki/Windows_Server_2003)
  + Forest trust
  + Domain rename
  + Linked-value replication makes it possible for you to change group membership to store and replicate values for individual members instead of replicating the entire membership as a single unit. Storing and replicating the values of individual members uses less network bandwidth and fewer processor cycles during replication, and prevents you from losing updates when you add or remove multiple members concurrently at different domain controllers.
  + The ability to deploy a read-only domain controller (RODC)
  + The intersite topology generator (ISTG) uses improved algorithms that scale to support forests with a greater number of sites than AD DS can support at the Windows 2000 forest functional level. The improved ISTG election algorithm is a less-intrusive mechanism for choosing the ISTG at the Windows 2000 forest functional level.
  + The ability to create instances of the dynamic auxiliary class named dynamicObject in a domain directory partition
  + The ability to convert an inetOrgPerson object instance into a User object instance, and to complete the conversion in the opposite direction
  + The ability to create instances of new group types to support role-based authorization. These types are called application basic groups and LDAP query groups.
  + Deactivation and redefinition of attributes and classes in the schema. The following attributes can be reused: ldapDisplayName, schemaIdGuid, OID, and mapiID.
  + Domain-based DFS namespaces running in Windows Server 2008 Mode, which includes support for access-based enumeration and increased scalability.
* [Windows 2008](https://en.wikipedia.org/wiki/Windows_Server_2008)
  + No additional features
* [Windows 2008 R2](https://en.wikipedia.org/wiki/Windows_Server_2008_R2)
  + Active Directory Recycle Bin, which provides the ability to restore deleted objects in their entirety while AD DS is running.
* [Windows 2012](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn250019%28v%3Dws.11%29)
  + No additional features
* [Windows 2012 R2](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn250019%28v%3Dws.11%29)
  + No additional features
* [Windows 2016](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-in-windows-server-2016)
  + Privileged access management (PAM) using Microsoft Identity Manager (MIM)
* [Windows 2019](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-in-windows-server-2019)
  + No additional features
* [Windows 2022](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-in-windows-server-2022)
  + No additional features
* [Windows 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
  + No additional features

**Domain Functional Level Features:**

* [Windows 2000](https://en.wikipedia.org/wiki/Windows_2000)
  + Universal groups for both distribution and security groups.
  + Group nesting
  + Group conversion, which allows conversion between security and distribution groups
  + Security identifier (SID) history
* [Windows 2003](https://en.wikipedia.org/wiki/Windows_Server_2003)
  + Domain Controller rename
  + The lastLogonTimestamp attribute is updated with the last logon time of the user or computer. This attribute is replicated within the domain.
  + The ability to set the userPassword attribute as the effective password on inetOrgPerson and user objects
  + The ability to redirect Users and Computers containers
  + The ability for Authorization Manager to store its authorization policies in AD DS
  + Constrained delegation makes it possible for applications to take advantage of the secure delegation of user credentials by means of Kerberos-based authentication.
  + You can restrict delegation to specific destination services only.
  + Selective authentication makes it is possible for you to specify the users and groups from a trusted forest who are allowed to authenticate to resource servers in a trusting forest.
* [Windows 2008](https://en.wikipedia.org/wiki/Windows_Server_2008)
  + Distributed File System (DFS) replication support for the Windows Server 2003 System Volume (SYSVOL)
  + Domain-based DFS namespaces running in Windows Server 2008 Mode
  + Advanced Encryption Standard (AES 128 and AES 256) support for the Kerberos protocol.
  + Last Interactive Logon Information displays the following information:
    - The total number of failed logon attempts at a domain-joined Windows Server 2008 server or a Windows Vista workstation
    - The total number of failed logon attempts after a successful logon to a Windows Server 2008 server or a Windows Vista workstation
    - The time of the last failed logon attempt at a Windows Server 2008 or a Windows Vista workstation
    - The time of the last successful logon attempt at a Windows Server 2008 server or a Windows Vista workstation
  + Fine-grained password policies
  + Personal Virtual Desktops
* [Windows 2008 R2](https://en.wikipedia.org/wiki/Windows_Server_2008_R2)
  + Authentication mechanism assurance, which packages information about the type of logon method (smart card or user name/password) that is used to authenticate domain users inside each user’s Kerberos token. When this feature is enabled in a network environment that has deployed a federated identity management infrastructure, such as Active Directory Federation Services (AD FS), the information in the token can then be extracted whenever a user attempts to access any claims-aware application that has been developed to determine authorization based on a user’s logon method.
  + Automatic SPN management for services running on a particular computer under the context of a Managed Service Account when the name or DNS host name of the machine account changes.
* [Windows 2012](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn250019%28v%3Dws.11%29)
  + The KDC support for claims, compound authentication, and Kerberos armoring KDC administrative template policy has two settings (Always...
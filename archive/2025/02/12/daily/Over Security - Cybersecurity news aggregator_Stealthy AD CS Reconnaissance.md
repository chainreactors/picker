---
title: Stealthy AD CS Reconnaissance
url: https://blog.compass-security.com/2025/02/stealthy-ad-cs-reconnaissance/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-12
fetch_date: 2025-10-06T20:39:55.601822
---

# Stealthy AD CS Reconnaissance

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Stealthy AD CS Reconnaissance](https://blog.compass-security.com/2025/02/stealthy-ad-cs-reconnaissance/ "Stealthy AD CS Reconnaissance")

[February 11, 2025](https://blog.compass-security.com/2025/02/stealthy-ad-cs-reconnaissance/ "Stealthy AD CS Reconnaissance")
 /
[Marc Tanner](https://blog.compass-security.com/author/mtanner/ "Posts by Marc Tanner")
 /
[0 Comments](https://blog.compass-security.com/2025/02/stealthy-ad-cs-reconnaissance/#respond)

> TLDR: Introducing a [`certipy parse` command](https://github.com/ly4k/Certipy/pull/247) to perform stealthy offline AD CS enumeration based on local registry data.

Ever since Will Schroeder and Lee Christensen from SpecterOps have released their seminal [Active Directory Certificate Services (AD CS)](https://posts.specterops.io/certified-pre-owned-d95910965cd2) research, it has been a popular avenue for Windows domain privilege escalation used by security professionals and threat actors alike.

Such attack paths usually begin with the enumeration of published certificate templates by means of LDAP queries to a domain controller (or COM / RPC requests to a certificate authority). However, in mature environments LDAP traffic is monitored, both on the client (API hooking, ETW) as well as server side (query logging, SACL based audit policies), for known tool behavior and malicious activities. To evade these detections, attackers use [selective queries](https://posts.specterops.io/bofhound-ad-cs-integration-91b706bc7958), [obfuscate their requests](https://github.com/MaLDAPtive/Invoke-Maldaptive), leverage [native utilities](https://github.com/CCob/DRSAT) and have [developed new enumeration techniques](https://www.mdsec.co.uk/2024/02/active-directory-enumeration-for-red-teams/) with [corresponding tooling](https://falconforce.nl/soaphound-tool-to-collect-active-directory-data-via-adws/) based on alternative protocols (ADWS).

Wouldn’t it be convenient to use another – less monitored – data source to learn the same information?

## Registry Certificate Template Cache

[![AD CS reconnaissance meme](https://blog.compass-security.com/wp-content/uploads/2025/01/image-9.png)](https://blog.compass-security.com/wp-content/uploads/2025/01/image-9.png)

This is what Cedric Van Bockhaven and Max Grim from Outflank have presented in their [The Registry Rundown](https://troopers.de/troopers24/talks/jlaupj/) talk at Troopers. They discovered that the local registry contains a certificate template cache:

[![Registry Certificate Template Cache slide from Outflank's Troopers presentation](https://blog.compass-security.com/wp-content/uploads/2025/01/image-11.png)](https://blog.compass-security.com/wp-content/uploads/2025/01/image-11.png)

AD CS is a gift that keeps on giving ([ESC13](https://posts.specterops.io/adcs-esc13-abuse-technique-fda4272fbd53), [ESC14](https://posts.specterops.io/adcs-esc14-abuse-technique-333a004dc2b9), [ESC15](https://trustedsec.com/blog/ekuwu-not-just-another-ad-cs-esc)) with new misconfigurations being discovered on a regular basis. It therefore seemed natural to plug this new data source into an existing analysis framework to reuse its capabilities and [structured data](https://posts.specterops.io/on-structured-data-707b7d9876c6) output.

## Extend Existing Tooling

This idea was realized by [introducing a new `certipy` command](https://github.com/ly4k/Certipy/pull/247) to parse TrustedSec’s [reg\_query BOF](https://github.com/trustedsec/CS-Situational-Awareness-BOF) output as well as the text-based Windows registry (.reg) file format.

### Using the `reg_query` BOF

Assuming you have code execution as a low privileged user on a domain-joined Windows machine, collect the cached certificate template meta data from the local registry using:

```
beacon> reg_query_recursive HKU .DEFAULT\Software\Microsoft\Cryptography\CertificateTemplateCache
```

One missing piece of information is whether the certificate template is actually published to a certificate authority. This still has to be queried via LDAP:

```
beacon> ldapsearch "(objectclass=pKIEnrollmentService)" --attributes certificateTemplates --dn "CN=Configuration,DC=ludus,DC=domain" --ldaps
```

Passing the returned comma separated list of published template names, the previously captured registry query output and a set of SIDs, belonging to owned principals, allows familiar analysis using certipy:

```
$ certipy parse -format bof -domain ludus.domain -ca ludus-CA -published "ESC13, ESC9, ESC7_CERTMGR, ESC4, ESC3_CRA, ESC3, ESC2, ESC1, DirectoryEmailReplication, DomainControllerAuthentication, KerberosAuthentication, EFSRecovery, EFS, DomainController, WebServer, Machine, User, SubCA, Administrator" -sids "S-1-5-21-3291837554-245906837-2404182060-513,S-1-5-21-3291837554-245906837-2404182060-1104" beacon.log
```

### Using `regedit.exe`

If you instead have interactive access to a compromised client and want to use the native `regedit.exe` utility to live off the land and better blend into the target environment, you can *File > Export* the relevant registry branch to a `.reg` file.

[![Native Registry Editor exporting branch HKEY_USERS\.DEFAULT\Software\Microsoft\Cryptography\CertificateTemplateCache](https://blog.compass-security.com/wp-content/uploads/2025/01/2025-01-20-13_36_22-ad-win11-22h2-enterprise-x64-and-74-more-pages-Work-Microsoft​-Edge.png)](https://blog.compass-security.com/wp-content/uploads/2025/01/2025-01-20-13_36_22-ad-win11-22h2-enterprise-x64-and-74-more-pages-Work-Microsoft%E2%80%8B-Edge.png)

Changing the `-format` to `reg`allows parsing of this too:

```
$ certipy parse -format reg -domain ludus.domain -ca ludus-CA -published "ESC13, ESC9, ESC7_CERTMGR, ESC4, ESC3_CRA, ESC3, ESC2, ESC1, DirectoryEmailReplication, DomainControllerAuthentication, KerberosAuthentication, EFSRecovery, EFS, DomainController, WebServer, Machine, User, SubCA, Administrator" -sids "S-1-5-21-3291837554-245906837-2404182060-513,S-1-5-21-3291837554-245906837-2404182060-1104" adcs.reg
```

## What’s next?

Of course, being aware of available certificate templates is only the first step. Obtaining a valid certificate while avoiding possible [honey pots](https://www.srlabs.de/blog-post/certiception-the-adcs-honeypot-we-always-wanted), detections based on [suspicious ticket options](https://www.synacktiv.com/publications/understanding-and-evading-microsoft-defender-for-identity-pkinit-detection) during PKINIT or [Kerberos traffic from an unusual process](https://www.elastic.co/guide/en/security/current/kerberos-traffic-from-unusual-process.html) is left as an exercise for the sophisticated attacker.

As for detection, the same mechanism (a custom SACL on the relevant registry keys) as for detecting [local SCCM reconnaissance](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/defense-techniques/DETECT/DETECT-9/detect-9_description.md) can be employed.

Happy red teaming.

[Red Teaming](https://blog.compass-security.com/category/red-teaming/)

[Active Directory](https://blog.compass-security.com/tag/active-directory/)[adcs](https://blog.compass-security.com/tag/adcs/)[red](https://blog.compass-security.com/tag/red/)

[##### Previous post

BloodHound Community Edition Custom Queries](https://blog.compass-security.com/2025/01/bloodhound-community-edition-custom-queries/ "Previous post: BloodHound Community Edition Custom Queries")
[##### Next post

Passke...
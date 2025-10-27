---
title: FarsightAD - PowerShell Script That Aim To Help Uncovering (Eventual) Persistence Mechanisms Deployed By A Threat Actor Following An Active Directory Domain Compromise
url: https://buaq.net/go-140008.html
source: unSafe.sh - 不安全
date: 2022-12-15
fetch_date: 2025-10-04T01:29:44.845484
---

# FarsightAD - PowerShell Script That Aim To Help Uncovering (Eventual) Persistence Mechanisms Deployed By A Threat Actor Following An Active Directory Domain Compromise

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

![](https://8aqnet.cdn.bcebos.com/47556e9960f0feb3b503d67855e8a309.jpg)

FarsightAD - PowerShell Script That Aim To Help Uncovering (Eventual) Persistence Mechanisms Deployed By A Threat Actor Following An Active Directory Domain Compromise

FarsightAD is a PowerShell script that aim to help uncovering (eventual) persistence mechan
*2022-12-14 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-140008.htm)
阅读量:27
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhJP8tw6l0QoEBdruA4N4Er85BrYaWKhJzKkkedilz9sHAmKJJI868hwqmHptnGoKzz4_m-IWfNzHr3VVnwN2fxpVQHDz4tF0GWa5zyh2EhMKNL6l1vf5C_A7NWcIdY_FH86AQLwnNzMnkEWZYVwreeTBgWT577M7IlC9cxFq3tRQPR_FR_Xug8YX8idw=w640-h360)](https://blogger.googleusercontent.com/img/a/AVvXsEhJP8tw6l0QoEBdruA4N4Er85BrYaWKhJzKkkedilz9sHAmKJJI868hwqmHptnGoKzz4_m-IWfNzHr3VVnwN2fxpVQHDz4tF0GWa5zyh2EhMKNL6l1vf5C_A7NWcIdY_FH86AQLwnNzMnkEWZYVwreeTBgWT577M7IlC9cxFq3tRQPR_FR_Xug8YX8idw)

`FarsightAD` is a PowerShell script that aim to help uncovering (eventual) persistence mechanisms deployed by a threat actor following an Active Directory domain compromise.

The script produces CSV / JSON file exports of various objects and their attributes, enriched with timestamps from replication metadata. Additionally, if executed with replication privileges, the `Directory Replication Service (DRS)` protocol is leveraged to detect fully or partially hidden objects.

For more information, refer to the [SANS DFIR Summit 2022 introductory slides](https://github.com/Qazeer/FarsightAD/blob/main/SANS_DFIR_Summit_2022-Hunting_for_Active_Directory_persistence-v1.2.pdf "SANS DFIR Summit 2022 introductory slides").

## Prerequisite

`FarsightAD` requires [`PowerShell 7`](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows "PowerShell script that aim to help uncovering (eventual) persistence mechanisms deployed by a threat actor following an Active Directory domain compromise (14)") and the `ActiveDirectory` module updated for `PowerShell 7`.

On Windows 10 / 11, the module can be installed through the `Optional Features` as [`RSAT:`](https://docs.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/remote-server-administration-tools "PowerShell script that aim to help uncovering (eventual) persistence mechanisms deployed by a threat actor following an Active Directory domain compromise (15)") `[Active Directory Domain](https://www.kitploit.com/search/label/Active%20Directory%20Domain "Active Directory Domain") Services and Lightweight Directory Services Tools`. Already installed module can be updated with:

```
Add-WindowsCapability -Online -Name Rsat.ServerManager.Tools~~~~0.0.1.0
```

If the module is correctly updated, `Get-Command Get-ADObject` should return:

```
CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Get-ADObject                                       1.0.X.X    ActiveDirectory
```

## Basic usage

```
. .\FarsightAD.ps1

Invoke-ADHunting [-Server <DC_IP | DC_HOSTNAME>] [-Credential <PS_CREDENTIAL>] [-ADDriveName <AD_DRIVE_NAME>] [-OutputFolder <OUTPUT_FOLDER>] [-ExportType <CSV | JSON>]
```

## AD Hunting cmdlets

| Cmdlet | Synopsis |
| --- | --- |
| `Invoke-ADHunting` | Execute all the FarsightAD AD hunting cmdlets (mentionned below). |
| `Export-ADHuntingACLDangerousAccessRights` | Export dangerous ACEs, i.e ACE that allow takeover of the underlying object, on all the domain's objects. May take a while on larger domain. |
| `Export-ADHuntingACLDefaultFromSchema` | Export the ACL configured in the defaultSecurityDescriptor attribute of Schema classes. Non-default (as defined in the Microsoft documentation) ACLs are identified and potentially dangerous ACEs are highlighted. |
| `Export-ADHuntingACLPrivilegedObjects` | Export the ACL configured on the privileged objects in the domain and highlight potentially dangerous access rights. |
| `Export-ADHuntingADCSCertificateTemplates` | Export information and [access rights](https://www.kitploit.com/search/label/Access%20Rights "access rights") on certificate templates. The following notable parameters are retrieved: certificate template publish status, certificate usage, if the subject is constructed from user-supplied data, and access control (enrollment / modification). |
| `Export-ADHuntingADCSPKSObjects` | Export information and access rights on sensitive PKS objects (NTAuthCertificates, certificationAuthority, and pKIEnrollmentService). |
| `Export-ADHuntingGPOObjectsAndFilesACL` | Export ACL access rights information on GPO objects and files, highlighting GPOs are applied on privileged users or computers. |
| `Export-ADHuntingGPOSettings` | Export information on various settings configured by GPOs that could be leveraged for persistence (privileges and logon rights, restricted groups membership, scheduled and immediate tasks V1 / V2, machine and user logon / logoff scripts). |
| `Export-ADHuntingHiddenObjectsWithDRSRepData` | Export the objects' attributes that are accessible through replication (with the Directory Replication Service (DRS) protocol) but not by direct query. Access control are not taken into account for replication operations, which allows to identify access control blocking access to specific objects attribute(s).  Only a limited set of sensitive attributes are assessed. |
| `Export-ADHuntingKerberosDelegations` | Export the Kerberos delegations that are considered dangerous (unconstrained, constrained to a privileged service, or resources-based constrained on a privileged service). |
| `Export-ADHuntingPrincipalsAddedViaMachineAccountQuota` | Export the computers that were added to the domain by non-privileged principals (using the ms-DS-MachineAccountQuota mechanism). |
| `Export-ADHuntingPrincipalsCertificates` | Export parsed accounts' certificate(s) (for accounts having a non empty userCertificate attribute). The [certificates](https://www.kitploit.com/search/label/Certificates "certificates") are parsed to retrieve a number of parameters: certificate validity timestamps, certificate purpose, certificate subject and eventual SubjectAltName(s), ... |
| `Export-ADHuntingPrincipalsDontRequirePreAuth` | Export the accounts that do not require Kerberos pre-authentication. |
| `Export-ADHuntingPrincipalsOncePrivileged` | Export the accounts that were once member of privileged groups. |
| `Export-ADHuntingPrincipalsPrimaryGroupID` | Export the accounts that have a non default primaryGroupID attribute, highlighting RID linked to privileged groups. |
| `Export-ADHuntingPrincipalsPrivilegedAccounts` | Export detailed information about members of privileged groups. |
| `Export-ADHuntingPrincipalsPrivilegedGroupsMembership` | Export privileged groups' current and past members, retrieved using replication metadata. |
| `Export-ADHuntingPrincipalsSIDHistory` | Export the accounts that have a non-empty SID History attribute, with resolution of the associated domain and highlighting of privileged SIDs. |
| `Export-ADHuntingPrincipalsShadowCredentials` | Export parsed Key [Credentials](https://www.kitploit.com/search/label/Credentials "Credentials") information (of accounts having a non-empty msDS-KeyCredentialLink attribute). |
| `Export-ADHuntingPrincipalsTechnicalPrivileged` | Export the technical privileged accounts (SERVER\_TRUST\_ACCOUNT and INTERDOMAIN\_TRUST\_ACCOUNT). |
| `Export-ADHuntingPrincipalsUPNandAltSecID` | Export the accounts that define a UserPrincipalName or AltSecurityIdentities attribute, highlighting potentia...
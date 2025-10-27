---
title: At the Edge of Tier Zero: The Curious Case of the RODC
url: https://shenaniganslabs.io/2023/01/25/RODCs.html
source: Shenanigans Labs
date: 2023-01-26
fetch_date: 2025-10-04T04:51:37.490013
---

# At the Edge of Tier Zero: The Curious Case of the RODC

[Shenanigans Labs](/)

# At the Edge of Tier Zero: The Curious Case of the RODC

25 January 2023
• Elad Shamir •
16 min read

The read-only Domain Controller (RODC) is a solution that Microsoft introduced for physical locations that don’t have adequate security to host a Domain Controller but still require directory services for resources in those locations. A branch office is the classic use case.

While RODCs, by definition, are not part of the set of resources that can control “enterprise identities”, known as Tier Zero, we have seen cases where there is a privilege escalation path from an RODC to domain dominance.

In this blog post, we’ll answer the question, “If I compromise a Read-Only Domain Controller, can I compromise the domain?” or, from an architectural perspective, “Do RODCs belong in Tier Zero?”

## Tl;dr — It’s Complicated

In the context of RODCs, the term “compromise” could mean several things:

1. Elevated access to the RODC host
2. Credential access to the RODC computer account
3. Control of the RODC computer object in Active Directory

In the case of elevated access to the RODC host (1) or credential access to the RODC computer account (2), there is a path for domain dominance only if the RODC is permitted to “reveal” the credentials of a Tier Zero security principal.

In the case of control of the RODC computer object in Active Directory (3), there is a generalized path to domain dominance.

**While the RODC hosts and the credentials for their computer accounts do not belong in Tier Zero, all RODC computer objects must be protected as Tier Zero resources.**

## Intro

Microsoft introduced, and since retired, the Enhanced Security Admin Environment (ESAE) architecture as the ideal for securing Active Directory (AD). Part of that architecture was the Administrative Tiering Model, which defined the concept of “Tier Zero” as a set containing the resources that control enterprise identities and their security dependencies. Most crucially, no resources outside of Tier Zero should have any control over anything inside Tier Zero.

RODCs are an alternative for Domain Controllers in less secure physical locations. They maintain a filtered copy of AD, excluding sensitive attributes, such as LAPS passwords, to support LDAP queries, and cache credentials for selected users and computers to support authentication. Typically, an RODC would be allowed to retrieve and cache credentials only for accounts that belong to the same physical location, such as a branch office, and have an equivalent or lower level of physical security.

By definition, Tier Zero resources *should* not be permitted to operate in less trustworthy locations that require RODCs, and RODCs *should* not control any Tier Zero resource. *Should* is the operative word.

## How Are RODCs Managed?

Domain Controllers don’t have local accounts and local groups per se. When a server is promoted to a Domain Controller, AD replaces the local accounts and groups, and the same applies to RODCs. However, if only Tier Zero admins are permitted to manage Domain Controllers, and RODCs aren’t trustworthy enough for Tier Zero admins to log onto them, then how are RODCs managed?

The *managedBy* attribute does not usually serve any function for an AD object, although it can be used for organizational purposes. However, RODC computer objects are the exception. Any user or group specified in the *managedBy* attribute of an RODC has local admin access to the RODC server (thanks to [Guido Grillenmeier](https://twitter.com/ggrillen) for teaching me that!).

[![managedBy](/images/RODCs/ManagedBy.png)](/images/RODCs/ManagedBy.png)

**If you compromise an account listed in the *managedBy* attribute of an RODC, you have local admin on the RODC. And if you compromise an account with delegated rights to modify the *managedBy* attribute of an RODC, you can make yourself an admin.**

## How Do RODCs Authenticate Users?

RODCs need access to the credentials of users and computers to authenticate them locally. Every RODC should have a specific list of principals that it is designated to authenticate and is therefore allowed to retrieve their credentials. This list is stored in the *msDS-RevealOnDemandGroup* attribute of the RODC’s computer object. The list may contain individual accounts or groups.

[![Allowed List](/images/RODCs/Allowed.png)](/images/RODCs/Allowed.png)

A similar list of principals for whom the RODC is explicitly denied from retrieving credentials is stored in the *msDS-NeverRevealGroup* attribute of the RODC. The deny list takes precedence over the allow list, meaning that if a user is listed in both, either directly or via nested groups, the RODC will not be able to retrieve the account’s credentials.

[![Denied List](/images/RODCs/Denied.png)](/images/RODCs/Denied.png)

After the RODC authenticates a user or computer, it needs to generate a Kerberos ticket-granting-ticket (TGT), but the RODC is not trustworthy enough to have access to the domain’s KRBTGT keys. Instead, when a Windows server is promoted to RODC, AD creates a new, dedicated version of the KRBTGT key. The new RODC will use this key to encrypt and sign the TGTs that it generates. The key is assigned a random key version number (typically five digits), stored in a new AD account named *KRBTGT\_XXXXX,* where *XXXXX* is the key version number. The key version number is also stored in the *msDS-SecondaryKrbTgtNumber* attribute of the new KRBTGT account.

The name of the new KRBTGT account is stored in the *msDS-KrbTgtLink* attribute of the RODC’s computer object, and the name of the RODC computer object is stored in the new KRBTGT account’s *msDS-KrbTgtLinkBl* (backlink) attribute. The RODC computer account is also granted the right to reset the password of the associated KRBTGT account.

```
PS C:\Users\elad> Get-ADComputer RODC -Properties msDS-KrbTgtLink

DistinguishedName : CN=RODC,CN=Computers,DC=shenanigans,DC=labs
DNSHostName       : RODC.shenanigans.labs
Enabled           : True
msDS-KrbTgtLink   : CN=krbtgt_25078,CN=Users,DC=shenanigans,DC=labs
Name              : RODC
ObjectClass       : computer
ObjectGUID        : 2b81a6b5-926d-438b-8003-cb173ce196d6
SamAccountName    : RODC$
SID               : S-1-5-21-1437000690-1664695696-1586295871-1110
UserPrincipalName :

PS C:\Users\elad> Get-ADUser krbtgt_25078 -Properties msDS-SecondaryKrbTgtNumber,msDS-KrbTGTLinkBl

DistinguishedName          : CN=krbtgt_25078,CN=Users,DC=shenanigans,DC=labs
Enabled                    : False
GivenName                  :
msDS-KrbTGTLinkBl          : {CN=RODC,CN=Computers,DC=shenanigans,DC=labs}
msDS-SecondaryKrbTgtNumber : 25078
Name                       : krbtgt_25078
ObjectClass                : user
ObjectGUID                 : bdac311c-60a7-45fc-8997-09cf258570c0
SamAccountName             : krbtgt_25078
SID                        : S-1-5-21-1437000690-1664695696-1586295871-1111
Surname                    :
UserPrincipalName          :
```

Whenever the RODC generates a TGT, it specifies its KRBTGT’s key version number in the ticket’s *kvno* field to indicate which key was used to encrypt and sign the ticket.

[![Wireshark TGS-REQ](/images/RODCs/WiresharkTGSREQ.png)](/images/RODCs/WiresharkTGSREQ.png)

A TGT generated by an RODC can be used in TGS-REQs to obtain service tickets from the same RODC or from writable Domain Controllers. When a TGT generated by an RODC is presented to a writable Domain Controller, the Domain Controller only accepts it if the ticket was generated for a principal listed in the RODC’s *msDS-RevealOnDemandGroup* attribute and not listed in the RODC’s *msDS-NeverRevealGroup* attribute.

If the criteria above are met, a TGT issued by an RODC can be “upgraded” to a full TGT, encrypted and signed by the domain’s KRBTGT account, by sending a TGS-REQ for the service “KRBTGT.”

## RODC Golden Ticket

As Sean Metcalf ([@PyroTek3](https://twitter.com/PyroTek3)) noted in his “[Attacking Read-Only Domain Controllers (RO...
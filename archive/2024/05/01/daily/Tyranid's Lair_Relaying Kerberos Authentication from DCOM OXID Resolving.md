---
title: Relaying Kerberos Authentication from DCOM OXID Resolving
url: https://www.tiraniddo.dev/2024/04/relaying-kerberos-authentication-from.html
source: Tyranid's Lair
date: 2024-05-01
fetch_date: 2025-10-06T17:17:27.298382
---

# Relaying Kerberos Authentication from DCOM OXID Resolving

# [Tyranid's Lair](https://www.tiraniddo.dev/)

## Monday, 29 April 2024

### Relaying Kerberos Authentication from DCOM OXID Resolving

Recently, there's been some good research into further exploiting DCOM authentication that I initially [reported to Microsoft](https://bugs.chromium.org/p/project-zero/issues/detail?id=325) almost 10 years ago. By inducing authentication through DCOM it can be relayed to a network service, such as [Active Directory Certificate Services (ADCS)](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) to elevated privileges and in some cases get domain administrator access.

The important difference with this new research is taking the abuse of DCOM authentication from local access (in the case of the [many Potatoes](https://powerofcommunity.net/poc2023/AntonioCocomazzi.pdf)) to fully remote by abusing security configuration changes or over granting group access. For more information I'd recommend reading the slides from [Tianze Ding](https://twitter.com/D1iv3) [Blackhat ASIA 2024 presentation,](http://i.blackhat.com/Asia-24/Presentations/Asia-24-Ding-CertifiedDCOM-The-Privilege-Escalation-Journey-to-Domain-Admin.pdf) or reading about [SilverPotato](https://decoder.cloud/2024/04/24/hello-im-your-domain-admin-and-i-want-to-authenticate-against-you/) by [Andrea Pierini](https://twitter.com/decoder_it).

This short blog post is directly based on slide 36 of Tianze Ding presentation where there's a mention on trying to relay Kerberos authentication from the initial OXID resolver request. I've reproduced the slide below:

[![Slide 36 from the Blackhat Asia presentation, discussing Kerberos relay from the ResolveOxid2 call.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFtsL-cKYvq10TZF0BK_uLzKP8lDZhNDF15QFO0V1RfNCWgCMfLVG2GJgxSlKGSP9wnNo40OZPJ32iEtTchy2A94bmoXtXOzbvtjItvMOItw9X7sRW0-KcYTczDQCrvKvnoCHCYrcwarK22yCYbRYoOazeCrtVVvaP9tc4YpAERhjNp2d_TvznEGTeXvQ/w640-h360/dcom_slide.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFtsL-cKYvq10TZF0BK_uLzKP8lDZhNDF15QFO0V1RfNCWgCMfLVG2GJgxSlKGSP9wnNo40OZPJ32iEtTchy2A94bmoXtXOzbvtjItvMOItw9X7sRW0-KcYTczDQCrvKvnoCHCYrcwarK22yCYbRYoOazeCrtVVvaP9tc4YpAERhjNp2d_TvznEGTeXvQ/s1152/dcom_slide.jpg)

The slides says that you can't relay Kerberos authentication during OXID resolving because you can't control the SPN used for the authentication. It's always set to *RPCSS/MachineNameFromStringBinding*. While you can control the string bindings in the standard OBJREF structure, RPCSS ignores the security bindings and so you can't specify the SPN unlikely with the an object RPC call which happens later.

This description intrigued me, as I didn't think this was true. You just had to abuse a "feature" I described in my original [Kerberos relay blog post](https://googleprojectzero.blogspot.com/2021/10/using-kerberos-for-authentication-relay.html). Specifically, that the Kerberos SSPI supports a special format for the SPN which includes marshaled target information. This was something I discovered when trying to see if I could get Kerberos relay from the SMB protocol, the SMB client would call the [SecMakeSPNEx2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-secmakespnex2) API, which in turn would call [CredMarshalTargetInfo](https://learn.microsoft.com/en-us/windows/win32/api/ntsecpkg/nf-ntsecpkg-credmarshaltargetinfo) to build a marshaled string which appended to the end of the SPN. If the Kerberos SSPI sees an SPN in this format, it calculates the length of the marshaled data, strips that from the SPN and continues with the new SPN string.

In practice what this means is you can build an SPN of the form *CLASS/<SERVER><TARGETINFO>* and Kerberos will authenticate using *CLASS/<SERVER>*. The interesting thing about this behavior is if the *<SERVER><TARGETINFO>* component is coming from the hostname of the server we're authenticating to then you can end up decoupling the SPN used for the authentication from the hostname that's used to communicate. And that's exactly what we got here, the *MachineNameFromStringBinding* is coming from an untrusted source, the OBJREF we specified. We can specify a machine name in this special format, this will allow the OXID resolver to talk to our server on hostname *<SERVER><TARGETINFO>* but authenticate using *RPCSS/<SERVER>* which can be anything we like.

There are some big caveats with this. Firstly, the machine name must not contain any dots, so it must be an intranet address. This is because it's close to impossible to a build a valid *TARGETINFO* string which represents a valid fully qualified domain name. In many situations this would rule out using this trick, however as we're dealing with domain authentication scenarios and the default for the Windows DNS server is to allow any user to create arbitrary hosts within the domain's DNS Zone this isn't an issue.

This restriction also limits the maximum size of the hostname to 63 characters due to the DNS protocol. If you pass a completely empty *CREDENTIAL\_TARGET\_INFORMATION* structure to the *CredMarshalTargetInfo* API you get the minimum valid target information string, which is 44 characters long. This only leaves 19 characters for the *SERVER* component, but again this shouldn't be a big issue. Windows component names are typically limited to 15 characters due to the old NetBIOS protocol, and by default SPNs are registered with these short name forms. Finally in our case while there won't be an explicit RPCSS SPN registered, this is one of the service classes which is automatically mapped to the HOST class which will be registered.

To exploit this you'll need to do the following steps:

1. Build the machine name by appending the hostname for for the target SPN to the minimum string *1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA*. For example for the SPN *RPCSS/ADCS*build the string ADCS*1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA.*
2. Register the machine name as a host on the domain's DNS server. Point the record to a server you control on which you can replace the listening service on TCP port 135.
3. Build an OBJREF with the machine name and induce OXID resolving through your preferred method, such as abusing *IStorage* activation.
4. Do something useful with the induced Kerberos authentication.

With this information I did some tests myself, and also [Andrea checked with SilverPotato](https://x.com/decoder_it/status/1784957248881451500) and it seems to work. There are limits of course, the big one is the security bindings are ignored so the OXID resolver uses Negotiate. This means the Kerberos authentication will always be negotiated with at least integrity enabled which makes the authentication useless for most scenarios, although it can be used for the default configuration of ADCS (I think).

Posted by
tiraniddo

at
[18:08](https://www.tiraniddo.dev/2024/04/relaying-kerberos-authentication-from.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4304739697716191998&postID=7302950235696417509&from=pencil "Edit Post")

[Newer Post](https://www.tiraniddo.dev/2024/06/working-your-way-around-acl.html "Newer Post")

[Older Post](https://www.tiraniddo.dev/2024/04/issues-resolving-symbols-on-windows-11.html "Older Post")
[Home](https://www.tiraniddo.dev/)

## Blog Archive

* ▼
  [2024](https://www.tiraniddo.dev/2024/)
  (4)
  + ►
    [June](https://www.tiraniddo.dev/2024/06/)
    (1)
  + ▼
    [April](https://www.tiraniddo.dev/2024/04/)
    (2)
    - [Relaying Kerberos Authentication from DCOM OXID Re...](https://www.tiraniddo.dev/2024/04/relaying-kerberos-authentication-from.html)
    - [Issues Resolving Symbols on Windows 11 on ARM64](https://www.tiraniddo.dev/2024/04/issues-resolving-symbols-on-windows-11.html)
  + ►
    [February](https://www.tiraniddo.dev/2024/02/)
    (1)

* ►
  [2022](https://www.tiraniddo.dev/2022/)
  (4)
  + ►
   ...
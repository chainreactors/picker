---
title: Reflecting Your Authentication: When Windows Ends Up Talking to Itself
url: https://decoder.cloud/2025/11/24/reflecting-your-authentication-when-windows-ends-up-talking-to-itself/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-24
fetch_date: 2025-11-25T03:12:56.817978
---

# Reflecting Your Authentication: When Windows Ends Up Talking to Itself

# [Decoder's Blog](https://decoder.cloud/ "Decoder's Blog")

Decoder's Blog

[Skip to content](#content "Skip to content")

* [Home](/)
* [Decoder’s Blog](https://decoder.cloud/)
* [Contact](https://decoder.cloud/contact/)

Search for:

Posted on [November 24, 2025November 24, 2025](https://decoder.cloud/2025/11/24/reflecting-your-authentication-when-windows-ends-up-talking-to-itself/) by [Decoder](https://decoder.cloud/author/decoderblogblog/)

# Reflecting Your Authentication: When Windows Ends Up Talking to Itself

Authentication reflection has been around for more than 20 years, but its implications in modern Windows networks are far from obsolete. Even after all the patches Microsoft has rolled out over the years, reflection attacks are still very much exploitable 😉

This post walks through what authentication reflection actually is, why it remains dangerous today, and how the most recent discoveries prove that reflection keeps coming back in places where it really shouldn’t. We will explore how recent Windows behaviors introduced entirely new attack surfaces involving Kerberos, NTLM, SMB, HTTP and DCE/RPC. We’ll also look at Ghost SPNs, the *[CredMarshalTargetInfo](https://www.tiraniddo.dev/2024/04/relaying-kerberos-authentication-from.html)* (CMTI) trick, and multiple cases where a single reflected authentication was enough to compromise an entire domain.

The goal is also to keep the explanations clear enough for readers who aren’t experts on these topics, without losing the important technical details

## **What Authentication Reflection Actually Is**

Authentication reflection is deceptively simple:

1. A victim (machine or user) is coerced into authenticating to an attacker-controlled endpoint.
2. The attacker reflects that authentication attempt back to a service the victim host runs itself.
3. The victim ends up authenticating to its own service using its own identity.

If the victim is a domain-joined Windows machine, the identity used is the computer account , effectively granting **NT AUTHORITY\SYSTEM** on that host.

![](https://decoder.cloud/wp-content/uploads/2025/11/image-1.png?w=1024)

Depending on the coercion vector, this results in:

➔ **Local Privilege Escalation (LPE)**

➔ **Remote Privilege Escalation (RPE)**

➔ **Full domain compromise** when the reflected authentication hits LDAP/LDAPS on a DC under certain conditions

Reflection attacks don’t steal credentials.
***They make Windows authenticate to itself, on your behalf.***

## **A Very Old Problem: MS08-68**

Authentication reflection was first widely exploited in 2008 via **MS08-68**, where NTLM authentication could be reflected back to SMB on the same host, yielding SYSTEM privileges.

Microsoft eventually patched classic NTLM loopback reflection, including:

➔ Same-protocol reflection (NTLM→NTLM)

➔ Cross-protocol reflection (NTLM→different service)

But the story didn’t end, there was still NTLM local authentication…

## **Kerberos Reflection: HardeR, Not Impossible**

Kerberos does not have a universal reflection-detection mechanism, but requiring control of the target SPN and valid Kerberos tickets makes such attacks substantially harder to exploit in practice.

Ok, I said, harder but for sure not impossible 😉

## **The CredMarshaltargetinfo (cmti) Trick: abusing spn metadata**

To perform a reflection attack, we must convince Windows to direct the authentication back to itself. In practice, this means spoofing the hostname so that the authentication is sent to an endpoint under our control, while the client still believes that the target hostname is local.

To achieve this, we need to control the Service Principal Name (SPN) that Kerberos and NTLMv2, as well, use to identify the target service.

In other words, for our forged SPN the ideal situation is that the client uses an SPN/TARGET where TARGET resolves to an IP address we control, but is still considered local by the client.

In the DCOM scenario, by abusing the various [‘\*potato’](https://www.sentinelone.com/labs/relaying-potatoes-another-unexpected-privilege-escalation-vulnerability-in-windows-rpc-protocol/) techniques, we can create a fake OXID Resolver. This allows us to instruct the client to use an SPN associated with the victim (SPN/VICTIM) while still contacting the endpoint under our control. That gives us the victim’s authentication, which we can then reflect back to the victim’s own service, because he is the victim 😉

However, if we want to use other protocols, such as SMB, which don’t give us control over the SPN, we need an alternative.

Enter [CredMarshalTargetInfo()](https://www.tiraniddo.dev/2024/04/relaying-kerberos-authentication-from.html), described by James Forshaw

Windows SSPI supports a “special” SPN format that includes an embedded Marshal Target Information block:

➔ `ServiceClass/Server[TargetInfo]`

where:

*TargetInfo* is a serialized, base64-like structure called Credential Target Information

The shortest valid blob is:

➔ *1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA*

This tiny blob is enough for Windows to consider the SPN well-formed, but it also allows us to spoof the hostname inside the SPN in a way that survives SPN canonicalization, Kerberos processing, and NTLM’s AV-pair parsing.

Even better: a standard domain user can by default create DNS records, which means they can freely introduce new names that point to attacker-controlled IP addresses.

When the SPN includes a CMTI blob, here’s what happens:

➔ Kerberos will request a TGS for *ServiceClass/Server*

➔ NTLM will embed the value into MsvAvTargetName

➔ The client (SMB, RPC, DCOM, …) will actually contact the host named:

➔ *1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA*

If that “hostname” resolves to an attacker-controlled IP, but the internal *TargetInfo* makes Windows treat it as local, then we get the exact situation reflection attacks rely on:

> **The authentication is sent to the attacker, but processed as if it were going to a local service.**
>
> ![](https://decoder.cloud/wp-content/uploads/2025/11/image-2.png?w=1024)

This is what allows SMB→SMB reflection even without direct SPN control, and it’s why CMTI-based spoofing became such a powerful tool in modern reflection attacks.

## **Remote Kerberos Reflection — DCOM → HTTP**

Abusing DCOM isn’t new, but Windows exposes interfaces that are particularly useful for coercion.

On Windows Servers with the Certificate Services role installed, the system exposes the *AD CS CertSrv Request* interface, which can be instantiated remotely by any domain user and will trigger an outbound machine authentication from the AD CS server.

I already covered this in my post ‘*[Hello, I’m your ADCS server and I want to authenticate against you’,](https://decoder.cloud/2024/02/26/hello-im-your-adcs-server-and-i-want-to-authenticate-against-you/)* where I also demonstrated that it is possible to reflect the machine Kerberos authentication back to the server and abuse it in an ESC8 scenario.

It is not possible to reflect DCOM → SMB, because SMB enforces anti-reflection protections for both Kerberos and NTLM. In this path, the *ISC\_REQ\_UNVERIFIED\_TARGET\_NAME* flag, set by the DCOM client, is actually honored by the SMB client, which prevents authentication from being reused against the same host by stripping the SPN in the case of loopback authentication.

## **SMB → SMB Kerberos/NTLM Reflection**

Prior to June 2025, SMB callback coercion using PrintSpooler, EFSRPC, or DFS could force SMB clients to authenticate to arbitrary endpoints.

By abusing *CMTI*, a remote attacker could abuse Kerberos and NTLM reflective authentication and ultimately gain SYSTEM privileges.

A detailed description can be found [here](https://www.synacktiv.com/en/publications/ntlm-reflection-is-dead-long-live-ntlm-reflection-an-in-depth-analysis-of-cve-2025) and [here](https://blog.redteam-pentesting.de/2025/reflective-kerberos-relay-attack/)

![](https://decoder.cloud/wp-content/uploads/2025...
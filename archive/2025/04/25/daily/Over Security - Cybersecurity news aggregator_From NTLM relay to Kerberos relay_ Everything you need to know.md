---
title: From NTLM relay to Kerberos relay: Everything you need to know
url: https://decoder.cloud/2025/04/24/from-ntlm-relay-to-kerberos-relay-everything-you-need-to-know/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-25
fetch_date: 2025-10-06T22:06:56.628461
---

# From NTLM relay to Kerberos relay: Everything you need to know

# [Decoder's Blog](https://decoder.cloud/ "Decoder's Blog")

Decoder's Blog

[Skip to content](#content "Skip to content")

* [Home](/)
* [Decoder’s Blog](https://decoder.cloud/)
* [Contact](https://decoder.cloud/contact/)

Search for:

Posted on [April 24, 2025May 14, 2025](https://decoder.cloud/2025/04/24/from-ntlm-relay-to-kerberos-relay-everything-you-need-to-know/) by [Decoder](https://decoder.cloud/author/decoderblogblog/)

# From NTLM relay to Kerberos relay: Everything you need to know

While I was reading Elad Shamir recent excellent [post](https://posts.specterops.io/the-renaissance-of-ntlm-relay-attacks-everything-you-need-to-know-abfc3677c34e) about NTLM relay attacks, I decided to contribute a companion piece that dives into the mechanics of Kerberos relays, offering an analysis and practical insights into how these attacks work and how they differ from NTLM based relays.

If you’ve been following my posts , tweets or checking out my GitHub, you probably know that lately I’ve been diving into Kerberos relay, trying to understand them better and demystify some concepts around them.

This post isn’t meant to dive too deep into the technical details, but rather to give a general idea of how Kerberos relay attacks work, what’s possible, what isn’t, and where the limitations lie. My goal is to (hopefully) provide an easy-to-read, approachable overview that helps make sense of the bigger picture, explain how my dedicated KrbRelayEx tools work in practice, and show how they can be used to perform these kinds of attacks.

## A Brief Recap of Kerberos Fundamentals

Kerberos is a network authentication protocol designed to securely verify the identities of users and services over an untrusted network. It uses symmetric key cryptography and a trusted Key Distribution Center (KDC) to enable secure communication without transmitting sensitive data like passwords.
Its main components include:

* Authentication Service (**AS**): Verifies client credentials and issues Ticket-Granting Tickets (**TGT**s).
* Ticket-Granting Service (**TGS**): Provides service-specific tickets based on a valid TGT.
* Client-Server Model: The **AP-REQ** (Authentication Protocol Request) message is used **by a client to authenticate to a service** after obtaining a service ticket (TGS).

![](https://decoder.cloud/wp-content/uploads/2025/04/image-2.png?w=688)

[Kerberos Network Authentication Service (V5) Synopsis](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/b4af186e-b2ff-43f9-b18e-eedb366abf13)

This multi-step process ensures mutual trust between client and server while protecting sensitive information across the network.

## What is kerberos relay

There hasn’t been much documentation on this topic, especially compared to NTLM relay. CrowdStrike researchers gave a great [presentation](https://media.defcon.org/DEF%20CON%2029/DEF%20CON%2029%20presentations/Sagi%20Sheinfeld%20Eyal%20Karni%20Yaron%20Zinar%20-%20Using%20Machine-in-the-Middle%20to%20Attack%20Active%20Directory%20Authentication%20Schemes.pdf) on Kerberos man-in-the-middle (MITM) attacks at DEFCON in 2021, which helped bring some attention. But the real *game changer* was an [article](https://googleprojectzero.blogspot.com/2021/10/using-kerberos-for-authentication-relay.html) by James Forshaw that went deep into the details of how Kerberos relay can be abused. I highly recommend reading it.

But as promised, I want to keep things simple in this post!

First of all let’s understand better the mechanism.

Kerberos authentication requires the target service to be known using a Service Principal Name (SPN). This is a unique string that identifies the service, often in the format **CLASS/INSTANCE:PORT/NAME**. For example, *HTTP/webserver.domain.com* or *CIFS/fileserver.domain.com*

When a client wants to access a service, the Kerberos Ticket Granting Service (TGS) uses the Service Principal Name (SPN) to determine which account in Active Directory the request is for. It then uses the corresponding encryption key,derived from that account’s password (typically a machine account),to generate a service ticket. This ticket includes the user’s identity and is tied to the original Ticket Granting Ticket (TGT).

The client sends this ticket to the target service as part of the **AP\_REQ** message.

Because the encryption key is based on the account that owns the SPN, not the SPN string itself, tickets can often be relayed between different services (e.g., from HTTP to SMB) as long as both SPNs are registered to the same account. Unless the target service explicitly verifies the SPN in the ticket (which is rarely enforced), the authentication will succeed.

But, in contrast to NTLM, we cannot relay to another host, as the encryption key, based on the account’s password, will change.

With this said, Kerberos relay attacks are conceptually far more straightforward than NTLM relays. Fundamentally, they involve intercepting the AP-REQ, the critical message sent by the client to a service (such as a server or application) to authenticate its identity and gain access.

This is how and AP-REQ looks like, we can easily identify the Service Principal Name:

![](https://decoder.cloud/wp-content/uploads/2025/04/image-4.png?w=1024)

If an attacker is able to intercept or coerce the AP-REQ request, they could use it to authenticate to the target server on behalf of the victim:

![](https://decoder.cloud/wp-content/uploads/2025/04/image-1.png?w=482)

Before we delve into the technical details, let’s first explore the limitation

Kerberos relaying shares the same limitation as NTLM relaying, namely:

* Encryption and integrity checks may prevent relaying protocols such as SMB, LDAP(S) , RPC, etc..
* Extended Protection for Authentication (EPA) can further restrict relaying for protocols such as HTTP and LDAPS

These limitations are well explained in ths excellent [article](https://en.hackndo.com/ntlm-relay/) regarding NTLM relay but alsow valid for Kerberos.

There is a third limitation, which isn’t a real one, the **Mutual Authentication** request. Normally this can be safely ignored by the client except certain conditions, but more on this later.

Okay, that’s the theory, but how does it work in practice?

At the core, all we need to do is extract the **Security Blob** , typically wrapped in [GSS-API](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Programming_Interface), sent by the client during the authentication process, and embed it into a new request targeting the desired service.

For example, we can insert that blob into an **SMB Session Setup Request** when relaying to an SMB service or, if the target service is HTTP(S), we simply Base64-encode the blob and include it in the Authorization: **Negotiate <Security Blob>** HTTP header.

As you might imagine, you need to manipulate raw packets over sockets, something that requires certain understanding of the underlying protocols.

For example, in the screenshot below we extract the **Security Blob** from an SMB Header:

![](https://decoder.cloud/wp-content/uploads/2025/04/image-6.png?w=1024)

In the next one, we embed the **Security Blob** in an HTTP header:

![](https://decoder.cloud/wp-content/uploads/2025/04/image-7.png?w=1024)

Luckily, I didn’t need to start from scratch, as Cube0x0 had already created an excellent [framework](https://github.com/cube0x0/KrbRelay) for relaying DCOM over Kerberos.

Now that we have a better understanding of the low-level mechanisms, let’s take a look at how we can actually implement this in practice.

Let’s consider two scenarios:

1. Spoofing DNS names
2. Having control over the SPN

## Spoofing dns host name resolution

In this “man-in-the middle” scenario, an attacker is able to spoof hostname resolution, tricking the victim into believing it is communicating with the legitimate target

There are several techniques for spoofing host resolution, let’s take a look at some common ones.

The attacker i...
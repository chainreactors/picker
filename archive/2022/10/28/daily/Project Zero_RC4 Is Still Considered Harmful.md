---
title: RC4 Is Still Considered Harmful
url: https://googleprojectzero.blogspot.com/2022/10/rc4-is-still-considered-harmful.html
source: Project Zero
date: 2022-10-28
fetch_date: 2025-10-03T21:06:52.006392
---

# RC4 Is Still Considered Harmful

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Thursday, October 27, 2022

### RC4 Is Still Considered Harmful

By James Forshaw, Project Zero

I've been spending a lot of time researching Windows authentication implementations, specifically Kerberos. In June 2022 I found an interesting issue number [2310](https://bugs.chromium.org/p/project-zero/issues/detail?id=2310) with the handling of RC4 encryption that allowed you to authenticate as another user if you could either interpose on the Kerberos network traffic to and from the KDC or directly if the user was configured to disable typical pre-authentication requirements.

This blog post goes into more detail on how this vulnerability works and how I was able to exploit it with only a bare minimum of brute forcing required. Note, I'm not going to spend time fully explaining how Kerberos authentication works, there's plenty of resources online. For example [this blog post](https://syfuhs.net/a-bit-about-kerberos) by [Steve Syfuhs](https://twitter.com/SteveSyfuhs) who works at Microsoft is a good first start.

## Background

Kerberos is a very old authentication protocol. The current version (v5) was described in [RFC1510](https://datatracker.ietf.org/doc/html/rfc1510) back in 1993, although it was updated in [RFC4120](https://datatracker.ietf.org/doc/html/rfc4120) in 2005. As Kerberos' core security concept is using encryption to prove knowledge of a user's credentials the design allows for negotiating the encryption and checksum algorithms that the client and server will use.

For example when sending the initial authentication service request (AS-REQ) to the Key Distribution Center (KDC) a client can specify a list supported encryption algorithms, as predefined integer identifiers, as shown below in the snippet of the ASN.1 definition from RFC4120.

KDC-REQ-BODY    ::= SEQUENCE {

...

    etype    [8] SEQUENCE OF Int32 -- EncryptionType

                                   -- in preference order --,

...

}

When the server receives the request it checks its list of supported encryption types and the ones the user's account supports (which is based on what keys the user has configured) and then will typically choose the one the client most preferred. The selected algorithm is then used for anything requiring encryption, such as generating session keys or the EncryptedData structure as shown below:

EncryptedData   ::= SEQUENCE {

        etype   [0] Int32 -- EncryptionType --,

        kvno    [1] UInt32 OPTIONAL,

        cipher  [2] OCTET STRING -- ciphertext

}

The KDC will send back an authentication service reply (AS-REP) structure containing the user's Ticket Granting Ticket (TGT) and an EncryptedData structure which contains the session key necessary to use the TGT to request service tickets. The user can then use their known key which corresponds to the requested encryption algorithm to decrypt the session key and complete the authentication process.

[![Alt Text: Diagram showing the based Kerberos authentication and requesting an AES key type.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRE6Kj-svyxGDL8OhnPM46jhk7cf3JEJrssrRSwToM3q63wAaqtboIVHeEiZ5bONQoHZNapfdxpDr3kXMbxLakja1tqshef6N4GDNlw1BXyhanRY_Jg2zDqTlIPmHZBZ2XvCMf_23GXoRSS-18_zLCfwYV2v4xOR5usrM4zq1AONy2U57oCk-n-BpW/s1062/image5.png "Alt Text: Diagram showing the based Kerberos authentication and requesting an AES key type.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRE6Kj-svyxGDL8OhnPM46jhk7cf3JEJrssrRSwToM3q63wAaqtboIVHeEiZ5bONQoHZNapfdxpDr3kXMbxLakja1tqshef6N4GDNlw1BXyhanRY_Jg2zDqTlIPmHZBZ2XvCMf_23GXoRSS-18_zLCfwYV2v4xOR5usrM4zq1AONy2U57oCk-n-BpW/s1062/image5.png)

This flexibility in selecting an encryption algorithm is both a blessing and a curse. In the original implementations of Kerberos only DES encryption was supported, which by modern standards is far too weak. Because of the flexibility developers were able to add support for AES through [RFC3962](https://datatracker.ietf.org/doc/html/rfc3962) which is supported by all modern versions of Windows. This can then be negotiated between client and server to use the best algorithm both support. However, unless weak algorithms are explicitly disabled there's nothing stopping a malicious client or server from downgrading the encryption algorithm in use and trying to break Kerberos using cryptographic attacks.

Modern versions of Windows have started to disable DES as a supported encryption algorithm, preferring AES. However, there's another encryption algorithm which Windows supports which is still enabled by default, [RC4](https://en.wikipedia.org/wiki/RC4). This algorithm was used in Kerberos by Microsoft for Windows 2000, although its documentation was in draft form until [RFC4757](https://datatracker.ietf.org/doc/html/rfc4757) was released in 2006.

The RC4 stream cipher has many substantial weaknesses, but when it was introduced it was still considered a better option than DES which has been shown to be sufficiently vulnerable to hardware cracking such as the EFF's "[Deep Crack](https://en.wikipedia.org/wiki/EFF_DES_cracker)". Using RC4 also had the advantage that it was relatively easy to operate in a reduced key size mode to satisfy US export requirements of cryptographic systems.

If you read the RFC for the implementation of RC4 in Kerberos, you'll notice it doesn't use the stream cipher as is. Instead it puts in place various protections to guard against common cryptographic attacks:

* The encrypted data is protected by a keyed MD5 HMAC hash to prevent tampering which is trivial with a simple stream cipher such as RC4. The hashed data includes a randomly generated 8-byte "confounder" so that the hash is randomized even for the same plain text.
* The key used for the encryption is derived from the hash and a base key. This, combined with the confounder makes it almost certain the same key is never reused for the encryption.
* The base key is not the user's key, but instead is derived from a MD5 HMAC keyed with the user's key over a 4 byte message type value. For example the message type is different for the AS-REQ and the AS-REP structures. This prevents an attacker using Kerberos as an encryption oracle and reusing existing encrypted data in unrelated parts of the protocol.

Many of the known weaknesses of RC4 are related to gathering a significant quantity of ciphertext encrypted with a known key. Due to the design of the RC4-HMAC algorithm and the general functional principles of Kerberos this is not really a significant concern. However, the biggest weakness of RC4 as defined by Microsoft for Kerberos is not so much the algorithm, but the generation of the user's key from their password.

As already mentioned Kerberos was introduced in Windows 2000 to replace the existing NTLM authentication process used from NT 3.1. However, there was a problem of migrating existing users to the new authentication protocol. In general the KDC doesn't store a user's password, instead it stores a hashed form of that password. For NTLM this hash was generated from the Unicode password using a single pass of the MD4 algorithm. Therefore to make an easy upgrade path Microsoft specified that the RC4-HMAC Kerberos key was this same hash value.

As the MD4 output is 16 bytes in size it wouldn't be practical to brute force the entire key. However, the hash algorithm has no protections against brute-force attacks for example no salting or multiple iterations. If an attacker has access to ciphertext encrypted using the RC4-HMAC key they can attempt to brute force the key through guessing the password. As user's will tend to choose weak or trivial passwords this increases the chance that a brute force attack would work to recover the key. And with the key the attacker can then authenticate as that user to any service they like.

To get appropriate cipher text the attacker can make requests ...
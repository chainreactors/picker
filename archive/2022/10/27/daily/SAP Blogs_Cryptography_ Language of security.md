---
title: Cryptography: Language of security
url: https://blogs.sap.com/2022/10/26/cryptography-language-of-security/
source: SAP Blogs
date: 2022-10-27
fetch_date: 2025-10-03T21:00:47.318893
---

# Cryptography: Language of security

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Cryptography: Language of security

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159356&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cryptography: Language of security](/t5/technology-blog-posts-by-sap/cryptography-language-of-security/ba-p/13554629)

![kleventcov](https://avatars.profile.sap.com/f/6/idf632f5b6ce90af03a4fe7edb3f8d53f203fda5c36a124a99a70a75020c680cc3_small.jpeg "kleventcov")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[kleventcov](https://community.sap.com/t5/user/viewprofilepage/user-id/40495)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159356)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159356)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554629)

‎2022 Oct 26
1:08 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159356/tab/all-users "Click here to see who gave kudos to this post.")

1,809

* SAP Managed Tags
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2022/10/banner-5.png)

[Formulas](https://docs.appgyver.com/docs/formula-functions) are a powerful tool and a core part of AppGyver’s functionality. With an intuitive approach, you can perform any transformation with relevant data such as the device and system info, GPS location, sensor values, data properties and the application state.

In one of the recent updates, we have powered formulas with cryptography, enabling essential security features for your applications. You can encrypt all user data via the new six hashing functions.

---

# Introduction to cryptography

Cryptography uses mathematical techniques to transform data and prevent it from being read or tampered with by unauthorized parties. That enables exchanging secure messages even in the presence of adversaries.

Nowadays, cryptography is an essential part of our day-to-day operations that facilitates strong, trusted standards and guidelines for data exchange. It is most commonly used in the following areas:

### Authentication

Through the use of cryptography, it is made sure that data is not changed while being stored or while being sent from one party to another. In other words, while developing an app with SAP AppGyver, you can protect your user’s data during the application-to-server transfer, as well as while keeping it in the backend.

### Privacy

From simple message cyphering to using virtual private networks, cryptography can provide day to day solutions for personal and enterprise privacy.

---

# Hashing

Cryptography Formulas in SAP AppGyver are implemented in a form of hashing. It is a process of modifying raw data until it can no longer be reproduced in its original form. It takes a piece of data and runs it through a hash function that manipulates the plaintext numerically. You can see a graphical representation in the image below. Notice how "User's secret password" can only be modified in one direction.

![](https://cdn-images-1.medium.com/max/800/1*rC-OECS0p34AJGUGrGSTMA.png)

To implement hashing in your application and protect your users from data leakage, convert all passwords into a hash value before sending them to a server. Additionally, **store hash values**, rather than plaintext passwords, and compare the received hash for password validation.

![](https://cdn-images-1.medium.com/max/800/1*bbYqUPGeWMh1UGx3Azgb-Q.png)

---

# Formula functions overview

## KECCAK

Keccak or SHA-3 is the latest generation secure hashing algorithm released by [NIST](https://csrc.nist.gov/csrc/media/projects/hash-functions/documents/keccak-slides-at-nist.pdf). On August 5, 2015, NIST announced that SHA-3 had become a [hashing standard](https://www.federalregister.gov/documents/2015/08/05/2015-19181/announcing-approval-of-federal-information-processing-standard-fips-202-sha-3-standard). In other words, it is the fastest and most secure option.

As a formula function, KECCAK accepts two inputs: text and a number of bits. That number can be 224, 256, 384 or 512. A higher bit number results in a larger output.

```
KECCAK(“Security is key”, 256)
```

![](https://cdn-images-1.medium.com/max/800/1*7mB7Hs-kTIEy97424G6ajw.png)

##

## MD5

MD5 is a cryptographically broken, but still widely used 128-[bit](https://en.wikipedia.org/wiki/Bit "Bit") hash function. It is vulnerable by design, so it is best to avoid using it for sensitive data. It is most commonly used to check file integrity. MD5 file hashes before and after data transfer are compared to detect corruption.

```
MD5("Hide this")
```

![](https://cdn-images-1.medium.com/max/800/1*5AFx-HGPC8lGIFO0Ninqmw.png)

##

## RIPEMD160

RIPEMD-160 is a cryptographic hash function based upon the Merkle–Damgård construction, which is a method of building collision-resistant cryptographic hash functions. It produces a 160-bit output, and is considered secure.

The most popular RIPEMD-160’s use case is [Bitcoin](https://en.bitcoin.it/wiki/RIPEMD-160).

```
RIPEMD160("My data is safe")
```

![](https://cdn-images-1.medium.com/max/800/1*HcCPGkZnr7l0xWIbF1Dl_A.png)

##

## SHA1

Similarly to MD5, SHA1 is a cryptographically broken function. NIST formally deprecated use of SHA-1 in 2011 and disallowed its use for digital signatures in 2013. Despite that, SHA1 is still used in low-security use cases.

```
SHA1("Hack this hash")
```

![](https://cdn-images-1.medium.com/max/800/1*Icot2ktkQfTrwq-H-tUL8Q.png)

##

## SHA256 & SHA512

Unlike their predecessor SHA1, SHA256 and SHA512 were designed using a [one-way compression function](https://en.wikipedia.org/wiki/One-way_compression_function), making them secure by design. SHA-2 functions are the industry standards for cryptography, used by the U.S. federal government and many other organizations globally.

256 and 512 represent the returned number of bits, respectively.

```
SHA256("Protect the users, not business")

SHA512("Information is the most valuable asset")
```

![](https://cdn-images-1.medium.com/max/800/1*NgaG351zjPCm-jtSaBAA1w.png)

---

# Final words

With our rapidly changing world, it is important to be up-to-date with tech standards and ensure that your client’s data is safe. Consider using the new cryptography formulas next time you use SAP AppGyver!

The image below should give you an idea, on how easy it is to enable security for your users - just hash the password.

![](/legacyfs/online/storage/blog_attachments/...
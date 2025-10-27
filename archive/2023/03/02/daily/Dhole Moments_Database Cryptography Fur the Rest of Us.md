---
title: Database Cryptography Fur the Rest of Us
url: https://soatok.blog/2023/03/01/database-cryptography-fur-the-rest-of-us/
source: Dhole Moments
date: 2023-03-02
fetch_date: 2025-10-04T08:27:00.987511
---

# Database Cryptography Fur the Rest of Us

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Cryptography](https://soatok.blog/category/cryptography/)

# Database Cryptography Fur the Rest of Us

An introduction to database cryptography.

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [March 1, 2023](https://soatok.blog/2023/03/01/database-cryptography-fur-the-rest-of-us/)
* [7 Comments on Database Cryptography Fur the Rest of Us](https://soatok.blog/2023/03/01/database-cryptography-fur-the-rest-of-us/#comments)

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2023/02/BlogHeader-2023-DatabaseCryptography.png?fit=1200%2C675&ssl=1)

Earlier this year, Cendyne wrote [a blog post covering the use of HKDF](https://cendyne.dev/posts/2023-01-30-how-to-use-hkdf.html), building partially upon [my own blog post about HKDF and the KDF security definition](https://soatok.blog/2021/11/17/understanding-hkdf/), but moreso inspired by [a cryptographic issue they identified in another company’s product](https://cendyne.dev/posts/2023-01-30-how-to-use-hkdf.html#Last-tweaks) (dubbed AnonCo).

At the bottom they teased:

> Database cryptography is hard. The above sketch is not complete and does not address several threats! This article is quite long, so I will not be sharing the fixes.
>
> Cendyne

If you read Cendyne’s post, you may have nodded along with that remark and not appreciate the degree to which our naga friend was *putting it mildly*. So I thought I’d share some of my knowledge about real-world database cryptography in an accessible and fun format in the hopes that it might serve as an introduction to the specialization.

Note: I’m also not going to fix Cendyne’s sketch of AnonCo’s software here–partly because I don’t want to get in the habit of assigning homework or required reading, but mostly because it’s kind of obvious once you’ve learned the basics.

![Soatok Smiling Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-smile.png?resize=512%2C512&ssl=1)

I’m including art of my fursona in this post… as is tradition for furry blogs.

 If you don’t like furries, please feel free to leave this blog and read about this topic elsewhere.

Thanks to [CMYKat](https://cmykatgraphics.carrd.co/) for the awesome [stickers](https://bunnypa.ws/search/1/pack%3ASoatokDhole).

## Contents

* [Database Cryptography?](#database-cryptography)
* [Cryptography for Relational Databases](#relational-databases)
  + [The Perils of Built-in Encryption Functions](#relational-built-in)
  + [Application-Layer Relational Database Cryptography](#relational-app-layer)
    - [Confused Deputies](#confused-deputies)
    - [Canonicalization Attacks](#canonicalization-attacks)
    - [Multi-Tenancy](#multi-tenancy)
* [Cryptography for NoSQL Databases](#cryptography-for-nosql-databases)
  + [NoSQL is Built Different](#nosql-built-different)
  + [Record Authentication](#record-authentication)
    - [Bonus: A Maximally Schema-Free, Upgradeable Authentication Design](#record-auth-bonus)
* [Searchable Encryption](#searchable-encryption)
  + [Order-{Preserving, Revealing} Encryption](#ope-ore)
  + [Deterministic Encryption](#deterministic-encryption)
  + [Homomorphic Encryption](#homomorphic-encryption)
  + [Searchable Symmetric Encryption (SSE)](#sse)
  + [You Can Have Little a HMAC, As a Treat](#hmac-indexing)
* [Intermission](#intermission)
* [Case Study: MongoDB Client-Side Encryption](#mongodb-client-side-encryption)
  + [MongoCrypt: The Good](#mongocrypt-good)
    - [How is Queryable Encryption Implemented?](#queryable-encryption)
  + [MongoCrypt: The Bad](#mongocrypt-bad)
  + [MongoCrypt: The Ugly](#mongocrypt-ugly)
* [Wrapping Up](#wrapping-up)

## Database Cryptography?

The premise of database cryptography is deceptively simple: You have a database, of some sort, and you want to store sensitive data in said database.

The consequences of this simple premise are anything but simple. Let me explain.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/02/Soatok-ScruffKerfluff.png?resize=768%2C614&ssl=1)

Art: [ScruffKerfluff](https://scruffkerfluff.carrd.co/)

The sensitive data you want to store may need to remain confidential, or you may need to provide some sort of integrity guarantees throughout your entire system, or sometimes both. Sometimes all of your data is sensitive, sometimes only some of it is. Sometimes the confidentiality requirements of your data extends to where within a dataset the record you want actually lives. Sometimes that’s true of some data, but not others, so your cryptography has to be flexible to support multiple types of workloads.

Other times, you just want your disks encrypted at rest so if they grow legs and walk out of the data center, the data cannot be comprehended by an attacker. And you can’t be bothered to work on this problem any deeper. This is usually what compliance requirements cover. Boxes get checked, executives feel safer about their operation, and the whole time nobody has really analyzed the risks they’re facing.

But we’re not settling for mere compliance on this blog. Furries have standards, after all.

![Soatok is _TOTALLY_ innocent](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-innocent.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

So the first thing you need to do before diving into database cryptography is **threat modelling**. The first step in any good threat model is taking inventory; especially of assumptions, requirements, and desired outcomes. A few good starter questions:

1. What database software is being used? Is it up to date?
2. What data is being stored in which database software?
3. How are databases oriented in the network of the overall system?
   * Is your database properly firewalled from the public Internet?
4. How does data flow throughout the network, and when do these data flows intersect with the database?
   * Which applications talk to the database? What languages are they written in? Which APIs do they use?
5. How will cryptography secrets be managed?
   * Is there one key for everyone, one key per tenant, etc.?
   * How are keys rotated?
   * Do you use envelope encryption with an HSM, or vend the raw materials to your end devices?

The first two questions are paramount for deciding how to write software for database cryptography, before you even get to thinking about the cryptography itself.

(This is not a comprehensive set of questions to ask, either. A formal threat model is much deeper in the weeds.)

The kind of cryptography protocol you need for, say, storing encrypted CSV files an S3 bucket is vastly different from relational (SQL) databases, which in turn will be significantly different from schema-free (NoSQL) databases.

Furthermore, when you get to the point that you can start to think about the cryptography, you’ll often need to tackle confidentiality and integrity separately.

If that’s unclear, think of a scenario like, “I need to encrypt PII, but I also need to digitally sign the lab results so I know it wasn’t tampered with at rest.”

My point is, right off the bat, we’ve got a three-dimensional matrix of complexity to contend with:

1. On one axis, we have the type of database.
   * Flat-file
   * Relational
   * Schema-free
2. On another, we have the basic confidentiality requirements of the data.
   * Field encryption
   * Row encryption
   * Column encryption
   * Unstructured record encryption
   * Encrypting entire collections of records
3. Finally, we have the ...
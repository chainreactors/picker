---
title: Looting iOS App’s Cache.db
url: https://www.trustedsec.com/blog/looting-ios-apps-cache-db/
source: Instapaper: Unread
date: 2022-12-06
fetch_date: 2025-10-04T00:36:24.404010
---

# Looting iOS App’s Cache.db

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Looting iOS App's Cache.db](https://trustedsec.com/blog/looting-ios-apps-cache-db)

December 01, 2022

# Looting iOS App's Cache.db

Written by
Drew Kirkpatrick

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/LootingiOSCache.db_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695568358&s=9dd0aeb70ad001c30f0cf9143a5ab008)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#8ab5f9ffe8e0efe9feb7c9e2efe9e1afb8bae5fffeafb8bafee2e3f9afb8baebf8fee3e9e6efafb8baecf8e5e7afb8badef8fff9feefeed9efe9afb8bbacebe7fab1e8e5eef3b7c6e5e5fee3e4edafb8bae3c5d9afb8bacbfafaafb8bdf9afb8bac9ebe9e2efa4eee8afb9cbafb8bae2fefefaf9afb9cbafb8ccafb8ccfef8fff9feefeef9efe9a4e9e5e7afb8cce8e6e5edafb8cce6e5e5fee3e4eda7e3e5f9a7ebfafaf9a7e9ebe9e2efa7eee8 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flooting-ios-apps-cache-db "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Looting%20iOS%20App%27s%20Cache.db%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Flooting-ios-apps-cache-db "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flooting-ios-apps-cache-db&mini=true "Share on LinkedIn")

## Insecure By Default

Mobile application assessments diverge somewhat from normal web application assessments as there is an installed client application on a local device to go along with the backend server. Mobile applications can often work offline, and thus have a local store of data. This is commonly in the form of SQLite databases stored in the application's filesystem "sandbox".

As part of a mobile application assessment, TrustedSec reviews how data is stored and cached in these local files. Sensitive information should not be stored in cleartext in the local files of an application. Both Android and iOS provide secure methods of storing sensitive data, by using the Android Keystore and the iOS Keychain.

These secure storage tools are perfect for storing session tokens, cookies, passwords, and encryption keys. While you may not wish to store a large amount of data in the Keychain or Keystore, you can easily encrypt a SQLite database using tools such as [SQLCipher](https://www.zetetic.net/sqlcipher) and keep the encryption key in the Keychain or Keystore.

You would think that such tools would lead to an abundance of encrypted databases in mobile application development. Unfortunately, we very rarely see SQLite databases encrypted in the local file store.

![](https://www.trustedsec.com/wp-content/uploads/2022/11/sadBaby.png)

But application developers are not the only ones to blame here. iOS provides a URL loading system to make application development easier. The *NSURLSession* classes help developers to get communication between their application and the back-end server up and running.

By default, this library will cache network traffic, in the application's local files, in an **unencrypted** file called *Cache.db*. This is a SQLite database we see on nearly all iOS application assessments.

![](https://www.trustedsec.com/wp-content/uploads/2022/11/goWrong.gif)

Fig.2 - How bad could it be?

So what do we find in *Cache.db*? More than 90% of the time, we find session cookies and tokens. That's not great as this information can lead to account compromise. We also find data contained in server responses cached in this database, potentially disclosing that information as well.

And fairly often, we'll find the full **cleartext credentials** for the user.

![](https://www.trustedsec.com/wp-content/uploads/2022/11/creds.png)

Fig.3 - That's some tasty loot

Before we cover how you would recover this information from the *Cache.db* file, I want to cover how an attacker might get their hands on this file. iOS and updated Android devices both provide strong security controls. Files such as *Cache.db* are stored in the application's sandbox, making access to these files challenging for attackers.

The most obvious attack path to acquire the local data is to gain access to the unlocked device, which is not an easy task.

A more likely avenue to access these files is from a device backup. Specifically for an iOS device, this could be through compromising an iCloud account, or gaining access to the desktop computer that contains a local backup of the device. Application developers have to specifically disable backups of their applications or data. I frequently retrieve *Cache.db* files from an iOS backup.

![](https://www.trustedsec.com/wp-content/uploads/2022/11/backup.png)

Fig.4 - Making iPhone b...
---
title: Dropping some TLS laggards
url: https://daniel.haxx.se/blog/2025/06/11/dropping-some-tls-laggards/
source: daniel.haxx.se
date: 2025-06-12
fetch_date: 2025-10-06T22:53:50.647882
---

# Dropping some TLS laggards

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/08/snail-4291296_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Security](https://daniel.haxx.se/blog/category/tech/security/)

# Dropping some TLS laggards

[June 11, 2025](https://daniel.haxx.se/blog/2025/06/11/dropping-some-tls-laggards/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2025/06/11/dropping-some-tls-laggards/#comments)

In the [curl](https://curl.se/) project we have a long tradition of supporting a range of different third party libraries that provide similar functionality. The person who builds curl needs to decide which of the *backends* they want to use out of the provided alternatives. For example when selecting which TLS library to use.

This is a fundamental and appreciated design principle of curl. It allows different users to make different choices and priorities depending on their use cases.

Up until May 2025, curl has supported **thirteen** different TLS libraries. They differ in features, footprint, speed and licenses.

## Raising the bar

We implicitly tell the user that you can use one of the libraries from this list to get good curl functionality. The libraries we support have met our approval. They passed the tests. They are okay.

As we support a large number of them, we can raise the bar and gradually increase the requirements we set for them to remain approved. For the good of our users. To make sure that the ones we support truly are good quality choices to build upon – ideally for years to come.

## TLS 1.3

The latest TLS version is called TLS 1.3 and the corresponding [RFC 8443](https://datatracker.ietf.org/doc/html/rfc8446) was published in August 2018, almost seven years ago. While there are no known major problems or security issues with the predecessor version 1.2, a modern TLS library that has not yet implemented and provide support for TLS 1.3 is a *laggard*. It is behind.

We take this opportunity to raise the bar and say that **starting June 2025, curl only supports TLS libraries that supports TLS 1.3** (in their modern versions). The first curl release shipping with this change is the pending 8.15.0 release, scheduled for mid July 2025.

This move has been announced, planned and repeatedly communicated for over a year. It should not come as a surprise, even if I have no doubt that this will be considered a such by some.

This makes sure that users and applications that decide to lean on curl are more future-proof. We no longer recommend using one of the laggards.

## Removed

This action affects these two specific TLS backends:

* BearSSL
* Secure Transport

## BearSSL

This embedded and small footprint focused library is probably best replaced by wolfSSL or mbedTLS.

## Secure Transport

This is a native library in Apple operating systems that has been deprecated by Apple themselves for a long time. There is no obvious native replacement for this, but we probably recommend either wolfSSL or an OpenSSL fork. Apple themselves have used libreSSL for their curl builds for a long time.

The main feature user might miss from Secure Transport that is not yet provided by any other backend, is the ability to use the native CA store on the Apple operating systems – iOS, macOS etc. We expect this feature to get implemented for other TLS backends soon.

## Network framework

On Apple operating systems, there is a successor to Secure Transport: the *Network framework*. This is however much more than just a TLS layer and because of their design decisions and API architecture it is totally unsuitable for curl’s purposes. It does not expose/use sockets properly and the only way to use it would be to hand over things like connecting, name resolving and parts of the protocol management to it, which is totally unacceptable and would be a recipe for disaster. It is therefore highly unlikely that curl will again have support for a *native* TLS library on Apple operating systems.

## Eleven remaining TLS backends in curl

In the order we added them.

1. OpenSSL
2. GnuTLS
3. wolfSSL
4. SChannel
5. libressl – an OpenSSL fork
6. BoringSSL – an OpenSSL fork
7. mbedTLS
8. AmiSSL – an OpenSSL fork
9. rustls
10. quictls – an OpenSSL fork
11. AWS-LC – an OpenSSL fork

## Eight removed TLS backends

With these two new removals, the set of TLS libraries we have removed support for over the years are, in the order we removed them:

1. QsoSSL
2. axTLS
3. PolarSSL
4. MesaLink
5. NSS
6. gskit
7. BearSSL
8. Secure Transport

## Going forward

Currently we have no plans for removing support for any other TLS backends, but we will of course reserve ourselves the right to do so when we feel the need, for the good of the project and our users.

We similarly have no plans to add support for any additional TLS libraries, but if someone would bring such work to the project for one of the few remaining quality TLS libraries that exist that curl does not already support, then we would most probably welcome such an effort.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[SecureTransport](https://daniel.haxx.se/blog/tag/securetransport/)[TLS](https://daniel.haxx.se/blog/tag/tls/)

# Post navigation

[Previous PostWhat we can’t measure](https://daniel.haxx.se/blog/2025/06/05/what-we-cant-measure/)[Next PostA family of forks](https://daniel.haxx.se/blog/2025/06/23/a-family-of-forks/)

## One thought on “Dropping some TLS laggards”

1. ![](https://secure.gravatar.com/avatar/fe981c24fa40ca343d9d03acd24495ab2cfc735cb44083b442babff88e2ea292?s=34&d=monsterid&r=g) **Clyde** says:

   [June 16, 2025 at 06:55](https://daniel.haxx.se/blog/2025/06/11/dropping-some-tls-laggards/#comment-27196)

   Glad to see AmiSSL, which is used by Commodore Amiga machines, is still on the list.
   Keep up the great work, cURL team!

Comments are closed.

# Recent Posts

* [How I maintain release notes for curl](https://daniel.haxx.se/blog/2025/10/01/how-i-maintain-release-notes-for-curl/)
  October 1, 2025
* [CRA compliant curl](https://daniel.haxx.se/blog/2025/09/22/cra-compliant-curl/)
  September 22, 2025
* [Bye bye Kerberos FTP](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/)
  September 19, 2025
* [From suspicion to published curl CVE](https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/)
  September 18, 2025
* [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/)
  September 13, 2025
* [curl 8.16.0](https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/)
  September 10, 2025

# Recent Comments

* F.Nagy on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27323)
* Fredrik on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27322)
* [Fazal Majid](https://majid.info/) on [preparing for the worst](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/comment-page-1/#comment-27321)
* Nikhil on [About](https://daniel.haxx.se/blog/about/comment-page-1/#comment-27320)
* A. Ros on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27318)
* [Daniel Stenberg](https://daniel.haxx.se/) on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27317)
* Yoann Ricordel on [HTTP is not simple](https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/comment-page-1/#comment-27316)
* Ond?ej Surý on [Hello Sprout](https://d...
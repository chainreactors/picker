---
title: Secure Transport support in curl is on its way out
url: https://daniel.haxx.se/blog/2025/01/14/secure-transport-support-in-curl-is-on-its-way-out/
source: daniel.haxx.se
date: 2025-01-15
fetch_date: 2025-10-06T20:10:24.144577
---

# Secure Transport support in curl is on its way out

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2021/06/trimming-hedge.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Security](https://daniel.haxx.se/blog/category/tech/security/)

# Secure Transport support in curl is on its way out

[January 14, 2025](https://daniel.haxx.se/blog/2025/01/14/secure-transport-support-in-curl-is-on-its-way-out/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [4 Comments](https://daniel.haxx.se/blog/2025/01/14/secure-transport-support-in-curl-is-on-its-way-out/#comments)

In May 2024 we finally decided that maybe the time has come for curl to drop support of older TLS libraries. Libraries that because they don’t support the modern TLS version (1.3) for many users are maybe not suitable to build upon for the future. We gave the world 12 months to adapt or to object. More than half of that time has passed.

This means that after May 2025, we intend to drop support for Secure Transport and BearSSL unless something changes drastically that makes us reconsider.

This blog post is an attempt to make everyone a little more aware and make sure that those who need to, prepare appropriately.

## Secure Transport

Secure Transport is a quite a horrible name, but it is still the name of a TLS library written by Apple, shipped as a component for macOS and all the different flavors of iOS. It has been supported by curl since 2012 but as of a few years back it is considered deprecated and “legacy” by Apple themselves. Secure Transport only supports TLS up to but not later than 1.2.

Once upon the time Apple shipped curl built against Secure Transport with macOS but they switched over to LibreSSL several years ago.

I hear two primary reasons mentioned why people still like using libcurl/Secure Transport on iOS:

1. It saves them from having to use and bundle a separate third party library that also adds to the footprint.
2. It gives them easy and convenient use of the iOS certificate store instead of having to manage a separate one..

## Network Framework

Continuing on their weird naming trajectory, the thing that Apple recommends the world to use instead of Secure Transport is called *Network Framework*.

Due to completely new paradigms and a (to me at least) funny way to design their API, it is far from straight-forward to write a backend for curl that uses the Network Framework for TLS. We have not even seen anyone try. Apple themselves certainly seem to be fine to simply not use their own TLS for their curl builds.

I am not sure it is even sensible to try to use the Network Framework in curl.

## Options

Without Secure Transport and no prospect of seeing Network Framework support, users of libcurl on macOS and iOS flavors need to decide on what to do next.

I can imagine that there are a few different alternatives to select from.

1. *Stick to an old libcurl.* At first an easy and convenient choice, but it will soon turn out to be a narrow path with potential security implications going forward.
2. *Maintain a custom patch*. The TLS backends are fairly independent so this is probably not an impossible task, but still quite a lot of work that also takes a certain amount of skill.
3. *Switch off from libcurl*. Assuming you find an alternative that offers similar features, stability, portability, speed and that supports the native cert storage fine. Could mean quite some work.
4. *Use libcurl with another TLS library*. This is then by itself two sub-categories. A) The easiest route is to accept that you need to maintain a separate CA store and then you can do this immediately and you can use a TLS library that supports the latest standards and that is well supported. B) Use a TLS library that supports use of the native iOS cert store. I believe maybe right now wolfSSL is the only one that does this out of the box, but there is also the option to pay someone or write the code to add such features to another curl TLS backend.
5. Some other approach

## Post removal

After this removed support of two libraries from curl, there is still support for *ten* different TLS libraries. There should be an adequate choice for everyone – and there is nothing stopping us from adding support for future newcomers on the scene.

## Protests are listened to

Part of [the deprecation process](https://curl.se/dev/deprecate.html) in curl is that we listen to what possible objections people might have in the time leading up to the actual future date when the code is cut out. Given a proper motivation a deprecation decision *can* be canceled or at least postponed.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[SecureTransport](https://daniel.haxx.se/blog/tag/securetransport/)[TLS](https://daniel.haxx.se/blog/tag/tls/)

# Post navigation

[Previous Postcurl with partial files](https://daniel.haxx.se/blog/2024/12/30/curl-with-partial-files/)[Next PostPresentation: curl from start to end](https://daniel.haxx.se/blog/2025/01/16/presentation-curl-from-start-to-end/)

## 4 thoughts on “Secure Transport support in curl is on its way out”

1. ![](https://secure.gravatar.com/avatar/764ffc9df8608ac137ed7a4904212d1af926bdd95591dfbda3d037a7c4c6a5ce?s=34&d=monsterid&r=g) **Timothy (TRiG)** says:

   [January 15, 2025 at 16:48](https://daniel.haxx.se/blog/2025/01/14/secure-transport-support-in-curl-is-on-its-way-out/#comment-27097)

   Why is BearSSL going?

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [January 16, 2025 at 00:51](https://daniel.haxx.se/blog/2025/01/14/secure-transport-support-in-curl-is-on-its-way-out/#comment-27098)

      @Timothy: same reason. No TLS 1.3 support. And really no development activity otherwise either.
2. ![](https://secure.gravatar.com/avatar/011b26083fc7b622c71eba7da55b05c7e61650ada61526492b691ec28d777905?s=34&d=monsterid&r=g) **Antwan** says:

   [January 17, 2025 at 13:15](https://daniel.haxx.se/blog/2025/01/14/secure-transport-support-in-curl-is-on-its-way-out/#comment-27102)

   Without having looked into the technical details (honestly never touched Network.framework during my time), is not supporting it simply a lack of someone providing such patches / support or just technically problematic?

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [January 17, 2025 at 14:00](https://daniel.haxx.se/blog/2025/01/14/secure-transport-support-in-curl-is-on-its-way-out/#comment-27103)

      @Antwan: curl is just code, I’m convinced it is possible. All I am saying is that “it is far from straight-forward”. It does not mean impossible.

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

* F.Nagy on [Developer of the year...
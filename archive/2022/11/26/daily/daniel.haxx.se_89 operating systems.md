---
title: 89 operating systems
url: https://daniel.haxx.se/blog/2022/11/25/89-operating-systems/
source: daniel.haxx.se
date: 2022-11-26
fetch_date: 2025-10-03T23:49:39.472622
---

# 89 operating systems

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202215.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# 89 operating systems

[November 25, 2022](https://daniel.haxx.se/blog/2022/11/25/89-operating-systems/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [13 Comments](https://daniel.haxx.se/blog/2022/11/25/89-operating-systems/#comments)

I occasionally do talks about curl. In these talks I often include a few slides that say something abut curl’s coverage and presence on different platforms. Mostly to boast of course, but also to help explain to the audience how curl has manged to reach its ten billion installations.

This is current incarnation of those seven slides in November 2022. I am of course also eager to get your feedback on the specific contents, especially if you miss details in them, that I should add so that my future curl presentations include more accurate data.

## curl runs in all your devices

curl is used in (almost) every Internet-connected device out there, and I try to visualize that with this packed slide. Cars, servers, game consoles, medical devices, games, apps, operating systems, watches, robots, TVs, speakers, light-bulbs, freezers, printers, motorcycles, music instruments and more.

The intent being to show with images that it runs in quite a few devices.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202212.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202212.jpg)

## 28 transfer protocols

More strictly speaking these are the 28 URL schemes curl supports right now, including in experimental builds. The image tries to put them in a sort of hierarchical way so that you can see what underlying protocol that is used for them: TCP, SSH, TLS, QUIC etc.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202213.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202213.jpg)

## 60 bindings

Volunteers have created and maintain libcurl bindings for at least these 60 different environments, making it possible for developers to access and use libcurl powers from virtually every programming language you can think of.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202214.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202214.jpg)

## 37 third party dependencies

curl’s modular design and ability letting the developer who builds curl to mix and match features and what particular third party dependencies to use, makes it possible to craft exactly the curl builds you want. Device manufacturers get the combination they like for exactly their purposes and needs.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-2022.png)](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-2022.png)

## 89 operating systems

This list has been worked on and bounced around several times between friends and it always brings out a few questions and people like to argue with me about a few entries I include and about a few entries I do not include. The problem is both that there is not a clear defining line between the definition of an operating systems and a distribution or a different running environment and sometimes it is just branding differences separating X from Y. With a “flexible” attitude to the definition of operating systems, this is the current collection of no less than 89 individual ones on which curl runs or *has run* on:

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202215.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202215.jpg)

## 24 CPU architectures

Older versions of this slide used to have x86-64 as a separate one, but I think we have concluded that a large amount of the architectures have separate 64 bit versions so if I were to keep x86-64 I should also include a lot of other 64 bit versions so I removed the x86-64 from the slide. Maybe I should rather go the other way and add all the 64 bit version as separate architectures?

Anyway, curl has been made to run on virtually all modern or semi-modern 32 bit or larger CPU architectures we can find:

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202216.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202216.jpg)

## 2 planets

I admit it. I include this slide in my presentation and in this blog post because it feels like the ultimate show-off. curl was used in [the mars 2020 helicopter mission](https://daniel.haxx.se/blog/2021/04/19/mars-2020-helicopter-contributor/).

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202218.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/11/curl-Nov-202218.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous PostConsidering C99 for curl](https://daniel.haxx.se/blog/2022/11/17/considering-c99-for-curl/)[Next PostFaster base64 in curl](https://daniel.haxx.se/blog/2022/12/06/faster-base64-in-curl/)

## 13 thoughts on “89 operating systems”

1. ![](https://secure.gravatar.com/avatar/2e13cc254880100bd9d6f0b0777b65621944609bdb65fcd3328792a8a730655e?s=34&d=monsterid&r=g) **[Ploum](https://ploum.net)** says:

   [November 25, 2022 at 18:42](https://daniel.haxx.se/blog/2022/11/25/89-operating-systems/#comment-26493)

   29 ? How about adding Gemini:// as the 29th protocol? (should be quite easy)

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [November 26, 2022 at 00:21](https://daniel.haxx.se/blog/2022/11/25/89-operating-systems/#comment-26494)

      @Ploum: there was once a start made but [it was abandoned](https://github.com/curl/curl/pull/6261) and while you say it “should be easy” nobody seems to do/want it…
2. ![](https://secure.gravatar.com/avatar/fb98d44ad7501a959f3f4f4a3f004fe2d9e581ea6207e218c4b02c08a4d75adf?s=34&d=monsterid&r=g) **Name** says:

   [November 26, 2022 at 19:40](https://daniel.haxx.se/blog/2022/11/25/89-operating-systems/#comment-26495)

   Native Linux build for Elbrus architecture (not publicly available) also seem to have it, in line with any other general purpose Linux desktop system.

   <http://mcst.ru/elbrus_linux>
   Fourth tab has the link to the lists of packages, and curl is one of them:
   <https://yadi.sk/d/ZASlXqAM84O1lw>

   ALT Linux have also had it in e2k ports for quite some time:
   <https://packages.altlinux.org/en/search?branch=sisyphus_e2k&name=curl>

   So you can add Elbrus as 25th architecture.
3. ![](https://secure.gravatar.com/avatar/795075b352585035bbb3f0c29809bc3192b8ac4141e98adb30b68cd67fb737d5?s=34&d=monsterid&r=g) **john** says:

   [November 28, 2022 at 10:52](https://daniel.haxx.se/blog/2022/11/25/89-operating-systems/#comment-26496)

   I was just thinking to myself:

   “I bet you know that some of this ‘Operating Systems’ are not actually operating systems, but kernels (e.g.: Hurd, Linux)… but why are there on an operating system’s list then? i wonder…”

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [November 28, 2022 at 13:03](https://daniel.haxx.se/blog/2022/11/25/89-operating-systems/#comment-26497)

      @john: you did not only think this to yourself, you also wrote it here….

      Let’s say that “operating systems” is in this context ...
---
title: What we can’t measure
url: https://daniel.haxx.se/blog/2025/06/05/what-we-cant-measure/
source: daniel.haxx.se
date: 2025-06-06
fetch_date: 2025-10-06T22:52:47.733914
---

# What we can’t measure

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/06/sunset-ocean.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# What we can’t measure

[June 5, 2025](https://daniel.haxx.se/blog/2025/06/05/what-we-cant-measure/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

The curl project is an independent Open Source project. Our ambition is to do internet transfers *right* and *securely* with the features “people” want. **But how do we know if we do this successfully or not?**

Possibly one rough way to measure if users are happy would be to know if the number of users go up or down.

*How do we know?*

## Number of users

We don’t actually know how many users we have – which devices, tools and services that are powered by our code. We don’t know how many users install curl. We also don’t know how many install it and then immediately uninstall it again because there is something about it they don’t like.

Most of our users install curl and libcurl from a distribution, unless they already had it installed there from the beginning without them having to do anything. They don’t download anything from us. Most users likely never visit our website for any purpose.

## No telemetry nor logs

We cannot do and will never try to do any kind of telemetry in the command line tool or library, so there is no automated way we can actually know how much any of them are used unless we are told explicitly.

We can search the web, guess and ask around.

## Tarball downloads

We can estimate how many people download the curl release tarballs from the website every month, but that is a nearly useless number without meaning. What does over a million downloads per month mean in this context? Presumably a fair share of these are just repeated CI jobs.

A single download of a curl tarball be used to build curl for a long time, for countless products and get installed in several billions of devices or never get used anywhere. Or somewhere in between. We will never know.

## GitHub

Our GitHub repository has a certain amount of stars. This number does not mean anything as just a random subset of developers ever see it, and just some of those decide to do the rather meaningless act of staring it. The git repository has been forked on GitHub several thousand times but that’s an almost equally pointless number.

We can get stats for how often our source code git repository is cloned, but then again that number probably gets heavily skewed as CI use of it goes up and down.

## Binary downloads

We offer curl for Windows binaries but since we run a website entirely without logs, those downloads are bundled with the tarballs in our rough stats. We only know how many *objects* in the 1M-10M size range are downloaded over a period of time. Besides, Windows ships with curl bundled so most Windows users never download anything from us.

We provide curl containers and since they are hosted by others, we can get some “pull” numbers. They mostly tell us people use the containers – but growing and shrinking trends don’t help us much as we don’t know who or why.

## Ecosystems

Because how libcurl is a fairly low-level C library, it is usually left outside of all *ecosystems*. With most infrastructure tooling for listing, counting and tracking dependencies etc, libcurl is simply left out and invisible. As if it is not actually used. Presumably just assumed to be part of the operating system or something.

These tools are typically done for Python, Node, Java, Rust, Perl, etc ecosystems where dependencies are easy to track via their package systems. Therefore, we cannot easily check how many projects or products that depend on libcurl with these tools. Because that number would be strangely low.

## Users

I try to avoid talking about *number of users* because for curl and libcurl I can’t really tell what a user is. curl is used directly by users, sure, but it is also used in countless scripts that run without a user directly running it.

libcurl is used many magnitudes more than the curl tool, and that is a component built-in into devices, tools and services that often operate independent of users being present.

## Installations

I tend to make my (wild) guesses on number of (lib)curl installations even though that is also highly error-prone.

I don’t know even nearly all the tools, games, devices and services that use libcurl because most of them never tell me or anyone else. They don’t have to. If we find out while searching the web or someone points us to a credit mention then we know. Otherwise we don’t.

I don’t know how many of those libcurl using applications exist in the world. New versions come, old versions die.

The largest volume libcurl users are most probably the mobile phones: libcurl is part of the operating systems in Apple’s iOS and in both Google’s and Samsung’s default Android setup. Probably in a few of the other popular Androids as well.

Since the libcurl API is not exposed by the mobile phone operating systems, a large amount of mobile phone applications subsequently build their own libcurl and ship with their apps, on both iOS and Android. This way, a single mobile phone can easily contain a dozen different libcurl installations, depending on exactly what set of apps that are used.

There is an estimated seven billion smart phones and one billion tablets in the world. Do they all have five applications on average that bundle libcurl? Who knows. If they do, that makes roughly eight billion times six installations.

## Also misleading

Staring on and focusing that outrageously large number is also complicated and may not be a particularly good indicator that we are on the right path. So ten *or perhaps forty-eight billion* libcurl installations are controlled and done by basically just a handful of applications and companies. Should some of them switch over to an alternative the number would dwindle immediately. And similarly if we get twice that amount of new users but on low volume installations (compared to smart phones everything is low volume), the total number of installations won’t really change, but we may have more satisfied users.

Maybe the best indicator of us keeping on the right track is the number of *different user*s or applications that are using libcurl and then we would count *Android*, *iOS* and *the mobile YouTube application* as three. Of course we have no means to even guess how many different users there are. That’s again also a very time-specific question as maybe there are a few new since yesterday and tomorrow a few existing users may ditch libcurl for something else.

We just don’t know and we can’t tell. With no expectations of this to change.

## Success

In many ways this is of course a success beyond our wildest dreams and a luxury position many projects only dream of. Don’t read this blog post as a *complaint* in any way. It just describes a challenge and reality.

## The old fashioned way

With no way to automatically or even half-decently guess how we are doing, we instead do it the old way. We rely on users to tell us what they think. We work on issues, we respond to questions and we do an annual survey. We try to be open for feedback and listen in how people and users want modern internet transfers done.

We make an effort to ship quality products and run a tight ship. To score top scores in all and every way you can evaluate a software project and our products.

Hopefully this will keep us on the right track. Let me know if you ever think we veer off.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-a...
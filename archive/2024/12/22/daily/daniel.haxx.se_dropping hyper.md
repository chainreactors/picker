---
title: dropping hyper
url: https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/
source: daniel.haxx.se
date: 2024-12-22
fetch_date: 2025-10-06T19:37:29.634653
---

# dropping hyper

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2020/09/auto-1661009_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# dropping hyper

[December 21, 2024](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [5 Comments](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/#comments)

The ride is coming to an end. The experiment is done. We tried, but we admit defeat.

Four years ago we started adding [support for an alternative HTTP backend in curl](https://daniel.haxx.se/blog/2020/10/09/rust-in-curl-with-hyper/). It would use a library written in rust, called [hyper](https://hyper.rs/). The idea was to introduce an alternative implementation of HTTP internals that you could make curl/libcurl use instead of the native implementation.

This new backend that used a library written in rust would enable users to run a product where a larger piece of the total code than otherwise would be written in a memory-safe language: rust. Memory-safety being all the rage these days.

The initial work was generously sponsored by [ISRG](https://www.abetterinternet.org/), the organization behind such excellent efforts such as Let’s Encrypt, which believes strongly in this concept. I cooperated intensely with Sean McArthur, the lead developer of hyper. We made it work.

We have shipped hyper support in curl labeled EXPERIMENTAL for several years by now, hoping to attract attention and trigger the experimental spirit in users out there. Seeing so many people seem to want more memory-safety, surely the users would come?

## 95% of the work is the easy part

I mean that we took it perhaps 95% of the way and *almost* the entire test suite ran identically independently of which backend we built curl to use. The final few percent would however turn out to be friction enough to now eventually make us admit defeat, give up and instead yank it all out again.

There simply were no users asking for it and there were almost no developers interested or knowledgeable enough to work on it. libcurl is written in C, hyper is written in rust and there is a C binding glue layer in between. It takes someone who is interested and good at both languages to dig in, understand the architectures, the challenges and the protocols to drive this all the way through.

But with no user demand, why do it?

It seems quite clear that rust users use hyper but few of them want to work on making it work for a C project like curl, and among existing curl users there is virtually no interest in hyper. The overlap in the Venn diagram of the two universes is not big enough.

With no expectation of seeing this work completed in the short to medium length term, the cost of keeping the hyper code is simply deemed too high. We gain code agility and reduce complexity by trimming this off.

## We improved

While the experiment itself is deemed a failure, I think we learned from it and improved curl in the process. We had to rethink and reassess several implementation details when we aligned HTTP behavior with hyper. libcurl parses and handles HTTP stricter now. Better.

I also believe that hyper benefited from this journey and gained experiences and input from us that led to improvements in their end and in their HTTP library. Which then by extension have benefited the hyper users.

When we started this, even rust itself was not ready and over this time rust has improved and it is today a better language and it is better prepared to offer something like this. For us or for other projects.

## Backends

With this *amputation* we are back to no separate HTTP/1 backends. We only provide the single native implementation.

I am not against revisiting the topic and the idea of providing alternative backends for HTTP/1 in the future, but I think we should proceed a little different next time. We also have a better internal architecture now to build on than what we had in 2020 when this attempt started.

## Less rust (for now?)

Before this step, we supported three different backends backed up by libraries written in rust. Now we are down to two: rustls (for TLS) and quiche (for QUIC and HTTP/3). Both of them are still marked experimental.

These two backends use better internal APIs in curl and are hooked into libcurl in a cleaner way that makes them easier to support and less of burden to maintain over time.

Of course nothing prevents us from adding support for more and other rust libraries in the future. libcurl is a protocol engine using a plethora of different backends for many different protocols and services hooked into its core. Virtually all of those backends *could* be provided by a rust library.

## Thanks

A big thank you go to Sean and all others who helped us take it as far as we did. You are great. Nothing of this should put any shade on you.

## When

The hyper backend code has been removed in git as of December 21. There will be no traces left of it in the curl 8.12.0 release coming in February 2025.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[hyper](https://daniel.haxx.se/blog/tag/hyper/)[rust](https://daniel.haxx.se/blog/tag/rust/)

# Post navigation

[Previous PostA twenty-five years old curl bug](https://daniel.haxx.se/blog/2024/12/12/a-twenty-five-years-old-curl-bug/)[Next Postcurl with partial files](https://daniel.haxx.se/blog/2024/12/30/curl-with-partial-files/)

## 5 thoughts on “dropping hyper”

1. ![](https://secure.gravatar.com/avatar/8a3cfec99cda5881db08a77744fcf14ac494068f8238b79cf5b04a4846e5490f?s=34&d=monsterid&r=g) **Vagelis** says:

   [December 28, 2024 at 05:28](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/#comment-27093)

   That’s a shame indeed.
   A big company should step up and push this forward.
   Anyway, thank you both for your efforts.
2. ![](https://secure.gravatar.com/avatar/6d42f7a3416656dabde9db3078e8b59499e5bdf2583baf4ac8500719ec288e5d?s=34&d=monsterid&r=g) **Filip** says:

   [December 28, 2024 at 16:46](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/#comment-27094)

   Damn, that’s a bummer. Thanks for trying ! I’m sure this is gonna be a helpful experience for both libcurl and hyper though
3. ![](https://secure.gravatar.com/avatar/d3a56809df2e52df710c5613d6823d60b36e1eb82cb5261095406393e08eaa0e?s=34&d=monsterid&r=g) **[Gavin Henry](https://antnetworks.com)** says:

   [January 16, 2025 at 13:32](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/#comment-27099)

   I’m interested in reading the code for this. Writing a book about C Rust at the moment for PragProg. Will take a look at how you did it.

   Love reading your post Daniel. Maybe we should talk about this on SE Radio? Would love to have you back – <https://se-radio.net/2022/03/episode-505-daniel-stenberg-on-25-years-with-curl/>

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [January 16, 2025 at 19:30](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/#comment-27100)

      @Gavin: you know how to reach me!

      1. ![](https://secure.gravatar.com/avatar/d3a56809df2e52df710c5613d6823d60b36e1eb82cb5261095406393e08eaa0e?s=34&d=monsterid&r=g) **[Gavin Henry](http://antnetworks.com)** says:

         [January 17, 2025 at 10:27](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/#comment-27101)

         Yep, will reach out for my April show!

Comments are closed.

# Recent Posts

* [How I maintain release notes for curl](https:...
---
title: chicken nuget
url: https://daniel.haxx.se/blog/2026/03/12/chicken-nuget/
source: daniel.haxx.se
date: 2026-03-12
fetch_date: 2026-03-13T04:06:04.899076
---

# chicken nuget

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2018/08/window-919333_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# chicken nuget

[March 12, 2026](https://daniel.haxx.se/blog/2026/03/12/chicken-nuget/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/03/12/chicken-nuget/#respond)

Background: [nuget.org](https://nuget.org/) is a Microsoft owned and run service that allows users to package software and upload it to nuget so that other users can download it. It is targeted for .Net developers but there is really no filter in what you can offer through their service.

Three years ago I [reported on how nuget](https://daniel.haxx.se/blog/2023/03/02/the-curl-nuget-story/) was hosting and providing ancient, outdated and insecure curl packages. Random people download a curl tarball, build curl and then upload it to nuget, and nuget then offers those curl builds to the world – forever.

To properly celebrate the three year anniversary of that blog post, I went back to [nuget.org](https://nuget.org/), entered *curl* into the search bar and took a look at the results.

I immediately found at least *seven* different packages where people were providing severely outdated curl versions. The most popular of those, [rmt\_curl](https://www.nuget.org/packages/rmt_curl), reports that it has been downloaded almost 100,000 times over the years and is still downloaded almost 1,000 times/week the last few weeks. *It is still happening*. The packages I reported three years ago are gone, but now there is a new set of equally bad ones. No lessons learned.

rmt\_curl claims to provide curl 7.51.0, a version we shipped in November 2016. Right now it has [64 known vulnerabilities](https://curl.se/docs/vuln-7.51.0.html) and we have done more than 9,000 documented bugfixes since then. No one in their right mind should ever download or use this version.

Conclusion: the state of nuget is just as sad now as it was three years ago and this triggered another *someone is wrong on the internet* moments for me. I felt I should do my duty and tell them. Again. Surely they will act this time! Surely they think of the security of their users?

## Trusting randos

The entire nuget concept is setup and destined to end up like this: random users on the internet put something together, upload it to nuget and then the rest of the world downloads and uses those things – trusting that whatever the description says is accurate and well-meaning. Maybe there are some additional security scans done in the background, but I don’t see how anyone can *know* that they don’t contain any backdoors, trojans or other nasty deliberate attacks.

And whatever has been uploaded once seems to then be offered in perpetuity.

## I reported this again

Like three years ago I listed a bunch of severely outdated curl packages in my report. nuget says I can email them a report, but that just sent me a bounce back saying they don’t accept email reports anymore. (Sigh, and yes I reported *that* as a separate issue.)

I was instead pointed over to the generic Microsoft security reporting page where there is not even any drop-down selection to use for “nuget” so I picked “.NET” instead when I submitted my report.

## “This is not a Microsoft problem”

Almost identically to three years ago, my report was closed within less than 48 hours. It’s not a nuget problem they say.

*Thank you again for submitting this report to the Microsoft Security Response Center (MSRC).*

*After careful investigation, this case has been assessed as not a vulnerability and does not meet Microsoft’s bar for immediate servicing. None of these packages are Microsoft owned, you will need to reach out directly to the owners to get patched versions published. Developers are responsible for removing their own packages or updating the dependencies.*

In other words: they don’t think it’s nuget’s responsibility to keep the packages they host, secure and safe for their users. I should instead report these things individually to every outdated package provider, who if they cared, would have removed or updated these packages many years ago already.

Also, that would imply a never-ending wack-a-mole game for me since people obviously keep doing this. I think I have better things to do in my life.

## Outdated efforts

In the cases I reported, the packages seem to be of the kind that once had the attention and energy by someone who kept them up-to-date with the curl releases for a while and then they stopped and since then the packages on nuget has just collected dust and gone stale.

Still, apparently users keep finding and downloading them, even if maybe not at terribly high numbers.

Thousands of fooled users per week is thousands too many.

## How to address

The uploading users are perfectly allowed to do this, legally, and nuget is perfectly allowed to host these packages as per the curl license.

I don’t have a definite answer to what exactly nuget should do to address this problem once and for all, but as long as they allow packages uploaded nine years ago to still get downloaded today, it seems they are asking for this. *They contribute and aid users getting tricked into downloading and using insecure software*, and they are indifferent to it.

A rare few applications that were uploaded nine years ago might actually still be okay but those are *extremely* rare exceptions.

## Conclusion

The last time I reported this nuget problem nothing happened on the issue until I tweeted about it. This time around, a well-known Microsoft developer (who shall remain nameless here) saw my [Mastodon post](https://mastodon.social/%40bagder/116160195073326855) about this topic when mirrored over to Bluesky and pushed for the case internally – but not even that helped.

The nuget management thinks this is okay.

If I were into puns I would probably call them *chicken nuget* for their unwillingness to fix this. Maybe just closing our eyes and pretending it doesn’t exist will just make it go away?

Absolutely no one should use nuget.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Microsoft](https://daniel.haxx.se/blog/tag/microsoft/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous Postcurl 8.19.0](https://daniel.haxx.se/blog/2026/03/11/curl-8-19-0/)

### Leave a Reply [Cancel reply](/blog/2026/03/12/chicken-nuget/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
3nine1one4

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [chicken nuget](https://daniel.haxx.se/blog/2026/03/12/chicken-nuget/)
  March 12, 2026
* [curl 8.19.0](https://daniel.haxx.se/blog/2026/03/11/curl-8-19-0/)
  March 11, 2026
* [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/)
  March 10, 2026
* [10K curl downloads per year](https://daniel.haxx.se/blog/2026/03/09/10k-curl-downloads-per-year/)
  March 9, 2026
* [curl up 2026](https://daniel.haxx.se/blog/2026/02/26/curl-up-2026/)
  February 26, 2026
* [curl security moves again](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/)
  February 25, 2026

# Recent Comments

* Matt on [Dependency tracking is hard](https://daniel.haxx.se/blog/2026/03/10/dependency-tracking-is-hard/comment-page-1/#comment-27415)
* Dmitry on [Dependency tracking is h...
---
title: The curl nuget story
url: https://daniel.haxx.se/blog/2023/03/02/the-curl-nuget-story/
source: daniel.haxx.se
date: 2023-03-03
fetch_date: 2025-10-04T08:32:16.996445
---

# The curl nuget story

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/03/stickers-2023.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# The curl nuget story

[March 2, 2023](https://daniel.haxx.se/blog/2023/03/02/the-curl-nuget-story/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [4 Comments](https://daniel.haxx.se/blog/2023/03/02/the-curl-nuget-story/#comments)

Recently there has been an interesting debate in the Open Source world where people have objected to being called “Suppliers” as in Supply Chain Security when you are but an Open Source developer offering your code to the world for free and at no cost *but also without any warranties*. That is not a supplier, that’s just a creator.

A supplier would have some form of relationship or contract with the users of your code.

Terminology is difficult and yet powerful but changing what words we use for certain things is an uphill fight. I suspect we will keep using the term supplier even when we are not under contract.

## Responsible suppliers

Over the last few years the Open Source ecosystem have gotten attention when serious security flaws have been found and exploited, like log4shell and similar. It has brought the discussions to a higher level and now we talk about SBOMs and what responsibility “suppliers” and users of software based products have.

Already back when I participated in the meeting with the [Cyber Safety Review Board](https://daniel.haxx.se/blog/2022/05/05/meeting-the-cyber-safety-review-board/) the Open Source people present stressed – in unison – that the security problems are *rarely* problems in the upstream Open Source projects:

**Most popular and widely used Open Source projects fix our security problem really fast**, in a responsibly manner and provide information and fixes within a time period few proprietary software vendors match.

The issue is rather that the fixed versions are not being used. Things remain unpatched and running old, stale, versions because upgrading is hard and has a cost attached to it. Many stick to not upgrading their product and rather make the bet that whatever problem that practice might bring in the future, it is cheaper than doing upgrades. Capitalism.

## Intermediate “suppliers”

Then there are *intermediates*. There are suppliers of software that are sitting in-between the producer of the code and the end user of it. They are for example Linux Distribution. They package Open Source products and provide them to users in a convenient way for users to install what they select. They take the role of the supplier.

## Package manager responsibilities

Open Source software distribution depends on intermediates: package managers and curators. It would be highly impractical to try to use the universe of existing code without them.

This however puts a lot of power and responsibility in the hands of these package managers.

## Download sites 2.0

In the early days of the Internet software was often provided via “download sites”. Websites featuring basically a catalog of software to which they allowed anyone to upload software to, and everyone to download whatever software they wanted from.

Those systems ended up highly criticized because they were too easily used to spread viruses or other malware. Over time we have switched to “package managers” which (usually) work in slightly more intelligent manners with package verification and more.

But not all package managers are sane package managers. Some of them are just download sites under a different name. Intermediates who do not accept their responsibilities as software *suppliers*.

## Hello nuget

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/nuget.png)

“[NuGet](https://www.nuget.org/) is the package manager for .NET” is the exact quote from their website.

NuGet is run by Microsoft (which gives it an official sounding status and flare), but packages are built and provided by volunteers. It is unclear to me what kind of checks, if any, that are done on the packages before they are allowed to get distributed by nuget to end users. I looked through their docs but I found no mention of this.

In early March 2023, I went to the nuget site and I searched for “curl”. I got a match for what is a packaged curl version and detailed instructions of how to install it.

On this curl page, it links to the curl project page and the libcurl landing page. For a casual user it probably looks official enough. It also mentions how users have downloaded curl 137,000 times from there. 3,388 is said to have downloaded curl in the last six weeks – proving that this page still tricks people.

A more experienced curler might spot that it links to the old curl domain name (which we moved away from two plus years ago) and that the links use `http://` (not https), which we all collectively stopped doing many years ago.

**This curl version is almost ten years old.** curl 7.30.0 was released in April 2013.

By using this official-sounding package manager to install what sounds like an official package, you get a curl package from a decade ago.

At the moment of this writing, curl 7.30.0 has been reported to have [68 individual security problems](https://curl.se/docs/vuln-7.30.0.html). Problems that have all since been fixed in later versions.

## Report it? Sure, you would think so…

I reported this as an issue to NuGet on February 27 and asked them to remove this severely outdated package. Now that [Windows 10 and 11 ship curl](https://daniel.haxx.se/blog/2018/01/13/microsoft-curls-too/) bundled already, and the curl project offers fresh [official Windows builds](https://curl.se/windows/).

(I would not be able to personally provide an update or “take over” responsibility for this package.)

The Nuget team responded after just six hours:

> Thank you for contacting support for the NuGet.org website. We do not support individual NuGet packages. Please contact the package owner directly using the “Contact owners” link on the package details page.

(The response email was also riddled with references to Microsoft, there is no doubt this is an official service. )

I did not ask for *support* of this package, but okay, I proceeded and contacted the owner of this package via another form. I asked them to either remove the package from nuget or to upgrade it to a modern version as soon as possible. Apparently the nuget admins do not consider this to be a problem worth addressing.

The owner of the nuget curl package is called [coapp](https://www.nuget.org/profiles/coapp), and is responsible for a whole series of packages, most of them seem to be packaged in the same style. Their 57 packages have been download 1.8 million times and I could only spot one of them as updated after 2015. Most of them have not been touched since 2013. The curl package is just the one that triggered me. There are probably about 55 other packages that should be updated or removed as well.

Someone pointed out to me that coapp was also the name of some kind of Windows build tool/system, that according to [nuget’s own GitHub issue](https://github.com/NuGet/Home/issues/3594) was declared dead already in 2016. They sound related.

When coapp (the owner of the curl package) had not responded after 16 hours, I tried another approach: I could report this package as vulnerable to security problems. I mean, I know for sure it is vulnerable for 68 errors that are well explained (and I wrote every single one of the explanations). But it did not succeed either.

When I tried to report this as a security problem, I could either report a pr...
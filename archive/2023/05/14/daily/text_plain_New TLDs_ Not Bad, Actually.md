---
title: New TLDs: Not Bad, Actually
url: https://textslashplain.com/2023/05/13/new-tlds-not-bad-actually/
source: text/plain
date: 2023-05-14
fetch_date: 2025-10-04T11:38:23.068263
---

# New TLDs: Not Bad, Actually

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# New TLDs: Not Bad, Actually

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-05-132024-05-29](https://textslashplain.com/2023/05/13/new-tlds-not-bad-actually/)Posted in[security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[dns](https://textslashplain.com/tag/dns/), [security](https://textslashplain.com/tag/security/), [zip](https://textslashplain.com/tag/zip/)

The `Top Level Domain (TLD)` is the final label in a fully-qualified domain name:

![](https://textslashplain.com/wp-content/uploads/2023/05/image-2.png?w=765)

The most common TLD you’ll see is `com`, but you may be surprised to learn that there are [1479 registered TLDs](https://data.iana.org/TLD/tlds-alpha-by-domain.txt) today. This list can be subdivided into categories:

* **Generic TLDs ([gTLD](https://en.wikipedia.org/wiki/Generic_top-level_domain))** like `.com`
* **Country Code TLDs ([ccTLDs](https://en.wikipedia.org/wiki/Country_code_top-level_domain))** like `.uk`, each of which is controlled by specific countries
* **Sponsored TLDs ([sTLDs](https://en.wikipedia.org/wiki/Sponsored_top-level_domain))** like `.museum`, which are designed to represent a particular community
* … and a few [more esoteric types](https://en.wikipedia.org/wiki/Generic_top-level_domain#Types)

Some TLD owners will rent domain names under the TLD to any buyer (e.g. anyone can register a `.com` site), while others impose restrictions:

* a ccTLD might require that a registrant have citizenship or a business nexus within their country to get a TLD in their namespace; e.g. to get a `.ie` domain name, you have to [prove Irish citizenship](https://www.weare.ie/document-requirements/)
* a sTLD may require that the registrant meet some other criteria; e.g. to register within the `[.bank](https://www.register.bank/)` TLD, you must hold an active banking license and meet other criteria

## Zip and Mov

Recently, there’s been some *excitement* about the relatively-new .ZIP and .MOV top-level domains.

Why?

Because `.zip` and `.mov` are longstanding [file extensions](https://textslashplain.com/2023/04/05/file-types/) used to represent ZIP Archives and video files, respectively.

The argument goes that allowing `.zip` and `.mov` TLDs means that there’s now ambiguity: if a human or code encounters the string `"example.zip"`, is that just a file name, or a bare hostname?

Alert readers might immediately note: *“Hey, that’s also true of `.com`, the most popular TLD– [COM files](https://en.wikipedia.org/wiki/COM_file) have existed since the 1970s!*” That’s true, as far as it goes, but it is fair to say that `.com` files are rarely seen by users any more; on Windows, `.com` has mostly been supplanted by `.exe` except in some exotic situations. Thanks to the popularity of the TLD, most people hearing *dotcom* are going to think “website” not “application”.

(The super-geeks over on HackerNews [point out](https://news.ycombinator.com/item?id=35932216) that name collisions also exist for popular source code formats: `pl` is the extension for Perl Scripts and the ccTLD for Poland, `sh` is the extension for bash scripts and the ccTLD for St. Helena, and `rs` is the extension for Rust source code and the ccTLD for the Republic of Serbia.)

Okay, so what’s the badness that could result?

### Automatic Hyperlinking

In poking the Twitter community, the top threat that folks have identified is concern about **automatic hyperlinkers**: If a user types a filename string into an email, or their blog editor, or twitter, etc, it might be misinterpreted as a URL and automatically converted into one. Subsequently, readers might see the automatically-generated link, and click it under the belief that the author intended to include a URL, effectively an *endorsement*.

This isn’t a purely new concern– for instance, folks mentioning the `ASP.NET` platform encounter the automatic linking behavior all the time, but that is a fairly constrained scenario, and the `https://asp.net` website is owned by the developers of ASP.NET, so there’s no real harm.

However, what if I sent an email to my family saying, “*hey, check out VacationPhotos.zip*” with a ZIP file of that name attached to my email, but the email editor automatically turned `VacationPhotos.zip` into a link to `https://VacationPhotos.zip/`.

I concede that this is absolutely possible, however, it does not seem terribly exciting as an attack vector, and I remain unconvinced that normal humans type filename extensions in most forms of communication.

Having said that, I would agree that it *probably* makes sense to exclude `.mov` and `.zip` from automatic hyperlinkers. Many (if not most) such hyperlinkers do not automatically link any string that contains *every individual instance* of the 1479 current TLDs, and I don’t think introducing autolinking for these two should be a priority for them either.

[![](https://textslashplain.com/wp-content/uploads/2023/05/image-3.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/05/image-3.png)

Google’s Gmail automatically hyperlinks 534 TLDs.

(As an aside, if I was talking to an author of an automatic hyperlinker library, my *primary* concern would be the fact that almost all such libraries convert `example.com` into a non-secure reference to `http://example.com` instead of a secure `https://example.com` URL.)

### User Confusion

Another argument goes that URLs are already exceedingly confusing, and by introducing a popular file extension as a TLD, they might become more so.

I do not find this argument compelling.

URLs are already [incredibly subtle](https://www.usenix.org/conference/enigma2019/presentation/stark), and relying on users to mentally parse them correctly is a losing proposition in multiple dimensions.

There’s no requirement that a URL contain a filename at all. Even before the introduction of the `ZIP` TLD, it was already possible to include `.zip` in the Scheme, UserInfo, Hostname, Path, Filename, QueryString, and Fragment components of a URL. The fact that a fully-qualified hostname can now *end* with this string does not seem especially more interesting.

### Omnibox Search

When Google Chrome was first released, one of its innovations was collapsing the then-common two input controls at the top of web browsers (“Address” and “Search”) into a single control, the aptly-named **omnibox**. This UX paradigm, now copied by basically every browser, means that the omnibox must have code to decide whether a given string represents a URL, or a search request.

One of the inputs into that equation is whether the string contains a known TLD, such that `example.zi` and `example.zipp` are treated as search queries, while `example.zip` is assumed to mean `https://example.zip/` as seen here:

[![](https://textslashplain.com/wp-content/uploads/2023/05/image-4.png?w=760)](https://textslashplain.com/wp-content/uploads/2023/05/image-4.png)

If you’d like to signal your intent to perform a search, you can type a leading question mark to flip the omnibox into its explicit Search mode:

[![](https://textslashplain.com/wp-content/uploads/2023/05/image-5.png?w=762)](https://textslashplain.com/wp-content/uploads/2023/05/image-5.png)

If you’d like to explicitly indicate that you want a navigation rather than a search, you can do so by typing a leading prefix of `//` before the hostname.

As with other concerns, omnibox ambiguity is not a new issue: it exists for `.com, .rs, .sh, .pl` domains/extensions, for example. The omnibox logic is also challenged when the user is on an Intranet that has servers that are accessed via “dotless” (aka “plain”) hostnames like `https://payroll`, (leading to [a Group Policy control](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#gotointranetsiteforsinglewordentryin...
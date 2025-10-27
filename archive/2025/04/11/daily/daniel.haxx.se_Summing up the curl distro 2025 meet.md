---
title: Summing up the curl distro 2025 meet
url: https://daniel.haxx.se/blog/2025/04/10/summing-up-the-curl-distro-2025-meet/
source: daniel.haxx.se
date: 2025-04-11
fetch_date: 2025-10-06T22:04:57.576505
---

# Summing up the curl distro 2025 meet

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/03/curl-distro-meeting-2024.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Summing up the curl distro 2025 meet

[April 10, 2025](https://daniel.haxx.se/blog/2025/04/10/summing-up-the-curl-distro-2025-meet/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

On April 10 we ran the [curl distro meeting 2025](https://github.com/curl/curl/wiki/curl-distro-discussion-2025). A, by now, annual open meeting where maintainers from the curl project hang out with curl package maintainers for distros and other people who are interested. The mission is to improve curl for distros, and improve how the distros “do” curl.

Around ten people joined. There were representatives present from several different Linux distributions (Arch, Gentoo, Alpine and Debian) and a few curl maintainers.

We spent our two full hours talking and while we did not really follow the agenda, we managed to touch all the included subjects. Some of them of course more than others. (There is no recording and I do not mention names here – on purpose.)

A fair amount of time was spent on the topic of TLS libraries and the different statuses for them in curl, in particular in regards to QUIC/HTTP/3, ECH and Post Quantum.

This exact day ngtcp2 merged [their PR that adds support for the OpenSSL QUIC API](https://github.com/ngtcp2/ngtcp2/pull/1582) which opens up the ability to soon do HTTP/3 using OpenSSL in curl better than before and there was some excitement and interest expressed around this.

Viktor explained to the team how you can enable *unity builds* and *test bundles* that in some environments speed up build and test execution times significantly. They basically lump all the source code files into a single file and then compile that. Worth testing if that helps your build!

We talked about the success of the recently introduced release candidates. I have promised to come up with a tag/branch scheme for them to make it easier for everyone to see them, find them and access them directly in and with git.

Lots of regressions (well, four or five at least) were found in the 8.13.0 rc releases due to Debian’s excellent reverse-dependencies rerunning tests against the rc builds. It was also reported that Debian has started to run curl’s *Debug tests*, that are tests in the curl test suite that requires that it was built Debug enabled. Such builds have extra special code in certain places to alter internals in ways suitable for extra testing, but not suitable to remain in there in production. The curl test infra was recently improved so that we can now run *only* the Debug tests when wanted.

We discussed how the Debian maintainers found a regression in 8.13.0 that broke reproducible builds, but that this problem had not been detected by the curl project itself and not by anyone else either. Ideas were shared about what we can do to make it more likely that we catch a similar mistake the next time. This problem was an unstable sort in a script that changed the order based on the locale but most of us ran the verification using the same locale as the original was produced with…

We had quite some discussions around wcurl and the proposal to bundle the [wcurl](https://curl.se/wcurl/) script in future curl release tarballs with the final verdict that yes we will do so. This was the second action item for me from the meeting: work out how to best include wcurl in future releases in a good reproducible manner and write a PR for it.

[trurl](https://curl.se/trurl/) was mentioned briefly, but no one had a lot to say. It’s there. It works. It is probably not terribly widely used.

Appreciation was expressed for the way we manage [security advisories](https://curl.se/docs/security.html) and the information we provide in association with them. I mentioned how I recently improved the JSON output format we offer. We briefly touched the fact that we (curl) are now a CNA and I was asked to maybe write a blog post about how it has been and how it works. My third action item.

The [curl-distros mailing list](https://lists.haxx.se/listinfo/curl-distros) was setup as a direct result of last year’s meeting and it has proven to be an asset during the last year. Let’s keep using it and maybe even use it more! curl related issues and problems in one distro very often affects or spill over to other distros. Sharing details and lessons bout found and fixed regressions allows us to share the load and improve universally.

There is a [curl Google calendar](https://calendar.google.com/calendar/u/0?cid=Yzl1NWQ2NG9kb3A5anM1NW9sdGZhcmprNmdAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) that contains all curl release dates, as well as the feature freeze/window dates and now also all rc release dates. Using this, future dates for these events should never have to come as a surprise!

Everyone is invited to join [curl up 2025](https://daniel.haxx.se/blog/2025/03/29/curl-up-2025/)! We were also invited to [DebConf25](https://debconf25.debconf.org/).

(Any mistake in this summary is mine, all mine.)

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous PostWriting C for curl](https://daniel.haxx.se/blog/2025/04/07/writing-c-for-curl/)[Next PostHow the CNA thing is working out](https://daniel.haxx.se/blog/2025/04/24/how-the-cna-thing-is-working-out/)

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
* Ond?ej Surý on [Hello Sprout](https://daniel.haxx.se/blog/2025/07/28/hello-sprout/comment-page-1/#comment-27315)
* H. Stefan on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27314)
* Tjark on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27313)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.co...
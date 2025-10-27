---
title: Funded curl improvements
url: https://daniel.haxx.se/blog/2022/10/19/funded-curl-improvements/
source: daniel.haxx.se
date: 2022-10-20
fetch_date: 2025-10-03T20:23:35.665420
---

# Funded curl improvements

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2018/11/guy-jumping-cliff-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Funded curl improvements

[October 19, 2022](https://daniel.haxx.se/blog/2022/10/19/funded-curl-improvements/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

I am happy to announce that curl receives funding from [The Sovereign Tech Fund](https://sovereigntechfund.de/en). This funding is directed towards three specific projects that we have identified as interesting and worthwhile to push forward as ways to improve curl and the life of curl users.

This “investment” will fund two developers to work on curl over a period of six months: [Stefan Eissing](https://eissing.org/) and myself. The three projects are explained at some detail below. Of course everyone and anyone is welcome to join in and help out with these projects. Everything will be done in the open, as usual.

At the end of the period, we will produce some kind of report or summary of how things turned out.

The three projects we are getting funded have been especially created and crafted (by me) to be good solid projects that we really want to see done. This funding is different than many others we have gotten over the years in that we got to decide and plan what we wanted done. These are things that are meant to improve curl as a project and to generally make Internet transfers better and more powerful for a vast amount of users.

## Project 1 – known bugs cleanup

The curl project currently lists 120+ items as [known bugs](https://curl.se/docs/knownbugs.html) (up from 77 just two years ago).

The items in that list are reported problems that were recognized as problems at the time of their submission but as nobody worked on the issues at the time they were added to this list. The list includes everything from smaller irks up to big things that will either take a long time  to fix or be (almost) impossible to address.

There is a good chance that the list will be extended during the project period just because some new bugs fall into the description mentioned above.

This project is an effort to go through *as many as possible* to make sure they are correctly categorized/described and work on fixing the issues or whatever is necessary to get them off the list.

The process would entail an initial proper research round to extend the description and increase the understanding of each entry, followed by a rough assessment of the amount of work it would take to fix them. Possibly with a 1 (easy) to 5 (extreme) scale.

The action would then be to address the issues, possibly in an easy to hard order. Addressing the issues could be to fix the code to remove the issue, dismiss it as not actually intended to work or document it as not working or even moving it over to the TODO document if it is more of *a good idea for the future*.

The goal being to reduce the list to zero entries and thus polish off numerous *rough corners* and annoyances in the project.

This will be done by Daniel Stenberg over a period of 6 months.

## Project 2 – HTTP/3

Make HTTP/3 release-ready.

curl features experimental HTTP/3 and QUIC support already since a few years back, but there are several details still lacking:

* known bugs
* proper multiplexing: doing multiple transfers to the same host should be able to reuse an existing connection and multiplex over that, just as curl already does when using HTTP/2
* HTTP/3 support for the test suite (and CI jobs) need to be done for us to be able to consider the support *release ready*. Cooperation can be had with QUIC libraries such as ngtcp2 to consider where/how some of the testing is best performed.
* considerations for 0-RTT connection establishments (if anything needs to be done)
* support for early data: to send off the HTTP request to the server faster.
* connection migration:, a QUIC feature that allows a server to move over a live connection from one server to another without disruption
* fallback to h1/h2 if the QUIC connection fails. The failure rate for QUIC connections are still in the 3-7% rate generally, so having a good fallback mechanism or documented for how applications can go back to an older HTTP version instead, is important.
* HTTPS RR. This fairly new DNS resource record might contain information about the target server’s support for HTTP/3. If such a record is provided, curl can avoid superfluous round-trips to get the Alt-Svc header and rather connect directly to the HTTP/3 server.

All features and changes need to be documented. Functionality needs to be verified by test cases. Interop with real world servers is of course implied and assumed.

Stefan Eissing will spend 4 months on this project.

## Project 3 – HTTP/2 over proxy

curl has provided support for doing network transfers via HTTP proxies since decades, and this is a very commonly used feature and network setup.

curl however only supports using HTTP version 1 over proxies. This makes applications less effective as it sometimes leads to many more TCP connections being used than otherwise would be necessary if HTTP/2 could be used. In particular when applications behind a proxy operate against many different hosts on the other side of the proxy.

It can also be noted that in many enterprise setups, this kind of HTTP proxy is used for all kinds of network operations through the use of the CONNECT method, so this functionality is not limited to plain HTTP(S), it should work for all TCP based protocols libcurl supports and which already work over HTTP/1 proxies.

The project will require adding new options to enable this functionality, to both the library and the command line tool. With associated documentation.

It will require creating or extending the HTTP/2 support in the curl test suite so that this new functionality can be verified and proven to work at a satisfactory level.

Considerations must be taken so that this work does not close the door for future extending this to support HTTP/3 over proxy. Time permitting, work should be taken to pave the road for that or even perhaps gently start the work to support that as well.

Stefan Eissing will spend 2 months on this project.

## The outcome(s)

I hope and presume that the results of these projects will appear as a stream of pull-requests for curl that will be done and managed through-out the project period and not saved up to the end or anything. The review, test and merge process of these pull requests will follow our normal and standard project guidelines and procedures.

The projects are fully packed and (over) ambitious. There is a high risk that we will not be able to complete all the details for these projects within the time frame. But we will try.

Thanks Sovereign Tech Fund for this.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[funding](https://daniel.haxx.se/blog/tag/funding/)[WolfSSL](https://daniel.haxx.se/blog/tag/wolfssl/)

# Post navigation

[Previous PostDeviating from specs](https://daniel.haxx.se/blog/2022/10/18/deviating-from-specs/)[Next Postcurl 7.86.0 with WebSocket](https://daniel.haxx.se/blog/2022/10/26/7-86-0-with-websocket/)

# Recent Posts

* [How I maintain release notes for curl](https://daniel.haxx.se/blog/2025/10/01/how-i-maintain-release-notes-for-curl/)
  October 1, 2025
* [CRA compliant curl](https://daniel.haxx.se/blog/2025/09/22/cra-compliant-curl/)
  September 22, 2025
* [Bye bye Kerberos FTP](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/)
  September 19, 2025
* [From suspicion to published curl CVE]...
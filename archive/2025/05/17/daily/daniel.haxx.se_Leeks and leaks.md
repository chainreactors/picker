---
title: Leeks and leaks
url: https://daniel.haxx.se/blog/2025/05/16/leeks-and-leaks/
source: daniel.haxx.se
date: 2025-05-17
fetch_date: 2025-10-06T22:27:15.032225
---

# Leeks and leaks

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/05/onions.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Leeks and leaks

[May 16, 2025](https://daniel.haxx.se/blog/2025/05/16/leeks-and-leaks/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [4 Comments](https://daniel.haxx.se/blog/2025/05/16/leeks-and-leaks/#comments)

On the completely impossible situation of blocking the Tor `.onion` TLD to avoid leaks, but at the same time not block it to make users able to do what they want.

## dot-onion leaks

The onion TLD is a Tor specific domain that does not mean much to the world outside of Tor. If you try to resolve one of the domains in there with a *normal* resolver, you will get told that the domain does not exist.

If you ask your ISP’s resolver for such a hostname, you also advertise your intentions to speak with that domain to a sizeable portion of the Internet. DNS is inherently commonly insecure and has a habit of getting almost broadcast to lots of different actors. *A user on this IP address intends to interact with this .onion site.*

It is thus of utter importance for Tor users to never use the *normal* DNS system for resolving .onion names.

## Remedy: refuse them

To help preventing DNS leaks as mentioned above, Tor people engaged with the IETF and the cooperation ultimately ended up with the publication of [RFC 7686](https://datatracker.ietf.org/doc/html/rfc7686): *The “.onion” Special-Use Domain Name*. Published in 2015.

This document details how libraries and software should approach handling of this special domain. It basically says that software should to a large degree *refuse* to resolve such hostnames.

## curl

In [November 2015 we were made aware](https://github.com/curl/curl/issues/543) of the onion RFC and how it says we should filter these domains. At the time nobody seemed keen to work on this, and the problem was added to the [known bugs document](https://curl.se/docs/knownbugs.html).

Eight years later the issue was still lingering in that document and curl had still not done anything about it, when Matt Jolly emerged from the shadows and brought [a PR that finally implemented the filtering](https://github.com/curl/curl/pull/10705) the RFC says we should do. Merged into curl on March 30, 2023. Shipped in the curl 8.1.0 release that shipped in May 17, 2023. Two years ago.

Since that release, curl users would not accidentally leak their .onion use.

A curl user that uses Tor would *obviously* use a SOCKS proxy to access the Tor network like they always have and then curl would let the Tor server do the name resolving as that is the entity here that knows about Tor and the dot onion domain etc.

That’s the thing with using a proxy like this. A network client like curl can hand the full host name to the proxy server and let that do the resolving magic instead of it being done by the client. It avoids leaking names to local name resolvers.

## Controversy

It did not take long after curl started support the RFC that Tor themselves had pushed for, when Tor users with *creative* network setups realized and had opinions.

A [proposal appeared](https://github.com/curl/curl/pull/11236) to provide an override of the filter based on an environment variable for users who have a setup where the normal name resolver is already protected somehow and is known to be okay. Environment variables make for horrible APIs and the discussion did not end up in any particular consensus for other solutions so this suggestion did not make it through into code.

This issue has subsequently popped up a few more times when users have had some issues, but no fix or solution has been merged. curl remains blocking this domain. Usually people realize that when using the SOCKS proxy correctly, the domain name works as expected and that has then been the end of the discussions.

## oniux

This week the Tor project announced a new product of their: [oniux](https://blog.torproject.org/introducing-oniux-tor-isolation-using-linux-namespaces/): *a command-line utility providing Tor network isolation for third-party applications using Linux namespaces*.

On their introductory web page explaining this new tool they even show it off using a curl command line:

```
$ oniux curl http://2gzyxa5ihm7wid.onion/index.html
```

(I decided to shorten the hostname here for illustration purposes.)

Wait a second, isn’t that a .onion hostname in that URL? Now what does curl do with .onion host names since that release two years ago?

Correct: that illustrated command line only works with old curl versions from before we implemented support for RFC 7686. From before we tried to do in curl what Tor indirectly suggested we should do. So now, when we try to do the right thing, curl does not work with this new tool Tor themselves launched!

At least we can’t say we get do live a dull life.

## Hey this doesn’t work!

No really? Tell us all about it. Of course there was immediately [an issue submitted](https://github.com/curl/curl/issues/17363) against curl for this, quite rightfully. That tool was quite clearly made for a use case like this.

So how do we fix this?

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[dns](https://daniel.haxx.se/blog/tag/dns/)[IETF](https://daniel.haxx.se/blog/tag/ietf/)[Tor](https://daniel.haxx.se/blog/tag/tor/)

# Post navigation

[Previous PostDetecting malicious Unicode](https://daniel.haxx.se/blog/2025/05/16/detecting-malicious-unicode/)[Next PostThe curl user survey 2025 is up](https://daniel.haxx.se/blog/2025/05/19/the-curl-user-survey-2025-is-up/)

## 4 thoughts on “Leeks and leaks”

1. ![](https://secure.gravatar.com/avatar/6c490b0f1e56c66fe0fa3d9aa2c307972a866c163f89892ff69425c73d22bd98?s=34&d=monsterid&r=g) **sam** says:

   [May 16, 2025 at 22:32](https://daniel.haxx.se/blog/2025/05/16/leeks-and-leaks/#comment-27167)

   The big, stupid, hilarious hammer would be to teach curl about Tor and how to connect to onion services directly so that it never needs to rely on the environment or configuration. But people might not appreciate the performance impact if any random curl invocation could start building a new Tor circuit and then throw it away when it terminates!
2. ![](https://secure.gravatar.com/avatar/022db8e72ccc20b444ddd3a4bb90f0927c520f8a808c6dc0d70453a5671825d4?s=34&d=monsterid&r=g) **H. Stefan** says:

   [May 18, 2025 at 12:08](https://daniel.haxx.se/blog/2025/05/16/leeks-and-leaks/#comment-27171)

   Stuff like oniux isn’t really relevant, it is Linux kernel specific.

   The RFCs and TOR are to blame. Also there is no TOR-protocol RFC yet. RFC 6761 i.e. states »Caching DNS servers SHOULD recognize these names as special and SHOULD NOT, by default, attempt to look up NS records for them, or otherwise query authoritative DNS servers in an attempt to resolve these names.«

   While 7686 states dot-onion is special and applications that implement the TOR protocol should care. CURL supports proxies and socks, there is no need to care about dot-onion, since you don’t implement the TOR protocol, and you can’t RFC-wise. There is no need to care, except when one wants to make CURL TOR-aware by using a command-line switch like –block-dot-onion because one doesn’t wants CURL to leak, because a proxy or socks may be outside the control of the person operating CURL, which is considered bad opsec btw.

   If you operate any DNS, you certainly block dot-onion because you care about your users not requesting a dot-onion outside of an dot-onion rendezvous request, because the answer is always NXDOM...
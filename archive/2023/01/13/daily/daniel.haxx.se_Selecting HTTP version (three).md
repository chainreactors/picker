---
title: Selecting HTTP version (three)
url: https://daniel.haxx.se/blog/2023/01/12/selecting-http-version-three/
source: daniel.haxx.se
date: 2023-01-13
fetch_date: 2025-10-04T03:45:25.869424
---

# Selecting HTTP version (three)

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/01/h3h2-signpost.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Selecting HTTP version (three)

[January 12, 2023](https://daniel.haxx.se/blog/2023/01/12/selecting-http-version-three/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [8 Comments](https://daniel.haxx.se/blog/2023/01/12/selecting-http-version-three/#comments)

The latest HTTP version is called HTTP/3 and is being transferred over QUIC instead of the old classic TCP+TLS duo.

An attempt of an architectural drawing could look like this:

[![](https://daniel.haxx.se/blog/wp-content/uploads/2023/01/HTTP_3-October-2022.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2023/01/HTTP_3-October-2022.jpg)

HTTP network stacks

## Remember: experimental

HTTP/3 support in curl is still **experimental** so we do reserve the right to change names, behavior and functionality during development.

We aim to remove this experimental label from HTTP/3 support during the spring of 2023.

## HTTP/3 is for HTTPS only

Before we dig into the details of this, remember that HTTP/3 can and will only be used for `HTTPS://` URLs. It is always encrypted and there is no way to do HTTP/3 over clear text. Asking to do HTTP/3 with a `HTTP://` URL is therefor a non-starter. An error.

## Cannot upgrade a connection

When [HTTP/2 was introduced](https://daniel.haxx.se/blog/2015/05/15/rfc-7540-is-http2/) to the world, there was a companion TLS extension created called [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation) that allows a client to ask for HTTP/2 to be used. This is a very convenient and slick way for a client to mostly transparently upgrade from HTTP/1.1 to HTTP/2 *over the same connection*. No penalty or extra time wasted even.

With HTTP/3, the procedure cannot be done in the same easy way. As my fancy picture above shows, HTTP/3 requires a separate QUIC connection done to the host. A connection that uses HTTP/1 or HTTP/2 cannot be upgraded to HTTP/3. The client needs to make a separate, dedicated connection for HTTP/3.

(Since QUIC is done over UDP, HTTP/3 also uses a different port number space than the earlier HTTP versions.)

If the QUIC connection fails, it means there can be no HTTP/3 and then a client might instead select to try an older HTTP version over another connection.

## Alt-Svc

The original and official (according to the HTTP/3 RFC) way of bootstrapping a transfer into HTTP/3 is done like this:

A client makes a request using HTTP/1 or HTTP/2 to a server and in its response headers, the server indicates that it supports HTTP/3 by including an `Alt-Svc:` header with details on where and how to connect to the HTTP/3 server – and also for how long into the future this information is valid.

The client can then make its next HTTP operation against that server with HTTP/3 to the above mentioned host name and port number. So unless this info was already cached, a client needs an initial “upgrade” round-trip before it can use HTTP/3. Also, many clients/browsers will rather prefer to reuse the existing initial (HTTP/2 or HTTP/1-using) connection for subsequent requests rather than creating a new one since that might be faster.

Thus, the upgrading to HTTP/3 might not happen until some time has passed that allow the initial connection to close.

curl supports alt-svc and can upgrade to HTTP/3 using it.

## Alt-Svc replacement

There are some inherent problems with this header and server operators do not like it. A working group set out to fix its problems have rather suggested a new header, [alt-svcb](https://martinthomson.github.io/alt-svcb/draft-thomson-httpbis-alt-svcb.html), to replace it. This header looks simpler, partly because it is made to lean on another newcomer in the game: the HTTPS DNS records.

## HTTPS records

This is [a proposed new DNS record](https://www.ietf.org/archive/id/draft-ietf-dnsop-svcb-https-11.html) which can contain information about a server’s support for (among other things) HTTP/3, called `HTTPS`. Called a DNS RR, where RR is Resource Record. A field of information stored in DNS.

Yes, the name of this DNS record makes discussions a little confusing as HTTPS is otherwise generally a URL scheme or perhaps even a “protocol”.

A client can use DNS to figure out if and where it should try HTTP/3 or an older HTTP version when speaking to a particular host by using this HTTPS record. This is not yet an official standard and the RFC is not finalized, but there are servers out there deploying it already and there are clients/browsers taking advantage of it.

curl does not support HTTPS records yet, but we have a rough plan for [how to do it](https://github.com/curl/curl/wiki/HTTPS-record).

## Just try it

During curl’s several years of having offered experimental HTTP/3 support, we have provided an option for the user to ask it to use HTTP/3 directly against the host mentioned in the URL. Known as `--http3` for the command line tool.

Going forward, this option is going to remain an option to ask curl to speak HTTP/3 with the server in the URL but it will also allow curl to fallback to an earlier HTTP version in case of QUIC problems. See below for details on exactly how.

Starting now, we also introduce a new separate option to ask for exactly and only HTTP/3 without any fallback. We expect this to be less commonly used by users. This option for the command line is currently called `--http3-only`.

## Happy eyeballs everything!

We want users to be able to ask for HTTP/3 with a fallback to an earlier HTTP version if needed. The option should start as an opt-in but with the expectation that maybe in a future it can become a default.

Challenges involve:

1. A not insignificant share of QUIC attempts are blocked when the company/organization from which the attempt is made does not allow them.
2. Sometimes UDP is just slowed down (a lot)
3. HTTP/3 is still only deployed in a fraction of all servers

This is how we envision to do it:

1. Start an HTTP/3 attempt
2. If it has not connected successfully within N milliseconds, start an HTTP/2 attempt in parallel. (That can become an HTTP/1 transfer depending what the server supports.)
3. The first successful connect wins and the other one is discarded.

For each of these separate attempts, IPv6/IPv4 is also selected in the same kind of race against each other to pick the one that connects first. Potentially making up to four parallel connect attempts going on at the same time: QUIC-IPv6, QUIC-IPv4, TCP-IPv6 and TCP-IPv4!

I made a little drawing to visualize how the different connect attempts then might get initiated:

[![](https://daniel.haxx.se/blog/wp-content/uploads/2023/01/HTTP3-happy-eyeballs.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2023/01/HTTP3-happy-eyeballs.jpg)

*Multi-layered happy eyeballs*

## This is planned

I just want to be clear: this is what we plan to make work going forward. The code does not actually work like this just yet.

## Update

In a slightly longer plan, before this feature is removed from its experimental state, we will probably remove both `--http3` and `--http3-only` from the command line tool and instead create a more generic `--http-versions` options to maybe replace a lot of HTTP selection options. The exact functionality and syntax for this is yet to be worked out.

The underlying libcurl options might still remain as described in this blog post though.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[HTTP/3](https://daniel.haxx.se/blog/tag/http3/)[QU...
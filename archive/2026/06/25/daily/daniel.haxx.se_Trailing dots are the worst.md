---
title: Trailing dots are the worst
url: https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/
source: daniel.haxx.se
date: 2026-06-25
fetch_date: 2026-06-26T06:07:50.682757
---

# Trailing dots are the worst

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/04/trailing-dot.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Trailing dots are the worst

[June 25, 2026](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/#comments)

Trailing dots after hostnames in URLs remain my worst enemies. I wrote about [several problems with them in the past](https://daniel.haxx.se/blog/2022/05/12/a-tale-of-a-trailing-dot/) that involved those nasty things. They are still painful. When we shipped [curl 8.21.0](https://daniel.haxx.se/blog/2026/06/24/curl-8-21-0/) on June 24 2026 we fixed at least *three* brand new problems that involved trailing dots. C’mon, follow me down the trailing dot rabbit hole, episode two. I can just feel that there will be a third episode as well in a future…

## IPv4 numerical address

Let’s for a second imagine that you create a URL that uses a numerical IPv4 address. Not entirely uncommon. For example lots of people use 127.0.0.1 in local tests etc. Used everywhere since the dawn of time.

Now imagine that you add a trailing dot to this hostname, like “192.168.0.1.”. *What does the trailing dot even mean here?*

This particular trailing dot caused a problem in curl. To figure out if curl should allow wildcard certificates when connecting to a TLS server, it needs to know if the given hostname is a numerical IP or a hostname. The check uses `inet_pton()` on the provided hostname extracted from the URL – which incidentally *returns false* for an IPv4 address that ends with dot! So if it isn’t a numerical address it is a hostname and then we allow wildcards… **Argh.**

I decided to solve this particular problem like this: if the address is a valid IPv4 address and there is only a single dot afterwards, that dot is “swallowed” as part of the regular IPv4 normalization process that curl always does for IPv4 addresses when parsing URLs. This way, a numerical IPv4 address with a trailing dot will never be passed on to curl internals anymore. And the meaning of the trailing dot for this use case is clear: it is a mistake so we get rid of it. (This also seems to be what browsers do.) Shipping in curl 8.21.0.

This choice has already been reported problematic by at least one user who expected a transfer for a URL like this to return error… I suppose this means that the jury is still out on what the best approach for this trailing dot is.

## Double trailing dots HSTS

What could be more fun than trailing dots if not two trailing dots!

Two trailing dots is not possible to use as a hostname when resolving hostnames using DNS. It is an illegal name and causes an error. But as curl provides other ways to populate the DNS cache with a provided name, and you can provide names in `/etc/hosts` etc you can make curl work with URLs where the hostname has two trailing dots. Or rather, you could up until recently until I made sure it is properly banned always because of the trouble they cause internally.

A double-dot is correctly treated as a host with a trailing dot, but it turns out that in for example the HSTS logic that became problematic as removing the trailing dot for some functions would still have a trailing dot there when there were two of them to begin with… and it would get confused and act up.

No more double trailing dots. One is annoying enough. Shipping in curl 8.21.0.

## Cookie domain

HTTP cookies are basically name/value pairs set by the server and held by the client to get sent back to the server again in later communications. The server can specify for which domain a cookie should apply to, so that it can be used across multiple domains. (Yes, it is a little crazy,)

To prevent the server from being able to set the cookie on a *too wide* domain cookie clients check if the specified domain is *Public Suffic Domain* (PSL) or not. A server is not allowed to set cookies for PSL domains, as that allows it to create “super cookies” that work across domains in ways that are not allowed. Cookies attempted to get set for such a name should be rejected.

In libcurl we check domains against the PSL using the [libpsl library](https://github.com/rockdaboot/libpsl).

Turns out this too could be tricked by trailing dots. If you communicate with the URL “example.co.uk.” (with a trailing dot) and it sets a cookie for for “co.uk.” (with a trailing dot), the internal check would ask libpsl about the PSL status and… it did not work with trailing dots. The exact same process without trailing dots correctly says it is a PSL and the cookie is refused. But with the trailing dots present it was fooled and curl would allow the cookie to get stored and later sent back to such a host…

This particular issue ended up considered a vulnerability known as [CVE-2026-8924](https://curl.se/docs/CVE-2026-8924.html). Fix shipped in curl 8.21.0.

## We should consider these things

Yes, you can of course quite correctly argue that none of these things are actually *new* or sudden changes. Trailing dots are there, they have always been there and people will continue to use them in the future. I’m not blaming anyone else. I’m just expressing my frustration.

Trailing dots are the worst.

[bugs](https://daniel.haxx.se/blog/tag/bugs/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous Posta CVE dispute](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/)

## 2 thoughts on “Trailing dots are the worst”

1. ![](https://secure.gravatar.com/avatar/89c9eaa96e911d3c4d8bfc9f520a9b38190a69e7350047373b7f7441f3a044f1?s=34&d=monsterid&r=g) **[Martijn](https://martijnv.com/)** says:

   [June 25, 2026 at 11:51](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/#comment-27518)

   Is there a specific reason why removing the dot is a better course of action than just returning an error? Seems like that would make more sense, at least to me

   [Reply](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/?replytocom=27518#respond)

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [June 25, 2026 at 11:55](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/#comment-27519)

      Since it is accepted by the browsers I figured it would be more in line with what users would expect…

      [Reply](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/?replytocom=27519#respond)

### Leave a Reply [Cancel reply](/blog/2026/06/25/trailing-dots-are-the-worst/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
one639one

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Trailing dots are the worst](https://daniel.haxx.se/blog/2026/06/25/trailing-dots-are-the-worst/)
  June 25, 2026
* [a CVE dispute](https://daniel.haxx.se/blog/2026/06/24/a-cve-dispute/)
  June 24, 2026
* [curl 8.21.0](https://daniel.haxx.se/blog/2026/06/24/curl-8-21-0/)
  June 24, 2026
* [QUERY with curl](https://daniel.haxx.se/blog/2026/06/21/query-with-curl/)
  June 21, 2026
* [curl summer of bliss](https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/)
  Ju...
---
title: the Apple curl security incident 12604
url: https://daniel.haxx.se/blog/2024/03/08/the-apple-curl-security-incident-12604/
source: daniel.haxx.se
date: 2024-03-09
fetch_date: 2025-10-04T12:10:23.781688
---

# the Apple curl security incident 12604

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/apples.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# the Apple curl security incident 12604

[March 8, 2024](https://daniel.haxx.se/blog/2024/03/08/the-apple-curl-security-incident-12604/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [27 Comments](https://daniel.haxx.se/blog/2024/03/08/the-apple-curl-security-incident-12604/#comments)

tldr: Apple thinks it is fine. I do not.

On December 28 2023, [bugreport 12604](https://github.com/curl/curl/issues/12604) was filed in the curl issue tracker. We get a lot issues filed most days so this fact alone was hardly anything out of the ordinary. We read the reports, investigate, ask follow-up questions to see what we can learn and what we need to address.

The title stated of the problem in this case was quite clear: *[flag –cacert behavior isn’t consistent between macOS and Linux](https://github.com/curl/curl/issues/12604)*, and it was filed by Yuedong Wu.

The friendly reporter showed how the curl version bundled with macOS behaves differently than curl binaries built entirely from open source. Even when running the same curl version on the same macOS machine.

The curl command line option `[--cacert](https://curl.se/docs/manpage.html#--cacert)` provides a way for the user to say to curl that **this is the exact set of CA certificates to trust** when doing the following transfer. If the TLS server cannot provide a certificate that can be verified with that set of certificates, it should fail and return error.

This particular behavior and functionality in curl has been established since many years (this option was added to curl in December 2000) and of course is provided to allow users to know that it communicates with a known and trusted server. A pretty fundamental part of what TLS does really.

When this command line option is used with curl on macOS, *the version shipped by Apple*, **it seems to fall back and checks the system CA store in case the provided set of CA certs fail the verification**. A *secondary check* that was not asked for, is not documented and plain frankly comes completely by surprise. Therefore, when a user runs the check with a trimmed and dedicated CA cert file, it will not fail if the system CA store contains a cert that can verify the server!

This is a security problem because now **suddenly certificate checks pass that should not pass.**

I reported this as a security problem in an email sent to Product Security at Apple on December 29 2023, 08:30 UTC. It’s not a major problem, but it is an issue.

## Apple’s says it is fine

On March 8, 2024 Apple Product Security responded with their wisdom:

```
Hello,

Thank you again for reporting this to us and allowing us time to investigate.

Apple’s version of OpenSSL (LibreSSL) intentionally uses the built-in system trust store as a default source of trust. Because the server certificate can be validated successfully using the built-in system trust store, we don't consider this something that needs to be addressed in our platforms.

Best regards,
KC
Apple Product Security
```

Case closed.

## I disagree

Obviously I think differently. This *undocumented feature* makes CA cert verification with curl on macOS totally unreliable and inconsistent with documentation. It tricks users.

Be aware.

Since this is not a security vulnerability in the curl version we ship, we have not issued a CVE or anything for this problem. The problem is strictly speaking not even in curl code. It comes with the version of LibreSSL that Apple ships and builds curl to use on their platforms.

## Discussion

[hacker news](https://news.ycombinator.com/item?id=39650498)

[Apple](https://daniel.haxx.se/blog/tag/apple/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous Postcurl’s built-in manual without nroff](https://daniel.haxx.se/blog/2024/03/07/curls-built-in-manual-without-nroff/)[Next Postgetting started with libcurl](https://daniel.haxx.se/blog/2024/03/18/getting-started-with-libcurl/)

## 27 thoughts on “the Apple curl security incident 12604”

1. ![](https://secure.gravatar.com/avatar/685ba1734fcdd6c21076eea14c5b629e8ebaae1dbb0107960ace97b93d76ed00?s=34&d=monsterid&r=g) **Yawar** says:

   [March 9, 2024 at 06:56](https://daniel.haxx.se/blog/2024/03/08/the-apple-curl-security-incident-12604/#comment-26925)

   Nice of you guys to look into investigate these kinds of issues, tbh I would close the issue pretty quickly and advise the reporter to follow up with the OS vendor.

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [March 9, 2024 at 10:39](https://daniel.haxx.se/blog/2024/03/08/the-apple-curl-security-incident-12604/#comment-26926)

      In this case I thought it was clearly a security related problem and I did not want to highlight that in the public issue so I decided to forward the issue myself.

      1. ![](https://secure.gravatar.com/avatar/9209d2715ce142529c2e1c680e32a97ff28c0992e87930992524afa5dcb065fb?s=34&d=monsterid&r=g) **[Xavier D Willis](http://www.xavier6.com)** says:

         [March 10, 2024 at 13:48](https://daniel.haxx.se/blog/2024/03/08/the-apple-curl-security-incident-12604/#comment-26934)

         It may be a security issue, but likely on the insecure user’s device, as it’s likely that anything new generated by the user will be rejected because it’s not secure.
2. ![](https://secure.gravatar.com/avatar/375320dd9ae7ed408002f3768e16cb5f28c861062fd50dff9a3bff62e9dce4ef?s=34&d=monsterid&r=g) **John Doe** says:

   [March 9, 2024 at 12:17](https://daniel.haxx.se/blog/2024/03/08/the-apple-curl-security-incident-12604/#comment-26927)

   Can this then be considered a backdoor?

   I mean, if Apple gets appraoched by let’s say some government agency (hypothetical scenario) to look into the communication of an individual, they could simply “fake” a CA in the cert store and read along the communication.
3. ![](https://secure.gravatar.com/avatar/cb098c4ef764785b2f09bd3145455077e9ac6fd7337bcccb479e9f1add9b8dde?s=34&d=monsterid&r=g) **[Kevin Cox](https://kevincox.ca)** says:

   [March 9, 2024 at 13:28](https://daniel.haxx.se/blog/2024/03/08/the-apple-curl-security-incident-12604/#comment-26928)

   Are you sure they understood the issue? The response says:

   > as a default source of trust.

   But the reported issue clearly isn’t about the default. It is about trusting the system CA list even when explicitly requested not to.

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [March 9, 2024 at 23:07](https://daniel.haxx.se/blog/2024/03/08/the-apple-curl-security-incident-12604/#comment-26933)

      I’ve explained the issue to Apple Product Security to the best of my abilities. I have to assume that they are intelligent enough to understand the issue or that they would have asked me for clarifications of they did not. Of course I cannot guarantee that they understood it.

      The dialogue with Apple has been sparse. They clearly don’t waste any words.

      1. ![](https://secure.gravatar.com/avatar/b59e16dd670ee2adc11edbd1e3ca93d4fe7689e435563f5c14c9f8cae56ba67c?s=34&d=monsterid&r=g) **James** says:

         [March 10, 2024 at 18:54](https://daniel.haxx.se/blog/2024...
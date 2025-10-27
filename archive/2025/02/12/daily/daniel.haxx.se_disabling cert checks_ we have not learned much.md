---
title: disabling cert checks: we have not learned much
url: https://daniel.haxx.se/blog/2025/02/11/disabling-cert-checks-we-have-not-learned-much/
source: daniel.haxx.se
date: 2025-02-12
fetch_date: 2025-10-06T20:36:14.968475
---

# disabling cert checks: we have not learned much

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/08/bad-mistakes-ahead.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# disabling cert checks: we have not learned much

[February 11, 2025](https://daniel.haxx.se/blog/2025/02/11/disabling-cert-checks-we-have-not-learned-much/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [4 Comments](https://daniel.haxx.se/blog/2025/02/11/disabling-cert-checks-we-have-not-learned-much/#comments)

And by that I mean the global “we” as in the world of developers.

## In the beginning there was SSL

When I first learned about SSL and how to use it in the mid to late 1990s, it took me a while to realize and understand the critical importance of having the client verifying the server’s certificate in the handshake. Once I had understood, we made sure that curl would default to doing the check correctly and refuse connecting if the certificate check fails.

Since curl and libcurl 7.10 (released in October 2002) we verify server certificates by default. Today, more than twenty-two years later, there should realistically be virtually no users left using a curl version that does not verify certificates by default.

## What’s verifying

The standard way to verify a TLS server certificate is by A) checking that it is signed by a trusted certificate authority (CA) and B) that the cert was created for the thing you interact with; that the domain name is listed in the certificate.

Optionally, you can opt to “pin” a certificate which then verifies that the certificate is the one that corresponds to a specific hash. This is generally considered more fragile but avoids the use of a “CA store” (a set of certificates for the certificate authorities “you” trust) needed to verify the digital signature of the server certificate.

## Skipping means insecure

*Skipping the certificate verification makes the connection **insecure***. Because if you do not verify, there is nothing that prevents a middle-man to sit between you and the real server. Or even to just fake being the real server.

## Challenges

If you try to use the production site’s certificate in your development environment, you might connect to the server using a different name and then the verification fails.

If you have an active middle man intercepting and wanting to snoop on the TLS traffic, it needs to provide a different certificate and unless that can get signed by a CA you trust, the verification fails.

If you have an outdated or maybe no CA store at all, then the verification fails.

If the server does not update its certificate correctly, it might expire and then the verification fails. Similarly, in order to do a correct verification your client needs a clock that is at least roughly in sync with reality or the verification might fail.

Verification also takes more time compared to how fast it is to just skip the entire step. Sometimes and to some, weirdly enticing.

And yet all curl and libcurl documentation for this *strongly* discourages users from disabling the check.

## A libcurl timeline

curl added support for SSL in April 1998 (years before they renamed it TLS). curl makes certificate checks by default since 2002, both the tool and the library. At the time, I felt I was a little slow to react but at least we *finally* made sure that curl users would do this check by default.

Ten years later, in October 2012, there was a paper published called [The most dangerous code in the world](https://daniel.haxx.se/blog/2012/10/25/libcurl-claimed-to-be-dangerous/), in which the authors insisted that the widespread problem of applications not verifying TLS certificates with libcurl was because *This interface is almost perversely bad*. The problem was apparently libcurl’s API.

The same “fact” would be repeated later, for example in this [2014 presentation](https://daniel.haxx.se/blog/2014/09/18/using-apis-without-reading-docs/) saying that this is our fault because the API (for PHP) looks like it takes a boolean when in reality it did not.

## The libcurl API for this

I do not claim that we have the best API in libcurl, but I can say that extremely few libraries can boast an API and ABI stability that comes even close to ours. We have not broken the ABI since 2006. We don’t mind carrying a world on our shoulders that have learned to depend on this and us. So we don’t change the API, even though it could have been done a little better.

[CURLOPT\_SSL\_VERIFYPEER](https://curl.se/libcurl/c/CURLOPT_SSL_VERIFYPEER.html) is a boolean option to ask for server certificate verification against the CA store. It is set TRUE by default, so an application needs to set it to FALSE (0) to disable the check. This option works together with the next one.

[CURLOPT\_SSL\_VERIFYHOST](https://curl.se/libcurl/c/CURLOPT_SSL_VERIFYHOST.html) is a separate option to verify that the name embedded in the certificate matches the name in the URL (basically). This option was never a boolean but accepts a number. 0 disables the check, and 2 was for the maximum check level. With 2 being the default.

Both options are thus by default set to verify, and an application can lessen the checks by changing one or both of them.

## Adaptations

After that most dangerous article was posted in 2012 that basically said we were worthless, without ever telling that to us or submitting an issue or pull-request with us, we changed how CURLOPT\_SSL\_VERIFYHOST worked in the 7.28.1 release – shipped in December 2012.

Starting then, we made setting the option to 1 an error (and it would just leave the original value untouched). Before that update, setting VERIFYHOST to 1 was a debug-like mode that made libcurl output warnings on mismatches but still let the connection through. A silly mode to offer.

In 2019 we tweaked the VERIFYHOST handling a little further and made the value 1 and 2 do the same thing: verify the name.

I have no idea what the authors of that 2012 paper would think about this API tweak, but at least the options are now two proper booleans.

I did not think the authors were right when they originally published that paper, but yet we improved the API a little. I dare to claim that the problem with disabled certificate checks is not because of a bad libcurl API.

## curl

The curl tool of course is a libcurl using application and it itself offers the `--insecure` (`-k`) option which when used switches off both those above mentioned libcurl options. Also strongly discouraged to actually use beyond testing and triaging.

## Other layers on top

libcurl is itself used by a lot of frameworks and languages that expose the options to their respective users. Often they then even use the same option names. We have over 60 documented language bindings for libcurl.

For example, the PHP/CURL binding is extremely popular and well used and it has the options provided and exposed using the exact same names, values and behavior.

## Disabling the checks

More than twenty-two years of having this enabled by default. More than twelve years since the *most dangerous* paper. After countless articles on the topic. Everyone I talk to knows that we all must verify certificates.

In almost all cases, you can fix the failed verification the *proper* way instead of disabling the check. It is just usually a little more work.

## State of checks using libcurl today

I searched GitHub on February 10 2025 for “CURLOPT\_SSL\_VERIFYPEER, FALSE” and it quickly showed me some 140,000 matching repositories. Sure, not all these matches are bad uses since they can be done conditionally etc and it ca...
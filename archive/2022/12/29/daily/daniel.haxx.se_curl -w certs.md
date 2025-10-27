---
title: curl -w certs
url: https://daniel.haxx.se/blog/2022/12/28/curl-w-certs/
source: daniel.haxx.se
date: 2022-12-29
fetch_date: 2025-10-04T02:40:14.902539
---

# curl -w certs

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2018/08/HTTPS-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl -w certs

[December 28, 2022](https://daniel.haxx.se/blog/2022/12/28/curl-w-certs/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

When a client connects to a TLS server it gets sent one or more certificates during the handshake.

Those certificates are verified by the client, to make sure that the server is indeed the right one: the server the client expects it to be; no impostor and no man in the middle etc.

When such a server certificate is signed by a Certificate Authority (CA), that CA’s certificate is normally not sent by the server but the client is expected to have it already in its [CA store](https://curl.se/docs/caextract.html).

## What certs?

Ever since the day SSL and TLS first showed up in the 1990s user have occasionally wanted to be able to save the certificates provided by the server in a TLS handshake.

The [openssl tool has offered this ability](https://stackoverflow.com/questions/27611193/use-self-signed-certificate-with-curl/27611319#27611319) since along time and is actually one of my higher ranked stackoverflow answers.

Export the certificates with the tool first, and then in subsequent transfers you can tell curl to use those certificates as a CA store:

```
$ echo quit | openssl s_client -showcerts -connect curl.se:443 > cacert.pem
$ curl --cacert cacert.pem https://curl.se/
```

This is of course most convenient when that server is using a self-signed certificate or something otherwise unusual.

(**WARNING**: *The above shown example is an insecure way of reaching the host, as it does not detect if the host is already MITMed at the time when the first command runs. Trust On First Use.*)

## OpenSSL

A downside with the approach above is that it requires the `openssl` tool. Albeit, not a big downside for most people.

There are also alternative tools provided by wolfSSL and GnuTLS etc that offer the same functionality.

## QUIC

Over the last few years we have seen a huge increase in number of servers that run QUIC and HTTP/3, and tools like curl and all the popular browsers can communicate using this modern set of protocols.

[OpenSSL cannot](https://daniel.haxx.se/blog/2021/10/25/the-quic-api-openssl-will-not-provide/). They decided to act against what everyone wanted, and as a result the openssl tool also does not support QUIC and therefore it cannot show the certificates used for a HTTP/3 site!

This is an inconvenience to users, including many curl users. I decided I could do something about it.

## `CURLOPT_CERTINFO`

Already back in 2016 we added a feature to libcurl that enables it to return a list of certificate information back to the application, including the certificate themselves in PEM format. We call the option [CURLOPT\_CERTINFO](https://curl.se/libcurl/c/CURLOPT_CERTINFO.html).

We never exposed this feature in the command line tool and we did not really see the need as everyone could use the openssl tool etc fine already.

Until now.

## curl -w is your friend

curl supports QUIC and HTTP/3 since a few years back, even if still marked as experimental. Because of this, the above mentioned `CURLOPT_CERTINFO` option works fine for that protocol version as well.

Using the [–write-out](https://everything.curl.dev/usingcurl/verbose/writeout) (`-w`) option and the new variables `%{certs}` and `%{num_certs}` curl can now do what you want. Get the certificates from a server in PEM format:

```
$ curl https://curl.se -w "%{certs}" -o /dev/null > cacert.pem
$ curl --cacert cacert.pem https://curl.se/
```

You can of course also add `--http3` to the command line if you want, and if you like to get the certificates from a server with a self-signed one you may want to use `--insecure`. You might consider adding `--head` to avoid the response body. This command line uses `-o` to write the content to `/dev/null` because it does not care about that data.

The `%{num_certs}` variable shows the number of certificates returned in the handshake. Typically one or two but can be more.

`%{certs}` outputs the certificates in PEM format together with a number of other details and meta data about the certificates in a “name: value” format.

## Availability

These new -w variables are only supported if curl is built with a supported TLS backend: OpenSSL/libressl/BoringSSL/quictls, GnuTLS, Schannel, NSS, GSKit and Secure Transport.

Support for these new -w variables has been merged into curl’s master branch and is scheduled to be part of the coming release of curl version 7.88.0 on February 15th, 2023.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[HTTP/3](https://daniel.haxx.se/blog/tag/http3/)[OpenSSL](https://daniel.haxx.se/blog/tag/openssl/)[QUIC](https://daniel.haxx.se/blog/tag/quic/)[TLS](https://daniel.haxx.se/blog/tag/tls/)

# Post navigation

[Previous PostAt 17000 curl commits](https://daniel.haxx.se/blog/2022/12/27/at-17000-curl-commits/)[Next PostAn m1 for curl](https://daniel.haxx.se/blog/2022/12/30/an-m1-for-curl/)

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

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

December 2022

| M | T | W | T | F | S | S |
| --- | --- | --- |...
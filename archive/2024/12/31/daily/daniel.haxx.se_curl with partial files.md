---
title: curl with partial files
url: https://daniel.haxx.se/blog/2024/12/30/curl-with-partial-files/
source: daniel.haxx.se
date: 2024-12-31
fetch_date: 2025-10-06T19:40:48.209185
---

# curl with partial files

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2021/04/curl-polynesia-puzzle.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl with partial files

[December 30, 2024](https://daniel.haxx.se/blog/2024/12/30/curl-with-partial-files/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [3 Comments](https://daniel.haxx.se/blog/2024/12/30/curl-with-partial-files/#comments)

Back in September 2023, we extended the curl command line tool with a new fairly advanced and flexible [variable system](https://everything.curl.dev/cmdline/variables.html). Using this, users can use files, environment variables and more in a powerful way when building curl command lines in ways not previously possible – with almost all existing command line options.

curl command lines were already quite capable before this, but these new variables certainly took it up several additional notches.

## Come February 2025

In the pending curl 8.12.0 release, we extend this variable support a little further. Starting now, you can assign a variable to hold the contents of a *partial* file. Get a byte range from a given file into a variable and use that variable in the command line, instead of using the entire file.

You can get the first few bytes and use as a username, you can get a hundred bytes in the middle of a file and POST that or do countless other things.

## Byte range

You ask curl to read a byte range from a file instead of the whole one by appending `[n-M]` to the variable name, when you assign a variable. Where N and M are the first and the last byte offsets into the file, 0 being the first byte. If you omit the second number, it means until the end of file.

For example, get the first 32 bytes from a file named *secret* and set as password for *daniel*:

```
curl --variable "pwd[0-31]@secret" \
     --expand-user daniel:{{pwd}} \
     https://example.com/
```

Skip the first thousand bytes from a file named *localfile* and send the rest of it in a POST:

```
curl --variable "upload[1000-]@localfile" \
     --expand-post '{{upload}}' \
     https://example.com/
```

## With functions

You can of course also combine the byte offsets with the standard *expand functions*. For example, get the first hundred bytes from the file called *random* and send them base64 encoded in a POST:

```
curl --variable "binary[0-99]@random" \
     --expand-post '{{binary:b64}}' \
     https://example.com/
```

I hope you will like it.

## Update

After his post was first published, we discussed the exact syntax for this feature and decided to tweak it a little to make it less likely that old curl versions could be tricked when trying a new command line options.

This version is now showing the updated syntax.

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous Postdropping hyper](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/)[Next PostSecure Transport support in curl is on its way out](https://daniel.haxx.se/blog/2025/01/14/secure-transport-support-in-curl-is-on-its-way-out/)

## 3 thoughts on “curl with partial files”

1. ![](https://secure.gravatar.com/avatar/31c5543c1734d25c7206f5fd591525d0295bec6fe84ff82f946a34fe970a1e66?s=34&d=monsterid&r=g) **example** says:

   [December 30, 2024 at 10:52](https://daniel.haxx.se/blog/2024/12/30/curl-with-partial-files/#comment-27095)

   Small error: In the last example you write ‘from the file called random’ but in the curl command you read from localfile.
2. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

   [December 30, 2024 at 10:55](https://daniel.haxx.se/blog/2024/12/30/curl-with-partial-files/#comment-27096)

   Thanks, fixed!
3. ![](https://secure.gravatar.com/avatar/221dcaf3ace2874384e4c0da0a2f383f84bbab30037d261c3f26fcd348f61811?s=34&d=monsterid&r=g) **Thomas** says:

   [January 23, 2025 at 15:47](https://daniel.haxx.se/blog/2024/12/30/curl-with-partial-files/#comment-27105)

   A stupid question maybe. But what could the use case be, except from a hacker who wants to exfiltrate data from a network? Or you have customers shutdown their clients before the whole backup is made.

Comments are closed.

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

December 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | 1 |
| 2 | [3](https://daniel.haxx.se/blog/2024/12/03/) | 4 | 5 | [6](https://daniel.haxx.se/blog/2024/12/06/) | 7 | 8 |
| 9 | 10 | [11](https://daniel.haxx.se/blog/2024/12/11/) | [12](https://daniel.haxx.se/blog/2024/12/12/) | 13 | 14 | 15 |
| 16 | 17 | 18 | 19 | 20 | [21](https://daniel.haxx.se/blog/2024/12/21/) | 22 |
| 23 | 24 | 25 | 26 | 27 | 28 | 29 |
| [30](https://daniel.haxx.se/blog/2024/12/30/) | 31 |  | | | | |

[« Nov](https://daniel.haxx.se/blog/2024/11/)

[Jan »](https://daniel.haxx.se/blog/2025/01/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)
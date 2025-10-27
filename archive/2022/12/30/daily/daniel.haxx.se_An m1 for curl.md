---
title: An m1 for curl
url: https://daniel.haxx.se/blog/2022/12/30/an-m1-for-curl/
source: daniel.haxx.se
date: 2022-12-30
fetch_date: 2025-10-04T02:44:56.098040
---

# An m1 for curl

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

# An m1 for curl

[December 30, 2022](https://daniel.haxx.se/blog/2022/12/30/an-m1-for-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [4 Comments](https://daniel.haxx.se/blog/2022/12/30/an-m1-for-curl/#comments)

A generous member of the wider curl community stepped up and donated an unused Mac mini m1 model to me to be used for curl development. Today it arrived at my home. An `8C CPU/16GB/1TB/8C GPU/1GbE` model as per the sticker on the box.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/PXL_20221229_121515059.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/PXL_20221229_121515059.jpg)

The m1 mac mini, still wrapped in plastic.

## Apple is not helping

Apple has shipped and used curl in their products for twenty years but **they never assist, help or otherwise contribute to the development**. They also don’t sponsor us in any way, like with hardware.

Yet, there are many curl users on the different Apple platforms and sometimes these [users run into issues](https://daniel.haxx.se/blog/2021/11/18/free-apple-support/) that are unique to those platforms and are challenging to address without direct access to such.

## For curl

I decided to accept this gift as I believe it might help the project, but this is not a guarantee or promise that I will run around and become the mac support guy in the project. It will just allow me to sometimes get a better grip and ability to help out.

I will also offer other curl committers access to the machine in case of need. For development and debugging and whatnot. Talk to me about it.

## A tiny speed comparison

My Intel-based development machine runs Linux, is ten years old and is equipped with an i7-3770K CPU at 3.5GHz. The source code is stored on an OCZ-VERTEX4 SSD on the Intel, the mac has SSD storage only.

Here’s a rough and not very scientific test of some of my most common build activities on the m1+macOS vs the old Intel+Linux machines. This is using the bleeding edge curl source code with roughly the same build config. Both used clang for compiling, a debug build.

|  |  |  |
| --- | --- | --- |
| **Test** | **m1** | **Intel** |
| configure | 19.8 s | 18.5 s |
| make -sj | 12.8 s | 14.2 s |
| autoreconf -fi | 7.9 s | 12.8 s |
| make -sj (in `tests/`) | 19.1 s | 33.9 s |

I expected the differences to be bigger.

The first line of curl -V for the two builds:

```
curl 7.87.1-DEV (aarch64-apple-darwin22.2.0) libcurl/7.87.1-DEV OpenSSL/3.0.7 zlib/1.2.11 brotli/1.0.9 zstd/1.5.2 c-ares/1.18.1 libidn2/2.3.4 libpsl/0.21.2 (+libicu/71.1) libssh2/1.10.0 nghttp2/1.51.0 libgsasl/2.2.0
```

```
curl 7.87.1-DEV (x86_64-pc-linux-gnu) libcurl/7.87.1-DEV OpenSSL/3.0.7 zlib/1.2.13 brotli/1.0.9 zstd/1.5.2 c-ares/1.17.0 libidn2/2.3.3 libpsl/0.21.0 (+libidn2/2.3.0) libssh2/1.10.1_DEV nghttp2/1.50.0-DEV librtmp/2.3 libgsasl/2.2.0
```

Interestingly, there is no mention anywhere that I can find in the OS settings/config or in the box etc as to what CPU speed the m1 runs at.

## Credits

This device was donated “to the cause” by “a member and supporter of the Network Time Foundation at nwtime.org” (real name withheld on request).

## Discussed

[Hacker news](https://news.ycombinator.com/item?id=34183020).

## Short follow-up

People mention that the Intel CPU uses much more power, runs at higher temperature and that the m1 is “just first generation” and all sorts of other excuses for the results presented above. Others insist that the Makefiles must be bad or that I’m not using the mac to its best advantage etc.

None of those excuses change the fact that my ten year old machine builds curl and related code at roughly the same speed as this m1 box while *I expected it to be a more noticeable speed difference* in the m1’s favor. Yes, it was probably bad expectations.

[Apple](https://daniel.haxx.se/blog/tag/apple/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Mac OS X](https://daniel.haxx.se/blog/tag/mac-os-x/)

# Post navigation

[Previous Postcurl -w certs](https://daniel.haxx.se/blog/2022/12/28/curl-w-certs/)[Next PostCopyright without years](https://daniel.haxx.se/blog/2023/01/08/copyright-without-years/)

## 4 thoughts on “An m1 for curl”

1. ![](https://secure.gravatar.com/avatar/2726891ebaed284a5788ab32a416467984b03d69cc72506916f8bd9b653f4df1?s=34&d=monsterid&r=g) **Sevan Janiyan** says:

   [December 30, 2022 at 00:46](https://daniel.haxx.se/blog/2022/12/30/an-m1-for-curl/#comment-26539)

   Regarding CPU, it supposedly has 8 (4 – high-performance, 4 – high-efficiency) cores running at 3.2 GHz (high-performance) and 2.1 GHz (high-efficiency). Source Mactracker app.
2. ![](https://secure.gravatar.com/avatar/c1b213bc636957546844809a1d889652232d6ac13f45a075a7da68634fb55a63?s=34&d=monsterid&r=g) **[Lars](https://feldeisen.de)** says:

   [December 30, 2022 at 11:07](https://daniel.haxx.se/blog/2022/12/30/an-m1-for-curl/#comment-26540)

   The shiny case distracts you which leads to a 90% faster build time.
3. ![](https://secure.gravatar.com/avatar/003ba95660e559a710f498bb963683de67ee3e23271b954b92fd4727602c7d45?s=34&d=monsterid&r=g) **T. Lindsay** says:

   [December 30, 2022 at 11:54](https://daniel.haxx.se/blog/2022/12/30/an-m1-for-curl/#comment-26542)

   Here’s another data point on what the M1 has vs your Intel:
   <https://versus.com/en/apple-m1-vs-intel-core-i7-3770k>
4. ![](https://secure.gravatar.com/avatar/f4afaf944d54db0855bc8e82f4fafcb1e9777358b7b524cf0a7d87678645cc6b?s=34&d=monsterid&r=g) **David** says:

   [December 30, 2022 at 17:40](https://daniel.haxx.se/blog/2022/12/30/an-m1-for-curl/#comment-26543)

   The maximum clock speeds for the M1 are 2064 MHz for the efficiency cores, and 3204 MHz for the performance cores. However, the run-time clock speeds of the CPU cores tend to vary quite a bit. If you want real-time details on that as well as the power usage, the `powermetrics` command provides extremely detailed information.

   I’d typically expect a higher speed-up than what you’re observing, but this might be because the project is relatively small, so it ends up being more I/O than CPU bound. For a large project, the performance difference does end up being substantial, at least compared to those older Intel CPUs. That said, Intel has caught up with their 12th gen processors, at least when not considering power consumption.

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
* [Fazal Majid](https://majid.info/) on [preparing for the worst](https://daniel.haxx.se/blog/2025/0...
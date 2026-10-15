---
title: A UAF turned RCE
url: https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/
source: daniel.haxx.se
date: 2026-10-14
fetch_date: 2026-10-15T06:44:02.096042
---

# A UAF turned RCE

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2017/10/bobby-car-crash-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Security](https://daniel.haxx.se/blog/category/tech/security/)

# A UAF turned RCE

[October 14, 2026](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/#respond)

In the [curl 8.23.0 release](https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/) we shipped a fix for one of the worst vulnerabilities in curl in a long time. We grade it severity HIGH. It is known as [CVE-2026-92392](https://curl.se/docs/CVE-2026-92392.html) with the title *HTTP/2 upload Use-After-Free*.

This post explains the bug, what the problem can lead to, and something about why it happened and what we have done to make it harder to introduce a problem like this in curl again in the future.

This is a much simplified explanation. Please refer to [the original report](https://hackerone.com/reports/4030333) for all the details and the full reproducible Docker image for all the low-level fun and education you could possibly want. I highly recommend doing that; the report and the reproducible are awesome.

## Use-After-Free

It is a [use-after-free](https://en.wikipedia.org/wiki/Dangling_pointer), which is a classic problem in memory-unsafe programming languages, like C, where we erroneously have a lingering pointer left, pointing to memory that is already freed, and yet we use that pointer and the memory it points to.

This family of errors is especially bad when a malicious actor can affect the content that gets stored into that memory area that is still used even though it was freed. Tricking the program to do something unintended.

## HTTP/2 is multiplexed

This problem involves HTTP/2. HTTP/2 is a multiplexed protocol, meaning that it handles multiple logical transfers over the same physical connection. curl needs to keep track of a number of transfers at the same time, and when data arrives or is to be sent off, it needs to keep things apart appropriately.

## Handles

For every transfer done using libcurl, the application creates and sets up a dedicated *handle*. We call it an *easy handle*. This handle is kept around for as long as the transfer is in progress, and the application can close and free it once the operation is completed. When doing multiple transfers, multiple handles are used.

libcurl also has *multi handles*, which is a super handle type that holds any amount of *easy handles*. This handle, and the corresponding multi interface, makes it possible to drive any amount of concurrent transfers. A transfer done with libcurl always has at least one multi handle and one easy handle. (Sometimes the multi handle is hiddenly used under the hood.)

## The setup

In order to trigger this problem, we need an application (such as the curl command line tool) to do an upload over HTTP/2 to a server. By default, libcurl negotiates HTTP/2 when a HTTPS:// URLs is used and the server agrees.

When the upload has started, the server pauses the send by zeroing the HTTP/2 window size, returns a piece of the response and then it resets the stream, which shuts down the transfer – but not the connection. curl then correctly pulls down the entire transfer, but it accidentally leaves a lingering pointer to the involved *easy handle*.

When the application finds out that the transfer completed (with an error), it subsequently frees the easy handle and then, and here comes the problematic part: cleans up the multi handle.

## The mistake

At this point, the *easy handle* was just freed but there is still a reference to that handle. When libcurl shuts down the multi handle, it misunderstands the situation, allocates memory to download data into, finds the still dangling pointer and manages to *download data* from the server that ends up in the very same memory previously used for the easy handle.

In this process, it sends off a request that leaks internal client details, which includes information about local addresses, which is crucial. Modern operating systems use [Address Space Layout Randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization) (ASLR), so a server needs this clue in order to generate a good attack payload.

Subsequently, when libcurl deals with this received data (using the handle the dangling pointer points to) in the download buffer, it uses a function pointer that now has been modified by data just downloaded from the server, and then *it runs remote code*.

## An illustration

Here’s a simplified 6-step illustration.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/10/RCE-explained.png)

## Conditions to trigger

In order to actually successfully execute remote code, lots of several specific conditions need to be met and we deem it extremely difficult to meet these requirements in the wild, which is why we decided this is “only” severity HIGH and not CRITICAL.

1. The victim needs to actually attempt to upload data to a malicious server, meaning that the server certificate must remain valid.
2. The size of the upload needs to be roughly the right size (~135KB)
3. The attacker needs to know curl’s architecture to *generate* and deliver the right code
4. The attack requires a specific sequence of allocations and allocation sizes so that the data from the server ends up in the right place (from the attacker’s view). This pattern differs between Linux distros, libc versions/flavors, TLS certificate bundles, libcurl using applications and more.
5. nghttp2 and OpenSSL/TLS 1.3 behavior, including allocation effects around session tickets
6. The payload storage area is small (around 23 bytes)

The most likely outcome of an attempted attack is rather just a crash. We estimate that the chance for a successful attack is slim.

## How was this found?

This problem was found and reported by Luna Tong at Anthropic using their new OSS Scanner. Presumably this involves their AI models.

## How do we fix this?

In general we have over the last few years been working on reducing the amount of internal pointers to handles that needs to be correct, and instead we store transfer identifiers that we look-up on demand. While this is a tiny bit slower, it is more foolproof when there are logical mistakes like the one mentioned here.

We also of course continue to add more tests and we verify the code with more tools and analyzers in order to find additional similar mistakes.

Multiplexed protocols like HTTP/2 have this challenge that there are many concurrent transfers going and they all have different life-times and with memory-unsafe languages, dangling pointer mistakes can indeed be fatal.

This is of course no guarantee that we do not have or will not introduce another use-after-free in the code now or later.

## Again on the language

libcurl is written in C – a memory unsafe language. With a *memory-safe* language, this mistake could probably have been avoided.

We have worked on curl for almost thirty years, and have over this time manage to make a rather polished transfer engine. For the longest time there really was no memory-safe alternative that also allowed libcurl to be a low-level library available on hundreds of operating systems and several dozen CPU architectures. It even barely exist alternatives now.

We do not rewrite curl. Not into another language but also not in C. We are set to iterate, polish, improve, refactor over and over until the end of time.

Porting curl...
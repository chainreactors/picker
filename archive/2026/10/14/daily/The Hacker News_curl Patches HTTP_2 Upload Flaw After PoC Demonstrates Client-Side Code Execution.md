---
title: curl Patches HTTP/2 Upload Flaw After PoC Demonstrates Client-Side Code Execution
url: https://thehackernews.com/2026/10/curl-patches-http2-upload-flaw-after.html
source: The Hacker News
date: 2026-10-14
fetch_date: 2026-10-15T06:45:39.151808
---

# curl Patches HTTP/2 Upload Flaw After PoC Demonstrates Client-Side Code Execution

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [curl Patches HTTP/2 Upload Flaw After PoC Demonstrates Client-Side Code Execution](https://thehackernews.com/2026/10/curl-patches-http2-upload-flaw-after.html)

**Swati Khandelwal**Oct 14, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4S_5rQ2kApGYmSMOh6PFsgD3yRugV3_nzSexwBhEe3BoSTQeBfSu2-3JSO4wDCnU2LmVMWtgA6AcBEcf2wOpsL2v22woZ5fel0XaSonlbgDWSXMuV3iu5ewohp9kqgf4OwmCvtnRyyYjFEP6Z3RRLT5sX8g7-xI1robnLmWtqFp6SvrGvpBeXI_D4ICo/s1700-nu-rw-lo-l85-e365/curl.jpg)

A flaw in how curl handles HTTP/2 uploads lets a malicious server receiving an upload corrupt the client's memory, and the researcher who reported it turned that into code execution on the uploading machine.

The curl project fixed it on October 14 in [curl 8.23.0](https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/). Taking over a client needs exact knowledge of its build and memory layout, and curl expects a real attack to end in a crash instead.

The flaw, a use-after-free tracked as [CVE-2026-92392](https://curl.se/docs/CVE-2026-92392.html), affects curl and libcurl 8.12.0 through 8.22.0, both the command-line tool and the library that many other programs use for transfers. curl rates it High on its own four-level scale, its first High-severity flaw since the [SOCKS5 heap overflow of October 2023](https://thehackernews.com/2023/10/two-high-risk-security-flaws-discovered.html). The project cut its release cycle by two weeks to ship the fix.

The attack runs from the server side. The client has to upload a file of roughly 135KB over HTTP/2 to a server controlled by the attacker, and the server's certificate must pass the client's checks. libcurl negotiates HTTP/2 by default for https:// URLs when the server offers it, and the library was built with HTTP/2 support.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The flaw has shipped in every curl release since 8.12.0 in February 2025. No source reports attacks that use it. The [reporter's HackerOne write-up](https://hackerone.com/reports/4030333), with the malicious server script and a Docker container described as reproducing the code execution, became public on October 14 with the advisory.

### What to Install, and What to Do Until Then

Upgrade to 8.23.0 or apply the [fix commit](https://github.com/curl/curl/commit/8b0744af5b1b631da5b938ca31c3f9895ad5a321) to a local build. curl's [machine-readable advisory](https://curl.se/docs/CVE-2026-92392.json) also lists fixed versions on three older branches, and the project said it would ship updated [Rock-solid curl](https://rock-solid.curl.dev/) releases, its long-term-support line for customers with support contracts, in step with 8.23.0:

* curl and libcurl 8.12.0 through 8.22.0: upgrade to 8.23.0
* 8.14.x branch: 8.14.3
* 8.16.x branch: 8.16.2
* 8.20.x branch: 8.20.2
* Debian 13 (trixie): 8.14.1-2+deb13u7 through DSA-6558-1, per [Debian's tracker](https://security-tracker.debian.org/tracker/CVE-2026-92392). Debian 12 (bookworm) does not carry the vulnerable code.

The release fixes 24 CVEs in all. The other 23 are rated Low.

If you cannot update yet, curl's advice is not to use HTTP/2. The [--http1.1](https://curl.se/docs/manpage.html#--http11) option asks the tool for HTTP/1.1, and applications set [CURLOPT\_HTTP\_VERSION](https://curl.se/libcurl/c/CURLOPT_HTTP_VERSION.html) to CURL\_HTTP\_VERSION\_1\_1. curl's documentation calls that setting a request, because an existing connection on another version may be reused.

HTTP/2 support in libcurl is a [build option](https://curl.se/docs/manpage.html#--http2). A build without it cannot negotiate HTTP/2, so it cannot reach the upload path the advisory describes.

### How a Hostile Server Turns the Bug Into Code Execution

Daniel Stenberg, curl's lead developer, [explained the bug](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/) in a post published with the release, and the public report lays out the code path. HTTP/2 carries several transfers over one connection, and libcurl tracks each transfer with an object it calls an easy handle.

During an upload, the server stalls the transfer by setting the HTTP/2 window to zero, returning part of the response, and then resetting the stream while keeping the connection open. curl treats the reset as a reason to retry.

In cleanup, curl first tells the HTTP/2 layer that the transfer is finished, then flushes the rest of the unsent upload into the same connection. With no transfer registered, those leftover bytes are read as a new request. The line pattern the reporter includes in the uploaded file makes them look like request lines. When they do, a new stream is opened that stores a pointer to the easy handle.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2U4xUHnZVByQi9dRmNa3V-eRSFdVMVfeH8ZXwS0cwANMmo6GS29HTcIid2TUj35EXeicpjXFkKbPZDWLGPabzj_pzl-H2K12Z9zM6aVAxaWCccx8HXLcECQ5utjl_6eL5-cdmJ-XJQ-oySosMkv5WmxUWd_U8vji0YgZwVC5Fr5Y4mDxQgUdjOFGc-M0/s1700-nu-rw-lo-l85-e365/curl.png)

The retry completes on a new HTTP/1.1 connection, and the application frees the handle. The old connection still holds the pointer and uses it when the server sends a frame on that stream, which can happen as the program exits.

In the reporter's exploit, data the server sends lands in the memory the freed handle had used. A request that goes out leaks local addresses, which the server needs to defeat address space layout randomization (ASLR). A function pointer in that memory is overwritten with bytes from the server, and curl then calls it.

Code execution needs the attacker to know the target's exact curl version, architecture, libc allocator and heap layout, to keep two parallel transfers on the right timing, and to fit the payload into about 23 bytes, according to curl's advisory. "The most likely outcome of an attempted attack is rather just a crash," Stenberg wro...
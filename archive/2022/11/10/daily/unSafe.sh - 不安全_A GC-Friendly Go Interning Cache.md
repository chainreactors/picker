---
title: A GC-Friendly Go Interning Cache
url: https://buaq.net/go-134927.html
source: unSafe.sh - 不安全
date: 2022-11-10
fetch_date: 2025-10-03T22:12:48.042265
---

# A GC-Friendly Go Interning Cache

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/f308f4b3415a42c66222c80a9ebb7dfe.jpg)

A GC-Friendly Go Interning Cache

I’ve seen a little gem pass by in a Go cryptography code review and I want to share it
*2022-11-9 22:28:2
Author: [words.filippo.io(查看原文)](/jump-134927.htm)
阅读量:12
收藏*

---

I’ve seen a little gem pass by in a Go cryptography code review and I want to share it because I think it’s a pattern that can be reused.

Let’s start with a problem statement: crypto/x509 `Certificate` values take a bunch of memory, and for every open TLS connection you end up with a copy of the leaf and intermediate certificate, and sometimes of the root too.[[1]](#fn1) That’s kind of a waste of memory, a big one if you open a lot of connections to the same endpoint or to endpoints that use the same roots.

Ideally, if there was already a parsed copy of a certificate in memory we’d just return a pointer to that. An easy way to do that would be to have a `map[string]*x509.Certificate` somewhere mapping the certificate bytes to the parsed structure, and reuse an old entry if present. This is the concept of [interning](https://en.wikipedia.org/wiki/String_interning), usually used for short strings and other commonly repeated immutable values.

The problem is: how do we evict entries from that cache when they aren’t needed anymore? We can’t have a client that connects to a lot of endpoints one after the other just grow its memory usage endlessly.

The “simplest” solution would be to store a reference counter, remember to decrease it when we don’t need the certificate anymore, and delete the entry from the map when it reaches zero. How do we decrement it though? The `x509.Certificate` is needed for as long as the `tls.Conn` is live, because you can call `PeerCertificates` on the `Conn`. Any manual way of doing it is guaranteed to turn out wrong, causing memory leaks.

Some languages have the concept of “weak reference” for this: a pointer that points to the thing but doesn’t keep it live. They are somewhat complicated to implement safely and intuitively, and Go just doesn’t have them. You could try to replicate them by casting `unsafe.Pointer`s to `uintptr`s but that’s also guaranteed to go wrong eventually, and this time instead of a memory leak you end up with memory corruption. It also relies on undocumented properties of the GC, such as the fact that the GC currently doesn’t move heap-allocated values.

The solution [suggested by Russ Cox](https://go-review.googlesource.com/c/go/%2B/426454/comment/0001ba1b_50f0b59f/) and [implemented by Roland Shoemaker](https://go.dev/cl/426454) uses the garbage collector itself to track when the map entry should be dropped.

It’s relatively simple: when you request a certificate from the cache, you get back an `x509.Certificate` wrapped in an `activeCert` struct. You’re expected to hold on to the `activeCert` for as long as you need the `x509.Certificate`. For example, `crypto/tls` sticks the `activeCert` in a private field of `tls.Conn`. The magic is that `activeCert` has a [finalizer](https://pkg.go.dev/runtime%40go1.19.2#SetFinalizer) attached to it, so that when it gets garbage-collected it also decrements the reference counter of the certificate in the map. When the counter hits zero, the map entry is deleted.

It’s using the GC to keep track of when entries in the cache stop being useful. You can’t put the finalizer on the certificate itself because the certificate is the thing kept alive by the map. Instead, you have a distinct `activeCert` for every place the certificate is used (specifically, for every `tls.Conn` that needs it), and keep track of when all of them have been garbage-collected.

I like it because it’s simple to use—you just store the `activeCert` next to the certificate—and because it fails gracefully. If you drop the `activeCert` while something is still using the certificate, for example if the certificate outlives the `Conn`, nothing bad happens besides potentially making the cache a little less efficient. The certificate itself will still be kept alive by the GC, even if it’s dropped from the cache.

[Finalizers are scary](https://crawshaw.io/blog/tragedy-of-finalizers) and generally speaking if you use them like destructors you’re gonna have a bad time. For example, what if the program runs with `GOGC=off`?[[2]](#fn2) However, this is a good use for them because what we are doing is exclusively related to memory management and value lifecycle. In David’s words, we’re managing “a resource whose use is tied closely to heap use”. A similar use of finalizers that makes sense to me is [autopool](https://web.archive.org/web/20220525085959/http%3A//www.golangdevops.com/2019/12/31/autopool/) which returns things to a `sync.Pool` automatically. This is the kind of thing that can happen “whenever the GC happens to collect the value” so is a good fit for finalizers.

As a nice side-effect, we also save the CPU cycles of parsing certificates that are already in use by other connections, although [Roland’s cryptobyte rewrite of the parser](https://go.dev/cl/274234) had made that way faster already.

This change has now landed in `master` and will be in Go 1.20 (unless we have to revert it) and it has zero exposed APIs: you just upgrade Go and every application that opens multiple TLS connections to the same endpoint will be automagically a little lighter and faster. ✨

Like for most Go standard library changes, a lot of the work was actually in a less visible part: we spent quite a bit of time discussing whether this change had backwards compatibility issues, because the certificates you get from `PeerCertificates` are now shared between connections, and what happens if you modify one? We concluded this is fine because it was already the case that some certificates in the chain could be shared between connections, for example if they referred to the roots or intermediates `CertPool`. [We added an explicit note about it to the docs, too.](https://go.dev/cl/427155)

![The Central Park fountain with the sun shining behind it and lighting up the water. In the distance, trees and a couple of the tall square skyscrapers. The bottom half is filled by the reflection of the fountain in the water.](https://words.filippo.io/content/images/2022/11/photo---1.jpeg)

---

文章来源: https://words.filippo.io/dispatches/certificate-interning/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
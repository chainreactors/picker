---
title: How Cloudflare runs machine learning inference in microseconds
url: https://buaq.net/go-169406.html
source: unSafe.sh - 不安全
date: 2023-06-20
fetch_date: 2025-10-04T11:47:06.732902
---

# How Cloudflare runs machine learning inference in microseconds

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

![](https://8aqnet.cdn.bcebos.com/3f06c13f8445bf3b1d931ab68d69066d.jpg)

How Cloudflare runs machine learning inference in microseconds

Loading...
*2023-6-19 21:0:13
Author: [blog.cloudflare.com(查看原文)](/jump-169406.htm)
阅读量:16
收藏*

---

Loading...

* [![Austin Hartzheim](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/ah.jpg)](https://blog.cloudflare.com/author/austinhartzheim/)

![How Cloudflare runs machine learning inference in microseconds](https://blog.cloudflare.com/content/images/2023/06/image1-6.png)

Cloudflare executes an array of security checks on servers spread across our global network. These checks are designed to block attacks and prevent malicious or unwanted traffic from reaching our customers’ servers. But every check carries a cost - some amount of computation, and therefore some amount of time must be spent evaluating every request we process. As we deploy new protections, the amount of time spent executing security checks increases.

Latency is a key metric on which [CDNs](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) are evaluated. Just as we optimize network latency by provisioning servers in close proximity to end users, we also optimize processing latency - which is the time spent processing a request before serving a response from cache or passing the request forward to the customers’ servers. Due to the scale of our network and the diversity of use-cases we serve, our edge software is subject to demanding specifications, both in terms of throughput and latency.

Cloudflare's [bot management](https://www.cloudflare.com/learning/bots/what-is-bot-management/) module is one suite of security checks which executes during the hot path of request processing. This module calculates a variety of bot signals and integrates directly with our front line servers, allowing us to customize behavior based on those signals. This module evaluates every request for heuristics and behaviors indicative of bot traffic, and scores every request with several machine learning models.

To reduce processing latency, we've undertaken a project to rewrite our bot management technology, porting it from Lua to Rust, and applying a number of performance optimizations. This post focuses on optimizations applied to the machine-learning detections within the bot management module, which account for approximately 15% of the latency added by bot detection. By switching away from a garbage collected language, removing memory allocations, and optimizing our parsers, we reduce the P50 latency of the bot management module by 79μs - a 20% reduction.

## Engineering for zero allocations

Writing software without memory allocation poses several challenges. Indeed, high-level programming languages often trade memory management for productivity, abstracting away the details of memory management. But, in those details, are a number of algorithms to find contiguous regions of free memory, handle fragmentation, and call into the kernel to request new memory pages. Garbage collected languages incur additional costs throughout program execution to track when memory can be freed, plus pauses in program execution while the garbage collector executes. But, when performance is a critical requirement, languages should be evaluated for their ability to meet performance constraints.

### Stack allocation

One of the simplest ways to reduce memory allocations is to work with fixed-size buffers. Fixed-sized buffers can be placed on the stack, which eliminates the need to invoke heap allocation logic; the compiler simply reserves space in the current stack frame to hold local variables. Alternatively, the buffers can be heap-allocated outside the hot path (for example, at application startup), incurring a one-time cost.

Arrays can be stack allocated:

```
let mut buf = [0u8; BUFFER_SIZE];
```

Vectors can be created outside the hot path:

```
let mut buf = Vec::with_capacity(BUFFER_SIZE);
```

To demonstrate the performance difference, let's compare two implementations of a case-insensitive string equality check. The first will allocate a buffer for each invocation to store the lower-case version of the string. The second will use a buffer that has already been allocated for this purpose.

Allocate a new buffer for each iteration:

```
fn case_insensitive_equality_buffer_with_capacity(s: &str, pat: &str) -> bool {
	let mut buf = String::with_capacity(s.len());
	buf.extend(s.chars().map(|c| c.to_ascii_lowercase()));
	buf == pat
}
```

Re-use a buffer for each iteration, avoiding allocations:

```
fn case_insensitive_equality_buffer_with_capacity(s: &str, pat: &str, buf: &mut String) -> bool {
	buf.clear();
	buf.extend(s.chars().map(|c| c.to_ascii_lowercase()));
	buf == pat
}
```

Benchmarking the two code snippets, the first executes in ~40ns per iteration, the second in ~25ns. Changing only the memory allocation behavior, the second implementation is ~38% faster.

### Choice of algorithms

Another strategy to reduce the number of memory allocations is to choose algorithms that operate on the data in-place and store any necessary state on the stack.

Returning to our string comparison function from above, let's rewrite it operate completely on the stack, and without copying data into a separate buffer:

```
fn case_insensitive_equality_buffer_iter(s: &str, pat: &str) -> bool {
	s.chars().map(|c| c.to_ascii_lowercase()).eq(pat.chars())
}
```

In addition to being the shortest, this function is also the fastest. This function benchmarks at ~13ns/iter, which is just slightly slower than the 11ns used to execute `eq_ignore_ascii_case` from the standard library. And the standard library implementation similarly avoids buffer allocation through use of iterators.

### Testing allocations

Automated testing of memory allocation on the critical path prevents accidental use of functions or libraries which allocate memory. `dhat` is a crate in the Rust ecosystem that supports such testing. By setting a new global allocator, `dhat` is able to count the number of allocations, as well as the number of bytes allocated on a given code path.

```
/// Assert that the hot path logic performs zero allocations.
#[test]
fn zero_allocations() {
	let _profiler = dhat::Profiler::builder().testing().build();

	// Execute hot-path logic here.

	// Assert that no allocations occurred.
	dhat::assert_eq!(stats.total_blocks, 0);
	dhat::assert_eq!(stats.total_bytes, 0);
}
```

It is important to note, `dhat` does have the limitation that it only detects allocations in Rust code. External libraries can still allocate memory without using the Rust allocator. FFI calls, such as those made to C, are one such place where memory allocations may slip past `dhat`'s measurements.

## Zero allocation decision trees

CatBoost is an open-source machine learning library used within the bot management module. The core logic of CatBoost is implemented in C++, and the library exposes bindings to a number of other languages - such as C and Rust. The Lua-based implementation of the bot management module relied on FFI calls to the C API to execute our models.

By removing memory allocations and implementing buffer re-use, we optimize the execution duration of the sample model included in the CatBoost repository by 10%. Our production models see gains up to 15%.

### Optimize for single-document evaluation

By optimizing CatBoost to evaluate a single set of features at a time, we reduce memory allocations and reduce latency. The CatBoost API has several functions which are optimized for evaluating multiple documen...
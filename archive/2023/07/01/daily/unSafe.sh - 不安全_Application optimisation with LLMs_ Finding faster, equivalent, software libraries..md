---
title: Application optimisation with LLMs: Finding faster, equivalent, software libraries.
url: https://buaq.net/go-170911.html
source: unSafe.sh - 不安全
date: 2023-07-01
fetch_date: 2025-10-04T11:51:08.176275
---

# Application optimisation with LLMs: Finding faster, equivalent, software libraries.

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

![](https://8aqnet.cdn.bcebos.com/daaa259e184054f9b956bdeb23a58944.jpg)

Application optimisation with LLMs: Finding faster, equivalent, software libraries.

A few months back I wrote a blog post where I mentioned that the least-effor
*2023-6-30 19:33:27
Author: [sean.heelan.io(查看原文)](/jump-170911.htm)
阅读量:17
收藏*

---

A few months back I wrote a [blog post](https://sean.heelan.io/2023/02/14/combining-static-and-dynamic-analysis-in-performance-optimisation-part-1-60-improvements-with-continuous-profiling-and-library-matching/) where I mentioned that the least-effort/highest reward approach to application optimisation is to deploy a whole-system profiler across your clusters, look at the most expensive libraries & processes, and then search Google for faster, equivalent replacements. At Optimyze/Elastic we have had customers of our [whole-system profiler](https://www.elastic.co/observability/universal-profiling) use this approach successfully on numerous occasions. The only difficulty with this approach is the amount of Googling for alternatives that you need to do, followed by even more Googling for comparative benchmarks. If only we had a compressed version of all information on the internet, and an interface that allowed for production of free-form text based on that!

As you’ve probably gathered: we do. OpenAI’s, and other’s, Large Language Models (LLMs), have been trained on a huge amount of the internet, including the blurbs describing a significant number of available software libraries, as well as benchmarks comparing them, and plenty of other relevant content in the form of blogs, StackOverflow comments, and Github content.

So why use an LLM as a search interface when you could just Google for the same information? There are a couple of reasons. The first is that an LLM provides a much broader set of capabilities than just search. You can, for example, ask something like *“Find me three alternative libraries, list the pros and cons of each, and then based on these pros and cons make a recommendation as to which I should use.”*. Thus, we can condense the multistep process of Googling for software and benchmarks, interpreting the results, and coming up with a recommendation, into a single step. The second reason is that because LLMs have a natural language input/output interface, it is far easier to programatically solve the problem and make use of the result than if we had to use Google’s API, scrape web pages, extract information, and then produce a report.

If you’d like to try this out, a couple of days ago I open sourced sysgrok ([blog](https://www.elastic.co/blog/open-sourcing-sysgrok-ai-assistant), [code](https://github.com/elastic/sysgrok)), a tool intended to help with automating solutions to systems analysis and understanding. It is organised into a series of subcommands, one of which is called *findfaster*. The *findfaster* subcommand uses a prompt that asks the question mentioned above. Here’s an example of using it to find a faster replacement for libjpeg.

[![](https://sean.heelan.io/wp-content/uploads/2023/06/screenshot-2023-06-30-at-11.57.01.png?w=887)](https://sean.heelan.io/wp-content/uploads/2023/06/screenshot-2023-06-30-at-11.57.01.png)

sysgrok also has a “–chat” parameter which will drop you into a chat session with the LLM after it has produced an initial response. This can be used to ask for clarification on recommendations, correct mistakes the LLM has made etc. For example, here we ask for replacements for Python’s stdlib JSON library. The LLM responds with three good alternatives (ujson, orjson, simdjson), and recommends we use the best of them (orjson). We then drop into a chat session and ask the LLM how to install and use the library.

[![asciicast](https://asciinema.org/a/593479.svg)](https://asciinema.org/a/593479)

Usually this works really well, and is the best automated solution to this problem that I have come across. That said, we are using an LLM, so it can go amusingly wrong at times. The most common way for it to fail is the wholesale hallucination of software projects. This is prone to happening when there are limited, or no, alternatives to the target software which provide the same functionality but better performance. A good example of this is *libtiff*. If you ask findfaster to find you a faster version of libtiff you’ll may be used to consider TurboTiff. TurboTiff is not a software project.

[![](https://sean.heelan.io/wp-content/uploads/2023/06/screenshot-2023-06-30-at-12.19.47.png?w=645)](https://sean.heelan.io/wp-content/uploads/2023/06/screenshot-2023-06-30-at-12.19.47.png)

If you use sysgrok and it comes back with a bad recommendation then I’d love to hear about it, as these examples are helpful in refining the prompts. You can open an issue on GitHub [here](https://github.com/elastic/sysgrok/issues).

文章来源: https://sean.heelan.io/2023/06/30/application-optimisation-with-llms-finding-faster-equivalent-software-libraries/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
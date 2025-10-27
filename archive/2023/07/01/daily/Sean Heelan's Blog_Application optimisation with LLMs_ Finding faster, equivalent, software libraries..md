---
title: Application optimisation with LLMs: Finding faster, equivalent, software libraries.
url: https://sean.heelan.io/2023/06/30/application-optimisation-with-llms-finding-faster-equivalent-software-libraries/
source: Sean Heelan's Blog
date: 2023-07-01
fetch_date: 2025-10-04T11:54:41.598139
---

# Application optimisation with LLMs: Finding faster, equivalent, software libraries.

[Skip to content](#content)

Open Menu

* [Home](https://sean.heelan.io/)
* [All Posts](https://sean.heelan.io/posts/)
* [Research & Publications](https://sean.heelan.io/research/)
* [About Me](https://sean.heelan.io/about-me/)

*Search*

Search for:

 Close

[![](https://sean.heelan.io/wp-content/uploads/2023/02/logo_ireland-1.jpg)](https://sean.heelan.io/)

# [Sean Heelan's Blog](https://sean.heelan.io/)

## Software Exploitation and Optimisation

[AI](https://sean.heelan.io/category/ai/) / [Performance Optimisation](https://sean.heelan.io/category/performance-optimisation/)

# Application optimisation with LLMs: Finding faster, equivalent, software libraries.

[June 30, 2023June 30, 2023](https://sean.heelan.io/2023/06/30/application-optimisation-with-llms-finding-faster-equivalent-software-libraries/) [seanhn](https://sean.heelan.io/author/seanhn/)

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

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://sean.heelan.io/2023/06/30/application-optimisation-with-llms-finding-faster-equivalent-software-libraries/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://sean.heelan.io/2023/06/30/application-optimisation-with-llms-finding-faster-equivalent-software-libraries/?share=x)

Like Loading...

### *Related*

# Post navigation

[Previous Post

Finding 10x+ Performance Improvements in C++ with CodeQL – Part 2/2 on Combining Dynamic and Static Analysis for Performance Optimisation](https://sean.heelan.io/2023/03/01/finding-10x-performance-improvements-in-c-with-codeql-part-2-2-on-combining-dynamic-and-static-analysis-for-performance-optimisation/)

[Next Post

How I used o3 to find CVE-2025-37899, a remote zeroday vulnerability in the Linux kernel’s SMB implementation](https://sean.heelan.io/2025/05/22/how-i-used-o3-to-find-cve-2025-37899-a-remote-zeroday-vulnerability-in-the-linux-kernels-smb-implementation/)

[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)

[*Back to top*](#top)

* Reblog
* Subscribe
  Subscribed

  + [![](https://sean.heelan.io/wp-content/uploads/2009/05/cropped-oxford_7602.jpg?w=50) Sean Heelan's Blog](https://sean.heelan.io)

  Join 44 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fsean.heelan.io%252F2023%252F06%252F30%252Fapplication-optimisation-with-llms-finding-faster-equivalent-software-libraries%252F)
* + [![](https://sean.heelan.io/wp-content/uploads/2009/05/cropped-oxford_7602.jpg?w=50) Sean Heelan's Blog](https://sean.heelan.io)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fsean.heelan.io%252F2023%252F06%252F30%252Fapplication-optimisation-with-llms-finding-faster-equivalent-software-libraries%252F)
  + [Copy shortlink](https://wp.me/pw5Z4-Ko)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://sean.heelan.io/2023/06/30/application-optimisation-with-llms-finding-faster-equivalent-software-libraries/)
  + [View post in Reader](https://wordpress.com/reader/blogs/7649502/posts/2876)
  + [Manage subscriptions](https://subscribe.wordpress.com/)
  + Collapse this bar

##

##

Loading Comments...

Write a Comment...

Email (Required)

...
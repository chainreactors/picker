---
title: Anti-AI tricks, Part 1
url: https://www.hexacorn.com/blog/2026/11/15/anti-ai-tricks-part-1/
source: Hexacorn
date: 2026-11-15
fetch_date: 2026-11-16T08:48:00.731409
---

# Anti-AI tricks, Part 1

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2026/10/25/ripgrep-as-a-lolbin/)

# Anti-AI tricks, Part 1

Posted on [2026-11-15](https://www.hexacorn.com/blog/2026/11/15/anti-ai-tricks-part-1/ "1:54 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Over a decade (or two, or three) ago we (reversers) used to face a lot of anti-reversing tricks. At that time many of them targeted both manual and automated reversing efforts (including debugging, monitoring, sandboxing). If you follow this blog for a while, you probably know that I described many novelty tricks of this sort on this this blog in the past…

Today, AI-based reverse engineering tools are changing the game and in most cases have replaced manual reversing efforts. As a result, one can simply throw a sample at AI-based ‘sandbox’ and get a very comprehensive report back pretty quickly. It must be noted (and appreciated) that these reports tend to be of high quality and they seem to (almost) effortlessly address most of the typical reversing questions:

* can the function/role of each submitted file be determined?
* what files in the submitted package / archive are malicious?
* for each file that includes code for multiple platforms, can all of them be analyzed?
* for each identified file of interest, can it be analyzed in depth from an adversarial point of view?
* does any file in the submitted sampleset include any interesting data? config? iocs? logs? keylogger files? encrypted strings?
* what functionality / business logic can we see implemented?
* is there a C2 functionality? what protocol does it follow? any built-in redundancies?
* is there a code to load additional modules? are they loaded from the network, file system, memory?
* what is the list of IOCs?
* etc.

I must say, I am super-impressed by AI reverse engineering capabilities, and in recent months I got beaten by AI on more than one occasion. Ouch.

BUT

It obviously made me think that there must be a way to make AI-based analysis a bit less reliable.

And this is where this post begins.

I hypothesized that I could build a program with a lot of entry points seen by AI, where the REAL entry point would be chosen during a run-time by a result of a predictable calculation that AI may not know about. That is, feed AI with a lot of possible outcomes, but when it comes to real world, just execute one code branch that is predictable and deterministic.

So, the idea is simple.

Build many code blocks. Execute only one.

For the testing purposes, I created a very simple assembly program that prints a message on the screen. What message it chooses to print is dependent on an input value chosen during a runtime, and one that is most likely impossible for AI to guess. One can use a slow mathematical calculation to choose it (same as traditional anti-sandbox stalling routines), or call an [API that delivers a predictable return value](https://www.hexacorn.com/blog/2019/04/27/returning-the-call-moshi-moshi-the-api-way-a-k-a-api-cold-calling-part-2/).

My test program calls *FreeResource* API that is known to return 0 as a default. This value determines the message shown on the screen that is one of the following:

* Hello00 –> show this message
* Hello01
* Hello02
* Hello03
* Hello04
* Hello05
* Hello06
* Hello07
* Hello08
* Hello09
* Hello0a
* Hello0b
* Hello0c
* Hello0d
* Hello0e
* Hello0f

and it is obviously ‘Hello00’:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti_ai_1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti_ai_1.png)

It must be noted that any traditional sandbox that executes samples in a controlled environment won’t be fooled by this lame trick and the report will undeniably show the correct result.

However. AI-based malware analysis tools often rely on static analysis only and as such, their reports can be manipulated.

Throwing this sample at freely available ChatGPT and Claude consoles (I ignore models here!) gives us these results:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti_ai_1_chatgpt.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti_ai_1_chatgpt.png)

and

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti_ai_1_claude.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti_ai_1_claude.png)

We can immediately see 3 things:

* AI can’t determine the value returned by the *FreeResource* API
* we can introduce a lot of noise in the final report by just adding a lot of ‘dead’ code that will never get executed, but will be ‘seen’ and will end up being described by AI
* AI may not always ‘understand’ the code it ‘sees’

In a more advanced scenario, we could use encrypted position independent code that is decrypted during run-time using a key derived from a predictable value and that would render lots of AI-based static analysis either useless, or would require additional work (introducing extra complexity, a need for more iterations, code passes, etc.).

We are entering an interesting era where reverse engineering is a solved problem, but only if the code creators allow it. It is not impossible that we will see an emergence of new types of code protectors soon…

This entry was posted in [Anti-\*](https://www.hexacorn.com/blog/category/anti/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/11/15/anti-ai-tricks-part-1/ "Permalink to Anti-AI tricks, Part 1").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
---
title: Anti-AI tricks, Part 2
url: https://www.hexacorn.com/blog/2026/11/20/anti-ai-tricks-part-2/
source: Hexacorn
date: 2026-11-20
fetch_date: 2026-11-21T09:00:29.005499
---

# Anti-AI tricks, Part 2

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

[← Previous](https://www.hexacorn.com/blog/2026/11/15/anti-ai-tricks-part-1/)

# Anti-AI tricks, Part 2

Posted on [2026-11-20](https://www.hexacorn.com/blog/2026/11/20/anti-ai-tricks-part-2/ "11:49 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Today I tried to see if AI can ‘understand’ .TLS callbacks. These are almost obsolete now, but back in a day they were used heavily for various anti-reversing and even anti-rootkits tricks. The idea is simple: since .tls callbacks execute before the ‘main’, we can use them to run some code that may mislead/misdirect the analysis…

So, I wrote a simple test assembly program that included one .tls callback routine. When that callback is executed, the program shows a message box. The routine then increments a value of a global counter that is initiated with 0. When the main routine of a program is executed, it checks if the value of that global counter is 0; if it is, it shows a different message box, otherwise – it just exits.

When I submitted the sample to Claude and ChatGPT neither of them were fooled and they both, and almost instantly reported that the message shown by the program is the one provided by the .tls callback…

Ouch.

Looks like old file format tricks are not gonna cut it in this series…

This entry was posted in [Anti-\*](https://www.hexacorn.com/blog/category/anti/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/11/20/anti-ai-tricks-part-2/ "Permalink to Anti-AI tricks, Part 2").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
---
title: Writing a Frida-based VBS API monitor, Take two
url: https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor-take-two/
source: Hexacorn
date: 2024-07-08
fetch_date: 2025-10-06T17:40:55.231559
---

# Writing a Frida-based VBS API monitor, Take two

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

[← Previous](https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor/)
[Next →](https://www.hexacorn.com/blog/2024/07/14/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise/)

# Writing a Frida-based VBS API monitor, Take two

Posted on [2024-07-07](https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor-take-two/ "6:34 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In my previous [post](https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor/) I introduced a simple VBS API Monitor developed using Frida framework.

Today I did some more code analysis of *vbscript.dll* and I realized that in my previous post I made a naive assumption that arguments are passed to VBS callback functions using the same conventions like Windows API.

It turns out that the arguments are passed via the argument 2 (r8 on 64-bit Windows), and the number of arguments is passed in the argument 1 (rdx on 64-bit Windows). So, we can get the value of argument 1, and then use it to loop over the memory region pointed to by r8. All arguments are placed every 24 bytes (8×3).

Additionally, I discovered that there is one more VARIANT type that indicates string arguments passed by reference. I have added it to the code as well, so now all the functions show proper arguments.

With these changes in place we get this (for the test script from the previous post):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs8.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs8.png)

The updated IDAPython script can be found [here](https://hexacorn.com/d/vbs_frida_2.py).

This entry was posted in [Frida](https://www.hexacorn.com/blog/category/frida/), [Sandboxing](https://www.hexacorn.com/blog/category/sandboxing/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor-take-two/ "Permalink to Writing a Frida-based VBS API monitor, Take two").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
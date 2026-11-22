---
title: Anti-AI tricks, Part 3
url: https://www.hexacorn.com/blog/2026/11/21/anti-ai-tricks-part-3/
source: Hexacorn
date: 2026-11-21
fetch_date: 2026-11-22T09:02:17.112817
---

# Anti-AI tricks, Part 3

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

[← Previous](https://www.hexacorn.com/blog/2026/11/20/anti-ai-tricks-part-2/)

# Anti-AI tricks, Part 3

Posted on [2026-11-21](https://www.hexacorn.com/blog/2026/11/21/anti-ai-tricks-part-3/ "11:26 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

After my last [test](https://www.hexacorn.com/blog/2026/11/20/anti-ai-tricks-part-2/) I tried one more .tls trick.

I built a test program that pretends to call FindWindowA function with some non-sensical arguments. When the program starts, the .tls callback is executed first and I use it to swap the pointer to FindWindowA function with a function address of MessageBoxA. Then the main function executes MessageBoxA instead of FindWindowA. A message box pops up.

Claude analysis nailed it:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti-ai-4_1-1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti-ai-4_1-1.png)

Note how it highlighted all the right things:

* program sections are writable (yup, I marked them like this)
* .tls callback patch is fully understood, and its intentions and inner working – fully explained
* it even highlights the presence of arguments that are more fitting for MessageBoxA than FindWindowA function
* last, but not least – it ”sees’ all my mischievous intentions and comments on that, too

The ChatGPT session is not too impressive though:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti-ai-4_2-522x1024.png)](https://www.hexacorn.com/blog/wp-content/uploads/2026/11/anti-ai-4_2.png)

It is more of a guess work than the walk through I expected and witnessed with Claude, but in the end, it still kinda gets it right.

I guess there is still some scope for fooling some AI analysis, especially if we introduce many patches, perhaps even overlapping ones, and for programs with a more complex business logic than my basic test files…

Still, I think I am losing this battle…

This entry was posted in [Anti-\*](https://www.hexacorn.com/blog/category/anti/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/11/21/anti-ai-tricks-part-3/ "Permalink to Anti-AI tricks, Part 3").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
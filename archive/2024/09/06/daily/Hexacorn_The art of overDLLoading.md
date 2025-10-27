---
title: The art of overDLLoading
url: https://www.hexacorn.com/blog/2024/09/05/the-art-of-overdlloading/
source: Hexacorn
date: 2024-09-06
fetch_date: 2025-10-06T18:26:48.126619
---

# The art of overDLLoading

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

[← Previous](https://www.hexacorn.com/blog/2024/09/05/technical-debt-of-cwindowssystem-path/)
[Next →](https://www.hexacorn.com/blog/2024/09/06/the-art-of-underdlloading/)

# The art of overDLLoading

Posted on [2024-09-05](https://www.hexacorn.com/blog/2024/09/05/the-art-of-overdlloading/ "11:05 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Some time ago I came up with a silly idea: i’d like to build an executable that statically links to most of the c:\windows\system32 libraries. It’s a non-sensical programming exercise, but it’s also an interesting challenge.

Forcing a static import of so many libraries into a single executable is actually a non-trivial task, and there are many approaches we can take to do it. Most of the high-level language-based avenues one can pursue here are kinda problematic though, because they are full of custom library building aka lots of troubleshooting. After looking at various programming languages I have eventually found myself looking at the assembly language compilers available out there. The incredible simplicity of generating your own, customized import tables offered by fasm immediately caught my attention.

With a bit of python foo and fasm compilation magic, I was able to build this [monster](https://www.virustotal.com/gui/file-analysis/NTliY2ZhZjM4ZGU1MDk5ZmMwNjcwOTlhYjMwM2E4ZmI6MTcyNTU3NjYyNQ%3D%3D) (79K APIs):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/overDLLoader.gif.gif)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/overDLLoader.gif.gif)

I am not 100% sure it is a correct PE file (in terms of all structures filled in properly), but it seems to run on windows 11 (with a caveat that it reports a critical error).

If you are wondering what is the purpose of this exercise, I’d like to throw a few ideas:

* linking to many OS-dependent libraries could be an interesting guardrail technique
* it may break tools (it would seem it breaks python’s pefile module and it causes problems to decompilers)
* it is a great learning exercise about a PE file format; after so many years of dealing with it I am still surprised how much I don’t know about it

And here’s the import table as seen by Ida:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/overdlloaded.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/overdlloaded.png)

An attempt to copy these function names to clipboard pretty much freezes the program.

This entry was posted in [Anti-Forensics](https://www.hexacorn.com/blog/category/anti-forensics/), [File Formats ZOO](https://www.hexacorn.com/blog/category/file-formats-zoo/), [Random ideas](https://www.hexacorn.com/blog/category/random-ideas/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/09/05/the-art-of-overdlloading/ "Permalink to The art of overDLLoading").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
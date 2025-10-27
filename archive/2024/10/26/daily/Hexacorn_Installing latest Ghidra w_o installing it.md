---
title: Installing latest Ghidra w/o installing it
url: https://www.hexacorn.com/blog/2024/10/25/installing-latest-ghidra-w-o-installing-it/
source: Hexacorn
date: 2024-10-26
fetch_date: 2025-10-06T18:52:17.729075
---

# Installing latest Ghidra w/o installing it

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

[← Previous](https://www.hexacorn.com/blog/2024/10/19/beyond-good-ol-run-key-part-143/)
[Next →](https://www.hexacorn.com/blog/2024/10/25/going-reverse-on-reversing-tools/)

# Installing latest Ghidra w/o installing it

Posted on [2024-10-25](https://www.hexacorn.com/blog/2024/10/25/installing-latest-ghidra-w-o-installing-it/ "10:18 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Today I wanted to upgrade my Ghidra setup so I downloaded its latest version. Now, I really don’t like running installers in general, because they clutter the system and the Registry, so I was nicely surprised when I learned that both the latest version of Ghidra, and also latest version of Java’s JDK that Ghidra requires can be downloaded as a ZIP file (aka portable version)…

So, with that in mind, it turns out that today you can install Ghidra in a portable way w/o running any installers! All you have to do is this:

* Download *https://download.oracle.com/java/23/latest/jdk-23\_windows-x64\_bin.zip* and unpack it to say *c:\jdk-23.0.1\*
* Download *https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra\_11.2\_build/ghidra\_11.2\_PUBLIC\_20240926.zip* and unpack it to say *c:\ghidra\_11.2\_PUBLIC\*
* You then run:

```
cmd.exe
cd c:\ghidra_11.2_PUBLIC\
path=c:\jdk-23.0.1\bin;%PATH%
ghidraRun
```

That’s it!

When you launch Ghidra this way, you will soon be seeing the familiar EULA window:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/ghidra2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/ghidra2.png)

and after accepting it, you are all set:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/ghidra3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/10/ghidra3.png)

This entry was posted in [Ghidra](https://www.hexacorn.com/blog/category/ghidra/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/10/25/installing-latest-ghidra-w-o-installing-it/ "Permalink to Installing latest Ghidra w/o installing it").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
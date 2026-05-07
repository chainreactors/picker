---
title: 1 little known secret of forfiles.exe, part 2
url: https://www.hexacorn.com/blog/2026/05/06/1-little-known-secret-of-forfiles-exe-part-2/
source: Hexacorn
date: 2026-05-06
fetch_date: 2026-05-07T05:33:39.079225
---

# 1 little known secret of forfiles.exe, part 2

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

[← Previous](https://www.hexacorn.com/blog/2026/04/22/some-unintelligent-fun-with-ms-notepad-protocol/)

# 1 little known secret of forfiles.exe, part 2

Posted on [2026-05-06](https://www.hexacorn.com/blog/2026/05/06/1-little-known-secret-of-forfiles-exe-part-2/ "9:12 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In this [old post](https://www.hexacorn.com/blog/2023/12/31/1-little-known-secret-of-forfiles-exe/) I have demonstrated how to abuse *forfiles.exe* to run your ‘cmd.exe’ of choice.

There is one more trick we can do with this tool.

When *forfiles.exe* enumerates the files it executes a default command *cmd /c echo @file*. It turns out that the execution of this command expands environment variables as well…

So…

If we create a file called *%foo%*, and make sure that there is an environmental variable called *foo,* we can now control the *cmd /c echo @file* command and force it to do some unusual stuff.

For example:

* create a file called *%foo%*
* set *foo* to *“&calc.exe&”*
* run *forfiles*

– it will enumerate files in a directory, print their names, and when it will come across the *%foo%* file, it will also … execute calculator…

This happens because *cmd /c echo @file* gets expanded to *cmd /c echo %foo%* which in turn will be executed as “echo *“&calc.exe&”*“.

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/05/06/1-little-known-secret-of-forfiles-exe-part-2/ "Permalink to 1 little known secret of forfiles.exe, part 2").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
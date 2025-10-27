---
title: This post is totally Iconic
url: https://www.hexacorn.com/blog/2024/09/07/this-post-is-totally-iconic/
source: Hexacorn
date: 2024-09-08
fetch_date: 2025-10-06T18:23:06.690587
---

# This post is totally Iconic

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

[← Previous](https://www.hexacorn.com/blog/2024/09/06/the-art-of-underdlloading/)
[Next →](https://www.hexacorn.com/blog/2024/09/11/rundll32-exe-bomb/)

# This post is totally Iconic

Posted on [2024-09-07](https://www.hexacorn.com/blog/2024/09/07/this-post-is-totally-iconic/ "10:32 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Over 6 years ago I decided to pursue yet another silly idea: extract all the unique .ico files from PE resources from as many samples as I can. This exercise yielded ~450K unique .ico files. If I remember correctly, the original idea was that I may somehow leverage them in my research & detection efforts (yara, malware family clustering, etc.), but when I came across this old, sad folder today it quickly dawned on me that I am quite good at extracting meaningful data, but even better at forgetting about it.

Calculating the number of all .ico files I gathered in that folder quickly lead me to an astonishing discovery: the total number of all files is very close to a square root of (NUMBER\_OF\_THE\_BEAST+1). Using a quick & dirty Python script I borrowed from StackOverflow I have created a PNG file that exposes the results of this old work to the world. Using a sophisticated algorithm that reads the .ico file, resamples it to 16×16 square and appends it to the final picture, I was able to build this final, iconic, 200MB in size, PNG file:

[iconic.png](https://hexacorn.com/d/iconic.png) (667 x 667)

I do not claim any copyright.

This entry was posted in [Silly](https://www.hexacorn.com/blog/category/silly/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/09/07/this-post-is-totally-iconic/ "Permalink to This post is totally Iconic").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
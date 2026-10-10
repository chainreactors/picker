---
title: Solving practical problems with AI – Part 1 – Jpeg files renaming using EXIF data
url: https://www.hexacorn.com/blog/2026/10/09/solving-practical-problems-with-ai-part-1-jpeg-files-renaming-using-exif-data/
source: Hexacorn
date: 2026-10-09
fetch_date: 2026-10-10T07:56:47.696014
---

# Solving practical problems with AI – Part 1 – Jpeg files renaming using EXIF data

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

[← Previous](https://www.hexacorn.com/blog/2026/10/03/the-boring-state-of-stalled-timelines/)

# Solving practical problems with AI – Part 1 – Jpeg files renaming using EXIF data

Posted on [2026-10-09](https://www.hexacorn.com/blog/2026/10/09/solving-practical-problems-with-ai-part-1-jpeg-files-renaming-using-exif-data/ "11:05 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I don’t write about AI much, because everyone else does. I use it though, more and more, despite being a dedicated late adopter of new technologies, by choice.

I thought it would be interesting to post examples of various practical (often cyber-related) problems, that often require some scripting / programming work done to be solved. Problems that in the past would take a few good hours of work to research, iteratively develop an early prototype script code, test it, troubleshoot it and finalize it so it can be successfully used to solve that given problem. And then I would post it on this blog. And yes, in the past I posted many manually written scripts here, and they were always a result of my many human cycles that I spent on creating them…

It turns out, today many of these practical problems can be solved by AI within less than 5 minutes…

I recently got a few hundred JPEG unsorted image files that I wanted to sort by the time of their creation. My solution idea was simple: add a prefix to all these files using a ISO 8601-like timestamp that I would extract from the EXIF data of each file… In the past a ‘simple’ idea like that would lead me to look at [EXIF](https://en.wikipedia.org/wiki/Exif) specification, [jpeg](https://en.wikipedia.org/wiki/JPEG) file format, existing jpeg/exif handling python/perl modules, and of course, potentially many existing solutions to this known problem, including many code snippets all over the place that I could quickly adapt to my needs.

In 2026 all of this potential work was replaced by a simple ChatGPT prompt:

> write a python script that enumerates all image files in the directory, recognizes jpeg files, extracts exif info and uses exif timestamp to rename the file to a format yyyy-MM-dd\_hh-mm-ss\_ followed by the old file name

The [script generated](https://hexacorn.com/d/jpeg_add_exif_timestamp_prefix.py) by this prompt not only worked ‘out of the box’ – that is, worked like a charm and helped me to rename the image files the way I wanted. It actually included some code that I didn’t expect. For instance, it handled 3 different exif timestamps “DateTimeOriginal”, “DateTimeDigitized”, “DateTime” that are associated with ‘image creation’ event. Secondly, it handled cases where the input file has been already a subject to a previous run of the script (avoiding adding multiple timestamp-based prefixes). It also made sure it doesn’t overwrite files if the ‘newly generated filename’ was identical with an existing file. Pretty clever. Doing far more than I would if it was my usual quick&dirty scripting exercise. And lo, and behold, it included comments and handled help/dry-run command line arguments too.

The AI technology can be seen as an amazing catalyst, prototyping and rapid development booster and performance multiplier. This can be true.

BUT

You need to know what you want. And for that, you need to know the foundations.

AND

You need to be able to check what you get (what AI produces). I actually did a full code review of the generated script before I executed it the first time. This is to make sure there are no surprises.

This entry was posted in [AI/ML](https://www.hexacorn.com/blog/category/ai-ml/), [Software Releases](https://www.hexacorn.com/blog/category/software-releases/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/10/09/solving-practical-problems-with-ai-part-1-jpeg-files-renaming-using-exif-data/ "Permalink to Solving practical problems with AI – Part 1 – Jpeg files renaming using EXIF data").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
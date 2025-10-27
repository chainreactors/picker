---
title: Optimizing the regexes, or not
url: https://www.hexacorn.com/blog/2025/02/22/optimizing-the-regexes-or-not/
source: Hexacorn
date: 2025-02-23
fetch_date: 2025-10-06T20:36:05.093160
---

# Optimizing the regexes, or not

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

[← Previous](https://www.hexacorn.com/blog/2025/02/21/the-rapidly-changing-geopolitics-and-its-inevitable-effect-on-cyber/)
[Next →](https://www.hexacorn.com/blog/2025/02/22/good-exports-are-real/)

# Optimizing the regexes, or not

Posted on [2025-02-22](https://www.hexacorn.com/blog/2025/02/22/optimizing-the-regexes-or-not/ "10:57 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Every once in a while we all contemplate solving interesting yet kinda abstract threat hunting problems. This post describes one of these…

The problem:

**Given a relatively long number of strings, how do you write a regular expression that covers them all, but doesn’t hit on any other string?**

The context:

I have extracted file names associated with kernel drivers referenced by all the .inf files present inside all of (unpacked) archives that can be found inside the [DriverPack](https://driverpack.tilda.ws/main-page).

The rationale:

Hunting for new kernel drivers introduced to the environment may be easier if I can extract kernel driver names from the telemetry, and only report creation of these that reference files that are NOT present on the ‘known list of good kernel driver file names’.

The solution:

Looking for existing tools that may help to address this problem in a generic way I came across this perl module – [Regexp::Optimizer](https://metacpan.org/release/DANKOGAI/Regexp-Optimizer-0.15/view/lib/Regexp/Optimizer.pm). To my surprise, it actually works quite nicely.

I gave it [7.5K file names](https://hexacorn.com/d/ServiceBinary2su.txt) associated with ‘known clean kernel module drivers’ and it gave me the following [regex](https://hexacorn.com/d/regex.txt). I have tested all the file names from the ‘ServiceBinary2su.txt’ file and the regex worked well. This is the test script:

> use strict;
> use warnings;
> use utf8;
>
> $| = 1;
>
> my $f=’regex.txt’;
> open F,”<$f”;
> binmode F;
> read F,my $regex,-s $f;
> close F;
>
> my $x=shift;
> if ($x=~/^$regex.sys$/i)
> {
>  print (“$x matched\n”);
> }
> else
> {
>  print (“$x didn’t match\n”);
> }

The final regex is 52624 bytes long. The input data was 103317 bytes long (including new lines). We have achieved a 51% ‘compression rate’, but debugging of such a complicated regex pattern sounds like a heck of a job. It would seem that sometimes solving interesting yet kinda abstract threat hunting problems brings more confusion to the process than we anticipate… And getting fixated on using regexes to solve this kind of problem is actually a bigger problem itself. The multi-pattern search-oriented trie structures are far more suitable to solve this sort of multi-pattern search/comparisons.

This entry was posted in [Threat Hunting](https://www.hexacorn.com/blog/category/threat-hunting/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/02/22/optimizing-the-regexes-or-not/ "Permalink to Optimizing the regexes, or not").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
---
title: Good Exports are real
url: https://www.hexacorn.com/blog/2025/02/22/good-exports-are-real/
source: Hexacorn
date: 2025-02-23
fetch_date: 2025-10-06T20:36:03.676123
---

# Good Exports are real

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

[← Previous](https://www.hexacorn.com/blog/2025/02/22/optimizing-the-regexes-or-not/)
[Next →](https://www.hexacorn.com/blog/2025/02/23/string-analysis-for-n00bs/)

# Good Exports are real

Posted on [2025-02-22](https://www.hexacorn.com/blog/2025/02/22/good-exports-are-real/ "11:24 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Collecting ‘good’ samples helps to discover a lot interesting patterns. In my [old post](https://www.hexacorn.com/blog/2022/07/02/driverpack-clean-pdb-paths/) I focused on the PDB paths extracted from the DriverPack driver collection, [yesterday I touched](https://www.hexacorn.com/blog/2025/02/22/optimizing-the-regexes-or-not/) on the list of ‘file names associated with good known kernel drivers’, and today I will cover the function names exported by a very large corpora of ‘good’ DLL samples.

You may ask what is the value here, and I can answer that ‘this is how the normal looks like’.

How is that useful to the Threat Hunting crowd?

If you monitor rundll32 invocations referencing DLLs and their API functions you may quickly discover a lot of anomalies. Any invocation referring to a non-OS DLL is suspicious. Any invocation referring to a DLL in a suspicious location is… suspicious. Any process using [unusual constructs](https://www.hexacorn.com/blog/2024/09/21/rundll32-goes-to-hell/) is suspicious. Any process invoking DLL exported functions via ordinal numbers is suspicious. Any process referencing API ordinals via [negative or large ordinal numbers](https://www.hexacorn.com/blog/2020/02/05/stay-positive-lolbins-not/) is super-suspicious, too.

These are great ‘suspicious’ tests, but we can do more.

The ‘StartW’ export used by Cobalt Strike DLLs is a good example. Invocations of this function are not necessarily ‘suspicious’ by default, because we don’t have a point of reference. There are so many legitimate invocations of rundll32 executing exported functions from so many DLLs that it’s hard to zoom-in on this particular function and declare that it’s bad. Again, we need a point of reference, of sort.

The list of functions exported by ‘good’ DLLs is far longer than expected: 11375507 unique entries, with many very popular and some only occurring once. You can download an archived text file referencing many ‘good export names’ from [here](https://github.com/hexacorn/clean_exports/releases/download/v0.0.1/exported_functions_sorted.zip).

There are so many uses for this set:

* known-good names for threat hunting purposes
* a very fertile ground for a deeper lolbin research
* a very fertile ground for discovering new vulnerabilities

The set is watermarked hence you have been warned. You cannot use this set for any commercial reason. You cannot create any commercial detection based on this data. The only exceptions are: fully unlimited use by law enforcement, and for educational and non-commercial research purposes only.

This entry was posted in [Threat Hunting](https://www.hexacorn.com/blog/category/threat-hunting/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/02/22/good-exports-are-real/ "Permalink to Good Exports are real").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
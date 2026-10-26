---
title: ripgrep as a lolbin
url: https://www.hexacorn.com/blog/2026/10/25/ripgrep-as-a-lolbin/
source: Hexacorn
date: 2026-10-25
fetch_date: 2026-10-26T07:18:39.399399
---

# ripgrep as a lolbin

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

[← Previous](https://www.hexacorn.com/blog/2026/10/24/solving-practical-problems-with-ai-part-2-the-most-popular-and-most-commonly-used-passwords-for-malicious-archives/)

# ripgrep as a lolbin

Posted on [2026-10-25](https://www.hexacorn.com/blog/2026/10/25/ripgrep-as-a-lolbin/ "1:11 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This is a lesser known feature of ripgrep that can be used to spawn your own executable via proxy. All you have to do is to run ripgrep with a ‘-z/–search-zip’ flag. Once you do it, any archive file that ripgrep comes across (and supports) will be preprocessed with a decompression tool as per the below [list](https://github.com/BurntSushi/ripgrep/blob/6892bc2b7efe5909cbbeec8f757ed2c4c76b1d30/crates/cli/src/decompress.rs#L490), first:

* \*.gz – gzip -d -c
* \*.tgz – gzip -d -c
* \*.bz2 – bzip2 -d -c
* \*.tbz2 – bzip2 -d -c
* \*.xz – xz -d -c
* \*.txz – xz -d -c
* \*.lz4 – lz4 -d -c
* \*.lzma – xz –format=lzma -d -c
* \*.br – brotli -d -c
* \*.zst – zstd -q -d -c
* \*.zstd – zstd -q -d -c
* \*.Z – uncompress -c

So, you can create a dummy *foo.gz* file, save payload to *gzip.exe* and run:

```
rg -z "whatever"
```

This will force *rg.exe* to launch *gzip.exe*.

This entry was posted in [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/10/25/ripgrep-as-a-lolbin/ "Permalink to ripgrep as a lolbin").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
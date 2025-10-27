---
title: Rundll32 goes to hell…
url: https://www.hexacorn.com/blog/2024/09/21/rundll32-goes-to-hell/
source: Hexacorn
date: 2024-09-22
fetch_date: 2025-10-06T18:23:21.498521
---

# Rundll32 goes to hell…

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

[← Previous](https://www.hexacorn.com/blog/2024/09/20/dexray-v2-34/)
[Next →](https://www.hexacorn.com/blog/2024/10/02/using-guids-to-guide-the-id-of-samples-capabilities-or-unique-attributable-properties/)

# Rundll32 goes to hell…

Posted on [2024-09-21](https://www.hexacorn.com/blog/2024/09/21/rundll32-goes-to-hell/ "10:43 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Parsing command line invocations is fun, because it’s impossible to do it right (all the time).

Imagine a test DLL that exports a function called *foobar*. We place this DLL in *c:\test* directory and name it like this:

```
test.dll, #666
```

We can then use *rundll32.exe* to execute the *foobar* function using the following syntax:

```
rundll32 "c:\test\test.dll, #666", foobar
```

A different version can use the following name:

```
test.dll,abcxyz
```

with the invocation:

```
rundll32 "test.dll,abcxyz", foobar
```

We do need quotes, because *rundll32.exe* does not accept file names with a ‘coma’ in them (for obvious reasons), and the full path is not needed if we are in the same directory, but the gist is that these are all proper DLL file names!:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll_1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll_1.png)

What your sophisticated regexes extracting DLL name and API’s ordinal number, or API name from this sort of invocations tell you today?

And then here’s another case for your consideration – create a test DLL with the following exports:

* A
* W
* AA
* AW
* WA
* WW

When you run the following invocations:

```
rundll32 c:\test\test.dll, A
rundll32 c:\test\test.dll, W
```

– which of these 6 exported functions will get executed?

I have [provided](https://www.hexacorn.com/blog/2019/09/28/rundll32-api-calling/) an answer to this question a few years ago, and here’s the DebugView output:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll_2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/rundll_2.png)

The bottom line is that you can’t use regexes for parsing command line invocations or make assumptions w/o running into many corner cases.

This entry was posted in [Anti-Forensics](https://www.hexacorn.com/blog/category/anti-forensics/), [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/09/21/rundll32-goes-to-hell/ "Permalink to Rundll32 goes to hell…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
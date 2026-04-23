---
title: Some unintelligent fun with ms-notepad protocol
url: https://www.hexacorn.com/blog/2026/04/22/some-unintelligent-fun-with-ms-notepad-protocol/
source: Hexacorn
date: 2026-04-22
fetch_date: 2026-04-23T04:43:44.837933
---

# Some unintelligent fun with ms-notepad protocol

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

[← Previous](https://www.hexacorn.com/blog/2026/04/18/a-few-more-protocol-handlers-part-2/)

# Some unintelligent fun with ms-notepad protocol

Posted on [2026-04-22](https://www.hexacorn.com/blog/2026/04/22/some-unintelligent-fun-with-ms-notepad-protocol/ "12:44 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In my previous [post](https://www.hexacorn.com/blog/2026/04/18/a-few-more-protocol-handlers-part-2/) I have provided a list of ‘new’ protocols I noticed in the latest Windows 11 build.

One that immediately caught my attention was “ms-notepad://”. You can use it to launch Notepad via “ms-notepad://<filename>” links and it also accepts command line switches.

So…

One could launch:

```
ms-notepad://foobar.txt
```

and that would make Notepad attempt to open one of these:

* C:\Users\<user>\ms-notepad:\foobar.txt\
* C:\Users\<user>\ms-notepad:\foobar.txt.txt

or

```
ms-notepad://..\..\..\foobar.txt
```

to open:

* C:\foobar.txt
* C:\foobar.txt.txt

If you embed a link pointing to the above *foobar.txt* file in a HTML file and open in f.ex. Microsoft Edge, and then click the link, you will see Notepad trying to open the following files:

* C:\Users\<user>\ms-notepad:..%5C..%5C..%5Cfoobar.txt\
* C:\Users\<user>\ms-notepad:..%5C..%5C..%5Cfoobar.txt.txt

It looks like the protocol handler is not doing very well with this unexpected input.

Additionally, new *Notepad.exe* accepts a */TESTING:>argument>* command line argument. I don’t fully understand how the program processes this *argument*, but I noticed it has to be provided in a Base64 form.

So:

```
file://..\..\..\test\foobar.txt
```

can be converted to a Base64 blob:

```
ZmlsZTovLy4uXC4uXC4uXHRlc3RcZm9vYmFyLnR4dCAgICA=
```

One can then launch Notepad with a TESTING argument from a command line or via a protocol handler:

```
notepad /TESTING:ZmlsZTovLy4uXC4uXC4uXHRlc3RcZm9vYmFyLnR4dCAgICA=
ms-notepad:// /TESTING:ZmlsZTovLy4uXC4uXC4uXHRlc3RcZm9vYmFyLnR4dCAgICA=
```

In both cases the Notepad will try to open:

```
C:\test\foobar.txt
```

And while nothing substantial comes out of this quick ‘research’, I find it pretty interesting that so many new URL-like protocols are still being introduced in new Windows builds.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/04/22/some-unintelligent-fun-with-ms-notepad-protocol/ "Permalink to Some unintelligent fun with ms-notepad protocol").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
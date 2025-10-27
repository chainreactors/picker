---
title: 3 little secrets of netsh.exe
url: https://www.hexacorn.com/blog/2024/12/25/3-little-secrets-of-netsh-exe/
source: Hexacorn
date: 2024-12-26
fetch_date: 2025-10-06T19:37:59.946413
---

# 3 little secrets of netsh.exe

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

[← Previous](https://www.hexacorn.com/blog/2024/12/22/windows-server-2025-and-msmpeng-exe/)
[Next →](https://www.hexacorn.com/blog/2024/12/26/la57setup-exe-lolbin/)

# 3 little secrets of netsh.exe

Posted on [2024-12-25](https://www.hexacorn.com/blog/2024/12/25/3-little-secrets-of-netsh-exe/ "11:15 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

It is typical for many of us to discover ‘the cool thing’, and then quickly move on to research something else. Over the last few years my ‘[little known secrets’](https://www.hexacorn.com/blog/category/little-known-secrets/) series exploited this phenomenon by showcasing scenarios that, admittedly, were available to many researchers before me, all of them ‘who were there first’, but… who then just stopped looking at other interesting things after they discovered, and then published about, ‘that one cool thing’.

if it sounds cryptic…

Take *netsh.exe* as an example.

Its [Lolbas](https://lolbas-project.github.io/lolbas/Binaries/Netsh/) page describes only one lolbin usage that relies on the ‘*netsh.exe add*‘ command in which we load an arbitrary DLL into *netsh.exe* process.

O-kay.

A casual study of *netsh.exe* [command line syntax](https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-contexts) offers two additional opportunities:

* -f <scriptfile>
* exec <scriptfile>

These commands take a script name as an input and then process the commands stored inside the <scriptfile> file. It’s super basic, but it works.

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh1.png)

And it’s not the end.

Turns out the Alias file processing works too:

* -a <AliasFile>

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh2.png)

And it’s not the end either.

Just trying to add a single alias leads to a DLL loading too! (and I don’t even know if this is a proper syntax!)

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh3.png)

And then it hits you…

You are doing all these tests on the very same system, one by one, in a context of changes you have already introduced to the system. And these changes should not be ignored!

The first test added a *netsh.exe* ‘plug-in’ to the Registry:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NetSh\test=test.dll
```

As a result, any subsequent invocations of *netsh.exe* attempted to load that *test.dll*!

Ouch.

It’s a classic example of contamination of the evidence/sample, and once it happens (and we miss it!), everything that follows, research-wise, is all wrong!

And this is the moment when we come back to the basics, and test our hypothesis one by one, using \_clean\_ environment for all the tests we have ever thought of.

And then, after careful testing, we can still prove that these are still very decent LOLBIN scenarios;

* -f <scriptfile>
* exec <scriptfile>
* -a <AliasFile>

And if you enter the interactive mode of *netsh.exe*, you can add a DLL-loading alias like this, too:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh4-1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh4-1.png)

or

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh5.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/netsh5.png)

The lesson here is that we always need to dig a bit more, but we also need to be careful, because some of our conclusions may be convenient, but also… incorrect…

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/12/25/3-little-secrets-of-netsh-exe/ "Permalink to 3 little secrets of netsh.exe").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
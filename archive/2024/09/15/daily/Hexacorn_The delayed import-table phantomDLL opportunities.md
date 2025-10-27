---
title: The delayed import-table phantomDLL opportunities
url: https://www.hexacorn.com/blog/2024/09/14/the-delayed-import-table-phantomdll-opportunities/
source: Hexacorn
date: 2024-09-15
fetch_date: 2025-10-06T18:23:45.849251
---

# The delayed import-table phantomDLL opportunities

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

[← Previous](https://www.hexacorn.com/blog/2024/09/11/rundll32-exe-bomb/)
[Next →](https://www.hexacorn.com/blog/2024/09/20/dexray-v2-34/)

# The delayed import-table phantomDLL opportunities

Posted on [2024-09-14](https://www.hexacorn.com/blog/2024/09/14/the-delayed-import-table-phantomdll-opportunities/ "9:31 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Many native OS PE files still rely on delayed imports. When APIs imported this way are called for the first time, a so-called *delay load helper* function is executed first – it loads the actual delayed library, resolves the address of its APIs and finally substitutes the APIs’ addresses (that point to a delay load helper function at first) with the actual API functions’ addresses, then the actual API is called. It’s a really clever mechanism that… is kinda obsolete today. Still, from this moment on, any calls to any of the delayed APIs will be redirected to the already resolved APIs addresses.

As expected, some of the DLLs listed as delayed imports by OS EXEs and DLLs are actually not present on the system. This is an opportunity. I originally wanted to research a bit more before publishing anything, but then [sixtyvividtails](https://x.com/sixtyvividtails) killed it with this [comment](https://x.com/sixtyvividtails/status/1831410281169539202):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/sixtyvividtails_delay_load.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/sixtyvividtails_delay_load.png)

I love this comment, because it demonstrates not only this individual’s in-depth knowledge of the OS but also a good nose for ‘the research opportunities’…

So, since the cat is out of the bag, let’s quickly assess what that means…

There is a small number of EXEs and DLLs (tested on windows 11 23H2) that reference delayed imports pointing to DLLs that do not exist.

For instance, *UPPrinterInstaller.exe* includes delay-imported APi set (*FindLivePdmPrinterById*, *SavePdmPrinter*, *RemovePdmPrinterById*) from a non-existing *PdmUtilities.dll*.

Analyzing the logic of the program, we can see that:

* it requires exactly 10 arguments (unlike 8 arguments that are presented as an example on Microsoft pages); in essence, the win11 versions of *UPPrinterInstaller.exe* require additional (on top of 8 already described) argument of *usersid/sid* f.ex:

```
"C:\Windows\System32\UPPrinterInstaller.exe" -i -psi 12345678-89ab-cdef-0123-456789abcdef -sid 1234 -oai 12345678-89ab-cdef-0123-456789abcdef -cri 12345678-89ab-cdef-0123-456789abcdef
```

* it requires some Registry settings to be present for the given printer’s shared ID (fake here, just for the test):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/UPPrinterInstalls.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/09/UPPrinterInstalls.png)

Yet it still won’t load that precious delay-imported code, because on your typical desktop or server OS instance a call to *RtlGetDeviceFamilyInfoEnum* that this program does (after checking all the Registry business I faked above) does not return 16 (*DEVICEFAMILYINFOENUM\_WINDOWS\_CORE*), but 3 (*DEVICEFAMILYINFOENUM\_DESKTOP*) or 9 (*DEVICEFAMILYINFOENUM\_SERVER*).

Executable files that delay-load phantom DLLs are at least approachable, because we can run them in the best possible conditions that we can create/optimize by creating necessary files, registry entries, etc.

What about DLLs importing delayed PhantomDLLs?

After looking at a few, I am pessimistic. The delay-loaded code usually requires a lot of conditions to be met before it can be reached via typical code paths exposed by the importing DLLs. As such, these are not very promising avenues. And after looking at it for far too long, I got a bit bored and am officially throwing a towel 🙂

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Research fails](https://www.hexacorn.com/blog/category/research-fails/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/09/14/the-delayed-import-table-phantomdll-opportunities/ "Permalink to The delayed import-table phantomDLL opportunities").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
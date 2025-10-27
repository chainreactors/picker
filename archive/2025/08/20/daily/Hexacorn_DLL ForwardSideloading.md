---
title: DLL ForwardSideloading
url: https://www.hexacorn.com/blog/2025/08/19/dll-forwardsideloading/
source: Hexacorn
date: 2025-08-20
fetch_date: 2025-10-07T00:47:52.591757
---

# DLL ForwardSideloading

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

[← Previous](https://www.hexacorn.com/blog/2025/08/17/beyond-good-ol-run-key-part-150/)
[Next →](https://www.hexacorn.com/blog/2025/09/03/dll-forwardsideloading-part-2/)

# DLL ForwardSideloading

Posted on [2025-08-19](https://www.hexacorn.com/blog/2025/08/19/dll-forwardsideloading/ "10:31 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Some DLLs export functions (via export table) that are just forwarding execution to functions implemented in other libraries. It’s a very common practice and one of the most known forwards are:

```
kernel32.dll HeapAlloc -> NTDLL.RtlAllocateHeap
kernel32.dll HeapReAlloc -> NTDLL.RtlReAllocateHeap
kernel32.dll HeapSize -> NTDLL.RtlSizeHeap
```

Now, most of us assume that lots of forwards redirect the execution to most popular Windows DLLs, and these are typically just your regular KnownDLLs: ntdll, kernelbase, ole32, etc. — ones that are on the KnownDLLs list + very often already loaded into memory.

I decided to check what forwards we can find on the Win 11 OS, because I had a cunning plan: If I can find a forward that does not redirect to KnownDlls, then I can execute an indirect DLL sideloading, one that is on par with traditional EXE sideloading technique.

Meaning?

Use a signed rundll32.exe to load a signed DLL that will then load the payload DLL of our choice… by using that exported function.

This is a [list of forwards](https://hexacorn.com/d/apis_fwd.txt) I have generated.

We can quickly identify a non-KnownDlls pair, where:

```
keyiso.dll KeyIsoSetAuditingInterface -> NCRYPTPROV.SetAuditingInterface
```

So, copying *keyiso.dll* to c:\test, and then placing a payload in *NCRYPTPROV.dll* in the same folder, and then finally executing:

```
rundll32.exe c:\test\keyiso.dll, KeyIsoSetAuditingInterface
```

will load a copy of the *keyiso.dll* first, then the function resolution of *KeyIsoSetAuditingInterface* will resolve it first to *NCRYPTPROV.SetAuditingInterface* forward, and then automatically load the *NCRYPTPROV.dll*, and only then execute the function’s code. In the example below, I didn’t bother to implement *SetAuditingInterface* in the test DLL, just to showcase the execution flow leading to (actually misleading, since it refers to the outer DLL/API name combo) ‘missing API’ message box.

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/keyiso.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/08/keyiso.png)

The *DLLMain\_64\_DLL\_PROCESS\_ATTACH.txt* file is created by the test payload, indicating its DllMain function has been executed.

Obviously, this technique does not need to rely on OS libraries. I am pretty sure that a bigger study of exported functions from a larger corpora of signed DLLs will yield a set of combos that can be used to implement this technique.

This entry was posted in [DLL ForwardSideloading](https://www.hexacorn.com/blog/category/sideloading/dll-forwardsideloading/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/), [Sideloading](https://www.hexacorn.com/blog/category/sideloading/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/08/19/dll-forwardsideloading/ "Permalink to DLL ForwardSideloading").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
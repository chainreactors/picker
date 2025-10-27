---
title: DLL ForwardSideloading, Part 2
url: https://www.hexacorn.com/blog/2025/09/03/dll-forwardsideloading-part-2/
source: Hexacorn
date: 2025-09-04
fetch_date: 2025-10-02T19:36:32.988184
---

# DLL ForwardSideloading, Part 2

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

[← Previous](https://www.hexacorn.com/blog/2025/08/19/dll-forwardsideloading/)
[Next →](https://www.hexacorn.com/blog/2025/09/08/beyond-good-ol-run-key-part-151/)

# DLL ForwardSideloading, Part 2

Posted on [2025-09-03](https://www.hexacorn.com/blog/2025/09/03/dll-forwardsideloading-part-2/ "11:36 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

The 2nd part following [my first take](https://www.hexacorn.com/blog/2025/08/19/dll-forwardsideloading/) on this subject was kinda inevitable.

Why?

[Sixtyvividtails](https://bsky.app/profile/sixtyvividtails.bsky.social) is one of my fav researchers, because a) he reads my posts, breaks them apart, and usually comes up with some amazing/creative comments/additional thoughts that often lead us to some new, cool discoveries (see f.ex. [this](https://www.hexacorn.com/blog/2020/02/05/stay-positive-lolbins-not/)) b) he also made a social media [bet](https://bsky.app/profile/sixtyvividtails.bsky.social/post/3lwtnu7inec2d) that I (obviously) couldn’t leave unchallenged. Thank you Sixtyvividtails, you are an inspiration and I love your research and creative ideas a lot!

So, to business…

My first find was this [unsigned Realtek DLL](https://bsky.app/profile/hexacorn.bsky.social/post/3lwuee5pvvc2y) (RealWoWDLL.dll – [VT Link](https://www.virustotal.com/gui/file/01150d92a3d4281ca7c66939750984cb322eb0fd9a786b2a3fade7780e256585)) that exported the intriguing forward:

```
testker -> kerberos.Spinitialize
```

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/09/dllforwardsideload_realtek.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/09/dllforwardsideload_realtek.png)

Then… I went for holidays 🙂

I did go there with an idea though that after coming back I will do a more structured follow-up research…

So when I came back, I immediately got to work.

The first target was an obvious one – run the very same forwarder-extractor script over the Windows 2025 server files. The results are [here](https://hexacorn.com/d/apis_fwd_srv2025.txt). Many of these combos can be used for DLL ForwardSideloading.

The second target was bigger. I checked my repo of ‘good’ files only to discover that I am sitting on around 700K ‘clean’ DLLs, both 32- and 64-bit. Sadly, I don know which ones of them are truly signed or not, unless the actual PE file of the DLL is physically signed (aka not via a catalogue). Still, 700K files is a lot, and there is a hope that it’s worth analyzing them all to see how many of them are non-Microsoft, and actually use/leverage the forwarded exports…

So, I ran my script over the last weekend and after few days it spat out its results.

And here’s the catch:

* yes, some vendors do appear to be using forwarded functions same as Microsoft and Realtek
* many functions that have their names exported by DLLs (mapping present in the export table) are not necessarily meant to be used by any other program, but since some do include a “.” character in their name, they could actually be used to facilitate DLL ForwardSideloading !

See the (filtered) results [here](https://hexacorn.com/d/fwd_sideload_results.txt).

This entry was posted in [DLL ForwardSideloading](https://www.hexacorn.com/blog/category/sideloading/dll-forwardsideloading/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/), [Sideloading](https://www.hexacorn.com/blog/category/sideloading/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/09/03/dll-forwardsideloading-part-2/ "Permalink to DLL ForwardSideloading, Part 2").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
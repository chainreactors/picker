---
title: PE Section names – re-visited, again, in 2023
url: https://www.hexacorn.com/blog/2023/05/11/pe-section-names-re-visited-again-in-2023/
source: Hexacorn
date: 2023-05-12
fetch_date: 2025-10-04T11:39:42.968323
---

# PE Section names – re-visited, again, in 2023

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

[← Previous](https://www.hexacorn.com/blog/2023/05/11/an-elf-walks-into-the-bar/)
[Next →](https://www.hexacorn.com/blog/2023/05/12/matlab-persistent-lolbin-2-years-too-late-but-always/)

# PE Section names – re-visited, again, in 2023

Posted on [2023-05-11](https://www.hexacorn.com/blog/2023/05/11/pe-section-names-re-visited-again-in-2023/ "11:16 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In [my](https://www.hexacorn.com/blog/2016/12/15/pe-section-names-re-visited/) [previous](https://www.hexacorn.com/blog/2019/07/26/pe-section-names-re-visited-again/) posts I have listed many PE sections present in different types of binaries. Today I am looking at win11 PE sections and am happy to report that the world of PE Sections has expanded a bit, again; here are some stats:

* 3176 b’.rsrc’
* 3109 b’.text’
* 3109 b’.reloc’
* 3108 b’.data’
* 3102 b’.pdata’
* 2983 b’.rdata’
* 2007 b’.a64xrm’ –> [CHPEV2 section](https://ffri.github.io/ProjectChameleon/new_reloc_chpev2/)
* 1958 b’.hexpthk’ –> possibly stands for [Hybrid Executable Push Thunk](https://blogs.blackberry.com/en/2019/09/teardown-windows-10-on-arm-x86-emulation)
* 1705 b’.didat’
* 241 b’.00cfg’
* 50 b’.orpc’
* 39 b’?g\_Encry’ –> [WarbirdPayload](https://downwithup.github.io/blog/post/2023/04/23/post9.html)
* 31 b’PAGE’
* 25 b’INIT’
* 25 b’GFIDS’
* 25 b’.edata’
* 19 b’.wpp\_sf’
* 14 b’.idata’
* 12 b’.mrdata’
* 9 b’PAGECMRC’
* 7 b’RT\_DATA’
* 7 b’RT\_BSS’
* 6 b’RT\_CODE’
* 5 b’\_RDATA’
* 5 b’.sdbid’
* 5 b’.no\_bbt’
* 5 b’.apiset’
* 4 b’RT\_CONST’
* 4 b’.isoapis’
* 4 b’.imrsiv’
* 2 b’PAGEWdfV’
* 2 b’PAGELK’
* 2 b’PAGEDATA’
* 2 b’PAGECONS’
* 2 b’.text\_hf’
* 2 b’.sipc’
* 1 b’msrodata’
* 1 b’debug\_wi’
* 1 b’cachelin’
* 1 b’\_\_Defaul’
* 1 b’SANONTCP’
* 1 b’RT’
* 1 b’FE\_TEXT’
* 1 b’ExtTel’
* 1 b’ERRATA’
* 1 b’CiPolicy’
* 1 b’.ssm\_url’
* 1 b’.proxy’
* 1 b’.ndr64′
* 1 b’.mytext’
* 1 b’.guids’
* 1 b’.detourd’
* 1 b’.detourc’
* 1 b’.bootdat’
* 1 b’.DDIData’

This entry was posted in [Reversing](https://www.hexacorn.com/blog/category/reversing/), [Windows 11](https://www.hexacorn.com/blog/category/windows-11/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/05/11/pe-section-names-re-visited-again-in-2023/ "Permalink to PE Section names – re-visited, again, in 2023").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")
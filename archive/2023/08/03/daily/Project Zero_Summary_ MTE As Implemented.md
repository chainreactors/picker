---
title: Summary: MTE As Implemented
url: https://googleprojectzero.blogspot.com/2023/08/summary-mte-as-implemented.html
source: Project Zero
date: 2023-08-03
fetch_date: 2025-10-04T12:01:26.241100
---

# Summary: MTE As Implemented

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Wednesday, August 2, 2023

### Summary: MTE As Implemented

By Mark Brand, Project Zero

In mid-2022, Project Zero was provided with access to pre-production hardware implementing the ARM MTE specification. This blog post series is based on that review, and includes general conclusions about the effectiveness of MTE as implemented, specifically in the context of preventing the exploitation of memory-safety vulnerabilities.

Despite its limitations, MTE is still by far the most promising path forward for improving C/C++ software security in 2023. The ability of MTE to detect memory corruption exploitation at the first dangerous access provides a significant improvement in diagnostic and potential security effectiveness. In comparison, most other proposed approaches rely on blocking later stages in the exploitation process, for example various hardware-assisted CFI approaches which aim to block invalid control-flow transfers.

No MTE-based mitigation is going to completely solve the problem of exploitable C/C++ memory safety issues. The unfortunate reality of speculative side-channel attacks is that MTE will not end memory corruption exploitation. However, there are no other practical proposals with a similarly broad impact on exploitability (and exploitation cost) of such a wide range of memory corruption issues which would additionally address this limitation.

Furthermore, given the long history of  innovation and research in this space, we believe that it is not possible to build a software solution for C/C++ memory safety with comparable coverage to MTE that has less runtime overhead than [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html)/[HWAsan](https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html). It's clear that such an overhead is not acceptable for most production workloads.

Products that expect to contain large C/C++ codebases in the long term, who consider the exploitation of memory corruption vulnerabilities to be a key risk for their product security, should actively drive support for ARM's MTE in their products.

For a more detailed analysis, see the following linked blog posts:

1. [Implementation Testing](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-1.html) - An objective summary of the tests performed, and some basic analysis. If you're interested in implementing a mitigation based on MTE, you should read this document first as it will give you more detailed technical background.

2. [Mitigation Case Studies](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-2-mitigation.html) - A subjective assessment of the impact of various mitigation approaches based on the use of MTE in various user-mode contexts, based on our experiences during the tests performed in Part 1. If you're not interested in implementing a mitigation based on MTE, but you are interested in the limits of how effective such a mitigation might be, you can skip Part 1 and start here.
3. [The Kernel](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-3-kernel.html) - A subjective assessment of the additional issues faced in using MTE for a kernel-mode mitigation.

Posted by

[Google Project Zero](https://www.blogger.com/profile/08975904405228580347 "author profile")

at
[9:30 AM](https://googleprojectzero.blogspot.com/2023/08/summary-mte-as-implemented.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4838136820032157985&postID=8958340167466970608&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8958340167466970608&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8958340167466970608&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8958340167466970608&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8958340167466970608&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8958340167466970608&target=pinterest "Share to Pinterest")

#### No comments:

#### Post a Comment

[Newer Post](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-2-mitigation.html "Newer Post")

[Older Post](https://googleprojectzero.blogspot.com/2023/04/technical-report-into-intel-tdx.html "Older Post")
[Home](https://googleprojectzero.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://googleprojectzero.blogspot.com/feeds/8958340167466970608/comments/default)

## Search This Blog

|  |  |
| --- | --- |
|  |  |

## Pages

* [About Project Zero](https://googleprojectzero.blogspot.com/p/about-project-zero.html)
* [0day "In the Wild"](https://googleprojectzero.blogspot.com/p/0day.html)
* [0day Exploit Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [Reporting Transparency](https://googleprojectzero.blogspot.com/p/reporting-transparency.html)
* [Vulnerability Disclosure FAQ](https://googleprojectzero.blogspot.com/p/vulnerability-disclosure-faq.html)
* [Working at Project Zero](https://googleprojectzero.blogspot.com/p/working-at-project-zero.html)

## Archives

* ►
  [2025](https://googleprojectzero.blogspot.com/2025/)
  (10)
  + ►
    [September](https://googleprojectzero.blogspot.com/2025/09/)
    (1)
  + ►
    [August](https://googleprojectzero.blogspot.com/2025/08/)
    (1)
  + ►
    [July](https://googleprojectzero.blogspot.com/2025/07/)
    (1)
  + ►
    [May](https://googleprojectzero.blogspot.com/2025/05/)
    (3)
  + ►
    [April](https://googleprojectzero.blogspot.com/2025/04/)
    (1)
  + ►
    [March](https://googleprojectzero.blogspot.com/2025/03/)
    (1)
  + ►
    [January](https://googleprojectzero.blogspot.com/2025/01/)
    (2)

* ►
  [2024](https://googleprojectzero.blogspot.com/2024/)
  (12)
  + ►
    [December](https://googleprojectzero.blogspot.com/2024/12/)
    (3)
  + ►
    [November](https://googleprojectzero.blogspot.com/2024/11/)
    (2)
  + ►
    [October](https://googleprojectzero.blogspot.com/2024/10/)
    (2)
  + ►
    [June](https://googleprojectzero.blogspot.com/2024/06/)
    (3)
  + ►
    [April](https://googleprojectzero.blogspot.com/2024/04/)
    (2)

* ▼
  [2023](https://googleprojectzero.blogspot.com/2023/)
  (11)
  + ►
    [November](https://googleprojectzero.blogspot.com/2023/11/)
    (1)
  + ►
    [October](https://googleprojectzero.blogspot.com/2023/10/)
    (1)
  + ►
    [September](https://googleprojectzero.blogspot.com/2023/09/)
    (1)
  + ▼
    [August](https://googleprojectzero.blogspot.com/2023/08/)
    (4)
    - [MTE As Implemented, Part 1: Implementation Testing](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-1.html)
    - [MTE As Implemented, Part 3: The Kernel](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-3-kernel.html)
    - [MTE As Implemented, Part 2: Mitigation Case Studies](https://googleprojectzero.blogspot.com/2023/08/mte-as-implemented-part-2-mitigation.html)
    - [Summary: MTE As Implemented](https://googleprojectzero.blogspot.com/2023/08/summary-mte-as-implemented.html)
  + ►
    [April](https://googleprojectzero.blogspot.com/2023/04/)
    (1)
  + ►
    [March](https://googleprojectzero.blogspot.com/2023/03/)
    (1)
  + ►
    [January](https://googleprojectzero.blogspot.com/2023/01/)
    (2)

* ►
  [2022](https://googleprojectzero.blogspot.com/2022/)
  (17)
  + ►
    [December](https://googleprojectzero.blogspot.com/2022/12/)
    (1)
  + ►
    [November](https://googleprojectzero.blogspot.com/2022/11/)
    (3)
  + ►
    [October](https://googleprojectzero.blogspot.com/2022/10/)
    (1)
  + ►
    [August](http...
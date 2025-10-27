---
title: Mind the Gap
url: https://googleprojectzero.blogspot.com/2022/11/mind-the-gap.html
source: Project Zero
date: 2022-11-23
fetch_date: 2025-10-03T23:29:42.803740
---

# Mind the Gap

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Tuesday, November 22, 2022

### Mind the Gap

By Ian Beer, Project Zero

Note: The vulnerabilities discussed in this blog post (CVE-2022-33917) are fixed by the upstream vendor, but at the time of publication, these fixes have not yet made it downstream to affected Android devices (including Pixel, Samsung, Xiaomi, Oppo and others). Devices with a Mali GPU are currently vulnerable.

## Introduction

In June 2022, Project Zero researcher Maddie Stone gave a talk at [FirstCon22](https://www.first.org/conference/2022/) titled [0-day In-the-Wild Exploitation in 2022…so far](https://googleprojectzero.blogspot.com/2022/06/2022-0-day-in-wild-exploitationso-far.html). A key takeaway was that approximately 50% of the observed 0-days in the first half of 2022 were variants of previously patched vulnerabilities. This finding is consistent with our understanding of attacker behavior: attackers will take the path of least resistance, and as long as vendors don't consistently perform thorough root-cause analysis when fixing security vulnerabilities, it will continue to be worth investing time in trying to revive known vulnerabilities before looking for novel ones.

The presentation discussed an in the wild exploit targeting the Pixel 6 and leveraging CVE-2021-39793, a vulnerability in the ARM Mali GPU driver used by a large number of other Android devices. ARM's advisory described the vulnerability as:

Title                    Mali GPU Kernel Driver may elevate CPU RO pages to writable

CVE                   CVE-2022-22706 (also reported in CVE-2021-39793)

Date of issue      6th January 2022

Impact                A non-privileged user can get a write access to read-only memory pages [sic].

The week before FirstCon22, Maddie gave an internal preview of her talk. Inspired by the description of an in-the-wild vulnerability in low-level memory management code, fellow Project Zero researcher Jann Horn started auditing the ARM Mali GPU driver. Over the next three weeks, Jann found five more exploitable vulnerabilities ([2325](https://bugs.chromium.org/p/project-zero/issues/detail?id=2325), [2327](https://bugs.chromium.org/p/project-zero/issues/detail?id=2327), [2331](https://bugs.chromium.org/p/project-zero/issues/detail?id=2331), [2333](https://bugs.chromium.org/p/project-zero/issues/detail?id=2333), [2334](https://bugs.chromium.org/p/project-zero/issues/detail?id=2334)).

## Taking a closer look

One of these issues ([2334](https://bugs.chromium.org/p/project-zero/issues/detail?id=2334)) lead to kernel memory corruption, one ([2331](https://bugs.chromium.org/p/project-zero/issues/detail?id=2331)) lead to physical memory addresses being disclosed to userspace and the remaining three ([2325](https://bugs.chromium.org/p/project-zero/issues/detail?id=2325), [2327](https://bugs.chromium.org/p/project-zero/issues/detail?id=2327), [2333](https://bugs.chromium.org/p/project-zero/issues/detail?id=2333)) lead to a physical page use-after-free condition. These would enable an attacker to continue to read and write physical pages after they had been returned to the system.

For example, by forcing the kernel to [reuse these pages as page tables](https://googleprojectzero.blogspot.com/2021/10/how-simple-linux-kernel-memory.html), an attacker with native code execution in an app context could gain full access to the system, bypassing Android's permissions model and allowing broad access to user data.

Anecdotally, we heard from multiple sources that the Mali issues we had reported collided with vulnerabilities available in the 0-day market, and we even saw one [public reference](https://twitter.com/jgrusko/status/1571921203723440135):

[![@ProjectZeroBugs\nArm Mali: driver exposes physical addresses to unprivileged userspace\n\n  @jgrusko Replying to @ProjectZeroBugs\nRIP the feature that was there forever and nobody wanted to report :)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHlABpgRGtGMlLmoEY3wDYvg13cwbxPVGScpjHBa0wa8vaohGjhB9YkYuIyfxxnm2iWh4czqp1YUdMCrSgy-dtdlZ8FkLV5IDrQZ1SSCNUoYjsJlHdPoOjtUar_uHQda_aAUu75_4sUUAFjM7Jvr-d6JOMHD7AexIZMXDsdrZIdKX7aA4wrhRC6PCD/s1200/tweet.png "@ProjectZeroBugs\nArm Mali: driver exposes physical addresses to unprivileged userspace\n\n
 @jgrusko Replying to @ProjectZeroBugs\nRIP the feature that was there forever and nobody wanted to report :)")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHlABpgRGtGMlLmoEY3wDYvg13cwbxPVGScpjHBa0wa8vaohGjhB9YkYuIyfxxnm2iWh4czqp1YUdMCrSgy-dtdlZ8FkLV5IDrQZ1SSCNUoYjsJlHdPoOjtUar_uHQda_aAUu75_4sUUAFjM7Jvr-d6JOMHD7AexIZMXDsdrZIdKX7aA4wrhRC6PCD/s1420/tweet.png)

## The "Patch gap" is for vendors, too

We reported these five issues to ARM when they were discovered between June and July 2022. ARM fixed the issues promptly in July and August 2022, disclosing them as security issues on their [Arm Mali Driver Vulnerabilities](https://developer.arm.com/Arm%20Security%20Center/Mali%20GPU%20Driver%20Vulnerabilities) page (assigning [CVE-2022-36449](https://nvd.nist.gov/vuln/detail/CVE-2022-36449)) and publishing the [patched driver source on their public developer website](https://developer.arm.com/downloads/-/mali-drivers/valhall-kernel).

In line with our [2021 disclosure policy update](https://googleprojectzero.blogspot.com/2021/04/policy-and-disclosure-2021-edition.html) we then waited an additional 30 days before derestricting our Project Zero tracker entries. Between late August and mid-September 2022 we derestricted these issues in the public Project Zero tracker: [2325](https://bugs.chromium.org/p/project-zero/issues/detail?id=2325), [2327](https://bugs.chromium.org/p/project-zero/issues/detail?id=2327), [2331](https://bugs.chromium.org/p/project-zero/issues/detail?id=2331), [2333](https://bugs.chromium.org/p/project-zero/issues/detail?id=2333), [2334](https://bugs.chromium.org/p/project-zero/issues/detail?id=2334).

When time permits and as an additional check, we test the effectiveness of the patches that the vendor has provided. This sometimes leads to follow-up bug reports where a patch is incomplete or a variant is discovered (for a recently compiled list of examples, see [the first table in this blogpost](https://googleprojectzero.blogspot.com/2022/06/2022-0-day-in-wild-exploitationso-far.html)), and sometimes we discover the fix isn't there at all.

In this case we discovered that all of our test devices which used Mali are still vulnerable to these issues. CVE-2022-36449 is not mentioned in any downstream security bulletins.

## Conclusion

Just as users are recommended to patch as quickly as they can once a release containing security updates is available, so the same applies to vendors and companies. Minimizing the "patch gap" as a vendor in these scenarios is arguably more important, as end users (or other vendors downstream) are blocking on this action before they can receive the security benefits of the patch.

Companies need to remain vigilant, follow upstream sources closely, and do their best to provide complete patches to users as soon as possible.

Posted by

[Google Project Zero](https://www.blogger.com/profile/08975904405228580347 "author profile")

at
[1:05 PM](https://googleprojectzero.blogspot.com/2022/11/mind-the-gap.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4838136820032157985&postID=7519748497805371118&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=7519748497805371118&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=7519748497805371118&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=7519748497805371118&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/s...
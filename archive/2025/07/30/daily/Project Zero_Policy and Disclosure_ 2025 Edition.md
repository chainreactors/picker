---
title: Policy and Disclosure: 2025 Edition
url: https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html
source: Project Zero
date: 2025-07-30
fetch_date: 2025-10-06T23:39:55.772894
---

# Policy and Disclosure: 2025 Edition

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Tuesday, July 29, 2025

### Policy and Disclosure: 2025 Edition

Posted by Tim Willis, Google Project Zero

In 2021, we updated our vulnerability disclosure policy to the current "90+30" model. Our goals were to drive faster yet thorough patch development, and improve patch adoption. While we’ve seen progress, a significant challenge remains: the time it takes for a fix to actually reach an end-user's device.

This delay, often called the "patch gap," is a complex problem. Many consider the patch gap to be the time between a fix being released for a security vulnerability and the user installing the relevant update. However, our work has highlighted a critical, earlier delay: the "upstream patch gap". This is the period where an upstream vendor has a fix available, but downstream dependents, who are ultimately responsible for shipping fixes to users, haven’t yet integrated it into their end product.

As Project Zero's recent work has focused on foundational, upstream technologies like chipsets and their drivers, we've observed that this upstream gap significantly extends the vulnerability lifecycle.

For the end user, a vulnerability isn't fixed when a patch is released from Vendor A to Vendor B; it's only fixed when they download the update and install it on their device. To shorten that entire chain, we need to address the upstream delay.

To address this, we're announcing a new trial policy: Reporting Transparency.

#### The Trial: Reporting Transparency

Our core [90-day disclosure deadline](https://googleprojectzero.blogspot.com/p/vulnerability-disclosure-policy.html) will remain in effect. However, we're adding a new step at the beginning of the process.

Beginning today, within approximately one week of reporting a vulnerability to a vendor, we will [publicly share](https://googleprojectzero.blogspot.com/p/reporting-transparency.html) that a vulnerability was discovered. We will share:

* The vendor or open-source project that received the report.
* The affected product.
* The date the report was filed, and when the 90-day disclosure deadline expires.

This trial maintains our existing 90+30 policy, meaning vendors still have 90 days to fix a bug before it is disclosed, with a 30-day period for patch adoption if the bug is fixed before the deadline.

Google Big Sleep, a collaboration between Google DeepMind and Google Project Zero, will also be trialling this policy for their vulnerability reports. The issue tracker for Google Big Sleep is at [goo.gle/bigsleep](https://goo.gle/bigsleep)

#### Why the Change? Increased Transparency to Close the Gap

The primary goal of this trial is to shrink the upstream patch gap by increasing transparency. By providing an early signal that a vulnerability has been reported upstream, we can better inform downstream dependents. For our small set of issues, they will have an additional source of information to monitor for issues that may affect their users.

We hope that this trial will encourage the creation of stronger communication channels between upstream vendors and downstream dependents relating to security, leading to faster patches and improved patch adoption for end users.

This data will make it easier for researchers and the public to track how long it takes for a fix to travel from the initial report, all the way to a user's device (which is especially important if the fix never arrives!)

#### Will this help attackers?

No — we anticipate that in the initial phase of this trial, there may be increased public attention on unfixed bugs. We want to be clear: no technical details, proof-of-concept code, or information that we believe would materially assist discovery will be released until the deadline. Reporting Transparency is an alert, not a blueprint for attackers.

We understand that for some vendors without a downstream ecosystem, this policy may create unwelcome noise and attention for vulnerabilities that only they can address. However, these vendors now represent the minority of vulnerabilities reported by Project Zero. We believe the benefits of a fair, simple, consistent and transparent policy outweigh the risk of inconvenience to a small number of vendors.

That said, in 2025, we hope that the industry consensus is that the mere existence of vulnerabilities in software is neither surprising nor alarming. End users are more aware of the importance of security updates than ever before. It's widely accepted as fact that any system of moderate complexity will have vulnerabilities, and systems that were considered impenetrable in the past have been shown to be vulnerable in retrospect.

This is a trial, and we will be closely monitoring its effects. We hope it achieves our ultimate goal: a safer ecosystem where vulnerabilities are remediated not just in an upstream code repository, but on the devices, systems and services that people use every day. We look forward to sharing our findings and continuing to evolve our policies to meet the challenges of the ever-changing security landscape.

Posted by

[Google Project Zero](https://www.blogger.com/profile/08975904405228580347 "author profile")

at
[7:54 AM](https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4838136820032157985&postID=6531365654051821564&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=6531365654051821564&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=6531365654051821564&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=6531365654051821564&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=6531365654051821564&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=6531365654051821564&target=pinterest "Share to Pinterest")

#### No comments:

#### Post a Comment

[Newer Post](https://googleprojectzero.blogspot.com/2025/08/from-chrome-renderer-code-exec-to-kernel.html "Newer Post")

[Older Post](https://googleprojectzero.blogspot.com/2025/05/the-windows-registry-adventure-8-exploitation.html "Older Post")
[Home](https://googleprojectzero.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://googleprojectzero.blogspot.com/feeds/6531365654051821564/comments/default)

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

* ▼
  [2025](https://googleprojectzero.blogspot.com/2025/)
  (10)
  + ►
    [September](https://googleprojectzero.blogspot.com/2025/09/)
    (1)
  + ►
    [August](https://googleprojectzero.blogspot.com/2025/08/)
    (1)
  + ▼
    [July](https://googleprojectzero.blogspot.com/2025/07/)
    (1)
    - [Policy and Disclosure: 2025 Edition](https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html)
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
    [January](htt...